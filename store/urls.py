from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('product/<str:pk>/', views.product, name='product'),
    path('category/<str:pk>/', views.category, name='category'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('login/', views.user_login, name='login'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),

    # teste CSS
    path('teste/', views.teste, name='teste'),
    path('teste-category/', views.teste2, name='teste-category'),
    path('teste-product/', views.teste3, name='teste-product'),
    path('teste-login/', views.teste4, name='teste-login'),
    path('teste-register/', views.teste5, name='teste-register'),
    path('teste-cart-empty/', views.teste6, name='teste-cart-empty'),
    path('teste-cart-empty-login/', views.teste7, name='teste-cart-empty-login'),
    # teste CSS

    path('update-item/', views.update_item, name='update-item'),
]
