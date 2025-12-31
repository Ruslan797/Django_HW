import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from datetime import timedelta
from django.utils import timezone
from taskmanager.models import Task, SubTask



# Создание записей
task = Task.objects.create(
    title="Prepare presentation",
    description="Prepare materials and slides for the presentation",
    status="New",
    deadline=timezone.now() + timedelta(days=3)
)

SubTask.objects.create(
    task=task,
    title="Gather information",
    description="Find necessary information for the presentation",
    status="New",
    deadline=timezone.now() + timedelta(days=2)
)

SubTask.objects.create(
    task=task,
    title="Create slides",
    description="Create presentation slides",
    status="New",
    deadline=timezone.now() + timedelta(days=1)
)

# Чтение записей
new_tasks = Task.objects.filter(status="New")
print("Tasks with status 'New':")
for new_task in new_tasks:
    print(f"Task: {new_task.title}, Status: {new_task.status}")

expired_done_subtasks = SubTask.objects.filter(
    status="Done",
    deadline__lt=timezone.now()
)
print("\nExpired 'Done' SubTasks:")
for subtask in expired_done_subtasks:
    print(f"SubTask: {subtask.title}, Status: {subtask.status}, Deadline: {subtask.deadline}")

# Изменение записей
task = Task.objects.get(title="Prepare presentation")
task.status = "In progress"
task.save()
print("\nTask status updated to 'In progress'")

subtask_info = SubTask.objects.get(title="Gather information", task=task)
subtask_info.deadline = timezone.now() - timedelta(days=2)
subtask_info.save()
print("Deadline for 'Gather information' updated to two days ago")

subtask_slides = SubTask.objects.get(title="Create slides", task=task)
subtask_slides.description = "Create and format presentation slides"
subtask_slides.save()
print("Description for 'Create slides' updated")

# Проверка изменений
updated_task = Task.objects.get(title="Prepare presentation")
print(f"\nUpdated Task: {updated_task.title}, Status: {updated_task.status}")

updated_subtask_info = SubTask.objects.get(title="Gather information", task=task)
print(f"Updated SubTask 'Gather information' Deadline: {updated_subtask_info.deadline}")

updated_subtask_slides = SubTask.objects.get(title="Create slides", task=task)
print(f"Updated SubTask 'Create slides' Description: {updated_subtask_slides.description}")

# Удаление записей
task = Task.objects.get(title="Prepare presentation")
task.delete()
print("\nTask 'Prepare presentation' and its subtasks deleted")

# Проверка удаления
print("\nAll Tasks after deletion:")
print(Task.objects.all())
print("\nAll SubTasks after deletion:")
print(SubTask.objects.all())


