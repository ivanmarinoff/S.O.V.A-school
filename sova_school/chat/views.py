from django.contrib.auth import views
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from rest_framework import generics
from .models import Room, Message
from .serializers import RoomSerializer, MessageSerializer
from .models import Room
from ..settings import LOGIN_URL


@login_required(login_url=LOGIN_URL)
def index_view(request):
    return redirect('room', room_name='general')
    # rooms = Room.objects.all()
    # return render(request, '../rtmp/index.html', {
    #     'rooms': rooms,
    # })


@login_required(login_url=LOGIN_URL)
def room_view(request, room_name):
    chat_room = Room.objects.get(name=room_name)
    return render(request, '../rtmp/index.html', {
        'room': chat_room,
    })


@login_required(login_url=LOGIN_URL)
def superuser_view(request, room_name):
    chat_room = Room.objects.get(name=room_name)
    request.user.is_superuser = True
    return render(request, '../rtmp/superuser.html', {
        'room': chat_room,
    })


class RoomListAPIView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class MessageListAPIView(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

# class SuperUserView(views.TemplateView):
#     template_name = '../rtmp/superuser.html'
#     success_url = reverse_lazy('../rtmp/superuser.html')
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context
