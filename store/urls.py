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
    path('teste/', views.teste, name='teste'),                                          # OK
    path('teste-category/', views.teste2, name='teste-category'),                       # OK
    path('teste-product/', views.teste3, name='teste-product'),
    path('teste-login/', views.teste4, name='teste-login'),                             # OK
    path('teste-register/', views.teste5, name='teste-register'),                       # OK
    path('teste-cart-empty/', views.teste6, name='teste-cart-empty'),
    path('teste-cart-empty-login/', views.teste7, name='teste-cart-empty-login'),
    path('teste-cart-full/', views.teste8, name='teste-cart-full'),
    path('teste-account-lost-1/', views.teste9, name= 'teste-account-lost-1'),          # OK
    path('teste-account-lost-2/', views.teste10, name='teste-account-lost-2'),          # OK
    path('teste-checkout/', views.teste11, name='teste-checkout'),
    # teste CSS

    path('update-item/', views.update_item, name='update-item'),
]
