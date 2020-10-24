from django.urls import path
from django.conf.urls import include
from . import views

app_name = 'generate_csv'
api_urls = [
    path('overview/', views.api_overview, name='api_view'),
    path('product-list/', views.product_list, name='product_list'),
    path('product-detail/<str:pk>/', views.product_detail, name='product_detail'),
    path('product-create/', views.product_create, name='product_create')
]
urlpatterns = [
    path('', views.index, name='index'),
    path('getfile/', views.get_file, name='getfile'),
    path('api/', include(api_urls)),
]