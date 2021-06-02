from django.contrib.auth.models import User

from django.db import models

class userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)

User.userprofile = property(lambda u:userprofile.objects.get_or_create(user = u)[0])

