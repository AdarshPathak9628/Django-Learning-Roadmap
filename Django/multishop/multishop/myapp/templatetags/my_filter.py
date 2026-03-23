from django import template
register=template.Library()


@register.filter
def Currency(value):
    return "₹"+str(int(value))

@register.filter
def selected_product(category,product):
    for cat in category:
        print(product.category.id==cat.id)
        if product.category.id == cat.id:
            return True 
    return False

@register.filter
def multiply(price, qty):
    sub = price * qty
    return sub

@register.filter
def total(cart_storage):
    s = 0
    for cart in cart_storage:
        s =s + cart.product.price * cart.product_qty
    return s 

@register.filter
def shipping_charge(cart_storage):
    gt =total(cart_storage) 
    if gt <= 1000:
        return 100
    else:
        return 0
    
@register.filter
def grand_total(cart_storage):
    gt =total(cart_storage)
    qt=shipping_charge(cart_storage)
    return gt + qt

@register.filter
def cart_counter(cart_storage):
    s=0
    for i in cart_storage:
        s=s+1

    
    return s

        

    # s = 0
    # for cart in cart_storage:
    #     s =s + cart.product.price * cart.product_qty
    #     if s >= 1000:
    #         return s + 100
    
    #     else:
    #         return s
        

