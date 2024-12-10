from django.db import models

# Create your models here.
class Student(models.Model):
    
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    cnumber = models.CharField(primary_key=True, max_length=10)
    major = models.CharField(max_length=50)
    dob = models.DateField()
    gpa = models.FloatField()

    def __str__(self):
        return self.lname
