from django.shortcuts import render

def index(request):
    return render(request, 'board2/index.html')
