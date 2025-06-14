# Generated by Django 5.2.2 on 2025-06-10 23:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='budget',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2025-06-10 12:00:00'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='emi',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2025-06-10 12:00:00'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='emi',
            name='issuing_bank',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='emi',
            name='loan_name',
            field=models.CharField(default=' ', max_length=100),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Rent', 'Rent'), ('Groceries', 'Groceries'), ('Utilities', 'Utilities'), ('Miscellaneous', 'Miscellaneous'), ('Entertainment', 'Entertainment'), ('Transport', 'Transport'), ('Health', 'Health'), ('Education', 'Education')], max_length=50)),
                ('amount', models.FloatField()),
                ('record_month', models.CharField(max_length=20)),
                ('record_year', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('target_amount', models.FloatField()),
                ('saved_amount', models.FloatField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deadline', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
