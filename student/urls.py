from django.urls import path

from student.views import (
all_exams_listview,
examAttempt,
submit_answers,
examAttemptConfirm,
examFinalReport
)

urlpatterns = [
    path('search-exams/', all_exams_listview, name='search-exams'),
    path('handle-attempt/<str:pk>', examAttempt, name='start-attempt'),
    path('ajax/submit_answers/', submit_answers, name='submit-answers'),
    path('exam-attempt-report/', examAttemptConfirm , name='exam-confirm-report'),
    path('exam-attempt-final-report/', examFinalReport , name='exam-final-report'),

    ]