from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.view_shopbag, name='view_shopbag'),
    path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),
]
