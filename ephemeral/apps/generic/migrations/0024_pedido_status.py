# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generic', '0023_auto_20150623_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='status',
            field=models.CharField(default='aguardando pagamento', max_length=30, db_column='pedStatus', choices=[('aguardando pagamento', 'aguardando pagamento'), ('pago', 'pago'), ('enviado', 'enviado'), ('entregue', 'entregue')]),
        ),
    ]
