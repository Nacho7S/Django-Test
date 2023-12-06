from django.shortcuts import render, redirect
from .forms import ProductForms
from .models import Produk
# Create your views here.

def Products_list(request):
  status_filter = request.GET.get('status_filter', 'all')  # Default to 'all' if not specified
  if status_filter == 'all':
      product_list = Produk.objects.all()
  elif status_filter == 'bisa_dijual':
      product_list = Produk.objects.filter(status__nama_status='bisa dijual')
  else:
      product_list = Produk.objects.none()

  context = {'product_list': product_list, 'status_filter': status_filter}
  return render(request, "Products/product_list.html", context)

def Products_form(request, id=0):
  if request.method == "GET":
    if id == 0 :
      form = ProductForms
    else:
      product = Produk.objects.get(id_produk=id)
      form = ProductForms(instance=product)
    return render(request, "Products/product_form.html", {'form': form})
  else:
    if id == 0:
      form = ProductForms(request.POST)
    else:
      product = Produk.objects.get(id_produk=id)
      form = ProductForms(request.POST, instance=product)
    if form.is_valid():
      form.save()
    return redirect('/product')

def Products_delete(request, id= 0):
  product = Produk.objects.get(id_produk=id)
  product.delete()
  return redirect('/product')


