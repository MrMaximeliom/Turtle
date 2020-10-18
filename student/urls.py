from django.urls import path

from student.views import (
all_exams_listview,
)

urlpatterns = [
    path('search-exams/', all_exams_listview, name='search-exams')
    ]