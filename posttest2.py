print("=================================")
print("   Selamat datang di Baby care   ")
print("=================================")

from prettytable import PrettyTable
# Tentukan nama kolom apa saja saat membuat tabel
tabelBarang = PrettyTable(["nomor barang", "nama barang", "Harga Barang", "stok barang", ])

# Tambahkan data baris
tabelBarang.add_row(["1", "Popok", "50.000", "10"            ])
tabelBarang.add_row(["2", "Stoler", "1.500.000", "15"        ])
tabelBarang.add_row(["3", "Bedong selimut", "100.000", "12"  ])
tabelBarang.add_row(["4", "Tempat tidur bayi", "250.000", "8"])
tabelBarang.add_row(["5", "Dot susu", "30.000", "16"         ])

# Data barang awal
barang = [
    {"nama": "Popok", "harga": 50000, "stok": 10},
    {"nama": "Stoler", "harga": 1500000, "stok": 15},
    {"nama": "Bedong selimut", "harga": 100000, "stok": 12},
    {"nama": "Tempat tidur bayi", "harga": 250000, "stok": 8},
    {"nama": "Dot susu", "harga": 30000, "stok": 16},
]


#Fungsi untuk menampilkan produk
def tampilan_barang() :
    print("Daftar Nama Barang:")
    print(tabelBarang)
    print("Tabel barang ditampilkan")

# Fungsi untuk menambahkan produk
def tambah_barang():
    nama_barang = input("Masukkan nama barang: ")
    harga_barang = float(input("Masukkan harga barang: "))
    stok_barang = int(input("Masukkan stok barang: "))  
# Menghitung nomor barang baru berdasarkan jumlah barang yang sudah ada
    nomor_barang = str(len(barang) + 1)
    barang.append({"nama": nama_barang, "harga": harga_barang, "stok": stok_barang})
    
    # Menambahkan data barang baru ke tabel
    tabelBarang.add_row([nomor_barang, nama_barang, harga_barang, stok_barang])
    
    print("Barang berhasil ditambahkan.")
    tampilan_barang()

# Fungsi untuk mengedit produk
def edit_barang():
    tampilan_barang()
    pilihan = int(input("Masukkan nomor barang yang ingin diubah: ")) - 1
    if 0 <= pilihan < len(barang):
        nama_baru = input("Masukkan nama barang baru: ")
        harga_baru = float(input("Masukkan harga barang baru: "))
        stok_baru = int(input("Masukkan stok baru: "))
        
        # Memperbarui data barang yang ada
        barang[pilihan]["nama"] = nama_baru
        barang[pilihan]["harga"] = harga_baru
        barang[pilihan]["stok"] = stok_baru
        print("Barang berhasil diubah.")
        
        # Memperbarui tabelBarang dengan data yang diperbarui
        tabelBarang.clear_rows()  # Menghapus semua baris dari tabel
        for i, item in enumerate(barang, 1):
            tabelBarang.add_row([str(i), item["nama"], item["harga"], item["stok"]])
        
# Memanggil kembali fungsi tampilan_barang() untuk menampilkan tabel yang diperbarui
        tampilan_barang()
    else:
        print("Nomor barang tidak valid.")

# Fungsi untuk menghapus produk
def hapus_barang():
    tampilan_barang()
    pilihan = int(input("Masukkan nomor barang yang ingin dihapus: ")) - 1
    if 0 <= pilihan < len(barang):
        del barang[pilihan]  # Menghapus barang dari list
        print("Barang berhasil dihapus.")
        
        # Membuat tabel baru setelah penghapusan
        tabelBarang.clear_rows()  # Menghapus semua baris dari tabel
        for i, item in enumerate(barang, 1):
            tabelBarang.add_row([str(i), item["nama"], item["harga"], item["stok"]])
        
        # Memanggil kembali fungsi tampilan_barang() untuk menampilkan tabel yang diperbarui
        tampilan_barang()
    else:
        print("Nomor barang tidak valid.")

# Data penjualan awal
penjualan = [
    {"nama_barang": "Popok", "jumlah": 4, "total_harga": 200000},
    {"nama_barang": "Stoler", "jumlah": 2, "total_harga": 3000000},
    {"nama_barang": "Bedong selimut", "jumlah": 2, "total_harga": 200000},
    {"nama_barang": "Dot susu", "jumlah": 5, "total_harga": 150000},
]

# Fungsi untuk menampilkan data penjualan
def tampilkan_penjualan():
    if not penjualan:
        print("Belum ada transaksi penjualan.")
        return
    
    tabelPenjualan = PrettyTable(["Nama Barang", "Jumlah", "Total Harga"])
    for item in penjualan:
        tabelPenjualan.add_row([item["nama_barang"], item["jumlah"], item["total_harga"]])
    
    print("Data Penjualan:")
    print(tabelPenjualan)

# Fungsi untuk transaksi pembeli
def transaksi_pembeli():
    tampilan_barang()
    pilihan = int(input("Masukkan nomor barang yang akan dibeli: ")) - 1
    if 0 <= pilihan < len(barang):
        jumlah_pembelian = int(input("Masukkan jumlah pembelian: "))
        if jumlah_pembelian <= barang[pilihan]["stok"]:
            total_harga = barang[pilihan]["harga"] * jumlah_pembelian

            # Menambahkan transaksi pembelian ke daftar penjualan
            penjualan.append({
                "nama_barang": barang[pilihan]["nama"],
                "jumlah": jumlah_pembelian,
                "total_harga": total_harga
            })

            # Mengurangi stok barang
            barang[pilihan]["stok"] -= jumlah_pembelian

            print(f"Transaksi berhasil. Total harga: {total_harga}")
        else:
            print("Stok barang tidak mencukupi.")
    else:
        print("Nomor barang tidak valid.")

# Program utama
while True:
    print("\nPilih peran Anda:")
    print("1. Admin")
    print("2. Pembeli")
    print("3. Keluar")
    peran = input("Pilih peran (1/2/3): ")

    if peran == "1":  # Admin
        print("\nPilihan Admin:")
        print("1. Tampilkan Produk")
        print("2. Tambah Produk")
        print("3. Edit Produk")
        print("4. Hapus Produk")
        print("5. Tampilkan Penjualan")
        print("6. Kembali")
        admin_pilihan = input("Pilih tindakan Admin (1/2/3/4/5/6): ")
        if admin_pilihan == "1":
            tampilan_barang()
        elif admin_pilihan == "2":
            tambah_barang()
        elif admin_pilihan == "3":
            edit_barang()
        elif admin_pilihan == "4":
            hapus_barang()
        elif admin_pilihan == "5":
            tampilkan_penjualan()
        elif admin_pilihan == "6":
            continue
        else:
            print("Pilihan tidak valid.")

    elif peran == "2":  # Pembeli
        print("Welcome to Baby care !")
        print("\nPilihan Pembeli:")
        print("1. Tampilkan Produk")
        print("2. Transaksi Pembelian")
        print("3. Kembali")
        pembeli_pilihan = input("Pilih tindakan Pembeli (1/2/3): ")
        if pembeli_pilihan == "1":
            tampilan_barang()
        elif pembeli_pilihan == "2":
            transaksi_pembeli()
        elif pembeli_pilihan == "3":
            continue
        else:
            print("Pilihan tidak valid.")

    elif peran == "3":  # Keluar
        print("Terima kasih telah menggunakan program ini.")
        break

    else:
        print("Pilihan tidak valid.")
