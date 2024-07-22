from django.db import models
from accounts.models import CITY_CHOICES

class Show(models.Model):
        showName  = models.CharField(null=True,blank=False,max_length=255)
        showVenue= models.CharField(max_length=200,null=True ,blank= True) 
        showCity = models.CharField(max_length=100,null=True,default='Not Selected' ,choices=CITY_CHOICES)
        showDate = models.DateTimeField( auto_now=False, auto_now_add=False ,null=True)
        vip_price = models.IntegerField(null= True,blank=True,default = 0)
        vvip_price = models.IntegerField(null= True,blank=True,default = 0)
        general_price = models.IntegerField(null= True,blank=True,default = 0)
        numbertickets= models.IntegerField(null= True,default=0)
        picture = models.ImageField(upload_to ='pics', blank=True ,null= True)
        created_on = models.DateTimeField( auto_now=False, auto_now_add=True ,null=True),
        updated_on = models.DateTimeField( auto_now=True, auto_now_add=False ,null=True)

        class Meta:
            ordering = ['showDate']
        @property
        def NewshowDate(self):
            if self.showDate is not None:
                return self.showDate.strftime("%d/%m/%Y")
            else:
                from datetime import date
                showDate = date(2023, 1, 1)
                return showDate.strftime("%d/%m/%Y")
        @property
        def createdOn(self):
            if self.created_on is not None:
                return self.created_on.strftime("%d/%m/%Y")
            else:
                from datetime import date
                created_on = date(2023, 1, 1)
                return created_on.strftime("%d/%m/%Y")
        @property
        def updated_on(self):
            if self.updated_on is not None:
                return self.updated_on.strftime("%d/%m/%Y")
            else:
                from datetime import date
                updated_on = date(2023, 1, 2)
                return updated_on.strftime("%d/%m/%Y")
               
        @property
        def ImageUrl(self):
            try:
                url = self.picture.url
            except ValueError:
                url = ''
            return url
      
        def __str__(self):
                return f"{(self.showName)} @ {self.showVenue} "