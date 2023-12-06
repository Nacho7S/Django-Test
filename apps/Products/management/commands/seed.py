import requests
import hashlib
from django.core.management.base import BaseCommand
from Products.models import Kategori, Status, Produk
import json

class Command(BaseCommand):
    help = 'Seed data from public API into the database'

    def handle(self, *args, **options):
        
        api_url = 'https://recruitment.fastprint.co.id/tes/api_tes_programmer'
        username = "tesprogrammer051223C21"
        password = "bisacoding-05-12-23" 
        hashed_password = hashlib.md5(password.encode()).hexdigest()
        print(hashed_password)

        newHeaders = {"Content-type": "application/json"}
        dataLogin = {"username": username, "password": hashed_password}


        print(dataLogin)
        print(json.dumps(dataLogin))
        response = requests.post(api_url, json=dataLogin, headers=newHeaders)


        # self.stdout.write(response)
        print(response)
        if response.status_code == 200:
            
            data = response.json()['data']
            
            kategori_mapping = {
                "L QUEENLY": "Queenly",
                "L MTH AKSESORIS (IM)": "MTH Aksesoris (IM)",
                "L MTH TABUNG (LK)": "MTH Tabung (LK)",
                "SP MTH SPAREPART (LK)": "MTH Sparepart (LK)",
                "CI MTH TINTA LAIN (IM)": "MTH Tinta Lain (IM)",
                "S MTH STEMPEL (IM)": "MTH Stempel (IM)"
            }

            
            status_bisa_dijual, _ = Status.objects.get_or_create(nama_status='bisa dijual')
            status_tidak_bisa_dijual, _ = Status.objects.get_or_create(nama_status='tidak bisa dijual')

            for item in data:
                kategori_nama = kategori_mapping.get(item['kategori'], 'Unknown')
                kategori, _ = Kategori.objects.get_or_create(nama_kategori=kategori_nama)

                status = status_bisa_dijual if item['status'] == 'bisa dijual' else status_tidak_bisa_dijual

                Produk.objects.create(
                    id_produk=item['id_produk'],
                    nama_produk=item['nama_produk'],
                    harga=item['harga'],
                    kategori=kategori,
                    status=status
                )

            self.stdout.write(self.style.SUCCESS('Data seeded successfully'))
        else:
            self.stdout.write(self.style.ERROR(f'Failed to fetch data from the API. Status code: {response.status_code}'))
