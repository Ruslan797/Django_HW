

###   Home Work 14

# from rest_framework import serializers
# from taskmanager.models import Task, SubTask, Category
# from datetime import datetime
#
#





# class SubTaskSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SubTask
#         fields = ['id', 'title', 'description', 'status', 'deadline', 'created_at']
#
#
# ###   Home Work 15
#
#
# class SubTaskSerializer(serializers.ModelSerializer):
#     task_title = serializers.CharField(source='task.title', read_only=True)
#
#     class Meta:
#         model = SubTask
#         fields = [
#             'id', 'title', 'description', 'task', 'task_title',
#             'status', 'deadline', 'created_at'
#         ]
#         read_only_fields = ['created_at', 'task_title']

from rest_framework import serializers
from taskmanager.models import SubTask


class SubTaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = SubTask
        fields = [
            "id",
            "title",
            "description",
            "owner",
            "task",
            "status",
            "deadline",
            "created_at",
        ]
        read_only_fields = ["created_at", "owner"]






