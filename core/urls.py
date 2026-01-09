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
    path('api/auth/', include('accounts.urls')),
    path('api/v1/', include(router.urls)),
]



