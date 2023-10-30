from django.contrib.auth import views
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from ..settings import LOGIN_URL


@login_required(login_url=LOGIN_URL)
def index_view(request):
    return redirect('room', room_name='general')
    # rooms = Room.objects.all()
    # return render(request, '../rtmp/index.html', {
    #     'rooms': rooms,
    # })

