# Generated by Django 4.1.3 on 2023-03-19 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance_app', '0006_alter_income_date_received_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='income',
            name='month_received',
            field=models.IntegerField(default=3),
        ),
        migrations.AddField(
            model_name='purchase',
            name='month_purchased',
            field=models.IntegerField(default=3),
        ),
    ]