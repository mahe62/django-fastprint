from django.shortcuts import render, get_object_or_404, redirect,HttpResponse
from django.db import IntegrityError
from .serializers import ProdukSerializer
from .models import Produk,Kategori
from .forms import ProdukForm
import requests

def postapiproduk(request):
    # API endpoint URL
    api_url = "https://recruitment.fastprint.co.id/tes/api_tes_programmer/"

    payload = {
        "username": "tesprogrammer250923C03",
        "password": "f09229a1106c4085b7b4578f52f366b8" 
    }
    try:
        response = requests.post(api_url, data=payload)

        if response.status_code == 200:
            data = response.json()
            
            if request.method == 'POST' and 'save_button' in request.POST:
                save_json_data_to_database(data)
            return render(request, 'restAPI/getdata.html', {'api_data': data})
        else:
            error_message = f"Failed to fetch data from the API. Status code: {response.status_code}"
            return HttpResponse(error_message)
    except requests.exceptions.RequestException as e:
        return HttpResponse(str(e))


# def getapiproduk(request):
#     api_url = "https://api.npoint.io/44c2454d8c5b7aa1ef73"
#     try:
#         # Make a GET request to the API
#         response = requests.get(api_url)

#         # Check the response status code
#         if response.status_code == 200:
#             data = response.json()
            
#             if request.method == 'POST' and 'save_button' in request.POST:
#                 save_json_data_to_database(data)
#             return render(request, 'restAPI/getdata.html', {'api_data': data})
#         else:
#             error_message = f"Failed to fetch data from the API. Status code: {response.status_code}"
#             return HttpResponse(error_message)
#     except requests.exceptions.RequestException as e:
#         return HttpResponse(str(e))


def produk_list(request):
    filter_status = request.POST.get('filter_status', 'off')

    if request.method == 'POST' and 'filter_button' in request.POST:
        if request.POST['filter_button'] == 'Filter On':
            filter_status = 'on'
        else:
            filter_status = 'off'

    lsitproduk = Produk.objects.values('id','nama_produk', 'harga', 'kategori__nama_kategori', 'status__nama_status')

    if filter_status == 'on':
        lsitproduk = lsitproduk.order_by('id')
        lsitproduk = lsitproduk.filter(status__nama_status="{'nama_status': 'bisa dijual'}").values('id','nama_produk', 'harga', 'kategori__nama_kategori', 'status__nama_status')
    else:
        lsitproduk = lsitproduk.order_by('id')
    return render(request, 'restAPI/list.html', {'produk': lsitproduk, 'filter_status': filter_status})


def produk_detail(request, id):
    produk = get_object_or_404(Produk, id=id)
    return render(request, 'restAPI/detail.html', {'produk': produk})

def produk_create(request):
    if request.method == 'POST':
        form = ProdukForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produk_list')
    else:
        form = ProdukForm()

    return render(request, 'restAPI/form.html', {'form': form})

def produk_update(request, id):
    produk = get_object_or_404(Produk, id=id)
    if request.method == 'POST':
        form = ProdukForm(request.POST, instance=produk)
        if form.is_valid():
            form.save()
            return redirect('produk_list')
    else:
        form = ProdukForm(instance=produk)
    return render(request, 'restAPI/form.html', {'form': form, 'produk': produk})

def produk_delete(request, id):
    produk = get_object_or_404(Produk, id=id)
    produk.delete()
    return redirect('produk_list')



def save_json_data_to_database(json_data):
    try:
        data_array = json_data.get('data', [])  

        for item in data_array:
            try:
                serializer = ProdukSerializer(data=item)
                if serializer.is_valid():
                    serializer.save()
                    print(f"Saved {item['nama_produk']} to the database.")
                else:
                    print(f"Error while saving {item['nama_produk']}: {serializer.errors}")
            except IntegrityError:
                print(f"Skipping duplicate entry for {item['nama_produk']}.")
    except KeyError:
        print("JSON data is missing the 'data' key.")