# Generated by Django 4.0.4 on 2022-11-12 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parking_lot', '0005_alter_slot_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='slot',
            name='who',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='parking_lot.customer'),
        ),
    ]
