from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    def clean(self):
        if self.date and self.date < timezone.now(): 
            raise ValidationError('The event date cannot be in the past.')