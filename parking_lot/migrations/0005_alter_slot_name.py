# Generated by Django 4.0.4 on 2022-11-12 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking_lot', '0004_slot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot',
            name='name',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
