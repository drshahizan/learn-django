from django import forms
from .models import Product, Category, Order


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'image', 'description', 'price']
        widgets = {
            'category': forms.Select(attrs={'class':'form-control'}),
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'image': forms.FileInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'price': forms.NumberInput(attrs={'class':'form-control'}),
            'slug': forms.TextInput(attrs={'class':'form-control','type':'hidden',}),
        }

class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'slug': forms.TextInput(attrs={'class':'form-control','type':'hidden',}),
        }

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
                                choices=PRODUCT_QUANTITY_CHOICES,
                                coerce=int)
    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)
    
class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address',
                  'postal_code', 'city']
        
class OrderStatusForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status']