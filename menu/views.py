from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from admin_panel.models import Dish
from menu.models import CartItem, Order


class UserPanelView(LoginRequiredMixin, TemplateView):
    template_name = 'user_panel/index.html'

class MenuListView(LoginRequiredMixin, ListView):
    model = Dish
    template_name = 'menu/menu_list.html'
    context_object_name = 'dishes'


class CartView(LoginRequiredMixin, ListView):
    model = CartItem
    template_name = 'menu/cart.html'
    context_object_name = 'cart_items'

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)





class OrderHistoryView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'menu/order_history.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    fields = []
    template_name = 'menu/order_confirm.html'

    def form_valid(self, form):
        cart_items = CartItem.objects.filter(user=self.request.user)
        order = form.save(commit=False)
        order.user = self.request.user
        order.save()
        order.items.set(cart_items)
        order.calculate_total_price()
        cart_items.delete()
        return redirect('order_history')

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'menu/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = Order.objects.filter(user=self.request.user)
        return context

def item_detail(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    return render(request, 'menu/item_detail.html', {'dish': dish})