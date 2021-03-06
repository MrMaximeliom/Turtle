from django.contrib.auth import authenticate,login as auth_login
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TeacherSignUpForm, StudentSignUpForm, loginForm
from django.utils.translation import gettext as _
from django.contrib.auth import logout
from .forms import UserUpdateForm , ProfileUpdateForm
from .models import User
from django.http import JsonResponse
from django.contrib.auth.password_validation import validate_password as validate
from django import forms

"""
تستخدم هذه الواجهة لإظهار فورم تسجيل معلم جديد
"""
def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = _('A user with this username already exists.')
    return JsonResponse(data)

def validate_password(request):
    password1 = request.GET.get('password1', None)
    data = { 'is_invalid': False, 'error_message':'error'}
    try:
        validate(password1)
    except ValidationError as error:
        data = {
        'is_invalid': True,
         'error_message':error.messages
        }
    return JsonResponse(data)

def teacher_sign_up(request):
    form = TeacherSignUpForm()
    context = {
        'title': _('SignUp Teacher'),
        'form': form,
        'user': 'teacher'
    }
    if request.method == 'POST':
        form = TeacherSignUpForm(request.POST)
        context = {
            'title': _('SignUp Teacher'),
            'form': form,
            'user': 'teacher'
        }

        if form.is_valid():
            # teacher_username = form.cleaned_data('username')
            # username = User.objects.filter(username=teacher_username)
            # if username.exists():
            #     form.
            teacher_model = form.save(commit=False)
            teacher_model.is_teacher = True
            teacher_model.save()

            messages.success(request, _('Your account has been created! you are now able to log in'))

            return redirect('login-page')

    # else:
    #     form = TeacherSignUpForm()
    return render(request, 'accounts/signup.html', context)

"""
تستخدم هذه الواجهة لإظهار فورم تسجيل طالب جديد
"""
def student_sign_up(request):
    form = StudentSignUpForm()
    context = {
        'title': _('SignUp Student'),
        'form': form,
        'user': 'student'
    }
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        context = {
            'title': _('SignUp Student'),
            'form': form,
            'user': 'student'
        }
        if form.is_valid():
            student_model = form.save(commit=False)
            student_model.is_student = True
            student_model.save()
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password')
            # user = authenticate(username=username, password=raw_password)
            messages.success(request, _('Your account has been created! you are now able to log in'))
            return redirect('login-page')

    # else:
    #     form = StudentSignUpForm()
    return render(request, 'accounts/signup.html', context)

"""
تستخدم هذه الواجهة لإظهار فورم تسجيل الدخول
"""
def login(request):
    form = loginForm()
    context = {
        'title': _('login'),
        'form': form
    }
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(username=email, password=password)

            if user:
                auth_login(request,user)
                return redirect('home-page')
            else:
                messages.error(request, _('Either username or password are wrong ! please try again ..'))
        else:
            messages.error(request, _('Either username or password are wrong ! please try again .. form is not valid'))
    return render(request, 'accounts/login.html', context)

"""
تستخدم هذه الواجهة لتسجيل الخروج من الحساب
"""
def logout_page(request):
    logout(request)
    return redirect('home-page')

def register_page(request):
    return render(request,'accounts/register.html')
"""
تستخدم هذه الواجهة لعرض فورم الملف الشخصي للمستخدم
"""
@login_required
def profile_page(request):
    context = {'title':_('Profile Page')}
    if request.method == 'POST':
        userUpdateForm = UserUpdateForm(request.POST,instance=request.user)
        profileUpdateForm = ProfileUpdateForm(request.POST,
                                              request.FILES,
                                              instance=request.user.profile)
        if userUpdateForm.is_valid() and profileUpdateForm.is_valid():
            userUpdateForm.save()
            profileUpdateForm.save()
            messages.success(request,_(f'Your account has been updated!'))
            return redirect('profile-page')
    else:
        userUpdateForm = UserUpdateForm(instance=request.user)
        profileUpdateForm = ProfileUpdateForm(instance=request.user.profile)
        context = {
        'u_form':userUpdateForm,
        'p_form':profileUpdateForm,
        'title':_('Profile Page'),
         }
    return render(request,'accounts/profile.html',context)

