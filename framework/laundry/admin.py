# admin.py
from django.contrib import admin
from .models import Layanan, Pesanan

class LayananAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama', 'harga_per_kg')  
    search_fields = ('nama',)  

class PesananAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama_pemesan', 'id_layanan', 'berat_cucian', 'total_harga')  
    search_fields = ('nama_pemesan',)  
    list_filter = ('id_layanan',) 

admin.site.register(Layanan, LayananAdmin)
admin.site.register(Pesanan, PesananAdmin)
