from django.urls import path

from api.view import TaskListView, DetailTaskView, DeleteView, DeleteViewProject, DetailProjectView, TaskUpdateView

urlpatterns = [
    # path('updatetask', TaskUpdateView.as_view(), name='task_update_api'),
    path('list_task', TaskListView.as_view(), name='task_view_api'),
    path('list_task/<int:pk>', DetailTaskView.as_view(), name='task_detail_view_api'),
    path('list_task/update/<int:pk>', TaskUpdateView.as_view(), name='task_update_view_api'),
    path('project/<int:pk>', DetailProjectView.as_view(), name='project_detail_view_api'),
    path('list_task/delete/<int:pk>', DeleteView.as_view(), name='task_delete_view_api'),
    path('project/delete/<int:pk>', DeleteViewProject.as_view(), name='project_delete_view_api'),

]
