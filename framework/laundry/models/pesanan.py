from django.db import models
from .layanan import Layanan 
from decimal import Decimal
 
class Pesanan(models.Model):
    id = models.AutoField(primary_key=True)
    nama_pemesan = models.CharField(max_length=255)
    id_layanan = models.ForeignKey(Layanan, on_delete=models.CASCADE) 
    berat_cucian = models.DecimalField(max_digits=5, decimal_places=2)  
    total_harga = models.IntegerField()

    def __str__(self):
        return self.nama_pemesan
      
    def hitung_total_harga(self):
        self.total_harga = int(self.berat_cucian * Decimal(self.id_layanan.harga_per_kg))
        return self.total_harga