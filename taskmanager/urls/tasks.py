# from django.urls import path, include
#
# urlpatterns = [
#     path('api/', include('taskmanager.urls.tasks')),  # Для задач
# ]


###   Home Work 14

# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from taskmanager.views.tasks import TaskViewSet
#
# router = DefaultRouter()
# router.register('tasks', TaskViewSet, basename='task')
#
# urlpatterns = router.urls


###   Home Work 15


from django.urls import path
from taskmanager.views.tasks import (
    TaskListCreateView,
    TaskRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('', TaskListCreateView.as_view(), name='task-list-create'),
    path('<int:pk>/', TaskRetrieveUpdateDestroyView.as_view(), name='task-detail'),
]



