from .views import *
from django.urls import path, include
from  rest_framework import routers

router = routers.DefaultRouter()
router.register(r'user', UserProfileView, basename='user_list')
router.register(r'client', ClientView, basename='cclient_list')
router.register(r'company', CompanyView, basename='company_list')
router.register(r'cart', CartView, basename='cart_list')
router.register(r'cart_item', CartItemView, basename='cart_item_list')
router.register(r'favorite', FavoriteView, basename='favorite_list')
router.register(r'favorite_item', FavoriteItemView, basename='favorite_item_list')




urlpatterns = [
    path('', include(router.urls)),
    path('client_user/', ClientRegisterView.as_view(), name='client_register'),
    path('company/', CompanyRegisterView.as_view(), name='client_register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('car/', CarListAPIView.as_view(), name='car_list'),
    path('car/<int:pk>/', CarDetailAPIView.as_view(), name='car_detail'),
    path('car/create/', CarCreateAPIView.as_view(), name='car_create'),
    path('cars/', CarOwnerAPIView.as_view(), name='car_edit'),
    path('cars/<int:pk>/', CarEditAPIView.as_view(), name='car_edit'),

    path('rating/create/', RatingCreateAPIView.as_view(), name='rating_create'),

    path('category/', CategoryListAPIView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),

    path('car_make/', CarMakeListAPIView.as_view(), name='car_make_list'),
    path('car_make/<int:pk>/', CarMakeDetailAPIView.as_view(), name='car_make_detail'),

    ]