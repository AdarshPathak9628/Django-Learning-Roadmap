from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # This URL takes a number (id) to identify the student
    path('delete/<int:id>/', views.delete_student, name='delete_student'),
]