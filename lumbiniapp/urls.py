from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('', views.faq, name='faq'),
    path ('about/', views.about, name='about')

]