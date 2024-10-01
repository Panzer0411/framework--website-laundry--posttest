from django.db import models

class Layanan(models.Model):
  id = models.AutoField(primary_key=True)
  nama = models.CharField(max_length=255)
  deskripsi = models.TextField()
  harga_per_kg = models.IntegerField()

  def __str__(self):
    return self.nama
