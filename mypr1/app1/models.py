from django.db.models import JSONField
from django.db import models


class Input(models.Model):
    field = models.CharField(max_length=30)
    data = JSONField()

    class Meta:
        verbose_name = "input"
        verbose_name_plural = "Inputs"

    def __str__(self):
        return self.field
