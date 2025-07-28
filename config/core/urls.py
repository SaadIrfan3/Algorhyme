from django.urls import path
from . import views
from .views import home_view
urlpatterns = [
    path('', views.home_view,name='home'),
    path('api/signup/',views.signup_user),
    path('api/login/',views.login_user,name = 'login'),
    path('api/profile/',views.get_profile,name = 'profile'),
    path('api/gameroom/',views.gameroom_view,name = 'gameroom'),
    

]