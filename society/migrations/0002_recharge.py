# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('society', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recharge',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.CharField(max_length=200, null=True)),
                ('price', models.FloatField()),
                ('created_at', models.DateTimeField()),
                ('member', models.ForeignKey(to='society.Member')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
