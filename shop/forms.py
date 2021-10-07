from django import forms
from django.forms import fields
from shop.models import Comment, CustomerProfiles

class CommentForm(forms.ModelForm):
    comment_author = forms.CharField(
        label='Your name',
        widget = forms.Textarea(attrs={
        'rows':'1',
        'name':'author',
        'placeholder':'Write your name'
        }
        )
    )
    comment_body = forms.CharField(
        label='What you think',
        widget=forms.Textarea(attrs={
        'name':'body',
        'rows':'3',
        'placeholder':'Write what you think about this post .....'
        }))
    class Meta:
        model = Comment
        fields = ['comment_author','comment_body']

class ProfileForm(forms.ModelForm):
    D_COUNTRIES = (
        ('NG','Nigeria'),
        ('GH','Ghana'),
        ('BN','Benin republic'),
        ('BF','Burkina Faso'),
    )
    full_name = forms.CharField(
    label = 'Your name: ',
    widget=forms.Textarea(attrs={
    'rows':'1',
    'placeholder':'Write your fulll name .....'
    }))
    country = forms.ChoiceField(
        choices = D_COUNTRIES,
        label = 'Select Your Country: ',
     )
    address = forms.CharField(
    label = 'Your address: ',
    widget=forms.Textarea(attrs={
    'rows':'3',
    'placeholder':'Write your full address .....'
    }))
    city = forms.CharField(
    label = 'City: ',
    widget=forms.Textarea(attrs={
    'rows':'3',
    'placeholder':'Write name of your city .....'
    }))
    address_description = forms.CharField(
    label = 'Your name: ',
    widget=forms.Textarea(attrs={
    'rows':'3',
    'placeholder':'Write a clear description of your address, including beside popular places .....'
    }))
    phone_number = forms.IntegerField(
    label = 'Phone Number with country code: ',
    widget = forms.CharField()
    )
    class Meta:
        model = CustomerProfiles
        fields = ['full_name','country','address','city','address_description','phone_number']
