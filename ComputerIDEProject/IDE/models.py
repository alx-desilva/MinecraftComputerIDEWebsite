from django.db import models


class Submission(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
