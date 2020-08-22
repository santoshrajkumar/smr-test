from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
  return render(request, 'chat/ind.html')

def room(request, room_name):
  return render(request, 'chat/room.html', {'room_name':room_name})

def room2(request, room_name):
  return render(request, 'chat/room2.html', {'room_name':room_name})

def loginUser(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    category = request.POST.get('category')
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      if category == 'controller':
        return redirect('/chat/control/webcon/')
      elif category == 'plant':
        return redirect('/chat/webcon/')
      else:
        return redirect('')
    else:
      return render(request, 'chat/login.html')
  return render(request, 'chat/login.html')