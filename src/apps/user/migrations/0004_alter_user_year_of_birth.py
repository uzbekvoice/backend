# Generated by Django 4.0.5 on 2022-10-04 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_rename_td_id_user_tg_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='year_of_birth',
            field=models.IntegerField(help_text='Please enter birth date...', max_length=4),
        ),
    ]