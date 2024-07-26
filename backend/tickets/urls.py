from django.urls import path
from .views  import createTicket

urlpatterns = [
    path('create/', createTicket, name='create-ticket')
]
