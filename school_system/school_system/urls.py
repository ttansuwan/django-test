"""school_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include, path
from rest_framework import routers
from rest_framework_nested import routers

from school_report.views import StudentViewSet, SchoolViewSet
from nested_school_system.views import NestedStudentViewSet

router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'schools', SchoolViewSet)

nested_router = routers.NestedSimpleRouter(router, r'schools', lookup='school')
nested_router.register(r'students', NestedStudentViewSet, basename='students')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include(nested_router.urls))
]
