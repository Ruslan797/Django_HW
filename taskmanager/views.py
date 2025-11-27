# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Task
# from .serializers import TaskSerializer
# from django.utils import timezone
# from django.db.models import Count
#
#
# @api_view(['POST'])
# def create_task(request):
#     serializer = TaskSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET'])
# def get_tasks(request):
#     tasks = Task.objects.all()
#     serializer = TaskSerializer(tasks, many=True)
#     return Response(serializer.data)
#
#
# @api_view(['GET'])
# def get_task_by_id(request, pk):
#     try:
#         task = Task.objects.get(pk=pk)
#     except Task.DoesNotExist:
#         return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
#
#     serializer = TaskSerializer(task)
#     return Response(serializer.data)
#
#
# @api_view(['GET'])
# def tasks_statistics(request):
#     total = Task.objects.count()
#
#     by_status = dict(
#         Task.objects.values_list('status').annotate(count=Count('status'))
#     )
#
#     overdue = Task.objects.filter(
#         deadline__lt=timezone.now(),
#         status__in=['New', 'In progress', 'Pending', 'Blocked']
#     ).count()
#
#     return Response({
#         "total_tasks": total,
#         "tasks_by_status": by_status,
#         "overdue_tasks": overdue
#     })

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import SubTask
from .serializers import SubTaskCreateSerializer

# Задание 5:
class SubTaskListCreateView(APIView):
    def get(self, request):
        subtasks = SubTask.objects.all()
        serializer = SubTaskCreateSerializer(subtasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SubTaskCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SubTaskDetailUpdateDeleteView(APIView):
    def get_object(self, pk):
        try:
            return SubTask.objects.get(pk=pk)
        except SubTask.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        subtask = self.get_object(pk)
        serializer = SubTaskCreateSerializer(subtask)
        return Response(serializer.data)

    def put(self, request, pk):
        subtask = self.get_object(pk)
        serializer = SubTaskCreateSerializer(subtask, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        subtask = self.get_object(pk)
        subtask.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
