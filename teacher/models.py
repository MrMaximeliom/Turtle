from django.db import models
from django.utils.translation import gettext as _

FIELDS = (
    ( ('Information Technology'), _('Information Technology')),
    ( ('Computer Science' ), _('Computer Science')),
    ( ('Software Engineering' ), _('Software Engineering')),
)
COURSES = (
    (('Cloud Computing'),(_('Cloud Computing'))),
    (('Cyber Security'),(_('Cyber Security'))),
    (('Advanced Dtabases'),(_('Advanced Databases'))),
    (('Network Principles'),(_('Network Principles'))),
    (('Network Security'),(_('Network Security'))),
    (('Multimedia'),(_('Multimedia'))),
    (('Programming Principles'),(_('Programming Principles'))),
)

class Field(models.Model):
    field_name = models.CharField(max_length=250,blank=False,verbose_name=_('field name'))

class Course(models.Model):
    field = models.ForeignKey(Field,on_delete=models.CASCADE,related_name='+')
    course_name = models.CharField(verbose_name=_('course'),max_length=250,blank=False)

class Exam(models.Model):
    teacher = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='+')
    exam_name = models.CharField(max_length=250,blank=False,verbose_name=_('exam name'))
    exam_date = models.DateField(verbose_name=_('exam date'),blank=False)
    exam_period = models.IntegerField(verbose_name=_('exam period'),blank=False)
    exam_note = models.TextField(verbose_name=_('exam notes'),blank=True,max_length=300)
    exam_secret_key = models.CharField(verbose_name=_('exam secret key'),blank=False,max_length=10)
    exam_full_mark = models.IntegerField(blank=False,verbose_name=_('exam full mark'))
    exam_pass_mark = models.IntegerField(blank=False,verbose_name=_('exam pass mark'))
    exam_status = models.CharField(max_length=30,verbose_name=_('exam status'),blank=False)
    exam_unique_identifier = models.CharField(verbose_name=_('exam unique identifier'),max_length=120,blank=True)
    exam_number_of_questions = models.IntegerField(verbose_name=_('exam number of questions'),blank=True,null=True)


class Question(models.Model):
    exam = models.ForeignKey(Exam,on_delete=models.CASCADE,related_name='+')
    question_text = models.CharField(max_length=650,blank=False)
    question_optimal_answer = models.TextField(blank=False)
    question_degree = models.IntegerField(blank=False)
