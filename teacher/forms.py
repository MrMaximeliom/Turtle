from .models import Exam, Question
from django import forms
from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm

TIME_LENGTH = (
    ('10 minutes', '10 minutes'),
    ('15 minutes', '15 minutes'),
    ('30 minutes', '30 minutes'),
    ('1 hour', '1 hour'),
    ('1:30 hour', '1:30 hour'),
    ('2 hours', '2 hours'),
)


class CreateExamQuestions(ModelForm):
    class Meta:
        model = Question
        fields = [
            'question_text',
            'question_optimal_answer',
            'question_degree',
        ]
        labels = {
            'question_text': _('question text'),
            'question_optimal_answer': _('question optimal answer'),
            'question_degree': _('question degree')
        }
        widgets = {
            'question_text': forms.Textarea(attrs={'placeholder': _('add your question here!'), 'cols': 25, 'rows': 2}),
            'question_optimal_answer': forms.Textarea(
                attrs={'placeholder': _("add your question's optimal answer here!"), 'cols': 25, 'rows': 2}),
            'question_degree': forms.NumberInput(
                attrs={'placeholder': _('add your question degree here!'), 'min': 1, 'max': 100}),

        }


class CreateExam(ModelForm):
    class Meta:
        model = Exam
        fields = ['teacher',
                  'exam_name', 'exam_date',
                  'exam_period', 'exam_note',
                  'exam_secret_key', 'exam_full_mark',
                  'exam_pass_mark', 'exam_status',
                  'exam_number_of_questions',
                  'exam_unique_identifier',
                  ]
        labels = {
            'teacher': _('teacher'),
            'exam_name': _('exam name'),
            'exam_date': _('exam date'),
            'exam_period': _('exam period'),
            'exam_secret_key': _('exam secret key'),
            'exam_full_mark': _('exam full mark'),
            'exam_note': _('exam notes'),
            'exam_pass_mark': _('exam pass mark'),
            'exam_status': _('exam status'),
            'exam_number_of_questions': _('exam number of questions'),
            'exam_unique_identifier': _('exam unique identifier'),
        }
        widgets = {
            'exam_name': forms.TextInput(attrs={'placeholder': _('exam name goes here!')}),
            'exam_note': forms.Textarea(attrs={'placeholder': _('add your exam notes here!'), 'cols': 25, 'rows': 2}),
            'exam_period': forms.Select(attrs={'placeholder': _('set exam period here!')}, choices=TIME_LENGTH),
            'exam_secret_key': forms.TextInput(attrs={'placeholder': _('specify exam secret key!')}),
            'exam_date': forms.TextInput(attrs={'placeholder': _('set exam date here!')}),
            'exam_pass_mark': forms.NumberInput(attrs={'placeholder': _('exam pass mark here!'), 'min': 1, 'max': 100}),
            'exam_full_mark': forms.NumberInput(attrs={'placeholder': _('exam full mark here!'), 'min': 1, 'max': 100}),
            'exam_status': forms.TextInput(attrs={'placeholder': _('exam status here!')}),
            'exam_number_of_questions': forms.NumberInput(attrs={'placeholder': _('exam number of questions!'),'min': 1, 'max': 100}),
            'exam_unique_identifier': forms.TextInput(
                attrs={'placeholder': _('exam unique identifier!'), 'readonly': True}),

        }
