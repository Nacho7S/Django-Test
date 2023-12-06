from django.db import models

# Create your models here.

class Kategori(models.Model):
  id_kategori = models.BigAutoField(primary_key=True)
  nama_kategori = models.CharField(max_length=250, unique=True)

  def __str__(self):
    return self.nama_kategori

class Status(models.Model):
  id_status = models.BigAutoField(primary_key=True)
  nama_status = models.CharField(max_length=250)

  def __str__(self):
    return self.nama_status

class Produk(models.Model):
  id_produk = models.BigAutoField(primary_key=True)
  nama_produk = models.CharField(max_length=250, null=False, blank=False)
  harga = models.DecimalField(max_digits=19, decimal_places=4, null=False)
  kategori = models.ForeignKey(Kategori , on_delete=models.CASCADE, to_field="id_kategori")
  status = models.ForeignKey(Status, on_delete=models.CASCADE, to_field="id_status")
