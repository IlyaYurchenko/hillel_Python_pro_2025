from django.urls import path

from .  import views

urlpatterns = [
    path('', views.teacher_dashboard, name='teacher_dashboard'),
    path('lessons/<int:id>/', views.lesson_details, name='lessons_detail'),
    path('lessons/<int: lesson_id/set_grade', views.set_grade, name='set_grade'),
]