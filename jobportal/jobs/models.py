from django.db import models
from django.contrib.auth.models import  User


class Job(models.Model):
    position_name = models.CharField(max_length=100)
    text_description = models.CharField(max_length= 300)
    age_criteria = models.IntegerField()
    min_age = models.IntegerField()
    max_age = models.IntegerField
    salary = models.IntegerField()
    no_of_openings = models.IntegerField()
    creater = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.position_name
