from django.contrib import admin
from django.urls import path, include
from . import views
app_name = "nsestock"
urlpatterns = [
    path('', views.nsehome, name = "nsehome"),
    path('nseadd_stock', views.nseadd_stock, name = "nseadd_stock"),
    path('nsedelete_stock', views.nsedelete_stock, name = "nsedelete_stock"),
    path('nsedelete/<nsestock_id>', views.nsedelete, name = "nsedelete"),
]