# Generated by Django 4.1.1 on 2022-09-27 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='accent_region',
            field=models.CharField(choices=[('Andijon', 'Andijon'), ('Buxoro', 'Buxoro'), ("Farg'ona", 'Fargona'), ('Jizzax', 'Jizzax'), ('Xorazm', 'Xorazm'), ('Namangan', 'Namangan'), ('Navoiy', 'Navoiy'), ('Qashqadaryo', 'Qashqadaryo'), ("Qoraqalpog'iston", 'Qoraqalpogiston'), ('Samarqand', 'Samarqand'), ('Surxondaryo', 'Surxondaryo'), ('Toshkent viloyati', 'Toshkent'), ('Toshkent shahri', 'Toshkent Shahri')], help_text='Please enter region...', max_length=18),
        ),
    ]
