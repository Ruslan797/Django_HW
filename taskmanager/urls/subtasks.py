# from django.urls import path
# from taskmanager.views.subtasks import (
#     SubTaskListCreateView,
#     SubTaskDetailUpdateDeleteView,
#     SubTaskFilterList,
# )
#
# urlpatterns = [
#     path('', SubTaskListCreateView.as_view(), name='subtasks-list-create'),
#     path('', SubTaskDetailUpdateDeleteView.as_view(), name='subtask-detail'),
#     path('', SubTaskFilterList.as_view(), name='subtasks-filter'),
# ]


from django.urls import path
from taskmanager.views.subtasks import (
    SubTaskListCreateView,
    SubTaskDetailUpdateDeleteView,
    SubTaskFilterList,
)

urlpatterns = [
    path('', SubTaskListCreateView.as_view(), name='subtasks-list-create'),
    path('<int:pk>/', SubTaskDetailUpdateDeleteView.as_view(), name='subtask-detail'),
    path('filter/', SubTaskFilterList.as_view(), name='subtasks-filter'),
]



