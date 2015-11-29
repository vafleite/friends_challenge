# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('pos_x', models.IntegerField()),
                ('pos_y', models.IntegerField()),
                ('friends', models.ForeignKey(to='friends.Friend')),
            ],
        ),
    ]
