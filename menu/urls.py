from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from menu.views import UserPanelView, MenuListView, CartView, OrderHistoryView, ProfileView, item_detail, OrderCreateView

urlpatterns = [
    path('', UserPanelView.as_view(), name='user_panel'),
    path('menu/', MenuListView.as_view(), name='menu_list'),
    path('cart/', CartView.as_view(), name='cart'),
    path('orders/', OrderHistoryView.as_view(), name='order_history'),
    path('order/create/', OrderCreateView.as_view(), name='order_create'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('menu/dish/<int:pk>/', item_detail, name='dish_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)