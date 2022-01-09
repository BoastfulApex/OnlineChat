from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, )
    bio = models.CharField(null=True, max_length=500)
    email = models.CharField(null=True, max_length=250)
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Message(models.Model):
    user1 = models.ForeignKey(Profile, related_name='user1',  on_delete=models.SET_NULL, null=True)
    user2 = models.ForeignKey(Profile, related_name='user2', on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=1000, default='')

    @property
    def time(self):
        return self.date.strftime('%H:%M')
    @property
    def time_to_int(self):
        return int(self.date.strftime("%Y%m%d%H%M%S"))