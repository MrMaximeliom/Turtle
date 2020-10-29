from .models import StudentResponse
from teacher.models import Question
from django import forms
from django.utils.translation import gettext_lazy as _


class StudentResponseForm(forms.ModelForm):
    class Meta:
        model = StudentResponse
        fields = ['student', 'question','student_response_text','student_response_degree']
        labels = {
            'student': _('Student'),
            'question': _('Question'),
            'student_response_text': _('Student Response Text'),
            'student_response_degree': _('Student Response Degree'),
        }
        exclude = ['student','question','student_response_degree']

class QuestionsForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            'question_text',
            'question_degree',
        ]
        exclude = ["exam"]
        labels = {
            'question_text': _('question text'),
            'question_degree': _('question degree')
        }
        widgets = {
            'question_text': forms.Textarea(attrs={'placeholder': _('add your question here!'), 'cols': 25, 'rows': 2}),
            'question_degree': forms.NumberInput(
                attrs={'placeholder': _('add your question degree here!'), 'min': 1, 'max': 100}),

        }


