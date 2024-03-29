# Generated by Django 4.0.5 on 2022-10-03 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sentence', '0003_alter_sentence_invalidity_reason_and_more'),
        ('user', '0003_rename_td_id_user_tg_id'),
        ('voice', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audio_url', models.URLField()),
                ('checks_count', models.PositiveSmallIntegerField(default=0, verbose_name='Checks count')),
                ('is_valid', models.BooleanField(default=False, verbose_name='Is valid')),
                ('invalidity_reason', models.IntegerField(choices=[(0, 'Not correct sentence'), (1, 'Other invalidities'), (2, 'Unknown yet')], default=2, verbose_name='Invalidity reason')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='user.user', verbose_name='Author')),
                ('sentence', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='sentence.sentence', verbose_name='Sentence')),
            ],
            options={
                'verbose_name': 'Voice',
                'verbose_name_plural': 'Voices',
            },
        ),
    ]
