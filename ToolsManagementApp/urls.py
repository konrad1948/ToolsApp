from django.urls import path
from .views import ToolListView


app_name = 'tools'

urlpatterns = [
    # GET  /tools/           → lista narzędzi
    path('', ToolListView.as_view(), name='tool-list'),

]
