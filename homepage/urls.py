from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('contact', views.contact, name='contact'),
    path('order', views.order, name='order'),
    path('confirm', views.confirm_order, name='confirm'),
    path('menu', views.menu, name='menu'),
    path('sitemap', views.sitemap, name='sitemap'),
    path('google', views.google, name='google'),
]
