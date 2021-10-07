from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from ckeditor.fields import RichTextField


class CustomerProfiles(models.Model):
     user = models.OneToOneField(User, primary_key=True, verbose_name='user',related_name='profile',on_delete=models.CASCADE)
     full_name = models.CharField(max_length=50,blank=True,null=True)
     country = models.CharField(max_length=50,blank=True,null=True)
     address = models.CharField(max_length=100,null=True,blank=True)
     email = models.EmailField(blank=True,null=True)
     city = models.CharField(max_length=50,null=True,blank=True)
     address_description = models.CharField(max_length=1000,null=True,blank=True)
     phone_number = models.IntegerField(blank=True,null=True)

     def __str__(self):
         return str(self.user)

@receiver(post_save,sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        CustomerProfiles.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance,**kwargs):
    instance.profile.save()

class Product(models.Model):
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    product_name = models.CharField(max_length=150,blank=False,null=False,verbose_name='product')
    date_added = models.DateTimeField(default=timezone.now)
    product_description = RichTextField(blank=False,null=False)
    product_price = models.FloatField(blank=False,null=False)
    product_image = models.CharField(max_length=350,default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTtav_T24wgWwQXtL5_CSuCahv5jT_q0ZXKNw&usqp=CAU')
    discount_price = models.FloatField(blank=True,null=True)
    product_likes = models.ManyToManyField(User,blank=True,related_name='product_likes')

    class Meta:
        ordering = ['-date_added']
    def __str__(self):
        return self.product_name

class Blog(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    featured_image=models.CharField(max_length=350,default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSfYcwp8-22XlEX4lZe_PM6PeNoFy5EMgdQMw&usqp=CAU")
    title = models.CharField(max_length=150,null=False,blank=False)
    time_created = models.DateTimeField(default=timezone.now)
    body = RichTextField(blank=False,null=False)
    likes = models.ManyToManyField(User,related_name='likes',blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('Blog',on_delete=models.CASCADE)
    comment_author = models.CharField(max_length=30,blank=False,default='Anon Visitor')
    comment_body = models.TextField()
    created_time = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_time']

    def __str__(self) -> str:
        return self.comment_author

class Category(models.Model):
    category_name = models.CharField(max_length=100, default='product')

    def __str__(self):
        return self.category_name

class Promotion(models.Model):
    header_legend = models.CharField(max_length=300,null=False,default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTtav_T24wgWwQXtL5_CSuCahv5jT_q0ZXKNw&usqp=CAU')
    legend_text = RichTextField(blank=False,null=False,default='70% Off')
    second_level_one = models.CharField(max_length=300,null=False,default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTtav_T24wgWwQXtL5_CSuCahv5jT_q0ZXKNw&usqp=CAU')
    second_level_two = models.CharField(max_length=300,null=False,default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTtav_T24wgWwQXtL5_CSuCahv5jT_q0ZXKNw&usqp=CAU')
    second_level_three = models.CharField(max_length=300,null=False,default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTtav_T24wgWwQXtL5_CSuCahv5jT_q0ZXKNw&usqp=CAU')
    second_level_four = models.CharField(max_length=300,null=False,default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTtav_T24wgWwQXtL5_CSuCahv5jT_q0ZXKNw&usqp=CAU')
    second_legend_image = models.CharField(max_length=300,null=False,default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTtav_T24wgWwQXtL5_CSuCahv5jT_q0ZXKNw&usqp=CAU')
    second_legend_text = RichTextField(blank=False,null=False)

    def __str__(self):
        return self.header_legend
