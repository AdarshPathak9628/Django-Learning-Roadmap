from django.db import models
from django.utils import timezone

# Create your models here.

#  admin modals are start

class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='category_images/')
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='products_images/')

    def __str__(self):
        return self.name

class admin_signupform(models.Model):
    admin_name=models.CharField(max_length=100)
    admin_phone=models.CharField(max_length=100)
    admin_username=models.CharField(max_length=100)
    admin_email=models.CharField(max_length=100)
    admin_password=models.CharField(max_length=100) 

class vendor_images(models.Model):
   name = models.CharField(max_length=255)
   image = models.ImageField(upload_to='vendor_images/')





# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
#     product_name = models.CharField(max_length=100)
#     product_price = models.DecimalField(max_digits=10, decimal_places=2)
#     quantity = models.PositiveIntegerField(default=1)


# admin model ends






# user model start

class User_SignupForm(models.Model):
    user_name = models.CharField(max_length=100)
    user_phone = models.CharField(max_length=100)
    user_username = models.CharField(max_length=100)
    user_email = models.CharField(max_length=100)
    user_password = models.CharField(max_length=100)
    
    # Additional columns
    user_address = models.CharField(max_length=255, blank=True, null=True)
    user_city = models.CharField(max_length=100, blank=True, null=True)
    user_state = models.CharField(max_length=100, blank=True, null=True)
    user_zipcode = models.CharField(max_length=20, blank=True, null=True)
    user_country = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='user_profile_image/', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.user_username
    
class cart_storage(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    cust = models.ForeignKey(User_SignupForm,on_delete=models.CASCADE)
    product_qty = models.IntegerField(default=1)

class BillingAddress(models.Model):
    user_id= models.ForeignKey(User_SignupForm, on_delete=models.CASCADE, related_name='user',null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pin_code = models.CharField(max_length=10)
    country = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    


class Order(models.Model):
    user = models.ForeignKey(User_SignupForm, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    category_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Order {self.id} by {self.user}'