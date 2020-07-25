from django.urls import path
from . import views


urlpatterns = [
   path('error_404/',views.error_404, name='error-404-page'),
   # path('error_404/',views.handler404, name='error-404-page'),
]
