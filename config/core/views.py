from django.shortcuts import render
from django.http import JsonResponse

def signup_user(request):
    return JsonResponse({'message':'Signuppp'})

def login_user(request):
    return JsonResponse({'message': 'loginnn'})

def get_profile(request):
    return JsonResponse({'message': 'your profiless'})
    
def home_view(request):
    return render(request,'core/home.html')

