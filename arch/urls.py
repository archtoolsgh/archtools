from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name = 'index'),
    path('index.html', views.index, name = 'index'),
    path('architecture.html', views.architecture, name = 'architecture'),
    path('engineering.html', views.engineering, name = 'engineering'),
    path('health.html', views.health, name = 'health'),
    path('explore.html', views.explore, name = 'explore'),
    path('cart.html', views.cart, name = 'cart'),
    path('checkout.html', views.checkout, name = 'checkout'),
    path('update_item', views.update_item, name ="update_item"),
    path('about', views.index, name = 'about'),
    path('singleProduct/<int:product_id>', views.singleProduct, name = 'singleProduct'),
    path('products', views.products, name = 'products'),
    # path('form', views.form, name = 'form'),
]
