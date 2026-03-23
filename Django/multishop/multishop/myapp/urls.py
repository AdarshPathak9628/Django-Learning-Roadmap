from django.urls import path
from . import views

urlpatterns = [

#   admin part start
    
    path('admin_signup/', views.admin_signup, name='admin_signup'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_logout/', views.admin_logout, name='admin_logout'),
    path('admin_dashboard/',views.admin_dashboard,name='admin_dashboard'),
    path('add_category/', views.add_category, name='add_category'),
    path('category_list/', views.category_list, name='category_list'),
    path('edit_cat/<int:id>',views.edit_category,name='edit_cat'),
    path('delete_cat/<int:id>',views.delete_category,name='delete_cat'),
    path('add_product/', views.add_product, name='add_product'),
    path('product_list/',views.product_list, name='product_list'),
    path('edit_pro/<int:id>',views.edit_product,name='edit_pro'),
    path('customer_view/', views.customer_view, name='customer_view'),
    path('vendor_images/',views.vendor_images_list, name='vendor_images'),
    path('profile/', views.profile, name='profile'),


#   admin part ends



#   user part start
    
    path('',views.user_index,name='user_index'),
    path('user_signup/',views.user_signup,name='user_signup'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('user_shop/',views.user_shop,name='user_shop'),
    path('user_shop_details/',views.shop_detail,name='user_shop_details'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('contact/',views.contact,name='contact'),
    path('user_profile/',views.user_profile,name='user_profile'),
    path('edit_view/',views.cart_edit,name='edit_view'),
    path('delete/<int:id>',views.delete_view,name='delete'),
    

    # path('order-success/', views.order_success, name='order_success'), 

#  user part ends 
]
