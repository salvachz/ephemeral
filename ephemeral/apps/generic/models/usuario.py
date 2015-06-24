from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('Email invalido.')

        if not kwargs.get('name'):
            raise ValueError('Nome invalido.')

        user = self.model(
            email=self.normalize_email(email), name=kwargs.get('name')
        )

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.create_user(email, password, **kwargs)

        user.is_admin = True
        user.save()

        return user


class Usuario(AbstractBaseUser):
    email = models.CharField(db_column='usrMail', max_length=255, unique=True)
    name = models.CharField(db_column='usrName', max_length=65)
    sobrenome = models.CharField(db_column='usrSobrenome', max_length=100, null=True)
    cpf = models.CharField(db_column='usrCpf', max_length=20, null=True)
    telefone = models.CharField(db_column='usrTelefone', max_length=20, null=True)
    linguaguem = models.CharField(db_column='usrLanguage', choices=( (x,x) for x in ('Portugues','Inglish')), default='Portugues',max_length=30)
    status = models.CharField(db_column='usrStatus', choices=( (x,x) for x in ('Ativo','Inativo')), default='Ativo',max_length=30)
    last_access_ip = models.CharField(db_column='usrLastAccessIP', max_length=45)
    nascimento = models.DateTimeField(db_column='usrNascimento',null=True)
    sexo = models.CharField(db_column='usrSexo',choices=((x,x) for x in ['masculino','feminino']), max_length=20, default='masculino')

    is_admin = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __unicode__(self):
        return self.email

    class Meta:
        db_table = 'Usuario'

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name.split()[0]

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

