from django.urls import path
from .import views

urlpatterns = [
    path('vo',views.ok),
    path('',views.home,name='home'),
]
