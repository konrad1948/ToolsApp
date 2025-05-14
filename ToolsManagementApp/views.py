from django.shortcuts import render
from .models import AddTool
from django.views.generic import ListView
from django.views.generic import TemplateView

class ToolListView(ListView):
    model = AddTool
    template_name = 'tools_list.html'
    context_object_name = 'tools'
    
    
class HomePageView(TemplateView):
    template_name = 'home.html'