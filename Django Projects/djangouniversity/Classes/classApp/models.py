import time

from django.db import models

# Create your models here.
class djangoClasses(models.Model):
    Title = models.CharField(max_length=60)
    Course = models.IntegerField(max_length=10, default="", blank=True, null=False)
    Instructor_Name = models.CharField(max_length=60, default="", blank=False)
    Duration = models.FloatField(max_length=2, default=time.time())

    Class_Library = models.Manager()

    def __str__(self):
        return self.Title