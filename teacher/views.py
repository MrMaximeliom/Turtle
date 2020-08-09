from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _
from .forms import CreateExam, CreateExamQuestions
from django.shortcuts import render, redirect
from django.contrib import messages
import random
import string


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
        form = CreateExam(request.POST, instance=request.user)
        context = {
            'title': _('Create New Exam'),
            'form': form,
        }
        # print(form.is_valid(), form.errors, type(form.errors))
        if form.is_valid():
            new_exam = form.save(commit=False)
            new_exam.teacher = request.user.id
            new_exam.save()
            exam_number_of_questions = form.cleaned_data.get('exam_number_of_questions')
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
    exam_question_count = {
        'count':request.session['exam_number_of_questions']
    }
    if request.method == 'POST':
        form = CreateExamQuestions(request.POST, instance=request.user)
        context = {
            'title': _('Create Exam Questions'),
            'form': form,
            'translations': translations,
            'exam_question_count':exam_question_count,
        }
        if form.is_valid():
            messages.success(request, _('Your Exam Questions has been created Successfully!'))
            return redirect('home-page')
    else:
        # print(request.session.get('exam_number_of_questions'))
        form = CreateExamQuestions()
        context = {
            'title': _('Create Exam Questions'),
            'form': form,
            'translations': translations,
            'exam_question_count': exam_question_count,
        }

    return render(request, 'teacher/createQuestions.html', context)
