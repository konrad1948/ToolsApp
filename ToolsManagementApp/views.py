from django.urls import reverse_lazy
from .models import AddTool
from django.views.generic import ListView, CreateView, TemplateView, DetailView, UpdateView, DeleteView

class ToolCreateView(CreateView):
    model = AddTool
    fields = ['name','description','quantity','price','image']
    template_name = 'tools/tool_form.html'      # <— własny formularz
    success_url = reverse_lazy('tools:tool-list')
    
class ToolListView(ListView):
    model = AddTool
    context_object_name = 'tools'               # w template: użyjesz {{ tools }}
    template_name = 'tools/tool_list.html' 
    
class ToolDetailView(DetailView):
    model = AddTool
    context_object_name = 'tool'                # w template: użyjesz {{ tool }}
    template_name = 'tools/tool_detail.html'     # <— własny szablon
    
class ToolUpdateView(UpdateView):
    model = AddTool
    fields = ['name','description','quantity','price','image']
    template_name = 'tools/tool_form.html'      # <— własny formularz
    success_url = reverse_lazy('tools:tool-list')
    
class ToolDeleteView(DeleteView):
    model = AddTool
    template_name = 'tools/tool_confirm_delete.html'
    success_url = reverse_lazy('tools:tool-list')
    
class HomePageView(TemplateView):
    template_name = 'home.html'