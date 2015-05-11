# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generic', '0004_auto_20150511_1719'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='marId')),
                ('nome', models.CharField(max_length=45, db_column='marNome')),
            ],
            options={
                'db_table': 'Marca',
            },
        ),
        migrations.AddField(
            model_name='produto',
            name='categoria',
            field=models.ForeignKey(db_column='proCatId', default=None, to='generic.Categoria'),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True, db_column='catId'),
        ),
        migrations.AddField(
            model_name='produto',
            name='marca',
            field=models.ForeignKey(db_column='proMarId', default=None, to='generic.Marca'),
        ),
    ]
