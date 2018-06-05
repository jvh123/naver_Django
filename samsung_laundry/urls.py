from django.urls import path

from . import views
app_name='samsung_laundry'
urlpatterns = [
    path('search/', views.search.as_view(), name='search'),
    path('search_id/', views.search_id, name='search_id'),
    path('', views.main, name='main'),
]