from django.shortcuts import render

# ray test added
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "home.html" # ray test extension is a must