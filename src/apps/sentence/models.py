from django.db import models
from src.apps.user.models import User
# Create your models here.
#lets start it
class Sentence(models.Model):
    text=models.TextField(verbose_name="text")
    author=models.ForeignKey(User,verbose_name="author_in_integer",on_delete=models.CASCADE)
    reads_count=models.IntegerField(verbose_name="reads_count_in_integer")
    is_valid=models.BooleanField(verbose_name="boolean")
    invalidity_reason=models.IntegerField(verbose_name="Integer")
    created_at=models.DateTimeField(verbose_name="datetime",auto_now_add=True)
    updated_at=models.DateTimeField(verbose_name="datetime",auto_now=True)

    def __str__(self):
        return self.text