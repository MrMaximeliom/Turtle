from django.db import models
from django.utils.translation import gettext as _
from accounts.models import User
from django.utils import timezone
from django.urls import reverse
from encrypted_id.models import EncryptedIDModel

FIELDS = (
    (('Information Technology'), _('Information Technology')),
    (('Computer Science'), _('Computer Science')),
    (('Software Engineering'), _('Software Engineering')),
)
COURSES = (
    (('Cloud Computing'), (_('Cloud Computing'))),
    (('Cyber Security'), (_('Cyber Security'))),
    (('Advanced Dtabases'), (_('Advanced Databases'))),
    (('Network Principles'), (_('Network Principles'))),
    (('Network Security'), (_('Network Security'))),
    (('Multimedia'), (_('Multimedia'))),
    (('Programming Principles'), (_('Programming Principles'))),
)


class Field(models.Model):
    field_name = models.CharField(max_length=250, blank=False, verbose_name=_('field name'))


class Course(models.Model):
    field = models.ForeignKey(Field, on_delete=models.CASCADE, related_name='+')
    course_name = models.CharField(verbose_name=_('course'), max_length=250, blank=False)


class Exam(EncryptedIDModel):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    exam_name = models.CharField(max_length=250, blank=False, verbose_name=_('exam name'))
    encrypted_id = models.BinaryField(max_length=400, blank=True, verbose_name=_('encrypted id'))
    exam_date = models.DateField(verbose_name=_('exam date'), blank=False)
    exam_period = models.CharField(max_length=250,verbose_name=_('exam period'), blank=False)
    exam_note = models.TextField(verbose_name=_('exam notes'), blank=True, max_length=300)
    exam_full_mark = models.IntegerField(blank=False, verbose_name=_('exam full mark'))
    exam_pass_mark = models.IntegerField(blank=False, verbose_name=_('exam pass mark'))
    exam_status = models.CharField(max_length=30, verbose_name=_('exam status'), blank=True)
    exam_unique_identifier = models.CharField(verbose_name=_('exam unique identifier'), max_length=120, blank=True)
    exam_number_of_questions = models.IntegerField(verbose_name=_('exam number of questions'), blank=True, null=True)
    exam_date_created = models.DateTimeField(default=timezone.now,blank=True)
    db_table = "teacher_exam"

    def get_absolute_url(self):
        return reverse('exam-detail', kwargs={'pk': self.pk})


class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=650, blank=False)
    question_optimal_answer = models.TextField(blank=False)
    question_degree = models.IntegerField(blank=False)
    question_number = models.IntegerField(blank=True,null=True)
