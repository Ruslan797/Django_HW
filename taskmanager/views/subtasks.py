
###  Home Work 14

# from rest_framework import generics
# from rest_framework.pagination import PageNumberPagination
# from taskmanager.models import SubTask
# from taskmanager.serializers.subtasks import SubTaskSerializer, SubTaskCreateSerializer
#
# class CustomSubTaskPagination(PageNumberPagination):
#     """Custom pagination class for subtasks."""
#     page_size = 5
#     page_size_query_param = 'page_size'
#     max_page_size = 100
#
# class SubTaskListCreateView(generics.ListCreateAPIView):
#     """
#     Endpoint for retrieving a list of subtasks (with pagination) and creating a new subtask.
#     Pagination: 5 items per page.
#     Sorting: by creation date in descending order.
#     """
#     queryset = SubTask.objects.all().order_by('-created_at')
#     pagination_class = CustomSubTaskPagination
#
#     def get_serializer_class(self):
#         if self.request.method == 'POST':
#             return SubTaskCreateSerializer
#         return SubTaskSerializer
#
# class SubTaskDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
#     """
#     Endpoint for retrieving, updating, and deleting a specific subtask.
#     """
#     queryset = SubTask.objects.all()
#
#     def get_serializer_class(self):
#         if self.request.method in ['PUT', 'PATCH']:
#             return SubTaskCreateSerializer
#         return SubTaskSerializer
#
# class SubTaskFilterList(generics.ListAPIView):
#     """
#     Endpoint for filtering subtasks by the name of the main task and/or status.
#     Pagination: 5 items per page.
#     Sorting: by creation date in descending order.
#     """
#     serializer_class = SubTaskSerializer
#     pagination_class = CustomSubTaskPagination
#
#     def get_queryset(self):
#         queryset = SubTask.objects.all().order_by('-created_at')
#         task_title = self.request.query_params.get('task_title', None)
#         subtask_status = self.request.query_params.get('status', None)
#         if task_title:
#             queryset = queryset.filter(task__title__icontains=task_title)
#         if subtask_status:
#             queryset = queryset.filter(status=subtask_status)
#         return queryset


###   Home Work 15

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from taskmanager.models import SubTask
from taskmanager.serializers.subtasks import SubTaskSerializer

class SubTaskListCreateView(ListCreateAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['status', 'deadline', 'task']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'deadline', 'title']
    ordering = ['title']


class SubTaskRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer

