from django.db import models

# Create your models here.

class Contact(models.Model):
    """
    Model representing contact,
    that are used for users to get in contact with the creators.
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
