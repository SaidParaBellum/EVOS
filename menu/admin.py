from django.contrib import admin

from admin_panel.models import Category, Dish
from menu.models import CartItem, Order


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')

admin.site.register(Category, CategoryAdmin)

class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'image')
    list_filter = ('category',)
    search_fields = ('name', 'description')

admin.site.register(Dish, DishAdmin)

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'dish', 'quantity')
    list_filter = ('user', 'dish')
    search_fields = ('user__username', 'dish__name')

admin.site.register(CartItem, CartItemAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_price', 'created_at', 'status', 'is_delivered')
    list_filter = ('status', 'created_at', 'is_delivered')
    search_fields = ('user__username', 'status')

admin.site.register(Order, OrderAdmin)