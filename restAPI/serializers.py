from rest_framework import serializers
from .models import Produk,Kategori,Status

class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = '__all__'

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'
        
class ProdukSerializer(serializers.ModelSerializer):
    kategori = serializers.CharField(source='kategori.nama_kategori')
    status = serializers.CharField(source='status.nama_status')
    class Meta:
        model = Produk
        fields = '__all__'

    def create(self, validated_data):
        kategori_data = validated_data.pop('kategori').pop('nama_kategori')
        status_data = validated_data.pop('status').pop('nama_status')

        kategori, _ = Kategori.objects.get_or_create(nama_kategori=kategori_data)
        status, _ = Status.objects.get_or_create(nama_status=status_data)

        produk = Produk.objects.create(
            kategori=kategori,
            status=status,
            **validated_data
        )

        return produk
