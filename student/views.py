from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render
from django.utils.translation import gettext as _
from django.utils.translation import gettext_lazy as lazy
from django.views.generic import ListView

from accounts.models import User
from teacher.models import Exam


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
            if search_phrase != '' and search_phrase is not None and search_phrase != 'Search Phrase'\
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
        return render(request, 'student/search_exams.html', context)
    else:
        queryset = Exam.objects.filter(exam_status='Active').order_by('-exam_date')
        paginator = Paginator(queryset, 5)
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
        context['teacher_names'] = teacher_names
        querySet = self.get_queryset()
        if not querySet.exists():
            context['exams'] = 'none'
            messages.error(self.request, _('There is no exam matching your search!! Please Try again!'))
        if not exam_query.exists():
            context['exams'] = 'none'
            messages.error(self.request, _('There is no exam created yet!! Please Try again later!'))
        return context
