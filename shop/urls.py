from django.urls import path
from shop.views import (IndexView, ProductDetailView,
                        BlogDetailView,BlogListView,
                        ProductListView,CustomerProfilesView,
                        ProfileEditView,BlogLikeView,
                        ProductLikeView,AboutUsView)

urlpatterns =[
    path('',IndexView.as_view(),name='index'),
    path('detail-for-product/<int:pk>/',ProductDetailView.as_view(),name='product_detail'),
    path('detail-for-post/<int:pk>/',BlogDetailView.as_view(),name='blog_detail'),
    path('posts-list/',BlogListView.as_view(),name='blog_list'),
    path('product-list/',ProductListView.as_view(),name='product_list'),
    path('profile/<int:pk>',CustomerProfilesView.as_view(),name='profile'),
    path('profile-edit/<int:pk>/',ProfileEditView.as_view(),name='profile_edit'),
    path('blog/<int:pk>/like',BlogLikeView.as_view(),name='blog_like'),
    path('product/<int:pk>/like',ProductLikeView.as_view(),name='product_like'),
    path('about/',AboutUsView.as_view(),name='about_us')
    # cart urls
    ]
