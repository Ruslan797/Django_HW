# from django.urls import path, include
# from rest_framework.routers import DefaultRouter, SimpleRouter
# from taskmanager.views.tasks import TaskViewSet
#
#
# router = DefaultRouter()
# router.register('task', TaskViewSet)
#
#
# urlpatterns = [
#     path('subtasks/', include('taskmanager.urls.tasks')),
#     path('subtasks/<int:pk>/', include('taskmanager.urls.subtasks')),
#     path('subtasks/filter/', include('taskmanager.urls.subtasks')),
#
# ] + router.urls


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('taskmanager.urls')),
]
