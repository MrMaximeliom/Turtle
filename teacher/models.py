from django.db import models
from django.utils.translation import gettext as _


class Field(models.Model):
    field_name = models.CharField(max_length=250,blank=False,verbose_name=_('field name'))

class Course(models.Model):
    field = models.ForeignKey(Field,on_delete=models.CASCADE,related_name='+')
    course_name = models.CharField(verbose_name=_('course'),max_length=250,blank=False)

class Exam(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='+')
    teacher = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='+')
    exam_name = models.CharField(max_length=250,blank=False,verbose_name=_('exam name'))
    exam_date = models.DateField(verbose_name=_('exam date'),blank=False)
    exam_period = models.IntegerField(verbose_name=_('exam period'),blank=False)
    exam_note = models.TextField(verbose_name=_('exam notes'),blank=True,max_length=300)
    exam_secret_key = models.CharField(verbose_name=_('exam secret key'),blank=False,max_length=10)
    exam_full_mark = models.IntegerField(blank=False,verbose_name=_('exam full mark'))
    exam_pass_mark = models.IntegerField(blank=False,verbose_name=_('exam pass mark'))
    exam_status = models.CharField(max_length=30,verbose_name=_('exam status'),blank=False)
