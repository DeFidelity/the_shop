from django.urls import path
from .views import CartAdd,CartRemove,cart_detail

app_name='cart'
urlpatterns=[
    path('',cart_detail,name='cart_detail'),
    path('add/<int:product_id>',CartAdd.as_view(),name='cart_add'),
    path('remove/<int:product_id>',CartRemove.as_view(),name='cart_remove')
]
