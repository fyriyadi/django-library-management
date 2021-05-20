from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from rest_framework import generics
from rest_framework import views
from rest_framework import mixins
from rest_framework import permissions

from .serializers import BookSerializer
from library_app.models import *

class BookView(APIView):
    # permission_classes =(IsAuthenticated,)
    
    def get(self,request,*args,**kwargs):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        filter_backends = [filters.SearchFilter]
        search_fields = ['title', 'subject']
        return Response(serializer.data)
        
class BookDetailView(APIView):
    # permission_classes =(IsAuthenticated,)
    
    def get(self,request,id,*args,**kwargs):
        books = Book.objects.get(id=id)
        serializer = BookSerializer(books)
        return Response(serializer.data)


class BookCreateView(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated,)
    # parser_classes = [MultiPartParser, FormParser]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def post(self, request, format=None):
        print(request.data)
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookEditView(generics.RetrieveUpdateAPIView):
    # permission_classes = (IsAuthenticated,)
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookDeleteView(generics.RetrieveDestroyAPIView):
    # permission_classes = (IsAuthenticated,)
    serializer_class = BookSerializer
    queryset = Book.objects.all()