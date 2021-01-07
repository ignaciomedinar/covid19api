from django.urls import path
from .import views

urlpatterns = [
    path('',views.home),
    path('table/',views.table,name='table'),
    path('charts/', views.charts, name='charts'),
]
