from django.db import models
from django.utils.translation import gettext as _
from accounts.models import User
from teacher.models import Exam,Question
from django.utils import timezone
from django.urls import reverse

class StudentExam(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    exam_status = models.CharField(max_length=30, verbose_name=_('exam status'), blank=True)

class StudentResponse(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    student_response_text =  models.TextField(blank=True, verbose_name=_('answer here'))
    student_response_degree = models.FloatField(blank=False,verbose_name=_('student degree'))

class StudentGrade(models.Model):
    student_grade_name = models.CharField(blank=False,verbose_name=_('grade name'),max_length=120)
    student_grade_rate = models.FloatField(blank=False,verbose_name=_('grade rate'))

class ExamDegrees(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    student_grade = models.ForeignKey(StudentGrade, on_delete=models.CASCADE)
    student_total_score = models.FloatField(blank=False,verbose_name=_('student total degree'))


