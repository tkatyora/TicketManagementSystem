from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required ,permission_required
from accounts.decorators import unauthenticated_user
from django.contrib import messages
from accounts.form import *
from django.http import HttpResponse
from django.template.loader import render_to_string
from reportlab.pdfgen import canvas
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
from xhtml2pdf import pisa
# Create your views here.

#VARIABLES

show = Show.objects.all()
tickets = Ticket.objects.all()


@login_required(login_url='sign_in')
def dashboard(request):
    content ={}
    content = {
        
   
    }  
    return render(request , 'dashboard.html',content)


@unauthenticated_user
def developed(request):
        
    content ={}
    content ={
      
    }
    
    return render(request , 'pagedeveloped.html',content)


@login_required(login_url='sign_in')
def createShow(request):
        if request.method == 'POST':
            form =ShowForm(request.POST)
            img2 = request.POST.get('img',None)
            print('inside show form')
            if form.is_valid():
                print('form is valid')
                img = form.cleaned_data.get('picture')
                show= form.save(commit=False)
                show.created_by = request.user
                show.numbertickets = 0
                print(img)
                print(img2)
                show.save()
                print('show created succesfully')
                mesage= f'Show Created  succesfully'
                messages.success(request,mesage)
                return redirect('view_show')   
            else:
                print('form not valid',form.erros)
                messages.warning(request, 'Sorry Product Creation failled!')
        else:
            form = ShowForm()
        content = {}
        content = {
            'form': form,

        }
        return render(request , 'create_show.html',content)

@login_required(login_url='sign_in')  
def viewShow(request):
    content ={}
    content ={
       
        'show': show
        
    }
    return render(request , 'view_show.html',content)

@login_required(login_url='sign_in') 
def deleteShow(request, pk):
    show_to_delete = Show.objects.get(id=pk)
    print('show to delete',show_to_delete)
    if request.method == 'POST':
        show_to_delete.delete()
        print('show deleted success')
        messages.success(request, 'show Succesfully Deleted')
        return redirect('view_show')
    content = {}
    content = {
        'show': show_to_delete
        
    }
    return render(request, 'delete_show.html', content)

@login_required(login_url='sign_in')  
def updateShow(request,pk):
    showToBeUpdated = Show.objects.get(id = pk) 
    if request.method == 'POST':
        form = ShowForm(request.POST ,instance =showToBeUpdated)
        print('form to update')
        if form.is_valid():
            img = form.cleaned_data.get('picture')
            print(img)
            show = form.save(commit=False)
            show.numbertickets = 0
            show.save()
            print('form saved') 
            mesage = f"Show updated succefully changed"
            messages.success(request, mesage)
            return redirect('view_show')
        else:
            print('form not valid',form.errors)
            
    else:
        form = ShowForm(instance=showToBeUpdated)
        
    content ={}
    content ={
        'form' : form,
        
    }
    return render(request,  'update_show.html', content)


#------------------------------------------TICKETS-----------------------------

@login_required(login_url='sign_in')
def createTicket(request,pk):
        ticket_show = Show.objects.get(id=pk)
        if request.method == 'POST':
            showform = ShowForm(request.POST ,instance =ticket_show)
            form =TicketForm(request.POST)
            print('inside show form')
            if form.is_valid():
                print('form is valid')
                users = form.cleaned_data.get('numberPeople')
                money = form.cleaned_data.get('money')
                unity_price = ticket_show.amount
                cashPaid = users * unity_price
                if money >= cashPaid: 
                    change =   money - cashPaid
                    ticket= form.save(commit=False)
                    ticket.created_by = request.user
                    ticket.amountPaid = cashPaid
                    ticket.showStatus ='outSide'
                    ticket.ticketStatus = 'valid'
                    if showform.is_valid():
                        print('show fromnot valid')
                        number_ticket = ticket_show.numbertickets+1
                        showforms = showform.save(commit=False)
                        ticket.save()
                        showforms.numbertickets = number_ticket
                        showforms.save()
                        
                        print('ticket and show saved  succesfully with below info' )
                        info = f'cashPad {cashPaid} , number of people{users}'
                        mesage= f'Ticket Generate Succesfully succesfully.Change is ${change}.00'
                        messages.success(request,mesage)
                        return redirect('view_ticket')        
                    else:
                        print('show form error',showform.errors)
                elif money < cashPaid:
                    print('less money')
                    change = cashPaid - money
                    messag = f'''Add extra ${change}.00 for the Ticket to be generated
                                Total Cost of Ticket is {cashPaid}'''
                    messages.warning(request , messag)


            else:
                print('Ticket form not valid',form.erros)
                messages.warning(request, 'Sorry Ticket Generation failled!')
        else:
            form = TicketForm()
            showform = ShowForm(instance =ticket_show)
        content = {}
        content = {
            'form': form,
            'data':ticket_show,
            'form2':showform
            

        }
        return render(request , 'generate_ticket.html',content)

@login_required(login_url='sign_in')  
def viewTicket(request):
    #show_ticket = Ticket.objects.get(show= showname)
    content ={}
    content ={
       
        'tickets': tickets
        
    }
    return render(request , 'view_tickets.html',content)


#printing ticket 

@login_required(login_url='sign_in')
def printTicket(request,ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    print(ticket.customerName)
    html_content = render_to_string('print_ticket.html', {'data': ticket})
    print(html_content)
    # Generate PDF from HTML content
    pdf_file = BytesIO()
    print(pdf_file)
    pisa.CreatePDF(html_content, dest=pdf_file)
    print(pisa.CreatePDF(html_content, dest=pdf_file))
    # p = canvas.Canvas(pdf_file, pagesize=letter)
    # p.drawString(100, 800, "Ticket Information")
    # p.drawHTML(html_content, (100, 780), forceWidth=400)  # Draw HTML content on PDF canvas
    # p.save()
    
    response = HttpResponse(pdf_file.getvalue(), content_type='application/pdf')
    print(response)
    response['Content-Disposition'] = 'attachment; filename="Ticket.pdf"'
    return response
