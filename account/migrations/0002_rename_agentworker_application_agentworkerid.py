# Generated by Django 4.2.1 on 2023-05-21 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='AgentWorker',
            new_name='AgentWorkerId',
        ),
    ]
