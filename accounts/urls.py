from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
   path('signup-as-teacher/',views.teacher_sign_up,name='teacher-signup-page'),
   path('signup-as-student/',views.student_sign_up,name='student-signup-page'),
   path('logout/',auth_views.LogoutView.as_view(template_name='accounts/logout.html'),name='logout-page'),
   path('login/',views.login, name='login-page'),
   path('registration/',views.register_page, name='register-page'),
   path('profile/',views.profile_page, name='profile-page'),
   path('ajax/validate_username/', views.validate_username, name='validate_username'),
   path('ajax/validate_password/', views.validate_password, name='validate_password'),

]
