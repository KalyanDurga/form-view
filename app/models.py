from django.db import models
from django.core import validators

# Create your models here.

class Student(models.Model):
    sname=models.CharField(max_length=50,validators=[validators.MinLengthValidator(5)])
    sid=models.IntegerField(primary_key=True,)
    sage=models.IntegerField(validators=[validators.MinValueValidator(20)])
    saddress=models.TextField()

    def __str__(self) -> str:
        return self.sname