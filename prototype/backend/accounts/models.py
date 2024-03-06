from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
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
        role = [
            ('admin', 'Admin'),
            ('guard', 'Security Guard'),
            ('customer', 'customer'),
          
            ]
        phoneNumber  = models.CharField(null=True,blank=True,max_length=12)
        city = models.CharField(max_length=100,null=True,default='Not Selected' ,choices=CITY_CHOICES)
        accountNumber = models.CharField(max_length=200,null=True ,blank= True) 
        nationalId = models.CharField(max_length=200,null=True,unique=True)    
        profilePicture = models.ImageField(upload_to ='Pictures', blank=True ,null= True) 
        roles = models.CharField(max_length=255, unique=False,choices=role,null=True,blank=True)
        is_customer = models.BooleanField(default=True, null = True)
        is_guard = models.BooleanField(default=False, null = True)
        is_admin = models.BooleanField(default=False, null = True)
        ranking = models.IntegerField(null = True)
        groups = models.ManyToManyField('auth.Group', related_name='User_user_set', blank=True)
        user_permissions = models.ManyToManyField('auth.Permission', related_name='User_user_set', blank=True)

       
        @property
        def ImageUrl(self):
            try:
                url = self.profilePicture.url
            except ValueError:
                url = ''
            return url
      
        def __str__(self):
                return f"Information for : {(self.username)} "

        
