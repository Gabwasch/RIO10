from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('', RedirectView.as_view(url='/index/')),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login_view, name='login'),
    path('minha_area/', views.minha_area, name='minha_area'),

]
