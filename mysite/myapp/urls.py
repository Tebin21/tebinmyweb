from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),  # <--- NEW LINE
    path('portfolio/', views.portfolio, name='portfolio'),  # <--- NEW LINE
    path('experience/', views.experience, name='experience'),  # <--- NEW LINE
    path('contact/', views.contact, name='contact'),  # <--- NEW LINE
]