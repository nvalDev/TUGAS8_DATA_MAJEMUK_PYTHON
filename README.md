# Tugas Tipe Data Majemuk: Stok Toko dan Antrean Kasir

Program Python untuk latihan tipe data majemuk. Bagian pertama mencatat stok barang toko alat tulis dengan nested list. Bagian kedua mencatat antrean kasir toko buku dengan nested dictionary. Program berjalan di terminal dan meminta 10 input dari pengguna.

## Cara menjalankan

Pastikan Python 3 sudah terpasang. Simpan kode dalam file `tugas_tipe_data_majemuk.py`, lalu jalankan:

```
python tugas_tipe_data_majemuk.py
```

Isi tiap pertanyaan yang muncul, lalu tekan Enter.

## Bagian 1: Stok toko (nested list)

Data awal berupa list yang menyimpan dua barang. Setiap barang adalah list kecil dengan urutan tetap:

| Indeks | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Isi | nama | kategori | harga satuan | jumlah stok |

```python
stokToko = [
    ["Buku Tulis Kampus", "Alat Tulis", 45000, 30],
    ["Spidol Papan Tulis", "Perlengkapan Kantor", 12000, 50]
]
```

Program menjalankan tiga operasi berurutan.

**1. Tambah barang baru.** Pengguna mengisi nama, kategori, harga, dan stok. Fungsi `input()` mengembalikan teks, jadi harga dan stok dibungkus `int()` supaya bisa dihitung. Barang baru masuk ke ujung list lewat `append()`.

**2. Kurangi stok Buku Tulis Kampus.** Pengguna mengisi jumlah buku yang terjual. Buku Tulis Kampus ada di indeks `0`, dan stoknya ada di indeks `3` dalam barang itu:

```python
stokToko[0][3] -= terjual
```

Baris ini sama dengan `stokToko[0][3] = stokToko[0][3] - terjual`. Tanda `=` menyimpan hasil pengurangan ke tempat asalnya. Tanpa `=`, Python menghitung angkanya lalu membuangnya, dan stok tetap 30.

**3. Hapus barang berdasarkan indeks.** Pengguna mengisi nomor posisi barang, lalu `pop()` menghapus barang di posisi itu. Indeks dihitung mulai dari 0, jadi angka `1` menghapus barang kedua.

## Bagian 2: Antrean kasir (nested dictionary)

Dictionary luar menyimpan antrean, dengan kunci `kasir_1` dan `kasir_2`. Dictionary dalam menyimpan data satu pembeli:

```python
antreanKasir = {
    "kasir_1": {
        "nama": "William",
        "barang": "Novel Fiksi",
        "harga_satuan": 85000,
        "jumlah": 1
    }
}
```

Ada tiga langkah.

**1. Tambah 2 buku untuk William, lalu hitung total bayar.** Jumlah naik dari 1 jadi 3 lewat `+=`. Total bayar dihitung sesudah jumlah berubah, supaya hasilnya 85.000 x 3 = 255.000. Kalau urutannya terbalik, totalnya masih 85.000.

**2. Tambah kasir 2 dari input pengguna.** Pengguna mengisi nama pembeli, barang, harga satuan, dan jumlah. Program menyimpan keempatnya bersama `totalBayar` yang berasal dari harga dikali jumlah.

**3. Hapus kasir 1.** William selesai dilayani, jadi `del antreanKasir["kasir_1"]` menghapus datanya. Yang tersisa di antrean hanya `kasir_2`.

## Contoh jalannya program

Input yang dipakai: Kertas HVS A4 (kategori Kertas, harga 55000, stok 20), terjual 12, hapus indeks 1, lalu pembeli Caesar Filbert membeli 2 Buku Coding seharga 75000.

```
=== Data Stok Awal ===
[['Buku Tulis Kampus', 'Alat Tulis', 45000, 30], ['Spidol Papan Tulis', 'Perlengkapan Kantor', 12000, 50]]

Masukkan Nama Barang baru: Kertas HVS A4
Masukkan Kategori: Kertas
Masukkan Harga Satuan: 55000
Masukkan Jumlah Stok: 20

=== Data Setelah Penambahan ===
[['Buku Tulis Kampus', 'Alat Tulis', 45000, 30], ['Spidol Papan Tulis', 'Perlengkapan Kantor', 12000, 50], ['Kertas HVS A4', 'Kertas', 55000, 20]]

Masukkan jumlah Buku Tulis Kampus yang terjual: 12
=== Data Setelah Update Stok Buku ===
[['Buku Tulis Kampus', 'Alat Tulis', 45000, 18], ['Spidol Papan Tulis', 'Perlengkapan Kantor', 12000, 50], ['Kertas HVS A4', 'Kertas', 55000, 20]]

Masukkan indeks barang yang ingin dihapus: 1
=== Data Final ===
[['Buku Tulis Kampus', 'Alat Tulis', 45000, 18], ['Kertas HVS A4', 'Kertas', 55000, 20]]

=== Data Kasir 1 Setelah Penambahan Barang ===
Nama Pembeli : William
Barang       : Novel Fiksi
Harga Satuan : 85000
Jumlah       : 3
Total Bayar  : 255000

Masukkan Nama Pembeli Kasir 2: Caesar Filbert
Masukkan Barang: Buku Coding
Masukkan Harga Satuan: 75000
Masukkan Jumlah: 2

=== Sisa Antrean Setelah Kasir 1 Selesai ===
{'kasir_2': {'nama': 'Caesar Filbert', 'barang': 'Buku Coding', 'harga_satuan': 75000, 'jumlah': 2, 'totalBayar': 150000}}

--- Kasir 2 ---
Nama Pembeli : Caesar Filbert
Barang       : Buku Coding
Harga Satuan : 75000
Jumlah       : 2
Total Bayar  : 150000
```

## Error yang mungkin muncul

| Penyebab | Error |
|---|---|
| Mengisi huruf saat program meminta harga, stok, jumlah, atau indeks | `ValueError` |
| Mengisi indeks hapus yang melebihi jumlah barang di list | `IndexError` |
| Lupa membungkus `input()` dengan `int()` sebelum menghitung | `TypeError` |

Program ini belum memeriksa input, jadi ketiganya menghentikan program. Perbaikan yang masuk akal untuk versi berikutnya adalah `try` dan `except`, atau pengecekan `if` sebelum memakai indeks.

## Konsep yang dipakai

- Nested list dan akses indeks ganda seperti `stokToko[0][3]`
- Nested dictionary dan akses kunci berlapis seperti `antreanKasir["kasir_1"]["jumlah"]`
- Method list: `append()` dan `pop()`
- Operator `-=` dan `+=`
- Perintah `del` untuk menghapus kunci dictionary
- Konversi tipe dengan `int()`
