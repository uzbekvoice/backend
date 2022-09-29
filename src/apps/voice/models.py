from django.db import models


# Create your models here.
class VoiceChecker(models.Model):
    #author=models.ForeignKey(User)
    #voice=models.OneToOneField(Voice)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_ad=models.DateTimeField(auto_now=True)


    