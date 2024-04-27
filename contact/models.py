from django.db import models

# Create your models here.


class Contact(models.Model):
    """
    Model representing contact information for users to get in touch with the creators.

    Attributes:
        name (CharField): The name of the contact person.
        email (EmailField): The email address of the contact person.
        subject (CharField): The subject of the message.
        message (TextField): The content of the message.
        created_at (DateTimeField): The timestamp when the contact message was created.
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
