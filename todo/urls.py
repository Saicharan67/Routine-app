
from django.urls import path
from . import views
urlpatterns = [
  
    path('',views.index,name='index'),
    path('addTodo',views.addTodo,name='add'),
    path('complete/<todo_id>', views.completeTodo,name='complete'),
    path('delcompleted',views.delcompleted,name='delcompleted'),
    path('delall',views.delall,name="delall")
]
