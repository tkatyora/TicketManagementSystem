from django.db import models
from accounts.models import StsUser
import qrcode
from PIL import Image ,ImageDraw
from io import BytesIO
from django.core.files import File



class Ticket(models.Model): 
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
        # infomation of the show  
        showName  = models.CharField(null=True,blank=False,max_length=255)
        customerName = models.CharField(null=True,blank=False,max_length=255)
        showVenue= models.CharField(max_length=255,null=True ,blank= True) 
        showCity = models.CharField(max_length=100,null=True,default='Not Selected' ,choices=CITY_CHOICES)
        showDate = models.DateTimeField( auto_now=False, auto_now_add=False ,null=True)
        created_by = models.ForeignKey(StsUser,  on_delete=models.CASCADE ,null=True,blank=True)
        created_on=models.DateTimeField( auto_now=False, auto_now_add=True ,null=True)
        updated_on=models.DateTimeField( auto_now=True, auto_now_add=False ,null=True)
        qr_code = models.ImageField(upload_to ='Pictures', blank=True ,null= True) 
        amountPaid = models.IntegerField(null= True)
        numberPeople= models.IntegerField(null= True)
       
        
       
        @property
        def ImageUrl(self):
            try:
                url = self.qr_code.url
            except ValueError:
                url = ''
            return url
      
        def __str__(self):
                return f"Information for : {(self.showName)} "


        def save(self,*args , **kwargs):
              qrcode_img = qrcode.make()
              canvas = Image.new('RGB',(200,200), 'white')
              draw = ImageDraw.Draw(canvas)
              canvas.paste(qrcode_img)
              fname = f'QR_CODE for{self.customerName}, for  {self.showName}.png Show'
              buffer = BytesIO()
              canvas.save(buffer,'PNG')
              self.qr_code.save(fname,File(buffer),save= False)
              canvas.close()
              super().save(*args,**kwargs)
        
