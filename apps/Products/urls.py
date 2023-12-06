from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.Products_list, name='product_list'),
    path('add-product/', views.Products_form, name='add_product'),
    path('edit-product/<int:id>/', views.Products_form, name='product_update'),
    path('delete/<int:id>', views.Products_delete, name='product_delete')
  ]