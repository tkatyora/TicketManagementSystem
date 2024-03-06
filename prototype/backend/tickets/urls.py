from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard, name = 'dashboard'),
    path('create-show',views.createShow, name = 'create_show'),
    path('page-developed',views.developed, name ='developed'),
    path('view-show',views.viewShow, name ='view_show'),
    path('delete-show/<int:pk>', views.deleteShow,name ='delete_show'),
    path('update-show/<int:pk>', views.updateShow,name ='update_show'),
    path('create-ticket/<int:pk>', views.createTicket,name ='generate_ticket'),
    path('view-ticket',views.viewTicket, name ='view_ticket'),
  
]


