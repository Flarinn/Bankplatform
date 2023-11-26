# Generated by Django 4.2.1 on 2023-06-01 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_alter_agentaccount_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fam', models.CharField(max_length=200)),
                ('Name', models.CharField(max_length=200)),
                ('LastName', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('role', models.CharField(choices=[('BANK', 'BANK'), ('AGENT', 'AGENT'), ('PLATFORM', 'PLATFORM')], max_length=9)),
                ('AgCompany', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.agentcompany')),
                ('BankCompany', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.bankcompany')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='bankaccount',
            name='Company',
        ),
        migrations.RemoveField(
            model_name='application',
            name='AgentWorkerId',
        ),
        migrations.RemoveField(
            model_name='application',
            name='BankWorkerId',
        ),
        migrations.RemoveField(
            model_name='application',
            name='PlatformWorkerId',
        ),
        migrations.DeleteModel(
            name='AgentAccount',
        ),
        migrations.DeleteModel(
            name='BankAccount',
        ),
        migrations.DeleteModel(
            name='PlatformAccount',
        ),
        migrations.AddField(
            model_name='application',
            name='WorkerId',
            field=models.ManyToManyField(related_name='related_users', to='account.account'),
        ),
    ]
