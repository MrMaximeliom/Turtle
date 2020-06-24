from django.shortcuts import render

# Create your views here.

def privacy_policy(request):
    return render(request,'support/privacy_policy.html')

def cookies_policy(request):
    return render(request,'support/cookies_policy.html')

def terms_and_conditions(request):
    return render(request,'support/terms_and_conditions.html')