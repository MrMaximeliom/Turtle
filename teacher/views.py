from django.shortcuts import render
from django.utils.translation import gettext as _
from .forms import createExam
from django.shortcuts import render, redirect
from django.contrib import messages



def creatExam(request):
    form = createExam()
    context = {
        'title': _('Create New Exam'),
        'form': form,
    }
    if request.method == 'POST':
        form = createExam(request.POST)
        context = {
            'title': _('Create New Exam'),
            'form': form,
        }
        if form.is_valid():
            exam_number_of_questions = form.cleaned_data.get('exam_number_of_questions')
            messages.success(request, _('Your New Exam has been created Successfully!'))
            return redirect('home-page')
    return render(request, 'teacher/createExam.html', context)

def createQuestions(request,questions):
    context = {
        'questions':questions,
    }
    return render(request,'teacher/createQuestions.html',context)