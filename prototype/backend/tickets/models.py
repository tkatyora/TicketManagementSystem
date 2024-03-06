from django.db import models
from accounts.models import User
import qrcode
from PIL import Image ,ImageDraw
from io import BytesIO
from django.core.files import File


class Show(models.Model):
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
        showVenue= models.CharField(max_length=200,null=True ,blank= True) 
        showCity = models.CharField(max_length=100,null=True,default='Not Selected' ,choices=CITY_CHOICES)
        showDate = models.DateTimeField( auto_now=False, auto_now_add=False ,null=True)
        created_by = models.ForeignKey(User,  on_delete=models.CASCADE ,null=True,blank=True)
        created_on=models.DateTimeField( auto_now=False, auto_now_add=True ,null=True),
        updated_on=models.DateTimeField( auto_now=True, auto_now_add=False ,null=True)
        amount = models.IntegerField(null= True,blank=True,default = 0)
        numbertickets= models.IntegerField(null= True,default=0)
        picture = models.ImageField(upload_to ='pics', blank=True ,null= True)

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
        def TotalCost(self):
            ammount = self.amount
            tickets = int(self.numbertickets)
            total_earning = ammount * tickets
                
            return str(total_earning)
               
        @property
        def ImageUrl(self):
            try:
                url = self.picture.url
            except ValueError:
                url = ''
            return url
      
        def __str__(self):
                return f"Information for : {(self.showName)} "
class Ticket(models.Model): 
        
        # infomation of the show  
        ticketstatus = [
        ('valid', 'valid'),
        ('expired', 'expired'),
        ('deleted', 'deleted'),
        ('updated', 'updated'),
        ]  
        showstatus = [
        ('inside', 'Inside The show'),
        ('outSide', 'Outside The show'),
        ] 
        show = models.ForeignKey('Show', on_delete=models.CASCADE ,null=True,blank=False)
        customerName = models.CharField(null=True,blank=False,max_length=255)
        created_by = models.ForeignKey(User,  on_delete=models.CASCADE ,null=True,blank=True)
        created_on=models.DateTimeField( auto_now=False, auto_now_add=True ,null=True),
        updated_on=models.DateTimeField( auto_now=True, auto_now_add=False ,null=True)
        qr_code = models.ImageField(upload_to ='picture', blank=True ,null= True) 
        amountPaid = models.IntegerField(null= True)
        numberPeople= models.IntegerField(null= True)
        showStatus = models.CharField(max_length=100,null=True,default='Out Side Show' ,choices=showstatus)
        ticketStatus = models.CharField(max_length=100,null=True,default='Valid' ,choices=ticketstatus)
       
        
       
        @property
        def ImageUrl(self):
            try:
                url = self.qr_code.url
            except ValueError:
                url = ''
            return url
      
        def __str__(self):
                return f"Information for : {(self.customerName)} "


        def save(self,*args , **kwargs):
                qrcode_img = qrcode.make()
                canvas = Image.new('RGB',(200,200), 'white')
                draw = ImageDraw.Draw(canvas)
                canvas.paste(qrcode_img)
                fname = f'QR_CODE for{self.customerName}, for{self.show.showName}.png Show'
                buffer = BytesIO()
                canvas.save(buffer,'PNG')
                self.qr_code.save(fname,File(buffer),save= False)
                canvas.close()
                super().save(*args,**kwargs)
