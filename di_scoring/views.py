from django.shortcuts import render
from django.views.generic import ListView, DetailView
from di_scoring import models


def indexView(request):
    return render(request, 'di_scoring/index.html')

class TeamListView(ListView):
    model = models.Team

class TeamDetailView(DetailView):
    model = models.Team
    slug_field = 'name'
