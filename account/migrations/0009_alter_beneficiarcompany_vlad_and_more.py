# Generated by Django 4.2.1 on 2023-05-31 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_person_rank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beneficiarcompany',
            name='Vlad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.person'),
        ),
        migrations.AlterField(
            model_name='principalcompany',
            name='Vlad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.person'),
        ),
    ]
