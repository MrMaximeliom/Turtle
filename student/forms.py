from .models import StudentResponse
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


