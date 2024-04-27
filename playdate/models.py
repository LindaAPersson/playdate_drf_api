from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.


class Playdate(models.Model):
    """
    Model representing a playdate event.

    Attributes:
        AGE_CHOICES (list of tuples): Choices for suitable_age field.
        title (CharField): Title of the playdate.
        image (ImageField): Image associated with the playdate.
        date (DateField): Date of the playdate.
        location (CharField): Location of the playdate.
        description (TextField): Description of the playdate.
        organizer (ForeignKey): User who organized the playdate.
        prize (DecimalField): Prize associated with the playdate (optional).
        created_at (DateTimeField): Timestamp when the playdate was created.
        parent_stay_required (BooleanField): Indicates if parent stay is required.
        time (TimeField): Time of the playdate.
        suitable_age (CharField): Suitable age group for the playdate.
    """
    AGE_CHOICES = [
        ('all', 'All Ages'),
        ('infant', 'Infant (0-2 years)'),
        ('toddler', 'Toddler (2-5 years)'),
        ('child', 'Child (5-12 years)'),
        ('teenager', 'Teenager (13-18 years)'),
    ]

    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/',
                              default='../default_posts_kcstnt', blank=True)
    date = models.DateField()
    location = models.CharField(max_length=100)
    description = models.TextField()
    organizer = models.ForeignKey(User, on_delete=models.CASCADE,
                                  related_name='organized_playdates')
    prize = models.DecimalField(max_digits=10, decimal_places=2,
                                null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    parent_stay_required = models.BooleanField(default=True)
    time = models.TimeField()
    suitable_age = models.CharField(max_length=20, choices=AGE_CHOICES)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.title

    def formatted_time(self):
        return self.time.strftime(['%H:%M'])

    def has_taken_place(self):
        return self.date < datetime.now()
