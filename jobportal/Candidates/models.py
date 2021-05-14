from django.db import models


GENDER_MALE = 'male'
GENDER_Female = 'female'
GENDER_CHIOCE = ((GENDER_MALE , 'male'),
                 (GENDER_Female , 'female'))

class Candidates(models.Model):
    name = models.CharField(max_length=100)
    age=models.IntegerField()
    gender=models.CharField(max_length=122, choices=GENDER_CHIOCE, default = GENDER_MALE)
    mobile = models.CharField(max_length=100,default='950')
    city_live_in = models.CharField(max_length= 20, default='hyderabd')
    salary_expectations = models.IntegerField(default=2000)
    willing_to_relocate = models.BooleanField(default=False)

    def __str__(self):
        return self.name