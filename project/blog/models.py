from unittest.mock import DEFAULT
from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=20)
    contents = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    cnt = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def summary(self):
        return self.contents[:100]
