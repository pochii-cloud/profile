# Generated by Django 3.1.7 on 2021-04-16 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='login',
            options={'verbose_name_plural': 'logins'},
        ),
        migrations.AlterModelOptions(
            name='signin',
            options={'verbose_name_plural': 'signins'},
        ),
    ]