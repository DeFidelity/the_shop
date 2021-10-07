from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart
from .forms import CartAddProducts
from shop.models import Product
from django.views import View


class CartAdd(View):
    def post(self,request,product_id,*args,**kwargs):
        cart = Cart(request)
        product = get_object_or_404(Product,id=product_id)
        form = CartAddProducts(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(product=product,quantity=cd['quantity'],override_quantity=True)

        return redirect('cart:cart_detail')


class CartRemove(View):
    def post(self,request,product_id,*args,**kwargs):
        cart = Cart(request)
        product = get_object_or_404(Product,id=product_id)
        cart.remove(product)

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProducts(initial={
                                                    'quantity':item['quantity'],
                                                    'override':True})
    return render(request,'cart/detail.html',{'cart':cart})
