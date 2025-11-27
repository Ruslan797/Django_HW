# from django.contrib import admin
#
#
# from django.urls import path
# from taskmanager.views import create_task, get_tasks, get_task_by_id, tasks_statistics
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('tasks/create/', create_task),
#     path('tasks/', get_tasks),
#     path('tasks/<int:pk>/', get_task_by_id),
#     path('tasks/statistics/', tasks_statistics),
# ]

from django.urls import path
from taskmanager.views import SubTaskListCreateView, SubTaskDetailUpdateDeleteView

urlpatterns = [
    path('subtasks/', SubTaskListCreateView.as_view(), name='subtask-list-create'),
    path('subtasks/<int:pk>/', SubTaskDetailUpdateDeleteView.as_view(), name='subtask-detail-update-delete'),
]

