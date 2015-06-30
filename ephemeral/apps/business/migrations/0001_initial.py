# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrinho',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='carId')),
                ('data', models.DateTimeField(null=True, db_column='carDate')),
                ('usuario', models.ForeignKey(db_column='carUsrId', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'db_table': 'Carrinho',
            },
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='comId')),
                ('data', models.DateTimeField(null=True, db_column='comDate')),
                ('usuario', models.ForeignKey(db_column='comUsrId', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'db_table': 'Compra',
            },
        ),
    ]
