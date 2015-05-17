# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import lists.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='')),
                ('image', models.FileField(upload_to=lists.models.get_upload_file_name)),
                ('parent', models.TextField(default='1')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
