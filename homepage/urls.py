from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('contact', views.contact, name='contact'),
    path('thank-you', views.contact_thanks, name='thanks'),
    path('order/<item>', views.order, name='order'),
    path('confirm/<item>', views.confirm_order, name='confirm'),
    path('payment-successful', views.purchase_thanks, name='payment_success'),
    path('menu', views.menu, name='menu'),
    path('sitemap', views.sitemap, name='sitemap'),
    path('google', views.google, name='google'),
]
