# Generated by Django 4.2.1 on 2023-06-03 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0022_alter_application_workerid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='WorkerId',
            field=models.ManyToManyField(related_name='applications', to='account.profile'),
        ),
    ]
