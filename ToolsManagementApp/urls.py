from django.urls import path
from .views import ToolListView, ToolCreateView, ToolUpdateView, ToolDeleteView, ToolDetailView


app_name = 'tools'

urlpatterns = [
    # GET  /tools/           → lista narzędzi
    path('', ToolListView.as_view(), name='tool-list'),
    # GET  /tools/add/      → formularz dodawania narzędzia
    path('add/', ToolCreateView.as_view(), name='tool-add'),
    
    path('<int:pk>/',    ToolDetailView.as_view(), name='tool-detail'),
    path('<int:pk>/edit/',   ToolUpdateView.as_view(), name='tool-edit'),
    path('<int:pk>/delete/', ToolDeleteView.as_view(), name='tool-delete'),
]
