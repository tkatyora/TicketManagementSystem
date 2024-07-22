from django.urls import path
from .views  import TicketList , TicketDetail

urlpatterns = [
    path('tickets/', TicketList.as_view() ),
    path('tickets/<int:pk>/', TicketDetail.as_view()),
]
