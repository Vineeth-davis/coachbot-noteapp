
#from .models import *
from rest_framework import generics, permissions
from .models import Note
from .serializers import NoteSerializer
from .permissions import IsOwnerOrShared
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from django.contrib.auth.models import User
from .serializers import UserRegister
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response




class NoteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class NoteRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrShared]

class NoteShareAPIView(generics.UpdateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrShared]

    def perform_update(self, serializer):
        shared_with = self.request.data.get('shared_with')
        if shared_with:
            serializer.instance.shared_with.set(shared_with)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    
def register(APIView):
    #if request.method == 'POST':
        #username = request.POST.get('username')
        #password = request.POST.get('password')
    def post(self,request,format=None):
        serializer=UserRegister(data=request.data)
        data={}
        if serializer.is_valid():
            account=serializer.save()
            data['response']='registered'
            data['username']=account.username
            data['email']=account.email
            token,create=Token.objects.get_or_create(user=account)
            data['token']=token.key
        else:
            data=serializer.errors
        return Response(data)