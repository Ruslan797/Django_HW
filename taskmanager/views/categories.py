from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from taskmanager.models import Category
from taskmanager.serializers.categories import CategorySerializer, CategoryCreateSerializer


# class CategoryViewSet(ModelViewSet):
#     queryset = Category.objects.all()
#
#     def get_serializer_class(self):
#         # A dedicated serializer is used for the creation process.
#         if self.action == 'create':
#             return CategoryCreateSerializer
#         return CategorySerializer
#
#     def perform_destroy(self, instance):
#         """
#         We override the delete method to implement soft deletion.
#         """
#         instance.is_deleted = True
#         instance.deleted_at = timezone.now()
#         instance.save()
#
#     @action(detail=True, methods=['get'])
#     def count_tasks(self, request, pk=None):
#         """
#         Custom method: number of tasks in the category.
#         """
#         category = self.get_object()
#         count = category.task_set.count()
#         return Response({'category': category.name, 'tasks_count': count})

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()

    def get_serializer_class(self):
        # A dedicated serializer is used for the creation process.
        if self.action == 'create':
            return CategoryCreateSerializer
        return CategorySerializer

    @action(detail=True, methods=['get'])
    def count_tasks(self, request, pk=None):
        """
        Custom method: number of tasks in the category.
        """
        category = self.get_object()
        count = category.tasks.count()
        return Response({'category': category.name, 'tasks_count': count})


    def perform_destroy(self, instance):
        """
        We override the delete method to implement soft deletion.
        """
        instance.is_deleted = True
        instance.deleted_at = timezone.now()
        instance.save()



    