# Generated by Django 4.2.1 on 2023-06-01 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_rename_account_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='Fam',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='LastName',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='Name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='last_login',
        ),
    ]
