# Generated by Django 4.2.5 on 2023-09-23 03:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_kategori', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_status', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Produk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_produk', models.CharField(max_length=255)),
                ('harga', models.DecimalField(decimal_places=2, max_digits=10)),
                ('kategori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restAPI.kategori')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restAPI.status')),
            ],
        ),
    ]
