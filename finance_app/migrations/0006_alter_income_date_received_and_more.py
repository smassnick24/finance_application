# Generated by Django 4.1.3 on 2023-02-17 17:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('finance_app', '0005_alter_income_date_received_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='date_received',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='date_purchased',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
