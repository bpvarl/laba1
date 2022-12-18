"""hous URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from building.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('lesson/', lesson, name='lesson'),
    path('contact/', contact, name='contact'),
    path('lesson/contact/', contact, name='contact'),
    path('lesson/chemical/', chemical, name='chemical'),
    path('lesson/english/', english, name='english'),
    path('lesson/math/', math, name='math'),
    path('lesson/physics/', physics, name='physics'),
    path('lesson/rus/', rus_language, name='rus'),
    path('lesson/biology/', biology, name='biology'),
]
