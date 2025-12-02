from rest_framework.routers import DefaultRouter
from taskmanager.views.categories import CategoryViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = router.urls