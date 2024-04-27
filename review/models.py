from django.db import models
from django.contrib.auth.models import User
from playdate.models import Playdate

# Create your models here.


class Review(models.Model):
    """
    Model to represent reviews for playdate posts.

    Attributes:
        playdate_post (ForeignKey): The playdate post associated with the review.
        user (ForeignKey): The user who made the review.
        comment (TextField): The content of the review.
        attendance (BooleanField): Indicates if the user attended the playdate.
        bring_this (TextField, optional): Item(s) brought to the playdate.
        age_recommendation (CharField, optional): Suitable age recommendation.
        created_at (DateTimeField): The timestamp when the review was created.
    """
    playdate_post = models.ForeignKey(Playdate, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    attendance = models.BooleanField(default=False)
    bring_this = models.TextField(blank=True, null=True)
    age_recommendation = models.CharField(max_length=100,
                                          blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.playdate.title}"
