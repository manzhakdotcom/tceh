# Generated by Django 2.1 on 2018-08-21 10:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WriteOut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_created', models.DateField(default=datetime.datetime(2018, 8, 21, 13, 52, 3, 640625))),
                ('write_out', models.TextField(default='Запись')),
            ],
            options={
                'verbose_name': 'Запись СЦБ',
                'verbose_name_plural': 'Записи СЦБ',
            },
        ),
    ]
