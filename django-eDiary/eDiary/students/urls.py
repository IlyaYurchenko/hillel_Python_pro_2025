from django.urls import path

from .  import views

urlpatterns = [
    path('', views.students_main_page, name='index'),
    path('lessons/', views.lessons_list, name='lessons'),
    path('lessons/<int:id>/', views.lessons_detail, name='lessons_detail'),
    path('my_grades/', views.my_grades_main_page, name='my_grades'),
]