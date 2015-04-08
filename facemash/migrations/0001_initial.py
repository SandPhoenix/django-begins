# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_rating', models.FloatField(default=1500)),
                ('user_name', models.CharField(max_length=100)),
                ('user_id', models.BigIntegerField(default=0)),
                ('user_gender', models.CharField(max_length=1, choices=[(b'm', b'Male'), (b'f', b'Female')])),
                ('user_picture', models.CharField(default=b'https://pbs.twimg.com/profile_images/3700906677/620e0c1391e55d928f4a7d34efd19e89.png', max_length=200)),
            ],
        ),
    ]
