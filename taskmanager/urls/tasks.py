from django.urls import path
from taskmanager.views.tasks import (
    TaskListCreateView,
    TaskRetrieveUpdateDestroyView,
    MyTasksListView,
)

urlpatterns = [
    path("", TaskListCreateView.as_view(), name="task-list-create"),
    path("my/", MyTasksListView.as_view(), name="my-tasks"),
    path("<int:pk>/", TaskRetrieveUpdateDestroyView.as_view(), name="task-detail"),
]



