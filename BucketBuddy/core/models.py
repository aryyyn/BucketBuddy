from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

User = get_user_model()


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=False)
    userimg = models.ImageField(upload_to='User_Images', default="default.png")


    def __str__(self):
        return self.user.username
        

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField(blank=False)
    description = models.TextField()
    category = models.CharField(max_length=255)  
    status = models.CharField(max_length=255)
    deadline = models.DateTimeField(default=datetime.now())


    def __str__(self):
        hello = self.user.username + "|Item: " +self.name
        return hello


