# Generated by Django 4.0.4 on 2022-04-26 22:20

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(blank=True, default='', max_length=60)),
                ('Last_name', models.CharField(blank=True, default='', max_length=60)),
                ('Initial_deposit', models.DecimalField(decimal_places=2, default=0.0, max_digits=10000)),
            ],
            managers=[
                ('Accounts', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Description', models.TextField(blank=True, default='', max_length=200)),
                ('Amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('Type', models.CharField(choices=[('Deposit', 'Deposit'), ('Withdrawal', 'Withdrawal')], max_length=10)),
                ('Account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Checkbook.account')),
            ],
            managers=[
                ('Transactions', django.db.models.manager.Manager()),
            ],
        ),
    ]
