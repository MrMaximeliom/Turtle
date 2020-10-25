from django.shortcuts import render
from django.utils.translation import gettext as _
from django.contrib.auth.decorators import login_required
# @login_required
def home(request):

    context = {
        'title':  _('HomePage'),
        'home' : 'active',

    }

    return render(request, 'home/home.html', context)

def about(request):
    context = {
        'title':'about',
        'about': 'active',
    }
    return render(request,'home/about.html',context)

def contact_us(request):
    context={
        'title':'Contact Us',
        'contact':'active',
    }
    return render(request,'home/contact.html',context)



def compare(request):
    return render(request, 'home/compare.html')

def base(request):
    return render(request, 'home/base.html')

