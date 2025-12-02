from django.db import models
from django.utils import timezone


class CategoryManager(models.Manager):
    def get_queryset(self):
        # Return only active (not deleted) categories.
        return super().get_queryset().filter(is_deleted=False)


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)


    class Meta:
        unique_together = ['name']
        db_table = 'task_manager_category'
        verbose_name = 'Category'


    objects = CategoryManager()
    all_objects = models.Manager()


    def delete(self, using=None, keep_parents=False):
        """Soft delete instead of physical delete"""
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

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

    title = models.CharField(max_length=150, unique=True)
    description = models.TextField()
    categories = models.ManyToManyField(Category, related_name="tasks")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('title', 'created_at')
        db_table = 'task_manager_task'
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        ordering = ['-created_at']

    def __str__(self):
        return f"Task - {self.title}"


class SubTask(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('in_progress', 'In progress'),
        ('pending', 'Pending'),
        ('blocked', 'Blocked'),
        ('done', 'Done'),
    ]

    title = models.CharField(max_length=150, unique=True)
    description = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="subtasks")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        unique_together = ('title', 'created_at')
        db_table = 'task_manager_subtask'
        verbose_name = "SubTask"
        verbose_name_plural = "SubTasks"
        ordering = ['title']

    def __str__(self):
        return f"SubTask: {self.title} (for {self.task.title})"










