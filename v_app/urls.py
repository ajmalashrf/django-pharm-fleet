from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('order',views.order,name='order'),
    path('about/',views.about,name='about'),
    path('customer',views.customers,name='customers'),
    path('category',views.category,name='category'),
    path('shop',views.shop,name='shop'),
    path('shop_single/<str:pro_name>/', views.shop_single, name='shop_single'),
    path('cart',views.cart,name='cart'),
    path('contact',views.contact,name='contact'),
    path('checkout',views.checkout,name='checkout'),
    path('thankyou',views.thankyou,name='thankyou'),
    path('pharmlab',views.pharmlab,name='pharmlab'),
    path('test_single/<test_name>/',views.test_single,name='test_single'),
    path('medicines',views.medicines,name='medicines'),
    path('med_checkout',views.med_checkout,name='med_checkout'),
    path('med_single/<str:med_name>/', views.med_single, name='med_single'),

]