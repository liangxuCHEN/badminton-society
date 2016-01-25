# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill_table',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.CharField(max_length=200, null=True)),
                ('created_at', models.DateTimeField()),
                ('is_pay', models.BooleanField(default=False)),
                ('total_price', models.FloatField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('sexual', models.IntegerField()),
                ('balance', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Personal_bill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bill_comment', models.CharField(max_length=200, null=True)),
                ('price', models.FloatField()),
                ('created_at', models.DateTimeField()),
                ('bill_table', models.ForeignKey(to='society.Bill_table')),
                ('member', models.ForeignKey(to='society.Member')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
