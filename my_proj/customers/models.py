from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.utils import timezone
from django.db import models
from django.urls import reverse
from django.db.models.signals import post_save
# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=20)
    paternal_surname = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    def __str__(self):
        return "%s %s %s" % (self.name,self.paternal_surname,self.email)

    def get_absolute_url(self):
        return reverse('customer_edit', kwargs={'pk': self.pk})

class Payment_Customer(models.Model):
    amount = models.FloatField()
    customer_id =  models.ForeignKey(Customer, on_delete=models.CASCADE)
    product_name  = models.CharField(max_length=20)
    quantity = models.IntegerField()
    #
    #

    def __str__(self):
        print(type(self.amount))
        print(type(self.customer_id))
        print(type(self.product_name))
        print(type(self.quantity))
        return "%f %s %i" % (self.amount,self.product_name,self.quantity)

    def get_absolute_url(self):
        return reverse('payments_customers_list', kwargs={'customer_id': self.customer_id})

class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("You have not provided a valid e-mail address")
        
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user( email, password, **extra_fields)
    
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(blank=True, default='', unique=True)
    name = models.CharField(max_length=255, blank=True, default='')

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name or self.email.split('@')[0]

    def get_is_super(self):
        return self.is_superuser
    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)
