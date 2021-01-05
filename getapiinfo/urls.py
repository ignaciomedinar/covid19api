from django.urls import path
from .import views

urlpatterns = [
    path('vo',views.ok),
    path('',views.home,name='home'),
    # url(r"^api/", 'loc_search', name="search")
]
