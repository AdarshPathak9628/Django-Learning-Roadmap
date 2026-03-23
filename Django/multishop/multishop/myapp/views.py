from django.shortcuts import render,redirect
from .forms import AdminSignupForm,AdminLoginForm,CategoryForm,ProductForm ,UserSignupForm,UserLoginForm,BillingAddressForm
from django.contrib.auth import authenticate, login
from .models import admin_signupform,Product,Category,vendor_images,User_SignupForm,cart_storage,BillingAddress,Order
from django.views import View
import os
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone

# Create your views here.



##  admin part start

def admin_signup(request):
    if request.session.get('admin_id'):
        if request.method == 'POST':
            form = AdminSignupForm(request.POST)
            if form.is_valid():
                # Check if password matches confirm password
                username= form.cleaned_data.get('admin_username')
                password = form.cleaned_data.get('admin_password')
                confirm_password = form.cleaned_data.get('confirm_password')
                user = None
                try:
                    user = admin_signupform.objects.get(admin_username=username)
                except Exception as msg:
                    print(msg)
                if user:
                    form.add_error('admin_username', "username  match.")
                else:
                    if password == confirm_password:
                        form.save()
                        return redirect('admin_login')  
                    else:
                        form.add_error('confirm_password', "Passwords do not match.")
        else:
            form = AdminSignupForm()
        
        return render(request, 'admin/admin_signup.html', {'form': form})
    else:
        return redirect('admin_login')

def admin_login(request):
    if request.method == 'POST':
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(email,"hello")
            try:
                user = admin_signupform.objects.get(admin_email=email)
            except admin_signupform.DoesNotExist:
                user = None
            try:
                if user.admin_email==email and user.admin_password==str(password):
                    request.session['admin_id'] = user.id
                    request.session['admin_username'] = user.admin_username
                    request.session['admin_email'] = user.admin_email
                    return redirect('admin_dashboard')
                else:
                    form.add_error(None, "Invalid username or password")
            except:
                form.add_error(None, "Invalid username or password")
    else:
        form = AdminLoginForm()
    return render(request, 'admin/admin_login.html', {'form': form})

@login_required(login_url='admin_login')
def admin_logout(request):
    try:
        del request.session['admin_id']
        del request.session['admin_username']
        del request.session['admin_email']
    except KeyError:
        pass  
    # request.session.fluse()
    return redirect('admin_login')
    
   
def admin_dashboard(request):
    if request.session.get('admin_id'):
        return render(request,'admin/admin_dashboard.html') 
    else:
        return redirect('admin_login')
   

def add_category(request):
    if request.session.get('admin_id'):
        if request.method == 'POST':
            fm = CategoryForm(request.POST, request.FILES)
            if fm.is_valid():
                fm.save()
                return redirect('category_list')
        else:
            fm = CategoryForm()
        return render(request, 'admin/add_category.html', {'form': fm})
    else:
        return redirect('admin_login')
    
def edit_category(request, id):
    if request.session.get('admin_id'):
        try:
            cat = Category.objects.get(id=id)  # Retrieve the category object
        except Category.DoesNotExist:
            return redirect('category_list')  # Redirect if the category does not exist

        if request.method == 'POST':
            fm = CategoryForm(request.POST, request.FILES, instance=cat)  # Pass the category instance to the form
            if fm.is_valid():
                fm.save()
                return redirect('category_list')
        else:
            fm = CategoryForm(instance=cat)  # Pre-populate the form with the existing category data
        return render(request, 'admin/edit_category.html', {'form': fm, 'edit': cat})
    else:
        return redirect('admin_login')
    
def delete_category(request,id):
    try:
        cat = Category.objects.get(id=id)
        print('hello i am first')
        if request.method == "POST":
            print('hello i am second')
            cat.delete()
            os.remove(cat.image.path)
            categories=Category.objects.all()
            return render(request,'admin/category_list.html',{'categories': categories}) 
        
    except Category.DoesNotExist:
        pass
    return redirect('category_list') 
    
def category_list(request):
    if request.session.get('admin_id'):   
        categories = Category.objects.all()
        return render(request, 'admin/category_list.html', {'categories': categories})
    else:
        return redirect('admin_login')

def add_product(request):
    if request.session.get('admin_id'):
        if request.method == 'POST':
            fm = ProductForm(request.POST, request.FILES)
            if fm.is_valid():
                fm.save()
                return redirect('product_list')
        else:
            fm = ProductForm()

        cats = Category.objects.all()
        context = {
            'form': fm,
            'cats': cats
        }
        return render(request, 'admin/add_product.html', context)
    else:
        return redirect('admin_login')
    

def edit_product(request, id):
    if request.session.get('admin_id'):
        try:
            product = Product.objects.get(id=id)  
        except Product.DoesNotExist:
            return redirect('product_list')  

        if request.method == 'POST':
            fm = ProductForm(request.POST, request.FILES, instance=product)  # Pass the product instance to the form
            if fm.is_valid():
                fm.save()
                return redirect('product_list')
        else:
            fm = ProductForm(instance=product)  # Pre-populate the form with the existing product data
        return render(request, 'admin/edit_product.html', {'form': fm, 'edit': product})
    else:
        return redirect('admin_login')



def product_list(request):
    if request.session.get('admin_id'):
        products = Product.objects.all()
        return render(request, 'admin/product_list.html', {'products': products})
    else:
        return redirect('admin_login')



def profile(request):
    if request.session.get('admin_id'):
        return render(request, 'admin/profile.html')
    
    else:
        return redirect('admin_login')


def customer_view(request):
    if request.session.get('admin_id'):
        products = Product.objects.all()
        return render(request,'admin/customer_view.html', {'products': products})
    else:
        return redirect('admin_login')

    



def vendor_images_list(request):
    if request.session.get('admin_id'):
        Vendor_Images = vendor_images.objects.all()
        return render(request,'admin/vendor.html',{'vendor_images':Vendor_Images})
    else:
        return redirect('admin_login')

#   admin part ends













# user part start

def user_signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST, request.FILES)
        if form.is_valid():
            username= form.cleaned_data.get('user_username')
            password = form.cleaned_data.get('user_password')
            confirm_password = form.cleaned_data.get('confirm_password')
            user=None

            try:
                user = User_SignupForm.objects.get(user_username=username)
                form.add_error('user_username', "Username is already in use.")
            except User_SignupForm.DoesNotExist:
                user = None
            if not user:
                if password == confirm_password:
                    form.save()
                    return redirect('user_login')
                else:
                    form.add_error('confirm_password', "Passwords do not match.") 
                
    else:
        form = UserSignupForm()
    return render(request,'user/user_signup.html',{'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('user_username')
            password = form.cleaned_data.get('user_password')
            print(username,"hello")
            try:
                user = User_SignupForm.objects.get(user_username=username)
            except User_SignupForm.DoesNotExist:
                user = None

            if user is not None:
                if user.user_password == str(password):
                    request.session['user_id'] = user.id
                    request.session['user_username'] = user.user_username
                    request.session['user_email'] = user.user_email
                    return redirect('user_index')
                else:
                    form.add_error(None, "Invalid password")
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = UserLoginForm()
    return render(request, 'user/user_login.html', {'form': form})

def user_logout(request):
    # request.session.clear()
    try:
        del request.session['user_id']
        del request.session['user_username']
        del request.session['user_email']
    except KeyError:
        pass  
    # request.session.fluse()
    return redirect('user_index')

def user_index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    Vendor_Images = vendor_images.objects.all()  # Ensure the model name is correct
    context = {
        'categories': categories,
        'products': products,
        'vendor_images': Vendor_Images
    }
    return render(request, 'user/index.html', context)

def user_shop(request):
    if request.GET.get('p_id'):
        p_id = request.GET.get('p_id')
        user=request.session['user_id']
        print(p_id,type(p_id),user,type(user))
        cart_obj=None
        try:
            cart_obj = cart_storage.objects.get(product_id=p_id,cust_id=user)
        except:
            print("Not in cart ")
        if cart_obj==None:
            pro_instance = Product.objects.get(id=p_id)
            cust_instance = User_SignupForm.objects.get(id=user)
            store = cart_storage(product=pro_instance, cust=cust_instance, product_qty=1)
            store.save()
    categories = Category.objects.all()
    products = Product.objects.all()
    Vendor_Images = vendor_images.objects.all()
    
    if request.GET.get('cat'):
        cat_id = request.GET.get('cat')
        categories = Category.objects.filter(id=cat_id)
    context = {
        'categories': categories,
        'products': products,
        'vendor_images': Vendor_Images,
        
    }
    print(categories)
    return render(request,'user/shop.html', context)

def shop_detail(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    Vendor_Images = vendor_images.objects.all()  # Ensure the model name is correct
    context = {
        'categories': categories,
        'products': products,
        'vendor_images': Vendor_Images
    }
    return render(request,'user/shop_details.html',context)


def cart(request):

    if request.session.get('user_id'):
        user=request.session['user_id']
        Cart_Storage = cart_storage.objects.filter(cust=user)
        context = {
        'cart_storage': Cart_Storage,
        }
        return render(request,'user/cart.html',context)
    return render(request,'user/cart.html')

def checkout(request):
    valid_payment='False'
    if request.session.get('user_id'):
        user=request.session['user_id']
        try:
            billing_address = BillingAddress.objects.get(user_id=user)
        except BillingAddress.DoesNotExist:
            billing_address = None
        if request.method == 'POST':
            print('jiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii')
            form = BillingAddressForm(request.POST, instance=billing_address)
            payment_option = request.POST.get('payment')
            valid_payment = request.POST.get('valid_payment')
            print(request.POST)
            if form.is_valid() and not bool(request.POST.get('valid_payment')):
                valid_payment='True'
                print('hhhhhhhhhhhhhhhhhhhhhhhhhhhh')
                billing_address = form.save(commit=False)
                userr=User_SignupForm.objects.get(id=user)
                billing_address.user_id = userr
                billing_address.save()
                print('helooo======================================')
                           
            if payment_option == 'banktransfer' and bool(request.POST.get('valid_payment')):
                cart_items = cart_storage.objects.filter(cust=user)
                print('hiiiiiiiiiiiiiii==============================')
                for item in cart_items:
                    Order.objects.create(
                        user=user,
                        product=item.product,
                        product_name=item.product.name,
                        category_name=item.product.category.name,
                        quantity=item.product_qty,
                        price=item.product.price,
                        created_at=timezone.localtime()
                    )
                    print('====================================')
                    
                    cart_items.delete()
                    messages.success(request, 'Order successfully placed!')
                    return redirect('checkout')
                else:
                    messages.error(request, 'Please select a valid payment option.')
                    return redirect('checkout')                
            else:
                print('eeeeeeeeeeeeeeeeeeee===========================')
                messages.error(request, 'Invalid form submission or payment option.')
        else:
            form = BillingAddressForm(instance=billing_address)

        
        Cart_Storage = cart_storage.objects.filter(cust=user)
        context = {
        'form': form,
        'cart_storage': Cart_Storage,
        'valid_payment':valid_payment
        }
        return render(request,'user/checkout.html',context)
    else:
        return render(request,'user/user_login.html')

def contact(request):
    return render(request,'user/contact.html')

def user_profile(request):
    return render(request,'user/user_profile.html')


def cart_edit(request):
    if request.method == "POST":
        cust_id = request.session['user_id']
        if 'minus' in request.POST:
            id = request.POST['minus']
            print("minus =====================",id)
            cart_obj = cart_storage.objects.get(product_id=id,cust_id=cust_id)
            if cart_obj.product_qty == 1:
                cart_obj.delete()
            else:
                cart_obj.product_qty -= 1
                cart_obj.save()
        elif 'plus' in request.POST:
            id = request.POST['plus']
            print("plus ==========================",id)
            cart_obj = cart_storage.objects.get(product_id=id,cust_id=cust_id)
            cart_obj.product_qty += 1
            cart_obj.save()
    return redirect('/cart/')


def delete_view(request, id):
    try:
        item = cart_storage.objects.get(id=id)

        if request.method == "POST":
            item.delete()
            return redirect('cart') 
    except cart_storage.DoesNotExist:
        pass
    return redirect('cart') 




# def checkout(request):
#     if request.method == 'POST':
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             order = form.save()
#             # Add order items (hardcoded for now, should be dynamically generated)
#             OrderItem.objects.create(order=order, product_name='Product Name 1', product_price=150, quantity=1)
#             OrderItem.objects.create(order=order, product_name='Product Name 2', product_price=150, quantity=1)
#             OrderItem.objects.create(order=order, product_name='Product Name 3', product_price=150, quantity=1)
#             return redirect('order_success')
#     else:
#         form = OrderForm()
#     return render(request, 'checkout.html', {'form': form})


# user part ends