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
    fornecedor = models.ForeignKey('Fornecedor', db_column='proForId', null=True, blank=True)
    marca = models.ForeignKey('Marca', db_column='proMarId', null=True, blank=True)
    preco = models.DecimalField(db_column='proPreco', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    precoFor = models.DecimalField(db_column='precoFor', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    quantidade = models.IntegerField(db_column='proQnt', blank=True, null=True)
    image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    slug = models.SlugField(editable=False,blank=True)

    class Meta:
        db_table = 'Produto'

    def __unicode__(self):
        return self.slug

    def save(self, *args, **kwargs):
        super(Produto, self).save(*args, **kwargs)
        self.slug = "%s-%s" % (slugify(self.nome), self.id)
        super(Produto, self).save(*args, **kwargs)
