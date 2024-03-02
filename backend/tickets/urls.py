from django.urls import path
from . import views

urlpatterns = [
    path('view/',views.getTickets),
    path('create/',views.createTicket),
    path('single/<int:pk>/',views.getTicket),
    path('update/<int:pk>/',views.updateTicket),
    path('delete/<int:pk>/',views.deleteTicket),
   
]
