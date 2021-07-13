# Generated by Django 3.1.7 on 2021-04-16 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210416_1016'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signin',
            old_name='password',
            new_name='lastname',
        ),
        migrations.AddField(
            model_name='signin',
            name='password1',
            field=models.CharField(default=1, max_length=200),
        ),
        migrations.AddField(
            model_name='signin',
            name='password2',
            field=models.CharField(default=1, max_length=200),
        ),
    ]
