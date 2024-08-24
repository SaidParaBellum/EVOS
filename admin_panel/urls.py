from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from admin_panel.views import AdminPanelView, CategoryListView, DishListView, UserListView, CategoryCreateView, \
    CategoryUpdateView, CategoryDeleteView, DishCreateView, DishUpdateView, DishDeleteView, UserOrdersView

urlpatterns = [
    path('', AdminPanelView.as_view(), name='index'),

    path('users/', UserListView.as_view(), name='user_list'),
    path('users/<int:pk>/orders/', UserOrdersView.as_view(), name='user_orders'),

    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('category/add/', CategoryCreateView.as_view(), name='add_category'),
    path('category/edit/<int:pk>/', CategoryUpdateView.as_view(), name='edit_category'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='delete_category'),

    path('dishes/', DishListView.as_view(), name='dish_list'),
    path('dishes/add/', DishCreateView.as_view(), name='add_dish'),
    path('dishes/edit/<int:pk>/', DishUpdateView.as_view(), name='edit_dish'),
    path('dishes/delete/<int:pk>/', DishDeleteView.as_view(), name='delete_dish'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)