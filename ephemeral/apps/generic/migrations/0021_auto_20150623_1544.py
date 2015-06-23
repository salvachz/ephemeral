# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generic', '0020_pedido_forma_pagament'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedido',
            old_name='forma_pagament',
            new_name='forma_pagamento',
        ),
    ]
