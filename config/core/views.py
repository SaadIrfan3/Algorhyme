from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def signup_user(request):
    if request.method == 'POST':
        username = request.POST.get('username') or request.GET.get('username')
        password = request.POST.get('password') or request.GET.get('password')

        if not username or not password:
            return JsonResponse({'error': 'username n password r required'})
        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'Username already exists'})
        User.objects.create_user(username=username,password=password)
        return redirect('login')
    return render(request,'core/signup.html')

  
@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username') or request.GET.get('username')
        password = request.POST.get('password') or request.GET.get('password')

        if not username or not password:
            return JsonResponse({'error': 'username n password r required'})
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('gameroom')
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=401)
    else:
        return render(request,'core/login.html')
    
@csrf_exempt
def get_profile(request):
    return JsonResponse({'message': 'your profiless'})
    
@csrf_exempt
def home_view(request):
    return render(request,'core/home.html')

@csrf_exempt
def gameroom_view(request):
    return render(request,'core/gameroom.html')

