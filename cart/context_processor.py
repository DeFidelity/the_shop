from cart.cart import Cart
def cart(request):
    cart = Cart(request)
    total_item = len(cart)
    return {'cart':cart,'total_item':total_item}
