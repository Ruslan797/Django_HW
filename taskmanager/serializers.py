# from rest_framework import serializers
# from .models import Task
#
# class TaskSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Task
#         fields = "__all__"


from rest_framework import serializers
from .models import Task, SubTask, Category
from datetime import datetime

# Задание 1:
class SubTaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = ['id', 'title', 'description', 'task', 'status', 'deadline', 'created_at']
        read_only_fields = ['created_at']

# Задание 2:
class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

    def validate_name(self, value):
        if Category.objects.filter(name=value).exists():
            raise serializers.ValidationError("Категория с таким названием уже существует.")
        return value

# Задание 3:
class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = ['id', 'title', 'description', 'status', 'deadline', 'created_at']

class TaskDetailSerializer(serializers.ModelSerializer):
    subtasks = SubTaskSerializer(many=True, read_only=True)
    categories = CategoryCreateSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'categories', 'status', 'deadline', 'created_at', 'subtasks']

# Задание 4:
class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'categories', 'status', 'deadline']

    def validate_deadline(self, value):
        if value < datetime.now():
            raise serializers.ValidationError("Дата дедлайна не может быть в прошлом.")
        return value
