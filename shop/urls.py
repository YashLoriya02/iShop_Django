from django.urls import path
from . import views

urlpatterns = [
    path("" , views.index, name= 'ShopHome'),
    path("contact/" , views.contact, name= 'contact'),
    path("search/" , views.search, name= 'search'),
    path("tracker/" , views.tracker, name= 'tracker'),
    path("about/" , views.about, name= 'about'),
    path("products/<int:myid>/" , views.productView, name= 'productView'),
    path("checkout/" , views.checkout, name= 'checkout'),
]