from django.urls import path

from api.view import TaskListView

urlpatterns = [
    # path('createtask', TaskCreateView.as_view(), name='task_create_api'),
    path('list_task', TaskListView.as_view(), name='task_view_api'),
]
