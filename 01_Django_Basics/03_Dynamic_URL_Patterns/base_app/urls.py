from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    # STEP 3: Path Converters <type:variable_name>
    path('user/<str:username>/', views.user_view, name='user_profile'),
    path('roll/<int:roll_no>/', views.roll_view, name='student_info'),
]