from django.shortcuts import render, redirect, get_object_or_404
from .models import Layanan, Pesanan 
from django.contrib import messages
from decimal import Decimal


def beranda(request):
    return render(request, 'laundry/beranda.html')

def layanan(request):
    layanan_list = Layanan.objects.all()
    return render(request, 'laundry/layanan.html', {'layanan_list': layanan_list})

def buat_pesanan(request):
    if request.method == "POST":
        nama_pemesan = request.POST['nama_pemesan']
        berat_cucian = float(request.POST['berat_cucian'])
        layanan_id = request.POST['layanan_id']
        
        layanan = Layanan.objects.get(id=layanan_id)

        pesanan = Pesanan(nama_pemesan=nama_pemesan, id_layanan=layanan, berat_cucian=berat_cucian)
        pesanan.hitung_total_harga() 
        pesanan.save() 
        return redirect('beranda')

    else:
        layanan_id = request.GET.get('layanan_id')
        layanan = Layanan.objects.get(id=layanan_id)
        return render(request, 'laundry/buat_pesanan.html', {'layanan': layanan})
      
def proses_pesanan(request):
    if request.method == 'POST':
        nama_pelanggan = request.POST.get('nama_pelanggan')
        layanan_id = request.POST.get('layanan_id')
        berat = request.POST.get('berat')

        if not nama_pelanggan or not layanan_id or not berat:
            messages.error(request, "Semua field harus diisi.")
            return redirect('buat_pesanan')

        layanan = get_object_or_404(Layanan, id=layanan_id)

        pesanan = Pesanan(
            nama_pemesan=nama_pelanggan,
            id_layanan=layanan,
            berat_cucian=Decimal(berat) 
        )
        
        pesanan.hitung_total_harga() 
        pesanan.save() 

        messages.success(request, f"Pesanan berhasil dibuat untuk {nama_pelanggan}. Total: Rp {pesanan.total_harga}")
        return redirect('beranda')

    return redirect('buat_pesanan')
  
def daftar_pesanan(request):
    pesanan_list = Pesanan.objects.all() 
    return render(request, 'laundry/daftar_pesanan.html', {'pesanan_list': pesanan_list})

def login(request):
  return render(request, 'laundry/login.html')
  