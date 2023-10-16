from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect


# Create your views here.
def login_view(request):
    if request.method == 'GET':
        return render(request, 'pages/users/login.html')
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user:
        login(request, user)
    return redirect(request.GET.get('next') or '/')
