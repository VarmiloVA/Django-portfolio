from django.db import models

class Topic(models.Model):
    """The topic about I'm talking about"""
    title = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns a representation of the topic"""
        return self.title

class Content(models.Model):
    """Content made about a topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns a brief introduction of the content"""
        return f'{self.text[:50]}...'