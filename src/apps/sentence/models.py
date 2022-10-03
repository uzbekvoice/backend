from django.db import models

# Create your models here
class InvalidityReasons(models.IntegerChoices):
    NOTCORRECT = 0, 'Not Correct Sentence'
    OTHERS = 1, 'Other invalidities'



#lets start it
class Sentence(models.Model):
    text=models.TextField(verbose_name="text")
    #author=models.ForeignKey(User,verbose_name="author_in_integer",on_delete=models.RESTRICT)
    reads_count=models.IntegerField(verbose_name="reads count")
    is_valid=models.BooleanField(verbose_name="boolean")
    invalidity_reason=models.IntegerField(choices=InvalidityReasons.choices,verbose_name="Integer")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text