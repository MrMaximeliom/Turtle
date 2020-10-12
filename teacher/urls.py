from django.urls import path
from .views import (
    ExamDetailView,
    TeacherExamListView,
    create_new_exam,
    create_questions,
    AllExamsListView,
    ExamUpdateView,
    ExamDeleteView,
    QuestionListView,
    QuestionUpdateView,
    QuestionDeleteView

)

urlpatterns = [
    path('create-exam/', create_new_exam, name='create_exam-page'),
    path('create-exam-questions/',create_questions, name='create_questions-page'),
    path('list-questions/',QuestionListView.as_view(), name='questions-list'),
    path('all-exams-list/', AllExamsListView.as_view(), name='all-exams_list'),#Home page here
    path('exam/<int:pk>/', ExamDetailView.as_view(), name='exam-detail'),
    path('user/<str:username>', TeacherExamListView.as_view(), name='teacher-exams'),
    path('exam/<int:pk>/update/', ExamUpdateView.as_view(), name='exam-update'),
    path('exam/update-questions/', QuestionUpdateView, name='exam-update-questions'),
    path('exam/<int:pk>/delete/', ExamDeleteView.as_view(), name='exam-delete'),
    path('question/<int:pk>/delete/', QuestionDeleteView.as_view(), name='question-delete'),
]
