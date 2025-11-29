# from rest_framework import viewsets, status
# from rest_framework.response import Response
# from taskmanager.models import Task
# from taskmanager.serializers.tasks import TaskSerializer
#
# class TaskViewSet(viewsets.ModelViewSet):
#     """
#     ViewSet для работы с задачами.
#     Поддерживает все стандартные операции CRUD (создание, чтение, обновление, удаление).
#     """
#     queryset = Task.objects.all().order_by('-created_at')
#     serializer_class = TaskSerializer
#
#     def list(self, request, *args, **kwargs):
#         """
#         Получение списка задач.
#         """
#         queryset = self.filter_queryset(self.get_queryset())
#         page = self.paginate_queryset(queryset)
#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#             return self.get_paginated_response(serializer.data)
#
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def create(self, request, *args, **kwargs):
#         """
#         Создание новой задачи.
#         """
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
#
#     def retrieve(self, request, *args, **kwargs):
#         """
#         Получение конкретной задачи.
#         """
#         instance = self.get_object()
#         serializer = self.get_serializer(instance)
#         return Response(serializer.data)
#
#     def update(self, request, *args, **kwargs):
#         """
#         Полное обновление задачи.
#         """
#         partial = kwargs.pop('partial', False)
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=partial)
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)
#         return Response(serializer.data)
#
#     def destroy(self, request, *args, **kwargs):
#         """
#         Удаление задачи.
#         """
#         instance = self.get_object()
#         self.perform_destroy(instance)
#         return Response(status=status.HTTP_204_NO_CONTENT)

from rest_framework.response import Response
from rest_framework import viewsets
from taskmanager.models import Task
from taskmanager.serializers.tasks import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = Task.objects.all().order_by('-created_at')
        day_of_week = self.request.query_params.get('day_of_week', None)
        if day_of_week:

            days = {
                'monday': 2,
                'tuesday': 3,
                'wednesday': 4,
                'thursday': 5,
                'friday': 6,
                'saturday': 7,
                'sunday': 1,
            }
            day_number = days.get(day_of_week.lower())
            if day_number:
                queryset = queryset.filter(deadline__week_day=day_number)
        return queryset


