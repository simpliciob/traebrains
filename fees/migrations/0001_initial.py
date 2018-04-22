# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-22 16:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=50)),
                ('Amount_paid', models.DecimalField(decimal_places=2, max_digits=5)),
                ('student_number', models.CharField(max_length=50)),
                ('invoice_number', models.CharField(max_length=50)),
                ('tutoring_fee', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Bank_name', models.CharField(max_length=50)),
            ],
        ),
    ]