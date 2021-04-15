from django import forms

from inventory.models import Category,Brands,Uom,Items
#from inventory.models import Brands

class CategoryForm(forms.ModelForm):
    class Meta():
        model=Category
        fields=('category_name','description',)

class BrandsForm(forms.ModelForm):
    class Meta():
        model=Brands
        fields=('brand_name','description',)

class UomForm(forms.ModelForm):
    class Meta():
        model=Uom
        fields=('uom_name','description',)

class ItemsForm(forms.ModelForm):
    class Meta():
        model=Items
        fields=('code','batch','supplier','item_name','generic_name','strength','brand','category','uom','quantity','qty_on_hand','discount','cost_price','markup_price',)
