# from django.urls import path, include
#
# urlpatterns = [
#     path('api/', include('taskmanager.urls.tasks')),  # Для задач
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from taskmanager.views.tasks import TaskViewSet

router = DefaultRouter()
router.register('tasks', TaskViewSet, basename='task')

urlpatterns = router.urls
