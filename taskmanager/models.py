from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('in_progress', 'In progress'),
        ('pending', 'Pending'),
        ('blocked', 'Blocked'),
        ('done', 'Done'),
    ]

    title = models.CharField(max_length=150)
    description = models.TextField()
    categories = models.ManyToManyField(Category, related_name="tasks")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('title', 'created_at')

    def __str__(self):
        return f"{self.title} ({self.status})"


class SubTask(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('in_progress', 'In progress'),
        ('pending', 'Pending'),
        ('blocked', 'Blocked'),
        ('done', 'Done'),
    ]

    title = models.CharField(max_length=150)
    description = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="subtasks")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"SubTask: {self.title} (for {self.task.title})"



