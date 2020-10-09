# Generated by Django 3.1.2 on 2020-10-09 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forum',
            name='description',
        ),
        migrations.RemoveField(
            model_name='forum',
            name='email',
        ),
        migrations.RemoveField(
            model_name='forum',
            name='link',
        ),
        migrations.RemoveField(
            model_name='forum',
            name='name',
        ),
        migrations.RemoveField(
            model_name='forum',
            name='topic',
        ),
        migrations.AddField(
            model_name='forum',
            name='code',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='forum',
            name='game_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]