# Generated by Django 4.0.4 on 2022-11-12 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parking_lot', '0003_customer_tel_parkinglot_qr_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=3, null=True)),
                ('status', models.BooleanField(default=True)),
                ('parking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking_lot.parkinglot')),
            ],
        ),
    ]
