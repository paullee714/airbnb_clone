# Generated by Django 2.2.5 on 2020-01-28 00:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_login_mehtod'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='login_mehtod',
            new_name='login_method',
        ),
    ]