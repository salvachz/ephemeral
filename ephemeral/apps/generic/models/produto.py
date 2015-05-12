from __future__ import unicode_literals
from django.db import models
from settings.settings import PRODUCT_ROOT
from django.template.defaultfilters import slugify
import os

def get_image_path(instance, filename):
    return os.path.join(PRODUCT_ROOT, str(instance.id), filename)

class Produto(models.Model):
    id = models.AutoField(db_column='proId', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='proNome', max_length=255)  # Field name made lowercase.       
    descricao = models.TextField(db_column='proDesc', blank=True, null=True)
    categoria = models.ForeignKey('Categoria', db_column='proCatId', null=True, blank=True)
    marca = models.ForeignKey('Marca', db_column='proMarId', null=True, blank=True)
    preco = models.DecimalField(db_column='proPreco', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    quantidade = models.CharField(db_column='proQnt', max_length=45, blank=True, null=True)  # Field name made lowercase.
    image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    slug = models.SlugField(editable=False,blank=True)

    class Meta:
        db_table = 'Produto'

    def __unicode__(self):
        return self.nome

    def save(self, *args, **kwargs):
        super(Produto, self).save(*args, **kwargs)
        self.slug = "%s-%s" % (slugify(self.nome), self.id)
        super(Produto, self).save(*args, **kwargs)
