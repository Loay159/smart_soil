from django.db import models


class Level(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return self.name
    
class Zone(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name='zone_level')

    def __str__(self) -> str:
        return self.name
    

    
