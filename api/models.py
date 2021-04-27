from django.db import models


class Todo(models.Model):
    title = models.CharField(blank=False, null=False, max_length=100)
    content = models.CharField(blank=False, null=False, max_length=500)

    def __str__(self):
        return self.title
