# from django.contrib import admin
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
#
# from taskmanager.views.categories import CategoryViewSet
# from taskmanager.views.tasks import TaskViewSet
# from taskmanager.views.subtasks import SubTaskViewSet
#
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
#
# from rest_framework.permissions import AllowAny
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi
#
#
# router = DefaultRouter()
# router.register(r"categories", CategoryViewSet, basename="category")
# router.register(r"tasks", TaskViewSet, basename="task")
# router.register(r"subtasks", SubTaskViewSet, basename="subtask")
#
#
# schema_view = get_schema_view(
#     openapi.Info(
#         title="Task Manager API",
#         default_version="v1",
#         description="API documentation (JWT auth + permissions + pagination)",
#     ),
#     public=True,
#     permission_classes=(AllowAny,),
# )
#
# urlpatterns = [
#     path("admin/", admin.site.urls),
#
#     # JWT endpoints (SimpleJWT)
#     path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
#     path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
#
#     # your auth endpoints (если они есть)
#     path("api/auth/", include("accounts.urls")),
#
#     # API
#     path("api/v1/", include(router.urls)),
#
#     # Swagger
#     path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
#     path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
# ]

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from taskmanager.views.categories import CategoryViewSet
from taskmanager.views.tasks import TaskViewSet
from taskmanager.views.subtasks import SubTaskViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.permissions import AllowAny


router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'tasks', TaskViewSet, basename='task')


schema_view = get_schema_view(
    openapi.Info(
        title="Task Manager API",
        default_version="v1",
        description="JWT (SimpleJWT), permissions, pagination",
    ),
    public=True,
    permission_classes=(AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/', include('accounts.urls')),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0),name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),

    path('api/v1/', include(router.urls)),
]





