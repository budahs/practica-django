# Generated by Django 2.2.5 on 2019-10-20 23:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20191020_2313'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='fecha_publicacion',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 20, 23, 14, 30, 51349), null=True),
        ),
    ]
