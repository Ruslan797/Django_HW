#  Home Work 19

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from taskmanager.models import Task
from taskmanager.serializers.tasks import TaskSerializer
from taskmanager.permissions import IsOwner


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        if self.action in ("update", "partial_update", "destroy"):
            return [IsAuthenticated(), IsOwner()]
        return [IsAuthenticated()]

    @action(detail=False, methods=["get"], url_path="my")
    def my(self, request):
        """
        GET /api/v1/tasks/my/
        Список задач текущего пользователя.
        """
        qs = self.get_queryset().filter(owner=request.user)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)





