from django.shortcuts import render


def error_404(request,exception):
    return render(request,'errors/error_404.html',status = 404)


def error_500(request):
    return render(request,'errors/error_500.html',status = 500)

def error_403(request,exception):
    return render(request,'errors/error_403.html',status = 403)

def error_400(request,exception):
    return render(request,'errors/error_400.html',status = 403)

