from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.home,name='Home'),
    path('Add/',views.add_category,name='Category')
    
]