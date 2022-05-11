from django.db import models

# Create your models here.
class Task(models.Model):
    # id
    name = models.CharField(max_length=70, blank=True)
    finished = models.BooleanField(blank=True)

    def __str__(self):
        return self.name