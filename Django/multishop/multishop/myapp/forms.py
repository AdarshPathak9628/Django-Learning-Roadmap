
from django import forms
from .models import admin_signupform,Category,Product,User_SignupForm,BillingAddress

class AdminSignupForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))
    class Meta:
        model = admin_signupform
        fields = ['admin_name', 'admin_phone', 'admin_username', 'admin_email', 'admin_password']
        widgets = {
            'admin_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Admin Name'}),
            'admin_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Admin Phone'}),
            'admin_username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Admin Username'}),
            'admin_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Admin Email'}),
            'admin_password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Admin Password'}),
        }


class AdminLoginForm(forms.Form):
    username = forms.CharField(
        max_length=100, 
        label="Username",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Admin Email'})
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'image', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category Name'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Category Description'}),
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'description', 'price', 'stock', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Name'}),
            'category': forms.Select(attrs={'class': 'form-control',}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Product Description'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Product Price'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Product Stock'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
        }


class BillingAddressForm(forms.ModelForm):
    class Meta:
        model = BillingAddress
        fields = [
            'first_name', 'last_name', 'email', 'phone', 
            'address', 'city', 'state', 'pin_code', 'country', 'notes'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@example.com'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+91 1234567890'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your full address'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your city name'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your state name'}),
            'pin_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your pin code'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your country'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Any special instructions for delivery'}),
        }




# admin forms end





# class OrderItemForm(forms.ModelForm):
#     class Meta:
#         model = OrderItem
#         fields = ['product_name', 'product_price', 'quantity']



#  user part start

class UserSignupForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))
    
    class Meta:
        model = User_SignupForm
        fields = [
            'user_name', 'user_phone', 'user_username', 'user_email', 
            'user_password', 'user_address', 'user_city', 'user_state', 
            'user_zipcode', 'user_country', 'date_of_birth', 'image', 'is_active'
        ]
        widgets = {
            'user_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'User Name'}),
            'user_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'User Phone'}),
            'user_username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'User Username'}),
            'user_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'User Email'}),
            'user_password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'User Password'}),
            'user_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'User Address'}),
            'user_city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'User City'}),
            'user_state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'User State'}),
            'user_zipcode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'User Zipcode'}),
            'user_country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'User Country'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date of Birth', 'type': 'date'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class UserLoginForm(forms.Form):
    user_username = forms.CharField(
        max_length=100,
        label="Username",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'})
    )
    user_password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'})
    )
