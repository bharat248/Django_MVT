from django.db import models

# Create your models here.
class user(models.Model):
    first_name = models.CharField(max_length = 256)
    last_name = models.CharField(max_length = 264)
    email = models.EmailField(unique = True,max_length = 264)
    def __str__(self):
        return self.email
