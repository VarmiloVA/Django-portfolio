from django.db import models

class Topic(models.Model):
    """A topioc which the user is learning about"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns a representation of the model as a string"""
        return self.text