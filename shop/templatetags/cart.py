from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product,cart):
    keys = cart.keys()
    for pk in keys:
        if int(pk) == product.pk:
            return True
        return False

@register.filter(name='cart_quantity')
def cart_quantity(product,cart):
    keys =cart.keys()
    for pk in keys:
        if int(pk) == product.pk:
            return cart.get(id)
        return 0
