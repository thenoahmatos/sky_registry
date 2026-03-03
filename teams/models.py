from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    manager = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
