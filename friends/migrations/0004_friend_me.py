# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0003_auto_20151129_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='me',
            field=models.BooleanField(default=False),
        ),
    ]
