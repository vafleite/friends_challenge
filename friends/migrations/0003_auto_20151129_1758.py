# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0002_auto_20151129_1658'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friend',
            old_name='pos_x',
            new_name='x',
        ),
        migrations.RenameField(
            model_name='friend',
            old_name='pos_y',
            new_name='y',
        ),
    ]
