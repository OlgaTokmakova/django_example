from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('course/<slug>', views.CourseDetailPage.as_view(), name='course-detail'),
    path('course/<slug>/<lesson_slug>', views.LessonDetailPage.as_view(), name='lesson-detail'),
    path('add-course', views.CourseAdd.as_view(), name='add-course')
]
