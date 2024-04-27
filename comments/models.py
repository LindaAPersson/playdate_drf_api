from django.db import models
from django.contrib.auth.models import User
from playdate.models import Playdate

# Create your models here.


class Comment(models.Model):
    """
    Model to represent comments on playdate posts.

    Attributes:
        user (ForeignKey): The user who made the comment.
        playdate_post (ForeignKey): The playdate post the comment is associated with.
        created_at (DateTimeField): The timestamp when the comment was created.
        content (TextField): The content of the comment.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    playdate_post = models.ForeignKey(Playdate, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content
