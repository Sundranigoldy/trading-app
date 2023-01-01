from django.contrib import admin
from django.urls import path
from . import views
app_name = "stock"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('add_stock', views.add_stock, name = 'add_stock'),
    path('delete_stock', views.delete_stock, name = 'delete_stock'),
    path('delete/<stock_id>', views.delete, name = 'delete'),
]
