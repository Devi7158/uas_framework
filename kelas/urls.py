from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
# from dashboard.views import dashboard, tambah_barang, Barang_View, Brand_View
from dashboard.views import *
from category.views import category




# def coba1(request):
#     return render(request, 'home.html')


def coba2(request): 
    title = "Home"
    konteks = {
        'titlenya': title,
    }
    return render(request, 'home.html', konteks)


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', coba1),
    path('', coba2),
    path('barang/', Barang_View,name='barang'),
    path('brand/', Brand_View),
    path('category/', category),
    path('addbrg/', tambah_barang),
    path('ubah/<int:id_barang>', ubah_brg, name='ubah_brg'),
    path('hapus/<int:id_barang>', hapus_brg, name='hapus_brg'),
]
