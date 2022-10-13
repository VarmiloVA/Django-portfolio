from xml.sax.handler import EntityResolver
from django.db import models

# Create your models here.
class Topic(models.Model):
    """Code-related topic that I'm learning about"""
    text = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns a representation of the topic"""
        return self.text

class Entry(models.Model):
    """What I've learned about a topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "entries"
    
    def __str__(self):
        """Returns a representation of the entry"""
        return f"{self.text[:50]}"