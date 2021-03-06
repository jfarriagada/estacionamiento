# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-14 03:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=40)),
                ('color', models.CharField(max_length=40)),
                ('patent', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=40)),
                ('name', models.CharField(max_length=40)),
                ('lastname', models.CharField(max_length=40)),
                ('sex', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], default='M', max_length=1)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Parking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', models.IntegerField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parkings.Car')),
            ],
        ),
    ]
