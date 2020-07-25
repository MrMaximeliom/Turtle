from django.urls import path
from . import views

urlpatterns = [
    path('create-exam/', views.createNewExam, name='create_exam-page'),
    path('create-exam-questions/', views.createQuestions, name='create_questions-page'),
]
