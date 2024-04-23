from django.db import models
from django.contrib.auth.models import User
from playdate.models import Playdate

# Create your models here.

class Review(models.Model):
    playdate_post = models.ForeignKey(Playdate, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    attendance = models.BooleanField(default=False)
    bring_this = models.TextField(blank=True, null=True)
    age_recommendation = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.playdate.title}"
