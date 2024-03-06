from .decorators import unauthenticated_user
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required ,permission_required
from django.contrib.auth import login,logout,authenticate,get_user_model
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from accounts.models import *
from .form import *
from accounts.utils import *
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str 
from .utils import generate_token ,account
from django.core.mail import EmailMessage
from django.conf import settings
import threading
from .models import *

# Create your views here.

#Variables
users= User.objects.all()
count = User.objects.count()

account = account()
class EmailThread(threading.Thread):
    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()

def activate_user(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        print('the id of the user ',uid)
        print('the user who is creating account',user)
    except Exception as e:
        user = None
        print('errors',e)
    print('checking the token')
    if user is not None and generate_token.check_token(user, token):
        print('the account is being activated')
        user.is_active = True
        user.save()
        print('the account has being activated')

        messages.success(request,'Account Activate, you can now login')
        return redirect('sign_in')
    else:
        return render(request, 'activate-failed.html', {"user": user})


def send_activation_email(user, request):
    current_site = get_current_site(request).domain
    email_subject = subject = "Verify Your Email"
    email_body = render_to_string('activate.html', {
        'first_name': user.first_name,
        'last_name':user.last_name,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': generate_token.make_token(user),
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        "protocol": 'https' if request.is_secure() else 'http'
    })
    print( 'id',urlsafe_base64_encode(force_bytes(user.pk)))
    print('token',generate_token.make_token(user))
    print(user.email)
    print(user.first_name)
    print(user.last_name)
    print(settings.EMAIL_HOST_USER)
    email = EmailMessage(subject=email_subject, body=email_body,
                         from_email=settings.EMAIL_HOST_USER,
                         to=[user.email]
                         )
    
    EmailThread(email).start()
    
@unauthenticated_user
def Regester(request):
    if request.method == 'POST':
        accountNum = generate_otp()
        print('Post Request of Regestration  ')
        user_form = CreateUserForm(request.POST)
        if user_form.is_valid():
            print('The Regestration Function Excuted') 
            email = user_form.cleaned_data.get('email',None)
            name = user_form.cleaned_data['first_name']
            surname = user_form.cleaned_data['last_name']
            user = user_form.save(commit = False)
            print('email is',email)
            if email == '':
                user.is_active = True
                user.roles = 'customer'
                user.accountNumber = accountNum
                user.save()
                print('user saved')
                return redirect('sign_in')
            else:
                user.is_active = False
                try:
                    print('Sending to send mail function')
                    send_activation_email(user, request)
                except TypeError as e:
                    
                    print("An error occurred while sending the activation email:", e)
                user.save()
                message = f'''
                            To Complete your account creation, please click the activation link that has been sent to {email}
                            '''
                messages.success(request, message)
                return render(request, 'account_create.html' , {'user':user_form})
        else:
            for error in list(user_form.errors.values()):
                #messages.warning(request,error)
                print('Form has following errors', error)

    else:
        print('Its a get Request')
        user_form = CreateUserForm()
        
    content ={}
    content ={
    'forms':forms,    
    'form': user_form
    }
    return render(request, 'regester.html' , content)
        
@unauthenticated_user
def signIn(request):
    print('inside sugn up')
    accounts = generate_otp()
    print(accounts)
    if request.method == 'POST':
        print('in log in function')
        username = request.POST['username']
        password = request.POST['password']
        User = authenticate(request , username = username , password = password)
        print('authenticated succesfully')
        if User is not None:
            print('user is not none')
            login(request, User)
            print('log in')
            messages.success(request, 'Log  Successfully')
            return redirect('dashboard') 
        else:
            print('user is  none')
            messages.warning(request, 'Invalid Username and  Paasword')
            return redirect('sign_in')
                      
    return render(request, 'sign_in.html' )

@login_required(login_url='sign_in') 
def signout(request):
    logout(request)
    messages.success(request, 'Log Out successfully')
    return redirect('sign_in')


   
@login_required(login_url='sign_in')  
def Allusers(request):
    content ={}
    content ={
       
        'users': users,
        'count': count
    }
    return render(request , 'viewusers.html',content)

@login_required(login_url='sign_in')  
def search_users(request):
    username = request.GET.get('username')
    surname = request.GET.get('surname')
    phone_number = request.GET.get('phone_number')
    email = request.GET.get('email')
    role = request.GET.get('role')

    users = User.objects.all()

    if username:
        users = users.filter(username__icontains=username)
    if surname:
        users = users.filter(last_name__icontains=surname)
    if phone_number:
        users = users.filter(phone_number__icontains=phone_number)
    if email:
        users = users.filter(email__icontains=email)
    if role:
        users = users.filter(role=role)

    return redirect('dashboard')
@login_required(login_url='sign_in')  
def changeRole(request,pk):
    userToBeUpdated = User.objects.get(id = pk) 
    if request.method == 'POST':
        form = UpdateUserForm(request.POST ,instance =userToBeUpdated)
        print('form to update')
        if form.is_valid():
            print('from valid')
            roles = form.cleaned_data['roles']
            print(roles)
            username = userToBeUpdated.username
            user = form.save(commit=False)
            if roles == 'admin':
                user.is_guard = False
                user.is_customer = False
                user.is_admin = True
                user.roles = 'admin'
                user.save()
                print('user set to admin')
            elif roles == 'guard':
                user.is_guard = True
                user.is_customer = False
                user.is_admin = False
                user.save()
                user.roles = 'guard'
                print('user set to guard')
            else:
                user.is_guard = False
                user.is_customer = True
                user.is_admin = False
                user.roles = 'customer'
                user.save()
                print('user set to customer') 
            mesage = f"{username.title()}'s Role  have been succefully changed  to {roles.title()}"
            messages.success(request, mesage)
            return redirect('users')
        else:
            print('form not valid',form.errors)
            
    else:
        form = UpdateUserForm(instance=userToBeUpdated)
        
    content ={}
    content ={
        'form' : form,
        
    }
    return render(request,  'changerole.html', content)