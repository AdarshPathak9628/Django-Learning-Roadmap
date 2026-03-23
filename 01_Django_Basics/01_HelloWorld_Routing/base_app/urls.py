from django.urls import path
from . import views

urlpatterns = [
    # STEP 5: Mapping empty path to our home function
    path('', views.home_view, name='home_page'),
]