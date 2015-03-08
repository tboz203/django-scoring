from django.shortcuts import render

def index(request):
    return render(request, 'di_scoring/index.html')
