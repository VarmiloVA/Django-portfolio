from django.db import models

class Project(models.Model):
    """Shows a coding Project"""
    title = models.CharField(max_length=255)
    link = models.TextField()

    def __str__(self):
        """Returns the project's title"""
        return self.title