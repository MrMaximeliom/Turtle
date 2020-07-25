from django.urls import path,include
from . import  views

urlpatterns = [
      path('privacy-policy/',views.privacy_policy,name='privacy-policy-page'),
      path('cookies-policy/',views.cookies_policy,name='cookies-policy-page'),
      path('terms-and-conditions/',views.terms_and_conditions,name='terms-and-conditions-page'),

    ]