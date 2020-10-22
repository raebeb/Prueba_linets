from django.urls import path

from . import views
app_name = 'generate_csv'

urlpatterns = [
    path('', views.index, name='index'),
    path('getfile/', views.getfile, name='getfile'),
    path('api_view/', views.apiOverview, name='api_view'),
    path('product-list/', views.productList, name='product_list'),
    path('product-detail/<str:pk>/', views.productDetail, name='product_detail'),
    path('product-create/', views.productCreate, name='product_create')
]