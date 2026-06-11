"""
URL configuration for demo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from student.views import *
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
routes=DefaultRouter()
routes.register('teacher',TeachersViewSet,basename="teach")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('first',firstRequest),
    path('postexample',postExample),
    path('putexample',putExample),
    path('student',StudentApiView.as_view()),
    path('student/<int:id>',SpecificStudentView.as_view()),
    path('assignment',AssignmentView.as_view()),
    path('assignment/<int:pk>',SpecificAssignmentView.as_view()),
    # path('todo',TodoView.as_view()),
    # path('todo/<int:pk>',SpecificTodoView.as_view())
    path('todo',TodoView.as_view()),
    path('todo/<int:pk>',SpecificTodoView.as_view()),
    # path('teachers', TeacherView.as_view()),

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
]+routes.urls
    