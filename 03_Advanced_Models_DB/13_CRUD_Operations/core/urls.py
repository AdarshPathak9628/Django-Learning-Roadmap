from django.contrib import admin
from django.urls import path
from crud_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view, name="home"),
    # STEP 3: Add Delete and Update URLs
    path('delete/<int:id>/', views.delete_data, name="deletedata"),
    path('update/<int:id>/', views.update_data, name="updatedata"),
]