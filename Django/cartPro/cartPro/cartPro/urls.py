"""cartPro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Index.as_view(),name='index'),
    path('adminlogin/',views.admin_login,name='adminlogin'),
    path('dashboard/',views.dashboard_view,name='dashboard'),
    path('addproduct/',views.addproduct_view,name='addproduct'),
    path('viewproduct/',views.viewproduct_view,name='viewproduct'),
    path('deleteproduct/<id>',views.deleteproduct_view,name='deleteproduct'),
    path('addcategory/',views.addcategory_view,name='addcategory'),
    path('userlogin/',views.userlogin_view,name='userlogin'),
    path('signup/',views.signup_view,name='signup'),
    path('logout/',views.logout_view,name='logout'),
    path('cart/',views.cart_view,name='cart'),
 


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
