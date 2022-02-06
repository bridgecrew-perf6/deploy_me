from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from .models import Todo
from .serializers import TodoSerializer


class TodoCreateListView(ListCreateAPIView):
  permission_classes = (permissions.AllowAny, )
  queryset = Todo.objects.order_by('id').all()
  serializer_class = TodoSerializer

class TodoView(RetrieveUpdateDestroyAPIView):
  permission_classes = (permissions.AllowAny, )
  queryset = Todo.objects.all()
  serializer_class = TodoSerializer
