from django.urls import path
from . import views

urlpatterns = [
    path('create-exam/', views.create_new_exam, name='create_exam-page'),
    path('create-exam-questions/', views.create_questions, name='create_questions-page'),
]
