"""
URL configuration for ToolsApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from ToolsManagementApp.views import HomePageView

urlpatterns = [
    # strona główna projektu
    path('',   HomePageView.as_view(), name='home'),

    # panel admina
    path('admin/', admin.site.urls),

    # wszystkie URL-e z aplikacji “ToolsManagementApp” pod /tools/
    path('tools/', include('ToolsManagementApp.urls', namespace='tools')),
]

# tylko w DEBUG-u serwujemy MEDIA
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)