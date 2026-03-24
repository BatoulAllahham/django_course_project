from django.urls import path, include
from course_project_api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register('profile',views.UserProfileViewSet)

urlpatterns = [
    path('hello-views/', views.HelloApiView.as_view()),
    path('', include(router.urls))
]
