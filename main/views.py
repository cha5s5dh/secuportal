# main/views.py

from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

def function1(request):
    return render(request, 'main/function1.html')

def function2(request):
    return render(request, 'main/function2.html')

def function3(request):
    return render(request, 'main/function3.html')

def function4(request):
    return render(request, 'main/function4.html')
