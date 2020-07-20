from .models import Exam,Field,Course
from django import forms
from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm

class createExam(ModelForm):
    class Meta:
        model = Exam
        fields = [ 'teacher',
                  'exam_name','exam_date',
                  'exam_period','exam_note',
                  'exam_secret_key','exam_full_mark',
                  'exam_pass_mark','exam_status',
                  'exam_number_of_questions',
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
            'exam_number_of_questions ':_('exam number of questions')
        }

