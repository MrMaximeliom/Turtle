from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.urls import resolve
from django.forms import modelformset_factory
from django.utils.translation import gettext as _
from django.utils.translation import gettext_lazy as lazy
from .forms import QuestionFormset, UpdateQuestionFormSet
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
import random
import string
from .models import Exam, Question
from accounts.models import User
from .forms import CreateExam
from django.core.serializers import serialize


def get_random_string(length):
    numbers = 1234567890
    letters = string.ascii_lowercase
    number_and_letters = str(numbers) + letters
    result_str = ''.join(random.choice(number_and_letters) for i in range(length))
    # print("Random string of length", length, "is:", result_str)
    return result_str


@login_required
def create_new_exam(request):
    if request.method == 'POST':
        form = CreateExam(request.POST)

        context = {
            'title': _('Create New Exam'),
            'form': form,
        }

        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.teacher = request.user
            new_form.exam_status = "active"
            new_form.save()
            exam_number_of_questions = form.cleaned_data.get('exam_number_of_questions')
            exam = Exam.objects.get(exam_unique_identifier=form.cleaned_data.get('exam_unique_identifier'))
            request.session['exam_id'] = exam.id
            if exam_number_of_questions is not None:
                request.session['exam_number_of_questions'] = exam_number_of_questions
            else:
                request.session['exam_number_of_questions'] = 0

            messages.success(request, _('Your New Exam has been created Successfully!'))
            return redirect('create_questions-page')
        else:
            print("not valid")
    else:
        form = CreateExam(initial={'exam_unique_identifier': get_random_string(16)})
        context = {
            'title': _('Create New Exam'),
            'form': form,
        }

    return render(request, 'teacher/createExam.html', context)


@login_required
def create_questions(request):
    translations = {
        'remove_question': _('Remove Question'),
        'question': _('Question')
    }
    if 'exam_number_of_questions' not in request.session:
        request.session['exam_number_of_questions'] = 0
    exam_question_count = {
        'count': request.session['exam_number_of_questions']
    }
    if request.method == 'POST':
        # form = CreateExamQuestions(request.POST, instance=request.user)
        formset = QuestionFormset(data=request.POST)

        context = {
            'title': lazy('Create Exam Questions'),
            'form': formset,
            'translations': translations,
            'exam_question_count': exam_question_count,
        }
        if formset.is_valid():
            new_formset = formset.save(commit=False)
            for form in new_formset:
                # Exam.objects.filter(id=5).first()
                form.exam_id = request.session['exam_id']
                form.save()
            messages.success(request, _('Your Exam Questions has been created Successfully!'))
            return redirect('teacher-exams', request.user)

        else:
            new_formset = formset.save(commit=False)
            for form in new_formset:
                print(form.errors, "\n")
    else:
        # form = CreateExamQuestions()
        formset = QuestionFormset(queryset=Question.objects.none())
        context = {
            'title': lazy('Create Exam Questions'),
            'form': formset,
            'translations': translations,
            'exam_question_count': exam_question_count,
        }

    return render(request, 'teacher/createQuestions.html', context)


class AllExamsListView(ListView):
    model = Exam
    template_name = 'teacher/all_exams_list.html'
    context_object_name = 'exams'
    ordering = ['-exam_date']
    extra_context = {
        'title': lazy("All Exams")
    }


class ExamDetailView(DetailView):
    model = Exam
    extra_context = {
        'title': lazy("Exam Details")
    }

def teacherExamListView(request,username):
    from datetime import date
    if 'teacher_searched' not in request.session:
        request.session['teacher_searched'] = False
    today = date.today()
    user = get_object_or_404(User, username=username)
    queryset = Exam.objects.filter(teacher=user).order_by('-exam_date')
    for record in queryset:
        if today > record.exam_date:
            record.exam_status = 'Expired'
        elif today < record.exam_date or today == record.exam_date:
            record.exam_status = 'Active'
        record.save()
    context = {
        'title': lazy("All teacher's exams"),
    }
    if request.method == 'POST' or request.session['teacher_searched']:
        print('here i am')
        basic_search_btn = request.POST.get('base_search')
        advanced_search_btn = request.POST.get('advanced_search')
        print('basic search',basic_search_btn)
        print('advanced search',advanced_search_btn)
        if basic_search_btn != None:
            request.session['advanced_search'] = False
            context['search_bar'] = True
            search_phrase = request.POST.get('search_phrase')
            search_option = request.POST.get('search_option')
            filters = {'exam_name': search_phrase}
            if search_phrase != '' and search_phrase != None and search_phrase != 'Search Phrase' and search_phrase != 'عبارة البحث':
                if search_option != 'none' and search_option != None:
                    if search_option == 'examName':
                        queryset = Exam.objects.filter(teacher=user, exam_name=search_phrase)
                        filters['exam_name'] = search_phrase
                    else:
                        queryset = Exam.objects.filter(teacher=user, exam_unique_identifier=search_phrase)
                        filters['exam_unique_identifier'] = search_phrase
                else:
                    queryset = Exam.objects.filter(teacher=user, exam_name=search_phrase)
            if not queryset.exists():
                messages.error(request,_("Sorry we didn't found any match for your search! Please Try another one!"))
                queryset = Exam.objects.filter(teacher=user).order_by('-exam_date')
            else:
                request.session['basic_search'] = filters
        elif advanced_search_btn != None:
            request.session['basic_search'] = False
            context['search_bar'] = True
            exam_name = request.POST.get('exam_name')
            exam_unique_identifier = request.POST.get('unique_identifier')
            exam_status = request.POST.get('exam_status')
            order_by = request.POST.get('order_by')
            filters = {}

            if exam_name != None and exam_name != '':
                filters['exam_name'] = exam_name
            if exam_unique_identifier != None and exam_unique_identifier != '':
                filters['exam_unique_identifier'] = exam_unique_identifier
            if exam_status != None and exam_status != '' and exam_status != 'none' :
                print(exam_status)
                filters['exam_status'] = exam_status
            if order_by != None and order_by != '' and order_by != 'none':
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
            print('before last else')
            print('base_search',basic_search_btn)
            print('advanced_search',advanced_search_btn)
            if request.POST.get('base_search') != None or request.POST.get('advanced_search') != None:
                request.session['teacher_searched'] = True
                print('in getto')
            if  'basic_search'  in request.session:
                if request.session['basic_search'] != False:
                    filters = request.session['basic_search']
                    queryset = Exam.objects.filter(teacher=user,**filters)
                    paginator = Paginator(queryset, 5)
                    page = request.GET.get('page')
                    context['page_obj'] = paginator.get_page(page)
                    context['exams'] = paginator.get_page(page)
                    context['is_paginated'] = True
            if 'advanced_search' in request.session:
                if request.session['advanced_search'] != False:
                    filters = request.session['advanced_search']
                    queryset = Exam.objects.filter(teacher=user,**filters)
                    paginator = Paginator(queryset, 5)
                    page = request.GET.get('page')
                    context['page_obj'] = paginator.get_page(page)
                    context['exams'] = paginator.get_page(page)
                    context['is_paginated'] = True
            else:
                paginator = Paginator(queryset, 5)
                page = request.GET.get('page')
                context['page_obj'] = paginator.get_page(page)
                context['exams'] = paginator.get_page(page)
                context['is_paginated'] = True
        return render(request,'teacher/teacher_exams.html',context)
    else:
        print('here i am in get')
        user = get_object_or_404(User, username=username)
        queryset = Exam.objects.filter(teacher=user).order_by('-exam_date')
        paginator = Paginator(queryset, 5)
        page = request.GET.get('page')
        context['page_obj'] = paginator.get_page(page)
        context['exams'] = paginator.get_page(page)
        context['is_paginated'] = True
        return render(request, 'teacher/teacher_exams.html', context)
#
# class TeacherExamListView(ListView):
#     model = Exam
#     template_name = 'teacher/teacher_exams.html'  # <app>/<model>_<viewtype>.html
#     context_object_name = 'exams'
#     extra_context = {
#         'title': lazy("All teacher's exams"),
#         'update': True
#     }
#
#     def get_queryset(self):
#         from datetime import date
#         today = date.today()
#         basic_search_btn = self.request.GET.get('base_search')
#         advanced_search_btn = self.request.GET.get('advanced_search')
#         context = self.extra_context
#         context['search_bar'] = False
#         user = get_object_or_404(User, username=self.kwargs.get('username'))
#         queryset = Exam.objects.filter(teacher=user).order_by('-exam_date')
#         for record in queryset:
#             if today > record.exam_date:
#                 record.exam_status = 'Expired'
#             elif today < record.exam_date or today == record.exam_date:
#                 record.exam_status = 'Active'
#             record.save()
#         if basic_search_btn != None:
#             context['search_bar'] = True
#             search_phrase = self.request.GET.get('search_phrase')
#             search_option = self.request.GET.get('search_option')
#             if search_phrase != '' and search_phrase != None and search_phrase != 'Search Phrase' and search_phrase != 'عبارة البحث':
#                 if search_option != 'none' and search_option != None:
#                     if search_option == 'examName':
#                         queryset = Exam.objects.filter(teacher=user, exam_name=search_phrase)
#                     else:
#                         queryset = Exam.objects.filter(teacher=user, exam_unique_identifier=search_phrase)
#                 else:
#                     queryset = Exam.objects.filter(teacher=user, exam_name=search_phrase)
#             if not queryset.exists():
#                 messages.error(self.request,_("Sorry we didn't found any match for your search! Please Try another one!"))
#                 queryset = Exam.objects.filter(teacher=user).order_by('-exam_date')
#         elif advanced_search_btn != None:
#             context['search_bar'] = True
#             exam_name = self.request.GET.get('exam_name')
#             exam_unique_identifier = self.request.GET.get('unique_identifier')
#             exam_status = self.request.GET.get('exam_status')
#             order_by = self.request.GET.get('order_by')
#             filters = {'exam_status': 'Active'}
#             if exam_name != None and exam_name != '':
#                 filters['exam_name'] = exam_name
#             if exam_unique_identifier != None and exam_unique_identifier != '':
#                 filters['exam_unique_identifier'] = exam_unique_identifier
#             if exam_status != None and exam_status != '' and exam_status != 'none':
#                 print(exam_status)
#                 filters['exam_status'] = exam_status
#             if order_by != None and order_by != '' and order_by != 'none':
#                 print(order_by)
#                 print(order_by)
#                 if order_by == '-exam_date':
#                     queryset = Exam.objects.filter(**filters).order_by('-exam_date')
#                 else:
#                     queryset = Exam.objects.filter(**filters).order_by('exam_date')
#             else:
#                 queryset = Exam.objects.filter(**filters)
#         context['path'] = self.request.get_full_path()
#         if 'page' in self.request.get_full_path():
#             path = self.request.get_full_path().split('?page=', 1)
#             context['path'] = path[0]
#
#         if not queryset.exists():
#             context['exams'] = 'none'
#             messages.error(self.request, _('There is no exam matching your search!! Please Try again!'))
#         self.paginate_by = 5
#         return queryset
#
#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super().get_context_data(**kwargs)
#         # Add in a QuerySet of all the books
#         user = get_object_or_404(User, username=self.kwargs.get('username'))
#         exam_query = Exam.objects.filter(teacher=user).order_by('-exam_date')
#
#         if not exam_query.exists():
#             context['exams'] = 'none'
#             messages.error(self.request, _('You did not create any exam yet! please create one and try again!'))
#         return context
#
#     paginate_by = 5

class ExamUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Exam
    form_class = CreateExam
    template_name = 'teacher/createExam.html'

    extra_context = {
        'title': lazy('Update Exam')

    }

    def form_valid(self, form):
        form.instance.teacher = self.request.user
        return super().form_valid(form)

    def test_func(self):
        exam = self.get_object()
        if self.request.user == exam.teacher:
            return True
        return False

    def get_success_url(self):
        self.request.session['updated_exam_id'] = self.get_object().id
        return '/teacher/exam/update-questions/'


@login_required
def QuestionUpdateView(request):
    translations = {
        'remove_question': _('Remove Question'),
        'question': _('Question')
    }

    exam_question_count = {
        'count': Question.objects.filter(exam_id=request.session['updated_exam_id']).count()
    }
    exam = Exam.objects.get(id=request.session['updated_exam_id'])
    if request.method == 'POST':
        print("here now")
        formset = UpdateQuestionFormSet(request.POST, request.FILES, instance=exam)
        context = {
            'title': lazy('Update Exam Questions'),
            'form': formset,
            'translations': translations,
            'exam_question_count': exam_question_count,
        }

        if formset.is_valid():

            new_formset = formset.save(commit=False)
            for form in new_formset:
                form.save()
            messages.success(request, _('Your Exam Questions has been updated Successfully!'))
            return redirect('exam-update-questions')

        else:

            new_formset = formset.save(commit=False)
            print(formset.forms)
            for form in new_formset:
                print("formset errors")
                print(form.errors, "\n")
    else:
        formset = UpdateQuestionFormSet(instance=exam)
        if exam_question_count['count'] == 0:
            request.session['exam_id'] = request.session['updated_exam_id']
            messages.error(request, _('Your Exam Does not contain any questions! please add at least one!'))
            return redirect('create_questions-page')

        context = {
            'title': lazy('Update Exam Questions'),
            'form': formset,
            'translations': translations,
            'exam_question_count': exam_question_count,
        }

    return render(request, 'teacher/updateQuestions.html', context)


class ExamDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Exam
    extra_context = {
        'title': lazy("Delete Exam")
    }

    def get_success_url(self):
        return '/teacher/user/' + str(self.request.user)

    def test_func(self):
        exam = self.get_object()
        if self.request.user == exam.teacher:
            return True
        return False


class QuestionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Question
    extra_context = {
        'title': lazy("Delete Question")
    }

    def get_success_url(self):
        return '/teacher/exam/update-questions/'

    def test_func(self):
        question = self.get_object()
        if self.request.user == question.exam.teacher:
            return True
        return False


class QuestionListView(ListView):
    model = Question
    template_name = "teacher/question_list.html"
    extra_context = {"title": lazy("Questions List")}
