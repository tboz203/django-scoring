from django.shortcuts import render

def indexView(request):
    return render(request, 'di_scoring/index.html')
