from django.urls import path
from . import views

urlpatterns = [
    path('addTask/',views.addTask,name='addTask'),
    path('markDone/<int:pk>',views.markDone,name='markDone'),
    path('mark_unDone/<int:pk>',views.mark_unDone,name='mark_unDone'),
    path('removeTask/<int:pk>',views.removeTask,name='removeTask'),
    path('edit_task/<int:pk>',views.edit_task,name='edit_task'),
]