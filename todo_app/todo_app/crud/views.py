from copy import error
from urllib import response
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import TodoListItems
from .serializers import CrudSerializers

@api_view(['GET','POST'])
def itemlist(request):
    if (request.method == 'GET'):
        data=TodoListItems.objects.all()
        serializer = CrudSerializers(data, many=True)
        return(Response(serializer.data))
    elif(request.method == 'POST'):
        serializer=CrudSerializers(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return(Response(serializer.data,status=status.HTTP_201_CREATED))
        return(Response(serializer.error,status=status.HTTP_400_BAD_REQUEST))
@api_view(['GET','DELETE'])
def itemdelete(request,pk):
    try:
        data=TodoListItems.objects.filter(pk=pk)
    except TodoListItems.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if(request.method=='GET'):
       serializer = CrudSerializers(data, many=True)
       return(Response(serializer.data))
    if(request.method=='DELETE'):
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

