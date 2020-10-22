from django.urls import path

from . import views
app_name = 'generate_csv'

urlpatterns = [
    path('', views.index, name='index'),
    path('getfile/', views.getfile, name='getfile'),
]