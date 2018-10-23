from django.db import models
from countries.models import Country

# Create your models here.
class State(models.Model): 
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10)
    countryId = models.IntegerField()
    #country = models.ForeignKey(Country, related_name='Country', on_delete=models.CASCADE)
