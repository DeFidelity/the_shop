from django import forms

class CartAddProducts(forms.Form):
    quantity =forms.IntegerField()
    override = forms.BooleanField(required=False,initial=False,widget=forms.HiddenInput)
