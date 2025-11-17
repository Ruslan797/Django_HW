from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        unique_together = ['name']
        db_table = 'task_manager_category'
        verbose_name = 'Category'

    def __str__(self):
        return f"Category - {self.name}"


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




"""
Домашнее задание: Проект "Менеджер задач" — продолжение
Цель:
Добавить строковое представление (str) и метаданные (Meta) к моделям менеджера задач, 
а также настроить административную панель для удобного управления этими моделями.

Реализуйте изменения в моделях:
Модель Task:
Добавить метод str, который возвращает название задачи.

Добавить класс Meta с настройками:

Имя таблицы в базе данных: 'task_manager_task'.
Сортировка по убыванию даты создания.
Человекочитаемое имя модели: 'Task'.
Уникальность по полю 'title'.

Модель SubTask:
Добавить метод str, который возвращает название подзадачи.
Добавить класс Meta с настройками:
Имя таблицы в базе данных: 'task_manager_subtask'.
Сортировка по убыванию даты создания.
Человекочитаемое имя модели: 'SubTask'.
Уникальность по полю 'title'.

Модель Category:
Добавить метод str, который возвращает название категории.

Добавить класс Meta с настройками:
Имя таблицы в базе данных: 'task_manager_category'.
Человекочитаемое имя модели: 'Category'.
Уникальность по полю 'name'.


Настройте отображение моделей в админке: 

В файле admin.py вашего приложения добавьте классы администратора для настройки отображения моделей Task, SubTask и Category.

Зафиксируйте изменения в гит: 
Создайте новый коммит и запушьте его в ваш гит.

Создайте записи через админку:
Создайте суперпользователя.
Перейдите в административную панель Django.
Добавьте несколько объектов для каждой модели.
Оформите ответ: 

Прикрепите ссылку на гит и скриншоты, где видны созданные объекты к ответу на домашнее задание.
"""



