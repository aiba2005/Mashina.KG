# Generated by Django 5.1.7 on 2025-03-11 09:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mashina', '0002_remove_cartitem_course_cartitem_car_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9')])),
                ('text', models.TextField()),
                ('created_date', models.DateField(auto_now_add=True)),
                ('car_ratting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mashina.car')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mashina.client')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mashina.company')),
            ],
        ),
    ]
