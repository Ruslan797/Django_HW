from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from taskmanager.models import Task


@receiver(pre_save, sender=Task)
def task_store_previous_status(sender, instance: Task, **kwargs):
    """
    Перед сохранением вытаскиваем старый статус из БД,
    чтобы потом понять — изменился он или нет.
    """
    if not instance.pk:
        instance._previous_status = None
        return

    try:
        old = Task.objects.only("status").get(pk=instance.pk)
        instance._previous_status = old.status
    except Task.DoesNotExist:
        instance._previous_status = None


@receiver(post_save, sender=Task)
def task_notify_owner_on_status_change(sender, instance: Task, created: bool, **kwargs):
    """
    После сохранения отправляем письмо владельцу,
    если статус изменился.
    Защита от повторной отправки: если статус не менялся (old == new),
    письмо не уходит.
    """

    if created:
        return

    old_status = getattr(instance, "_previous_status", None)
    new_status = instance.status

    # защита от повторов: если статус не поменялся — ничего не шлём
    if old_status == new_status:
        return

    owner = getattr(instance, "owner", None)
    if not owner:
        return

    owner_email = getattr(owner, "email", None)
    if not owner_email:
        # нет email — некуда отправлять
        return

    subject = f"Task status changed: {instance.title}"
    message = (
        f"Hello, {getattr(owner, 'username', 'user')}!\n\n"
        f"Your task status has changed.\n"
        f"Task: {instance.title}\n"
        f"Old status: {old_status}\n"
        f"New status: {new_status}\n\n"
        f"Regards,\nTaskManager"
    )

    send_mail(
        subject=subject,
        message=message,
        from_email=getattr(settings, "DEFAULT_FROM_EMAIL", None),
        recipient_list=[owner_email],
        fail_silently=True,
    )
