from django.urls import path
from . import views

urlpatterns = [
  path('', views.beranda, name='beranda'),
  path('login', views.login, name='login'),
  path('layanan', views.layanan, name='layanan'),
  path('buat_pesanan', views.buat_pesanan, name='buat_pesanan'),
  path('proses_pesanan', views.proses_pesanan, name='proses_pesanan'),
  path('daftar_pesanan/', views.daftar_pesanan, name='daftar_pesanan'),
]
