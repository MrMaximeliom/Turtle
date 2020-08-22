from django.urls import path
from .views import (
    ExamDetailView,
    TeacherExamListView,
    create_new_exam,
    create_questions,
    ExamListView,
    ExamUpdateView,
    ExamDeleteView,
    QuestionListView,

)

urlpatterns = [
    path('create-exam/', create_new_exam, name='create_exam-page'),
    path('create-exam-questions/',create_questions, name='create_questions-page'),
    path('list-questions/',QuestionListView.as_view(), name='questions-list'),
    path('exams-list/', ExamListView.as_view(), name='exam_list'),#Home page here
    path('exam/<int:pk>/', ExamDetailView.as_view(), name='exam-detail'),
    path('user/<str:username>', TeacherExamListView.as_view(), name='teacher-exams'),
    path('exam/<int:pk>/update/', ExamUpdateView.as_view(), name='exam-update'),
    path('exam/<int:pk>/delete/', ExamDeleteView.as_view(), name='exam-delete'),
]
