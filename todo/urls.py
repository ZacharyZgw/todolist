from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name = "index"),
    path('list/',views.index,name = "todolist"),
    path('add/',views.add,name = 'add'),
    path('select/<int:todo_id>/',views.select,name='select'),
    path('delete/<int:todo_id>/',views.delete,name='delete')
]

