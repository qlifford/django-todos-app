from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, UpdateView

urlpatterns = [
    path('', TaskList.as_view(), name="todos"),
    path('create/', TaskCreate.as_view(), name="todos-create"),
    path('todos/<int:pk>/', TaskDetail.as_view(), name="todos-get"),
    path('todos/<int:pk>/', UpdateView.as_view(), name="todos-update"),
]
