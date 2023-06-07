from django.db import models


class Zone(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    level = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.name
