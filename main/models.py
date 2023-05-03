from django.db import models
from django.conf import settings

# Create your models here.
class Resume(models.Model):
    user = models.OneToOneField( settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    address = models.TextField()
    age = models.IntegerField()
    dob = models.DateField()
    sscSchoolName = models.CharField(max_length=250)
    hscSchoolName = models.CharField(max_length=250)
    graduationCollegeName = models.CharField(max_length=250)
    sscPercentage = models.IntegerField()
    hscPercentage = models.IntegerField()
    graduationPercentage = models.IntegerField()
    experience = models.TextField()
    career_objective = models.TextField()
    skills = models.TextField()
    contacts = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
