# Generated by Django 4.2.6 on 2023-10-30 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_customer_preference1_customer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='userID',
            field=models.BigIntegerField(default=0),
        ),
    ]
