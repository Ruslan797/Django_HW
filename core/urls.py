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

# from django.urls import path
# from taskmanager.views.subtasks import SubTaskListCreateView, SubTaskDetailUpdateDeleteView
#
# urlpatterns = [
#     path('subtasks/', SubTaskListCreateView.as_view(), name='subtask-list-create'),
#     path('subtasks/<int:pk>/', SubTaskDetailUpdateDeleteView.as_view(), name='subtask-detail-update-delete'),
# ]

# from django.contrib import admin
# from django.urls import path, include
#
#
# urlpatterns = [
#     path('admin/', admin.site.urls),  # http://127.0.0.1:8000/admin/
#     path('api/v1/', include('routers')),  # http://127.0.0.1:8000/api/v1/
# ]

###   Home Work 14

# from django.contrib import admin
# from django.urls import path, include
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/v1/tasks/', include('taskmanager.urls.tasks')),  # Маршруты для задач
#     path('api/v1/subtasks/', include('taskmanager.urls.subtasks')),  # Маршруты для подзадач
# ]


###   Home Work 15


# from django.urls import path, include
#
# urlpatterns = [
#     path('tasks/', include('taskmanager.urls.tasks')),
#     path('subtasks/', include('taskmanager.urls.subtasks')),
# ]
#
# Homework 16

# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from taskmanager.views.categories import CategoryViewSet
#
# router = DefaultRouter()
# router.register(r'categories', CategoryViewSet, basename='category')
#
# urlpatterns = [
#     path('api/v1/', include(router.urls)),
# ]


from django.contrib import admin
from django.urls import path, include
# from taskmanager.views.subtasks import SubTaskListCreateView
# from taskmanager.views.tasks import TaskListCreateView
# from taskmanager.views.categories import CategoryViewSet
#
#
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/v1/', include('routers')),
#     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
#     path('api/subtask/', SubTaskListCreateView.as_view(), name='subtask-list-create'),
#     path('api/task/', TaskListCreateView.as_view(), name='task-list-create'),
#     path('api/catigory/', CategoryViewSet.as_view(), name='category-list-create'),
#
# ]
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from taskmanager.views.categories import CategoryViewSet
from taskmanager.views.tasks import TaskViewSet
from taskmanager.views.subtasks import SubTaskViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'subtasks', SubTaskViewSet, basename='subtask')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/', include(router.urls)),
]



