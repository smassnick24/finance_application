# Generated by Django 4.1.3 on 2023-02-17 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance_app', '0002_alter_purchase_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='income',
            name='income_source',
            field=models.TextField(default='wesco'),
            preserve_default=False,
        ),
    ]
