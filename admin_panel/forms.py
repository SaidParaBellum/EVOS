from django import forms

from admin_panel.models import Dish


class DishCreateForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'description', 'price', 'category', 'image', 'available']
