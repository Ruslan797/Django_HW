

###   Home Work 14

# from django.urls import path
# from taskmanager.views.subtasks import (
#     SubTaskListCreateView,
#     SubTaskDetailUpdateDeleteView,
#     SubTaskFilterList,
# )
#
# urlpatterns = [
#     path('', SubTaskListCreateView.as_view(), name='subtasks-list-create'),
#     path('<int:pk>/', SubTaskDetailUpdateDeleteView.as_view(), name='subtask-detail'),
#     path('filter/', SubTaskFilterList.as_view(), name='subtasks-filter'),
# ]


### Home work 15



from django.urls import path
from taskmanager.views.subtasks import (
    SubTaskListCreateView,
    SubTaskRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('', SubTaskListCreateView.as_view(), name='subtask-list-create'),
    path('<int:pk>/', SubTaskRetrieveUpdateDestroyView.as_view(), name='subtask-detail'),
]





