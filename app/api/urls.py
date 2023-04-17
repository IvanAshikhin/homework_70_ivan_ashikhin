from django.urls import path

from api.view import TaskListView, TaskUpdateView, DetailTaskView

urlpatterns = [
    # path('updatetask', TaskUpdateView.as_view(), name='task_update_api'),
    path('list_task', TaskListView.as_view(), name='task_view_api'),
    path('list_task/<int:pk>', DetailTaskView.as_view(), name='task_detail_view_api'),
]
