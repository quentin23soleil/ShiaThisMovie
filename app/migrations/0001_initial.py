# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('tmdb_id', models.IntegerField()),
                ('title', models.CharField(max_length=255)),
                ('rating', models.IntegerField()),
                ('rating_number', models.IntegerField()),
            ],
        ),
    ]
