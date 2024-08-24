from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

from admin_panel.models import Dish

User = get_user_model()

class CartItem(models.Model):
    user = models.ForeignKey(User, related_name='cart_items', on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, related_name='cart_items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.dish.name} ({self.quantity})'

    def get_total_price(self):
        return self.quantity * self.dish.price

class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, default='Pending')
    is_delivered = models.BooleanField(default=False)

    def calculate_total_price(self):
        self.total_price = sum(item.get_total_price() for item in self.items.all())
        self.save()

    def __str__(self):
        return f'Order {self.id} by {self.user.username}'