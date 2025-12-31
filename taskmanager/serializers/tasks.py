

###   Home Work 14

from rest_framework import serializers
from taskmanager.models import Task, SubTask, Category

from datetime import datetime
from taskmanager.serializers.subtasks import SubTaskSerializer
from taskmanager.serializers.categories import CategoryCreateSerializer, CategorySerializer


# class TaskDetailSerializer(serializers.ModelSerializer):
#     subtasks = SubTaskSerializer(many=True, read_only=True)
#     categories = CategoryCreateSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = Task
#         fields = ['id', 'title', 'description', 'categories', 'status', 'deadline', 'created_at', 'subtasks']
#
# class TaskCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Task
#         fields = ['id', 'title', 'description', 'categories', 'status', 'deadline']
#
#     def validate_deadline(self, value):
#         if value < datetime.now():
#             raise serializers.ValidationError("The deadline date cannot be in the past.")
#         return value
#
#
# class TaskSerializer(serializers.ModelSerializer):
#     categories = CategorySerializer(many=True, read_only=True)
#     category_ids = serializers.PrimaryKeyRelatedField(
#         many=True,
#         queryset=Category.objects.all(),
#         source='categories',
#         write_only=True,
#         required=False
#     )
#
#     class Meta:
#         model = Task
#         fields = [
#             'id',
#             'title',
#             'description',
#             'categories',
#             'category_ids',
#             'status',
#             'deadline',
#             'created_at'
#         ]
#         read_only_fields = ['id', 'created_at']


### Home Work 15

from rest_framework import serializers
from taskmanager.models import Task, Category
from taskmanager.serializers.categories import CategorySerializer

class TaskSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    categories_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Category.objects.all(),
        source='categories',
        write_only=True,
    )

    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'categories', 'categories_ids',
            'status', 'deadline', 'created_at'
        ]
        read_only_fields = ['created_at']

