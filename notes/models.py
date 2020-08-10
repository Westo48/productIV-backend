from django.db import models
from django.conf import settings

# Create your models here.


class Note(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='notes',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=50, blank=True, null=False)
    body = models.TextField(max_length=500, blank=False, null=False)
    date_added = models.DateTimeField(
        auto_now_add=True, verbose_name='date added')
