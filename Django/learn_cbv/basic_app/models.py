from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    #Additional
    portfolio = models.URLField(blank=True)

    def __str__(self):
        return self.user.username

class School(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('basic_app:detail',kwargs={'pk':self.pk})

class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School,related_name = 'students',on_delete=models.CASCADE)

    def __str__(self):
        return self.name
