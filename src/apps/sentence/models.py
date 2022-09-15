from django.db import models

# Create your models here.
#lets start it
class Sentence(models.Model):
    id=models.AutoField(primary_key=True)
    text=models.CharField(max_length=500)
    