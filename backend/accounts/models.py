from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractUser , Group, Permission , BaseUserManager ,PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField as ModelPhoneNumberField
from django.core.validators import EmailValidator
from rest_framework.authtoken.models import Token

CITY_CHOICES = [
        ('Harare', 'Harare'),
        ('Bulawayo', 'Bulawayo'),
        ('Gweru', 'Gweru'),
        ('Chitungwiza', 'Chitungwiza'),
        ('Mutare', 'Mutare'),
        ('Kwekwe', 'Kwekwe'),
        ('Kadoma', 'Kadoma'),
        ('Masvingo', 'Masvingo'),
        ('Norton', 'Norton'),
        ('Chinhoyi', 'Chinhoyi'),

        ]  

class StsUserManager(BaseUserManager):
    def create_user(self, email=None,username = None ,password=None, **kwargs):
        if not email and not username:
            raise ValueError("User must have either an email address or Username")

        user = self.model(
            email=self.normalize_email(email) if email else None,
            username=username,
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None, **kwargs):
        user = self.create_user(
            email=email,
            password=password,
            **kwargs
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        token, created = Token.objects.get_or_create(user=user)
        print(f'Superuser token: {token.key}') 
        
        return user


class StsUser(AbstractUser,PermissionsMixin):
    Account = [('bussiness','Bussiness Account'),
               ('personal','Personal Account')]
    username = models.CharField(max_length=255,blank=True,unique=True,null=True)
    account_type = models.CharField(max_length=255,blank=True,null=True,choices=Account)
    phone_number = ModelPhoneNumberField(unique=True, null=True, blank=False)
    full_name = models.CharField(max_length=255, null=True)
    email = models.EmailField(unique=True, null=True, blank=True,validators=[EmailValidator()])
    city = models.CharField(max_length=100, null=True, default='Not Selected')
    profile_picture = models.ImageField(upload_to='Pictures', blank=True, null=True)
    is_customer = models.BooleanField(default=False, null=True)
    is_admin = models.BooleanField(default=False, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    is_active = models.BooleanField(default=False, null=True)
    code = models.CharField(max_length=7,blank=False,null=True)
    token = models.TextField(null=True)
    groups = models.ManyToManyField(
        Group,
        related_name='erp_user_groups',  
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='erp_user_permissions', 
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['full_name']

    objects = StsUserManager()

    def __str__(self):
        return f"Information for : {self.full_name}=> {self.email}"

    @property
    def image_url(self):
        if self.profile_picture:
            return self.profile_picture.url
        return ''

class Admin(StsUser):
    ranking = models.IntegerField(null = True)
    roles = models.CharField(max_length=255, unique=False,null=True,blank=True)
    national_id = models.CharField(max_length=200, unique=True, null=True, blank=False)
    is_sts_team = models.BooleanField(default=True, null=True)
    is_security = models.BooleanField(default=True, null=True)
    sp_number = models.CharField(max_length=200, null=True, blank=True)
    def save(self, *args, **kwargs):
        if not self.sp_number:
            last_sp = Admin.objects.filter(sp_number__startswith='stsA').order_by('-sp_number').first()
            if last_sp:
                last_number = int(last_sp.sp_number[4:])
                new_number = last_number + 1
            else:
                new_number = 1
            self.sp_number = f"stsA{new_number:03d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email

from django.db import models

class Customer(StsUser):
    customer_number = models.CharField(max_length=200, null=True, blank=False, unique=True)

    def save(self, *args, **kwargs):
        if not self.customer_number:
            last_customer = Customer.objects.filter(customer_number__startswith='stsc').order_by('-customer_number').first()
            if last_customer:
                last_number = int(last_customer.customer_number[4:])
                new_number = last_number + 1
            else:
                new_number = 1
            self.customer_number = f"stsc{new_number:03d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email

