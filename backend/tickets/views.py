from django.http import Http404
from django.shortcuts import render
from rest_framework.decorators import api_view , APIView
from .serializers import TicketSerializer
from rest_framework.response import Response
from .models import *
from rest_framework import status


# Create your views here.
class TicketList(APIView):
    def get(self, request):
        tickets = Ticket.objects.all()
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data)
    # adding a new ticket
    def post(self, request):
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class TicketDetail(APIView):
    def get_object(self, pk):
        try:
            return Ticket.objects.get(pk=pk)
        except Ticket.DoesNotExist:
            raise Http404

   
    def get(self, request, pk):
        ticket = self.get_object(pk)
        serializer = TicketSerializer(ticket)
        return Response(serializer.data)
    
     #updatin the ticktes 
    def put(self, request, pk):
        ticket = self.get_object(pk)
        serializer = TicketSerializer(ticket, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        ticket = self.get_object(pk)
        ticket.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# 1.1 getAllTickets and create ticket

# @api_view(['GET'])
# def getTickets(request):
#     print('inside the ticket function')
#     if request.method == 'GET':
#         print('inside the get metod')
#         tickets = Ticket.objects.all()
#         serializer = TicketSerializer(tickets,many=True)
#         return Response(serializer.data)
#     else:
#         return Response(serializer.errors, status =status.HTTP_405_METHOD_IS_NOT_ALLOWED)

# # 1.2 getTicket
# @api_view(['GET'])
# def getTicket(request ,pk):
#     try: 
#         ticket = Ticket.objects.get(id= pk)
#     except ticket.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         print(ticket)
#         serializer = TicketSerializer(ticket) 
#         print(serializer.data)
#         return Response(serializer.data)
#     else:
#         return Response(serializer.errors, status =status.HTTP_405_METHOD_NOT_ALLOWED)

# # 1.3 createTicket
# @api_view(['POST'])
# def createTicket(request): 
#     if request.method == 'POST':
#             saved_data = request.data
#             print(saved_data)
#             serializer = TicketSerializer(data=saved_data , many=False)
#             if serializer.is_valid():
#                 print('serilizer valid')
#                 serializer.save()
#                 return Response(serializer.data ,status=status.HTTP_201_CREATED)  
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# # 1.4 updateTicket
# @api_view(['PUT'])
# def updateTicket(request,pk): 
#     if request.method == 'PUT':
#         ticket = Ticket.objects.get(id= pk)
#         serializer = TicketSerializer(ticket,data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             print('updated')
#             return Response(serializer.data, status= status.HTTP_201_CREATED)
#         else:
#             print('not updated',serializer.errors,'errors')
#             return Response(status= status.HTTP_400_BAD_REQUEST)
#     else:
#         return Response(serializer.errors, status =status.HTTP_405_METHOD_NOT_ALLOWED)
# # 1.5 deleteTicket   
# @api_view(['DELETE'])
# def deleteTicket(request,pk): 
#     if request.method == 'DELETE':
#         ticket = Ticket.objects.get(id= pk)
#         ticket.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     else:
#         return Response( status =status.HTTP_405_METHOD_NOT_ALLOWED)

