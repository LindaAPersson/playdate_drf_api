from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Playdate(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', default='../default_posts_kcstnt', blank=True)
    date = models.DateField()
    location = models.CharField(max_length=100)
    description = models.TextField()
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organized_playdates')
    prize = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    parent_stay_required = models.BooleanField(default=True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.title