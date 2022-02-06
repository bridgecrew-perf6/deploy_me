from django.urls import path
from .views import TodoCreateListView, TodoView


urlpatterns = [
  path('todo', TodoCreateListView.as_view()),
  path('todo/<pk>', TodoView.as_view()),
]
