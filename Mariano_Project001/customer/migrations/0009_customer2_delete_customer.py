# Generated by Django 4.2.6 on 2023-10-24 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_customer_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=100)),
                ('username2', models.CharField(max_length=100)),
                ('comments', models.CharField(default='not specified', max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
