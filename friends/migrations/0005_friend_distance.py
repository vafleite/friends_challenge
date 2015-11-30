# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0004_friend_me'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='distance',
            field=models.FloatField(null=True),
        ),
    ]
