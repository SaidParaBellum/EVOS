from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

# Create your views here.

from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

from User.models import User
from admin_panel.forms import DishCreateForm
from admin_panel.models import Category, Dish
from menu.models import Order


class AdminPanelView(TemplateView):
    template_name = 'admin_panel/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context




# USER

class UserListView(ListView):
    model = User
    template_name = 'admin_panel/user_list.html'
    context_object_name = 'users'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

class UserOrdersView(ListView):
    model = Order
    template_name = 'admin_panel/user_orders.html'
    context_object_name = 'orders'

    def get_queryset(self):
        user_id = self.kwargs.get('pk')
        return Order.objects.filter(user_id=user_id)

# CATEGORY
class CategoryListView(ListView):
    model = Category
    template_name = 'admin_panel/category_list.html'
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class CategoryCreateView(CreateView):
    model = Category
    fields = ['name', 'description']
    template_name = 'admin_panel/add_category.html'
    success_url = reverse_lazy('category_list')

class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name', 'description']
    template_name = 'admin_panel/edit_category.html'
    success_url = reverse_lazy('category_list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'admin_panel/delete_category.html'
    success_url = reverse_lazy('category_list')



# DISH
class DishListView(ListView):
    model = Dish
    template_name = 'admin_panel/dish_list.html'
    context_object_name = 'dishes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

class DishCreateView(CreateView):
    model = Dish
    form_class = DishCreateForm
    template_name = 'admin_panel/dish_add.html'
    success_url = reverse_lazy('dish_list')

class DishUpdateView(UpdateView):
    template_name = 'admin_panel/dish_update.html'
    model = Dish
    form_class = DishCreateForm
    success_url = reverse_lazy('dish_list')

class DishDeleteView(DeleteView):
    template_name = 'admin_panel/dish_delete.html'
    model = Dish
    success_url = reverse_lazy('dish_list')
