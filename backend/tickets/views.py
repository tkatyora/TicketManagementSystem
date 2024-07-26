from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated , AllowAny
from rest_framework.response import Response
from rest_framework import status
from .serializers import TicketSerializer
from .models import *

@api_view(['POST'])
@permission_classes([AllowAny])  
def createTicket(request):
    try:
        if request.method == 'POST':
            serializer = TicketSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                response_data = {
                "message": "Ticket created successfully",
                "data": serializer.data
                            }
                return Response(response_data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def getAllTickets(request):
    if request.method == 'GET':
        print('inside the get metod')
        tickets = Ticket.objects.all()
        serializer = TicketSerializer(tickets,many=True)
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status =status.HTTP_405_METHOD_IS_NOT_ALLOWED)

# # 1.2 getTicket
@api_view(['GET'])
def getTicket(request ,pk):
    try: 
        ticket = Ticket.objects.get(id= pk)
    except ticket.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        print(ticket)
        serializer = TicketSerializer(ticket) 
        print(serializer.data)
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status =status.HTTP_405_METHOD_NOT_ALLOWED)


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

