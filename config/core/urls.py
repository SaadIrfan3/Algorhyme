from django.urls import path
from . import views
from .views import home_view
urlpatterns = [
    path('api/signup/',views.signup_user),
    path('api/login/',views.login_user),
    path('api/profile',views.get_profile),
    path('', home_view,name='home'),

]