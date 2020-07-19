from django.urls import path
from . import views

urlpatterns = [
    path('create-exam/', views.createExam, name='create_exam-page'),
    path('create-exam-questions/', views.createQuestions, name='create_questions-page'),
]
