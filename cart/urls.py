from django.urls import path
from .import views

urlpatterns = [
    path('add_to_cart/<int:id>',views.add_to_cart,name="add_to_cart"),
    path('cartpage',views.cart_home,name="cartpage"),
    path('updatecart/<int:id>/',views.update_cart,name="updatecart"),
    path('cart_delete/<int:id>',views.delete_cart_product,name="cart_delete")
]