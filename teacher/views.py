from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.utils.translation import gettext as _
from django.utils.translation import gettext_lazy as lazy
from .forms import QuestionFormset
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
import random
import string
from .models import Exam, Question
from accounts.models import User
from .forms import CreateExam
from django.urls import reverse_lazy
from django.http import JsonResponse
from django import forms


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
            if exam_number_of_questions is not None:
                request.session['exam_number_of_questions'] = exam_number_of_questions
            else:
                request.session['exam_number_of_questions'] = 0

            messages.success(request, _('Your New Exam has been created Successfully!'))
            return redirect('add-questions')
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
                form.exam_id = 5
                print(form.question_text+"\n")
                form.save()
            messages.success(request, _('Your Exam Questions has been created Successfully!'))
            return redirect('questions-list')

        else:
            new_formset = formset.save(commit=False)
            for form in new_formset:
                print(form.errors,"\n")
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


class ExamListView(ListView):
    model = Exam
    template_name = 'teacher/teacher_examList.html'
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


class TeacherExamListView(ListView):
    model = Exam
    template_name = 'teacher/teacher_exams.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'exams'
    extra_context = {
        'title': lazy("All teacher's exams")
    }

    # paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Exam.objects.filter(teacher=user).order_by('-exam_date')


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


class ExamDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Exam
    success_url = '/'
    extra_context = {
        'title': lazy("Delete Exam")
    }

    def test_func(self):
        exam = self.get_object()
        if self.request.user == exam.teacher:
            return True
        return False


class QuestionListView(ListView):
    model = Question
    template_name = "teacher/question_list.html"
    extra_context = {"title":lazy("Questions List")}
