from django.db import models

class Foo(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

class User(models.Model):
    full_name = models.CharField(max_length=200)
    td_id = models.IntegerField()
    gender = models.ForeignKey(Foo, on_delete=models.CASCADE)
    year_of_birth = models.IntegerField()
    accent_region = models.IntegerField()
    native_language = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    
    
    def __str__(self):
        return self.full_name
    
    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"