from django.urls import path
from course_project_api import views

urlpatterns = [
    path('hello-views/', views.HelloApiView.as_view()),
]
