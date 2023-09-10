"""
URL configuration for company project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# from api.views import employeelist
from api.views import *

from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('manager',ManagerViewSet,basename='man')
router.register('manmv',ManagerViewSet,basename='manmv')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('emp',employeelist),
    path('emp',EmployeeView.as_view()),
    path('emp/<int:id>',EmployeeSpecific.as_view()),
    path('employee',EmpView.as_view()),
    path('employee/<int:id>',EmpspecificView.as_view()),
    path('man',ManagerView.as_view()),
]+router.urls
