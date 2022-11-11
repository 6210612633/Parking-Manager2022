# Generated by Django 4.0.4 on 2022-11-11 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking_lot', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parkinglot',
            name='customer',
        ),
        migrations.AddField(
            model_name='parkinglot',
            name='customer',
            field=models.ManyToManyField(to='parking_lot.customer'),
        ),
    ]
