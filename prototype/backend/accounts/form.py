from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import *
from accounts.models import *
from tickets.models import Ticket ,Show
import datetime

today_date = datetime.date.today()
min_date = (today_date + datetime.timedelta(days=1 * 7))


#MODULES FORMS
class CreateUserForm(UserCreationForm):
    
    email = forms.EmailField(required=False , label='Enter  Email address(optional)',
                              widget=forms.EmailInput(
                                  attrs={
                                      'class':'form-control input',
                                       'type':'email'
                                     
                                  })),
    first_name = forms.CharField(required=True , label='Enter First Name',
                                 widget=forms.TextInput(
                                  attrs={
                                      
                                      'class':'form-control input',
                                       'spellcheck':"true",
                                       'type':'text'
                                  }
                              ))
    last_name = forms.CharField(required=True , label='Enter Surname' ,
                                 widget=forms.TextInput(
                                  attrs={
                                      
                                      'class':'form-control input',
                                       'spellcheck':"true",
                                       'type':'text'
                                  }
                              ))
    username = forms.CharField(required=True , label='Create username' ,
                                 widget=forms.TextInput(
                                  attrs={
                                      
                                      'class':'form-control input',
                                       'spellcheck':"true",
                                       'type':'text'
                                  }
                              ))
    nationalId = forms.CharField(required=True , label='Enter Your National Id' ,
                                 widget=forms.TextInput(
                                  attrs={
                                      
                                      'class':'form-control input',
                                       'spellcheck':"true",
                                       'type':'text'
                                  }
                              ))
    city = forms.ChoiceField(
        required=False,
        label='Select  City',
        choices=User.CITY_CHOICES,
        widget=forms.Select(
            attrs={
                'class': 'form-control input',
            }
        )
    ) 
    terms_accepted = forms.BooleanField(
        label='I accept the terms and conditions',
        required=True,
    ) 
    
   
    class Meta:
        model = User
        #fields = '__all__'
        fields = ['last_name','first_name','phoneNumber','city','nationalId','password1','password2','terms_accepted','email','username','accountNumber','roles'] 
    
class UpdateUserForm(ModelForm):
                           
 
   
    class Meta:
        model = User
        #fields = '__all__'
        fields = ['roles'] 
    

class TicketForm(ModelForm):
    money =forms.DecimalField(label='Enter Amount Paid(USD)', required=True,initial=00.00,max_digits=7,decimal_places=2)
    class Meta:
        model =Ticket
        fields = ['customerName','numberPeople','money'] 
        


class ShowForm(ModelForm):
    showName = forms.CharField(required=True , label='Enter Show Name' ,
                                widget=forms.TextInput(
                                attrs={
                                    
                                    'class':'form-control input',
                                    'spellcheck':"true",
                                    'type':'text'
                                }
                            ))
    showVenue = forms.CharField(required=True , label='Enter Show Venue' ,
                                widget=forms.TextInput(
                                attrs={
                                    
                                    'class':'form-control input',
                                    'spellcheck':"true",
                                    'type':'text'
                                }
                            ))
    showCity = forms.ChoiceField(
        required=False,
        label='Select Show  City',
        choices=Show.CITY_CHOICES,
        widget=forms.Select(
            attrs={
                'class': 'form-control input',
            }
        )
    ) 
    picture =forms.ImageField(label='Upload Picture', required=False)
    amount =forms.DecimalField(label='Price (USD)', required=True,initial=00.00,max_digits=7,decimal_places=2)
    showDate= forms.DateTimeField(label='Date of Show', required=False ,widget = forms.DateInput(
     attrs={
         'type':'date',
         'min':min_date,
        }
    ))
    class Meta:
        model =Show
        fields = ['showName','showVenue','showCity','showDate','amount','picture'] 

  
     
        
     
      
      
    
     
      


        
        

