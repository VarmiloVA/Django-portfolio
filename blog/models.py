from xml.sax.handler import EntityResolver
from django.db import models

# Create your models here.
class Post(models.Model):
    """Code-related topic that I'm learning about"""
    title = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns a representation of the post"""
        return self.title

class Content(models.Model):
    """What I've learned about a topic"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "contents"
    
    def __str__(self):
        """Returns a representation of the post's content"""
        return f"{self.content[:50]}"