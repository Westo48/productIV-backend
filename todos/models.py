from django.db import models
from django.conf import settings

# Create your models here.


class Todo(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='todos',
        on_delete=models.CASCADE
    )
    body = models.CharField(max_length=50)
    is_complete = models.BooleanField(
        verbose_name='is complete', default=False)
    date_added = models.DateTimeField(
        verbose_name='date added', auto_now_add=True)
