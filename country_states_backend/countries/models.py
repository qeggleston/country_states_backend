from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles



class Country(models.Model):
    code = models.CharField(max_length='100')
    name = models.CharField(max_length='100')

