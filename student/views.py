from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from django.utils.translation import gettext as _
from django.utils.translation import gettext_lazy as lazy
from django.views.generic import ListView
from encrypted_id import decode
from datetime import date

from accounts.models import User
from teacher.models import Exam, Question
from .forms import StudentResponseForm
from .models import StudentResponse, StudentExam


@login_required
def all_exams_listview(request):
    from datetime import date
    if 'student_searched' not in request.session:
        request.session['student_searched'] = False
    today = date.today()
    # user = get_object_or_404(User, username=username)
    queryset = Exam.objects.filter(exam_status='Active')
    for record in queryset:
        if today > record.exam_date:
            record.exam_status = 'Expired'
        elif today < record.exam_date or today == record.exam_date:
            record.exam_status = 'Active'
        record.save()
    context = {
        'title': lazy("All exams"),
    }
    """ 
    get all teachers that have created exams
    
    """
    teachers = Exam.objects.select_related('teacher').values('teacher_id').distinct()
    empty = User.objects.none()
    for teacher in teachers:
        t = User.objects.filter(id=teacher['teacher_id'])
        empty |= t
    context['teacher_names'] = empty
    if request.method == 'POST' or request.session['student_searched']:
        print('here i am')
        basic_search_btn = request.POST.get('base_search')
        advanced_search_btn = request.POST.get('advanced_search')
        print('basic search', basic_search_btn)
        print('advanced search', advanced_search_btn)
        if basic_search_btn is not None:
            request.session['advanced_search'] = False
            context['search_bar'] = True
            search_phrase = request.POST.get('search_phrase')
            search_option = request.POST.get('search_option')
            filters = {'exam_status': 'Active'}
            if search_phrase != '' and search_phrase is not None and search_phrase != 'Search Phrase' \
                    and search_phrase != 'عبارة البحث':
                if search_option != 'none' and search_option is not None:
                    if search_option == 'examName':
                        queryset = Exam.objects.filter(exam_name=search_phrase, exam_status='Active')
                        filters['exam_name'] = search_phrase
                    else:
                        queryset = Exam.objects.filter(exam_unique_identifier=search_phrase, exam_status='Active')
                        filters['exam_unique_identifier'] = search_phrase
                else:
                    queryset = Exam.objects.filter(exam_name=search_phrase, exam_status='Active')
            if not queryset.exists():
                messages.error(request, _("Sorry we didn't found any match for your search! Please Try another one!"))
                queryset = Exam.objects.filter(exam_status='Active').order_by('-exam_date')
            else:
                request.session['basic_search'] = filters
        elif advanced_search_btn is not None:
            request.session['basic_search'] = False
            context['search_bar'] = True
            exam_name = request.POST.get('exam_name')
            exam_unique_identifier = request.POST.get('unique_identifier')
            exam_status = request.POST.get('exam_status')
            teacher_name = request.POST.get('teacher_name')
            order_by = request.POST.get('order_by')
            filters = {'exam_status': 'Active'}
            if teacher_name is not None and teacher_name != '' and teacher_name != 'none':
                filters['teacher_id'] = teacher_name
            if exam_name is not None and exam_name != '':
                filters['exam_name'] = exam_name
            if exam_unique_identifier is not None and exam_unique_identifier != '':
                filters['exam_unique_identifier'] = exam_unique_identifier
            if exam_status is not None and exam_status != '' and exam_status != 'none':
                print(exam_status)
                filters['exam_status'] = exam_status
            if order_by is not None and order_by != '' and order_by != 'none':
                print(order_by)
                print(order_by)
                if order_by == '-exam_date':
                    queryset = Exam.objects.filter(**filters).order_by('-exam_date')
                else:
                    queryset = Exam.objects.filter(**filters).order_by('exam_date')
            else:
                queryset = Exam.objects.filter(**filters)

            if not queryset.exists():
                context['exams'] = 'none'
                messages.error(request, _('There is no exam matching your search!! Please Try again!'))
            else:
                request.session['advanced_search'] = filters
        if not queryset.exists():
            context['exams'] = 'none'
            messages.error(request, _('There is no exam matching your search!! Please Try again!'))
        else:
            if request.POST.get('base_search') is not None or request.POST.get('advanced_search') is not None:
                request.session['student_searched'] = True
            if 'basic_search' in request.session:
                if request.session['basic_search']:
                    filters = request.session['basic_search']
                    queryset = Exam.objects.filter(**filters)
                    paginator = Paginator(queryset, 5)
                    page = request.GET.get('page')
                    context['page_obj'] = paginator.get_page(page)
                    context['exams'] = paginator.get_page(page)
                    context['is_paginated'] = True
            if 'advanced_search' in request.session:
                if request.session['advanced_search']:
                    filters = request.session['advanced_search']
                    queryset = Exam.objects.filter(**filters)
                    paginator = Paginator(queryset, 6)
                    page = request.GET.get('page')
                    context['page_obj'] = paginator.get_page(page)
                    context['exams'] = paginator.get_page(page)
                    context['is_paginated'] = True
            else:
                paginator = Paginator(queryset, 6)
                page = request.GET.get('page')
                context['page_obj'] = paginator.get_page(page)
                context['exams'] = paginator.get_page(page)
                context['is_paginated'] = True
        return render(request, 'student/search_exams.html', context)
    else:
        queryset = Exam.objects.filter(exam_status='Active').order_by('-exam_date')
        paginator = Paginator(queryset, 6)
        page = request.GET.get('page')
        context['page_obj'] = paginator.get_page(page)
        context['exams'] = paginator.get_page(page)
        context['is_paginated'] = True
        return render(request, 'student/search_exams.html', context)


class AllExamsListView(ListView):
    model = Exam
    template_name = 'student/search_exams.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'exams'
    paginate_by = 5
    extra_context = {
        'title': lazy("All Exams"),
        'update': True
    }

    def get_queryset(self):
        from datetime import date
        today = date.today()
        basic_search_btn = self.request.GET.get('base_search')
        advanced_search_btn = self.request.GET.get('advanced_search')
        querySet = Exam.objects.all()

        for record in querySet:
            if today > record.exam_date:
                record.exam_status = 'Expired'
            elif today < record.exam_date or today == record.exam_date:
                record.exam_status = 'Active'
            record.save()
        querySet = Exam.objects.filter(exam_status='Active')
        if basic_search_btn != None:
            search_phrase = self.request.GET.get('search_phrase')
            search_option = self.request.GET.get('search_option')
            if search_phrase != '' and search_phrase != None and search_phrase != 'Search Phrase' and search_phrase != 'عبارة البحث':
                if search_option != 'none' and search_option != None:
                    if search_option == 'examName':
                        querySet = Exam.objects.filter(exam_name=search_phrase, exam_status='Active')
                    elif search_option == 'examUniqueIdentifier':
                        querySet = Exam.objects.filter(exam_unique_identifier=search_phrase, exam_status='Active')
                else:
                    querySet = Exam.objects.filter(exam_unique_identifier=search_phrase, exam_status='Active')
            else:
                querySet = Exam.objects.filter(exam_name=search_phrase, exam_status='Active')
            if not querySet.exists():
                messages.error(self.request,
                               _("Sorry we didn't found any match for your search! Please Try another one!"))
                querySet = Exam.objects.all().order_by('-exam_date')
        elif advanced_search_btn != None:
            print('advanced search btn')
            teacher_username = self.request.GET.get('teacher_name')
            exam_name = self.request.GET.get('exam_name')
            exam_unique_identifier = self.request.GET.get('unique_identifier')
            exam_status = self.request.GET.get('exam_status')
            order_by = self.request.GET.get('order_by')
            filters = {'exam_status': 'Active'}
            if teacher_username != None and teacher_username != '' and teacher_username != 'none':
                print(teacher_username)
                user = User.objects.get(username=teacher_username)
                filters['teacher_id'] = user.id
            if exam_name != None and exam_name != '':
                print('exam name')
                print(exam_name)
                filters['exam_name'] = exam_name
            if exam_unique_identifier != None and exam_unique_identifier != '':
                filters['exam_unique_identifier'] = exam_unique_identifier
            if exam_status != None and exam_status != '' and exam_status != 'none':
                filters['exam_status'] = exam_status
            if order_by != None and order_by != '' and order_by != 'none':
                print(order_by)
                if order_by == '-exam_date':
                    querySet = Exam.objects.filter(**filters).order_by('-exam_date')
                else:
                    querySet = Exam.objects.filter(**filters).order_by('exam_date')
            else:
                querySet = Exam.objects.filter(**filters)

        return querySet

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        # user = get_object_or_404(User, username=self.kwargs.get('username'))
        exam_query = Exam.objects.all()
        teacher_names = User.objects.filter(is_teacher=1)
        encryptedIds = list()
        context['teacher_names'] = teacher_names
        querySet = self.get_queryset()
        if not querySet.exists():
            context['exams'] = 'none'
            context['examIDs'] = 'none'
            messages.error(self.request, _('There is no exam matching your search!! Please Try again!'))

        if not exam_query.exists():
            context['exams'] = 'none'
            context['examIDs'] = 'none'
            messages.error(self.request, _('There is no exam created yet!! Please Try again later!'))

        return context


@login_required
def examAttempt(request, pk):
    exams = Exam.objects.all()
    checked = False
    for exam in exams:
        if exam.ekey == pk:
            checked = True
            break
    if not checked:
        return TemplateResponse(request, status=404, template='errors/error_400.html')
    exam_id = decode(pk, "teacher_exam")
    exam_details = Exam.objects.get(id=exam_id)
    exam_period = exam_details.exam_period
    questions = Question.objects.filter(exam_id=exam_id)
    questions_count = Question.objects.filter(exam_id=exam_id).count()
    questions = Question.objects.filter(exam_id=exam_id)
    student = User.objects.get(id=request.user.id)
    exam = Exam.objects.get(id=exam_id)
    paginator = Paginator(questions, 6)
    page = request.GET.get('page')
    questions_list = list()
    answer_nums = list()

    if request.method == 'POST':
        for question in questions:
            answer_nums.append(question.question_number)
            questions_list.append(question)

        studentResponseForm = StudentResponseForm(request.POST)
        t = 0
        if studentResponseForm.is_valid():
            # well functioning code
            # StudentExam.objects.create(exam=exam, student=student, exam_status="Active")
            # studentResponseObjects = list()
            # for t in range(questions_count):
            #     answer = request.POST.get('answer_' + str(answer_nums[t]), None)
            #     studentResponseObjects.append(StudentResponse(student=student, question=questions_list[t], student_response_text=answer,
            #                                    student_response_degree=23))
            # StudentResponse.objects.bulk_create(studentResponseObjects)
            # examAttemptConfirm(request)
            request.session['exam_request'] = request.POST
            request.session['attempted_exam_id'] = exam_id

            return redirect('exam-confirm-report')

    translations = {
        'remove_question': _('Remove Question'),
        'question': _('Question')
    }
    context = {
        'questions': paginator.get_page(page),
        'questions2': questions,
        'page_obj': paginator.get_page(page),
        'is_paginated': True,
        'num_pages': paginator.num_pages,
        'per_page': 6,
        'translations': translations,
        'exam_question_count': questions_count,
        'exam_period': exam_period,
        'exam_id': exam_id,
        'ekey': pk,
        'title': _("Exam Attempt"),
    }

    return render(request, 'student/handle_exam.html', context)


def submit_answers(request):
    exam_id = request.GET.get('exam_id', None)
    user_id = request.GET.get('user_id', None)
    exam = Exam.objects.get(id=exam_id)
    user = User.objects.get(id=user_id)
    StudentExam.objects.create(exam=exam, student=user, exam_status="Active")
    questions_count = Question.objects.filter(exam_id=exam_id).count()
    queryset = Question.objects.filter(exam_id=exam_id)
    answer_nums = list()
    question_ids = list()
    for question in queryset:
        answer_nums.append(question.question_number)
        question_ids.append(question)
    for t in range(questions_count):
        answer = request.GET.get('answers[answer_' + str(answer_nums[t]) + ']', None)
        StudentResponse.objects.create(student=user, question=question_ids[t], student_response_text=answer,
                                       student_response_degree=23)
    data = {
        'url': '/home/'
    }
    return JsonResponse(data)


def examAttemptConfirm(request):
    request_data = request.session['exam_request']
    exam_id = request.session['attempted_exam_id']
    questions_list = list()
    answer_nums = list()
    student = User.objects.get(id=request.user.id)
    exam = Exam.objects.get(id=exam_id)

    questions = Question.objects.filter(exam_id=exam_id)
    questions_count = Question.objects.filter(exam_id=exam_id).count()
    answered_questions = 0
    for question in questions:
        answer_nums.append(question.question_number)
        questions_list.append(question)
    altered_answers = list()
    answers_status = list()

    for f in range(1, questions_count + 1):
        altered_answers.append(request_data.get('answer_' + str(f)))
        if (request_data.get('answer_' + str(f)) is None or request_data.get('answer_' + str(f)) == ""):
            answers_status.append("Didn't Answer")
        else:
            answers_status.append("Answer Saved")
            answered_questions = answered_questions + 1
    request.session['answered_questions_count'] = answered_questions

    if request.method == "POST":
        studentResponseForm = StudentResponseForm(request.POST)
        questions_count = Question.objects.filter(exam_id=exam_id).count()
        t = 0
        if studentResponseForm.is_valid():
            StudentExam.objects.create(exam=exam, student=student, exam_status="Active")
            studentResponseObjects = list()
            for t in range(questions_count):
                answer = request_data.get('answer_' + str(answer_nums[t]), None)
                studentResponseObjects.append(
                    StudentResponse(student=student, question=questions_list[t], student_response_text=answer,
                                    student_response_degree=23))
            StudentResponse.objects.bulk_create(studentResponseObjects)
        return redirect('exam-final-report')
    context = {
        'questions': questions,
        'answers_status': answers_status,
        'exam_ekey': exam.ekey,
        'exam_period': exam.exam_period,
        'title':_('Attempt Submit Confirmation')
    }
    return render(request, 'student/exam_confirmation_report.html', context)


def examFinalReport(request):
    exam_id = request.session['attempted_exam_id']
    exam = Exam.objects.get(id=exam_id)
    exam_name = exam.exam_name
    exam_period = exam.exam_period
    today = date.today()
    # Textual month, day and year
    attempt_date = today.strftime("%B %d, %Y")
    context = {
        'exam_id':exam_id,
        'answered_questions_count':request.session['answered_questions_count'],
        'exam_name':exam_name,
        'questions_count':Question.objects.filter(exam_id=exam_id).count(),
        'attempt_date':attempt_date,
        'exam_period':exam_period,
        'title':_("Attempt Report"),

    }
    return render(request, 'student/exam_final_report.html',context)
