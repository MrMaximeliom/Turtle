from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('home/', views.home, name='home-page'),
    path('about/', views.about, name='about-page'),

    path('contact/', views.contact_us, name='contact_us-page'),
    path('compare/', views.compare, name='compare-page'),
    path('base/', views.base, name='fix-page'),

]
