# urls
path('cart/', views.ListCart, name='list-carts'),
path('cart/<int:pk>/', views.DetailCart.as_view(), name='detail-cart'),
path('cart/create/', views.CreateCart.as_view(), name='create-cart'),
path('cart/<int:pk>/update/', views.Updatecart.as_view(), name='update-cart'),
path('cart/<int:pk>/delete/', views.DeleteCart.as_view(), name='delete-cart'),

# CartItem Urls

path('cartitem/', views.ListCartItem.as_view(), name='list-cartitem'),
path('cartitem/<int:pk>/', views.DetailCartItem.as_view(), name='detail-cartitem'),
path('cartitem/create/', views.CreateCartItem.as_view(), name='create-cartitem'),
path('cartitem/<int:pk>/update/', views.UpdateCartItem.as_view(), name='update-cartitem'),
path('cartitem/<int:pk>/delete/', views.DeleteCartItem.as_view(), name='delete-cartitem'),


# views:
class CartItemView(View,LoginRequiredMixin,UserPassesTestMixin):
    def get(self,request,*args,**kwargs):
        cart = CartItem.objects.filter(cart__user = request.user)
        cart.price = cart.product.discount_price
        cart.save()

        context = {
            'cart':cart,
        }
        return render(request,'shop/cart.html',context)

    def post(self,request,pk,*args,**kwargs):
        cart = CartItem.objects.filter(cart__user = [request.user])
        cart.quantity = request.GET.get('quantity')
        cart.price = cart.product.discount_price
        cart.save()
        price = cart.price_ttc()

        context ={
            'cart':cart,
            'price':price,
        }
        return redirect('cart',pk=pk)

    def delete(self,request,pk,*args,**kwargs):
        cart = CartItem.objects.get(pk=pk)
        cart.delete()
        return redirect(cart,pk=pk)

    def test_func(self):
        user_profile = self.get_object()
        return self.request.user  == user_profile.cart.user

class AddToCart(View):
    pass


class AddToCart(View):
    def post(self,request,pk,*args,**kwargs):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')

        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity -1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        return redirect(product_detail)


# cut template
{% if product|is_in_cart:request.session.cart %}
    <div class="row no-gutters">
      <form class="col-lg-2" action="" method="POST">
        {% csrf_token %}
        <input hidden type="text" name="product" value="{{product.pk}}">
        <input hidden type="text" name="remove" value="True">
        <input type="submit" name="" class="btn col-lg-2 btn-block" value="-">
      </form>
        <div class="text-center mt-2 text-white col">{{product|cart_quantity:request.session.cart}} in cart</div>
    <form class="col-lg-2" action="" method="POST">
      {% csrf_token %}
      <input hidden type="text" name="product" value="{{product.pk}}">
      <input type="submit" name="" class="btn col-lg-2 btn-block" value="+">
    </form>
    </div>
{% else %}
<form action="" method="POST" class="btn">
  {% csrf_token %}
  <input hidden type="text" name="product" value="{{product.pk}}">
  <input type="submit" class="btn" name="" value="Add to Cart">
</form>
{% endif %}

# models
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.FloatField(blank=True)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)


    def price_ttc(self):
        return self.price * self.quantity

    def __str__(self):
        return  self.customer_name + " - " + self.product
