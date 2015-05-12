from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('Users must have a valid email address.')

        if not kwargs.get('name'):
            raise ValueError('Users must have a valid name.')

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
    nome = models.CharField(db_column='usrName', max_length=65)
    linguaguem = models.CharField(db_column='usrLanguage', choices=( (x,x) for x in ('Portugues','Inglish')), default='Portugues',max_length=30)
    status = models.CharField(db_column='usrStatus', choices=( (x,x) for x in ('Ativo','Inativo')), default='Ativo',max_length=30)
    last_access_ip = models.CharField(db_column='usrLastAccessIP', max_length=45)

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

