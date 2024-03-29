from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.home,name='home'),
    path('Add/',views.add_Task,name='Task'),
    path('Edit/<int:id>',views.edit_Task,name='edit'),
    path('Delete/<int:id>',views.delete_Task,name='delete'),
    path('Done/<int:id>',views.done,name='done')
]