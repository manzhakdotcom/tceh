# Generated by Django 2.1 on 2018-08-23 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0007_auto_20180823_0908'),
    ]

    operations = [
        migrations.AddField(
            model_name='extrawriteout',
            name='write_down_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='journal.WriteDown'),
            preserve_default=False,
        ),
    ]
