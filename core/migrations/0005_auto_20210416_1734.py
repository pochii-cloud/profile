# Generated by Django 3.1.7 on 2021-04-16 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210416_1732'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signin',
            old_name='password2',
            new_name='confirmpassword',
        ),
    ]