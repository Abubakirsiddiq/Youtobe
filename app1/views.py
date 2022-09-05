from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.response import Response


class AccountCreate(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializers


class Account(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializers


class VideoCreate(generics.CreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializers
    def post(self, request):
        if Account.user == self.request.user:
            ser = VideoSerializers(data=self.request.data)
            if ser.is_valid():
                ser.save()
            return Response(ser.data)
        return Response()


class Video(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializers
    def perform_destroy(self, instance):
        v = Video.objects.get(account=self.request.user)
        if v:
            instance.delete()
        return Response(instance)


class PleylistCreate(generics.CreateAPIView):
    queryset = Pleylist.objects.all()
    serializer_class = PleylistSerializers
    def post(self, request):
        if Account.user == self.request.user:
            ser = PleylistSerializers(data=self.request.data)
            if ser.is_valid():
                ser.save()
            return Response(ser.data)
        return Response()


class Pleylist(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pleylist.objects.all()
    serializer_class = PleylistSerializers


class ObunaCreate(generics.CreateAPIView):
    queryset = Obuna.objects.all()
    serializer_class = ObunaSerializers


class Obuna(generics.RetrieveUpdateDestroyAPIView):
    queryset = Obuna.objects.all()
    serializer_class = ObunaSerializers


class LikeCreate(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializers


class Like(generics.RetrieveUpdateDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializers


class HistoryCreate(generics.CreateAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializers
    def post(self, request):
        if Account.user == self.request.user:
            ser = HistorySerializers(data=self.request.data)
            if ser.is_valid():
                ser.save()
            return Response(ser.data)
        return Response()


class History(generics.RetrieveUpdateDestroyAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializers

