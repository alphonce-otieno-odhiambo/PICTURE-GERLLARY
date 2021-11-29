from django.urls import path
from . import views

#create the paths of the urls

urlpatterns = [
    path('',views.home,name='home'),
    path('pictures/',views.pictures,name='pictures'),
    path('search', views.search, name= 'search')

]