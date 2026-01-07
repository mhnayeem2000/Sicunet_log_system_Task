import subprocess
import os
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils.timezone import now
from django.conf import settings
from .models import AccessLog

event_log = os.path.join(settings.BASE_DIR, "event_list.txt")


@receiver(post_save, sender=AccessLog)
def log_event_store(sender, instance, created, **kwargs):
    if created:
        status = "GRANTED" if instance.access_granted else "DENIED"

        log_text = (
            f"[{now().strftime('%Y-%m-%d %H:%M:%S')}] - "
            f"CREATE: Access Log Created for CARD {instance.card_id}. "
            f"Status: {status}"
        )

        print(log_text)

        subprocess.run(
            f'cmd /c echo {log_text}>>"{event_log}"',
            shell=True
        )


@receiver(post_delete, sender=AccessLog)
def log_event_delete(sender, instance, **kwargs):
    log_text = (
        f"[{now().strftime('%Y-%m-%d %H:%M:%S')}] - "
        f"DELETE: Access log (ID: {instance.id}) "
        f"for card {instance.card_id} was deleted."
    )

    print(log_text)

    subprocess.run(
        f'cmd /c echo {log_text}>>"{event_log}"',
        shell=True
    )
