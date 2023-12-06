from django import forms
from .models import Produk


class ProductForms(forms.ModelForm):

  class Meta:
    model = Produk
    fields = ('nama_produk', 'harga', 'kategori', 'status')
    labels = {
        'nama_produk': 'nama produk'
      }
    
  def __init__(self, *args, **kwargs):
    super(ProductForms, self).__init__(*args, **kwargs)
    self.fields['kategori'].empty_label = "Select Kategori"
    self.fields['status'].empty_label = "Select Status"