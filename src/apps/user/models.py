from django.db import models


class User(models.Model):
    class GenderChoices(models.TextChoices):
          MALE = 'M'
          FEMALE = 'F'
          
    class RegionChoices(models.TextChoices):
          Andijon = "Andijon"
          Buxoro = "Buxoro"
          Fargona = "Farg'ona"
          Jizzax = "Jizzax"
          Xorazm = "Xorazm"
          Namangan = "Namangan"
          Navoiy = "Navoiy"
          Qashqadaryo = "Qashqadaryo"
          Qoraqalpogiston = "Qoraqalpog'iston"    
          Samarqand = "Samarqand" 
          Surxondaryo = "Surxondaryo" 
          Toshkent = "Toshkent viloyati"    
          Toshkent_shahri = "Toshkent shahri"    
    
    class LanguageChoices(models.TextChoices):
          UZ = 'Uz'
          RU = 'Ru'
          QQ = 'Qq'
          
    full_name = models.CharField(max_length=200, help_text="Please enter full name...")
    tg_id = models.PositiveIntegerField(help_text="Please enter td id...")
    gender = models.CharField(max_length=1, choices=GenderChoices.choices)
    year_of_birth = models.DateField(help_text="Please enter birth date...")
    accent_region = models.CharField(max_length=18, choices=RegionChoices.choices, help_text="Please enter region...")
    native_language = models.CharField(
        max_length=2, choices=LanguageChoices.choices, help_text="Please choose language..."
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
