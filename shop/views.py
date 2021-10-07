from django.shortcuts import render,get_object_or_404,redirect
from django.views import View
from django.views.generic import DetailView,ListView,UpdateView,TemplateView
from .models import Product, Blog,Comment,CustomerProfiles,Promotion
from .forms import CommentForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from cart.forms import CartAddProducts

class IndexView(View):
    def get(self,request,*args,**kwargs):
        products = Product.objects.all()
        blog = Blog.objects.all()
        promotion = Promotion.objects.all()
        latest_products= Product.objects.all().order_by('date_added')
        # lengend_image = products.create(legend_image=)

        context ={
            'products':products,
            'blogs': blog,
            'promotion':promotion,
            'latests':latest_products
        }
        return render(request,'shop/index.html',context)
class ProductDetailView(View):
    def get(self,request,pk,*args,**kwargs):
        product = get_object_or_404(Product,pk=pk)
        products = Product.objects.all()[:5]
        related_products = Product.objects.filter(category=product.category)
        cart_add_form = CartAddProducts()
        blogs = Blog.objects.all()
        context = {
            'product':product,
            'products':products,
            'blogs':blogs,
            'related_products':related_products,
            'cart_add_form':cart_add_form,
        }
        return render(request,'shop/product-details.html',context)

    def post(self,request,pk,*args,**kwargs):
        product = get_object_or_404(Product,pk=pk)
        products = Product.objects.all()
        related_products = Product.objects.filter(category=category)
        num_to_cart = request.GET.get('item_num')

        context = {
            'product':product,
            'products':products,
            'related_products':related_products,
        }
        return render(request,'shop/product-details.html',context)


class BlogDetailView(View):
    def get(self,request,pk,*args,**kwargs):
        post = get_object_or_404(Blog,pk=pk)
        other_posts = Blog.objects.all().order_by('-time_created')[:5]
        comments = Comment.objects.filter(post=post)
        product = Product.objects.all()
        form = CommentForm()

        context ={
            'post':post,
            'other_posts':other_posts,
            'comments':comments,
            'form':form,
            'products':product,
        }
        return render(request,'shop/blog_detail.html',context)

    def post(self,request,pk,*args,**kwargs):
        post = get_object_or_404(Blog,pk=pk)
        other_posts = Blog.objects.all().order_by('-time_created')[:5]
        comments = Comment.objects.filter(post=post)
        form = CommentForm(request.POST)
        product = Product.objects.all()

        if form.is_valid():
            new_comment = Comment(
                comment_author = request.POST.get('author'),
                comment_body = request.POST.get('body'),
                post = post,
            )
            new_comment.save()

        context ={
            'post':post,
            'other_posts':other_posts,
            'comments':comments,
            'form':form,
            'products':product,
        }
        return rendirect('blog_detail')
class BlogListView(ListView):
    context_object_name = 'blogs'
    model = Blog
    page_kwarg = 'page'
    paginate_by = 50
    template_name = 'blog_list.html'


class ProductListView(ListView):
    context_object_name = 'products'
    model = Product
    page_kwarg = 'page'
    paginate_by = 50
    template_name = 'product_list.html'

class ProfileView(View):
    pass

class CustomerProfilesView(View, LoginRequiredMixin, UserPassesTestMixin):
    def get(self,request,pk,*args,**kawrgs):
        profile = CustomerProfiles.objects.get(pk=pk)
        user = profile.user
        liked_products = Product.objects.filter(product_likes__in=[user])

        context = {
            'profile':profile,
            'customer':user,
            'liked_products':liked_products,
        }
        def test_func(self):
                user_profile = self.get_object()
                return self.request.user  == user_profile.customer_name
        return render(request,'shop/customer_profile.html',context)

class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = CustomerProfiles
    fields = ['user','country','address','city','address_description','phone_number']
    template_name = 'shop/profile_edit.html'
    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('profile',kwargs={'pk':pk})
    def test_func(self):
            user_profile = self.get_object()
            return self.request.user  == user_profile.user

class BlogLikeView(View):
    def post(self,request,pk,*args,**kwargs):
        blog = Blog.objects.get(pk=pk)
        its_liked = False
        for like in blog.likes.all():
            if like == request.user:
                its_liked = True
                break
        if its_liked:
            blog.likes.remove(request.user)
        if not its_liked:
            blog.likes.add(request.user)

        next = request.POST.get('next','/')
        return HttpResponseRedirect(next)

class ProductLikeView(View):
    def post(self,request,pk,*args,**kwargs):
        product = Product.objects.get(pk=pk)
        its_liked = False
        for like in product.product_likes.all():
            if like == request.user:
                its_liked = True
                break
        if its_liked:
            product.product_likes.remove(request.user)
        if not its_liked:
            product.product_likes.add(request.user)

        next = request.POST.get('next','/')
        return HttpResponseRedirect(next)

class AboutUsView(TemplateView):
    template_name = 'shop/about.html'
