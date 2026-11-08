# LIST
stokToko = [
    ["Buku Tulis Kampus", "Alat Tulis", 45000, 30],
    ["Spidol Papan Tulis", "Perlengkapan Kantor", 12000, 50]
]

print("=== Data Stok Awal ===")
print(stokToko) 
print()

# tambah barang baru
namaBarang = input("Masukkan Nama Barang baru: ")
kategori = input("Masukkan Kategori: ")
harga = int(input("Masukkan Harga Satuan: "))
stok = int(input("Masukkan Jumlah Stok: "))
stokToko.append([namaBarang, kategori, harga, stok])


print()
print("=== Data Setelah Penambahan ===")
print(stokToko)
print()

# kurangi stok Buku Tulis Kampus (pake aritmatika)
terjual = int(input("Masukkan jumlah Buku Tulis Kampus yang terjual: "))
stokToko[0][3] -= terjual

print("=== Data Setelah Update Stok Buku ===")
print(stokToko)
print()

# hapus barang berdasarkan indeks nya
indeksHapus = int(input("Masukkan indeks barang yang ingin dihapus: "))
stokToko.pop(indeksHapus)

print("=== Data Final ===")
print(stokToko)
print()

# DICT
antreanKasir = {
    "kasir_1": {
        "nama": "William",
        "barang": "Novel Fiksi",
        "harga_satuan": 85000,
        "jumlah": 1
    }
}

# tambah 2 buku, terus hitung total_bayar
antreanKasir["kasir_1"]["jumlah"] += 2
antreanKasir["kasir_1"]["totalBayar"] = (
    antreanKasir["kasir_1"]["harga_satuan"] * antreanKasir["kasir_1"]["jumlah"]
)

print("=== Data Kasir 1 Setelah Penambahan Barang ===")
print("Nama Pembeli :", antreanKasir["kasir_1"]["nama"])
print("Barang       :", antreanKasir["kasir_1"]["barang"])
print("Harga Satuan :", antreanKasir["kasir_1"]["harga_satuan"])
print("Jumlah       :", antreanKasir["kasir_1"]["jumlah"])
print("Total Bayar  :", antreanKasir["kasir_1"]["totalBayar"])
print()

#  kasir 2 dari input user
nama = input("Masukkan Nama Pembeli Kasir 2: ")
barang = input("Masukkan Barang: ")
hargaSatuan = int(input("Masukkan Harga Satuan: "))
jumlah = int(input("Masukkan Jumlah: "))

antreanKasir["kasir_2"] = {
    "nama": nama,
    "barang": barang,
    "harga_satuan": hargaSatuan,
    "jumlah": jumlah,
    "totalBayar": hargaSatuan * jumlah
}

# hapus kasir1 sama cetak sisa antrean
del antreanKasir["kasir_1"]
print()


#deploy output data yang telah di kalkulasi diawal tadi
print("=== Sisa Antrean Setelah Kasir 1 Selesai ===")
print(antreanKasir)
print()
print("--- Kasir 2 ---")
print("Nama Pembeli :", antreanKasir["kasir_2"]["nama"])
print("Barang       :", antreanKasir["kasir_2"]["barang"])
print("Harga Satuan :", antreanKasir["kasir_2"]["harga_satuan"])
print("Jumlah       :", antreanKasir["kasir_2"]["jumlah"])
print("Total Bayar  :", antreanKasir["kasir_2"]["totalBayar"])