from django.db import models



class User(models.Model):
    class GenderChoices(models.TextChoices):
          MALE = 'M',
          FEMALE = 'F',
          
    class RegioinChoices(models.TextChoices):
          Andijon = "Andijon",
          Buxoro = "Buxoro",
          Fargona = "Farg'ona",
          Jizzax = "Jizzax",
          Xorazm = "Xorazm",
          Namangan = "Namangan",
          Navoiy = "Navoiy",
          Qashqadaryo = "Qashqadaryo",
          Qoraqalpogiston = "Qoraqalpog'iston",    
          Samarqand = "Samarqand",    
          Surxondaryo = "Surxondaryo",    
          Toshkent = "Toshkent",    
    
    class LanguageChoices(models.TextChoices):
          UZ = 'Uz',
          RU = 'Ru',
          QR = 'Qr',
          
    full_name = models.CharField(max_length=200, help_text="Please enter full name...")
    td_id = models.PositiveIntegerField(max_length=20, help_text="Please enter td id...")
    gender = models.CharField(max_length=1, choices=GenderChoices.choices)
    year_of_birth = models.DateField(help_text="Please enter birth date...")
    accent_region = models.CharField(choices=RegioinChoices.choices, help_text="Please enter region..."),
    native_language = models.CharField(max_length=2, choices=LanguageChoices.choices, help_text="Please choose language...")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.full_name
    
    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"