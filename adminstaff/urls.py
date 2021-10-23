from django.urls import path
from . import views


urlpatterns = [
    path('login', views.login, name='login'),
    path('pending-orders', views.orders, name='pending-orders'),
    path('confirmed-orders', views.orders, name='confirmed-order'),
    path('add-item', views.add_item, name='add-item'),
    path('menu', views.menu, name='staff-menu'),
    path('upload', views.upload_item, name='upload'),

]
