from django.urls import path
from . import views
urlpatterns =[
    path('pets_list/',views.pets_list,name='pets_list'),
    path('pet_details/<int:pk>',views.pet_details,name='pet_details'),
    path('dog_list/',views.dog_list,name='dog_list'),
    path('cat_list/',views.cat_list,name='cat_list'),
    path('search/',views.search_product,name='search'),
]