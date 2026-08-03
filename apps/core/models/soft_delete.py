from django.db import models


class SoftDeleteModel(models.Model):
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True