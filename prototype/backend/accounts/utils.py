# utils.py
from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six
import random
from .models import *
import string
from django.contrib.sites.shortcuts import get_current_site
from . import views
from django.contrib import messages
from django.core.mail import send_mail ,EmailMessage
from django.shortcuts import render, redirect



class TokenGenerator(PasswordResetTokenGenerator):

    def _make_hash_value(self, user, timestamp):
        return six.text_type(user.pk) + six.text_type(timestamp)  + six.text_type(user.is_active)


generate_token = TokenGenerator()



def generate_otp():
    return ''.join(random.choices('0123456789', k=6))



account =generate_otp()

def account():
    #Generating 2 random numbers
    num = random.randrange(11,99)
    num2 = random.randrange(100,999)
    #Generating 2 alpabhet letters
    Alphabet =list(string.ascii_uppercase)
    A = random.choice(Alphabet)
    B = random.choice(Alphabet)

    C = random.choice(Alphabet)
    accountNum = f'{A}{B}{C}{account}{num2}'

    return accountNum

def sending_email(user,request):
    domain = get_current_site(request).domain
    email = user.email
    print('this is the ',email)
    print(domain)
    subject = 'Your One-Stop Solution for Farm Produce-MurimiWangu'
    body = f'''
            Dear {user.email},

            Did you know that with MurimiWangu, you can buy any farm produce you want online and have it delivered straight to your doorstep?

            As a farmer, you have the opportunity to increase your revenue by advertising all your products to a global audience.

            Furthermore, you can benefit from expert advice from agronomists and easily purchase all the necessary equipment for your business.

            Are you a supplier? Join MurimiWangu today to supply your products to fellow farmers and expand your market reach.

            Join MurimiWangu today at http://{domain}/CreateAccount

            MurimiWangu - where agriculture meets opportunity.

            Best regards,
            
            MurimiWangu Team

            WhatsApp : 0773735227 

            Call     :0773643464

            Website  : http://{domain}/murimi-wangu

            Email     :info@murimiwangu.co.zw
            
        '''
    emails = EmailMessage(subject=subject, body=body,
                         from_email='tkatyora7@gmail.com',
                         to=[email]
                         )
    
    views.EmailThread(emails).start()
    mesage= f'''
                Thanks for Leaving Your Comments.We really Appreciate.
                Create Account To Enjoy MurimiWangu
            '''
    messages.success(request,mesage)
    print('comment saved for ', email)



def send_email_from_form(request):
    if request.method == 'POST':
            forms = CommentsForm(request.POST)
            if forms.is_valid():
                email = forms.cleaned_data.get('email')
                user = forms.save(commit=False)
                user.save()
                print('the user',user)
                print('going to the send email ')
                sending_email(user,request)
                return redirect('create_account')
                
            else:
                print('Form is not valid',forms.errors)
                for error in list(forms.errors.values()):
                    messages.warning(request,error)
                return redirect('create_account')
                
    else:
        forms = CommentsForm()
        print('Not a post request')

   


