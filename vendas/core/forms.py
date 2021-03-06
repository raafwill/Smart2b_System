from django import forms
from .models import Sale, SaleDetail, Product


class SaleForm(forms.ModelForm):

    class Meta:
        model = Sale
        fields = '__all__'


class SaleDetailForm(forms.ModelForm):

    class Meta:
        model = SaleDetail
        fields = '__all__'


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['ncm',
                  'brand',
                  'product',
                  'price',
                  'ipi',
                  'stock',
                  'stock_min',
                  'category']


class ProductUpdateForm(forms.ModelForm):

   class Meta:
     model = Product
     fields = ['ncm', 'brand', 'product', 'price', 'ipi', 'stock', 'stock_min', 'category']