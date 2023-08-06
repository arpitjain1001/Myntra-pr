from django.urls import path,include
from . import views

urlpatterns = [
    path('log/',views.log ,name="log"),
    path('register/',views.register ,name="register"),
    path('',views.profile),
    path('logout/',views.logout),
    path('test/',views.test),
]
