from django.urls import path
from .views import TodoListAPIView, TodoDetailAPIView


urlpatterns = [
    path('todo/', TodoListAPIView.as_view(), name='todo_list'),
    path('todo/<int:pk>', TodoDetailAPIView.as_view(), name='todo_detail')
]
