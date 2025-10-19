# =========================
# === FUNGSI-FUNGSI UTAMA
# =========================
arr = [2, 1, 3, 4, 5]
for i, t in enumerate(arr, start=2):
    print(t)
def tampilkan_barang(data_barang):
    print("\n=== Daftar Barang ===")
    for i, barang in enumerate(data_barang, start=2):
        print(f"{i}. {barang['nama']} - Rp{barang['harga']} (stok: {barang['stok']})")

def proses_kotak_saran(kotak_saran):
    barang_baru = input("Masukkan nama barang yang Anda sarankan: ")
    alasan = input("Mengapa Anda menyarankan barang ini? ")
    kotak_saran.append({"nama": barang_baru, "alasan": alasan})
    print(f"Terima kasih! Barang '{barang_baru}' ditambahkan ke kotak saran.")

def proses_manage(data_barang, kotak_saran, data_karyawan, keranjang, total, jumlah_uang, data_penjualan):
    password = input("Masukkan password: ")
    if password != "bossgalak123":
        print("Password salah!")
        return jumlah_uang

    while True:
        print("\n=== Mode Manage Toko ===")
        print("1. Tambah Barang")
        print("2. Hapus Barang")
        print("3. Update Stok Barang")
        print("4. Print Penjualan Hari Ini")
        print("5. Kelola Karyawan")
        print("6. Kembali")
        pilihan_manage = input("Pilih opsi (1-6): ")

        if pilihan_manage == "1":
            print(f"Saran dari pelanggan adalah \n{kotak_saran}")
            nama_baru = input("Masukkan nama barang baru: ")
            harga_baru = int(input("Masukkan harga barang baru: "))
            stok_baru = int(input("Masukkan stok barang baru: "))
            data_barang.append({"nama": nama_baru, "harga": harga_baru, "stok": stok_baru})
            print(f"Barang '{nama_baru}' berhasil ditambahkan.")

        elif pilihan_manage == "2":
            tampilkan_barang(data_barang)
            hapus_index = int(input("Masukkan nomor barang yang ingin dihapus: ")) - 1
            if 0 <= hapus_index < len(data_barang):
                barang_dihapus = data_barang.pop(hapus_index)
                print(f"Barang '{barang_dihapus['nama']}' dihapus dari toko.")
            else:
                print("Nomor barang tidak valid.")

        elif pilihan_manage == "3":
            tampilkan_barang(data_barang)
            update_index = int(input("Masukkan nomor barang yang ingin diupdate stoknya: ")) - 1
            if 0 <= update_index < len(data_barang):
                new_stok = int(input(f"Masukkan stok baru untuk '{data_barang[update_index]['nama']}': "))
                data_barang[update_index]['stok'] = new_stok
                print(f"Stok '{data_barang[update_index]['nama']}' diperbarui menjadi {new_stok}.")
            else:
                print("Nomor barang tidak valid.")

        elif pilihan_manage == "4":
            print("\n=== Penjualan Hari Ini ===")
            if data_penjualan:
                for i, transaksi in enumerate(data_penjualan, start=1):
                    print(f"\nTransaksi {i}:")
                    for item in transaksi['keranjang']:
                        print(f"  {item['nama']} x {item['jumlah']} = Rp{item['subtotal']}")
                    print(f"  Total: Rp{transaksi['total']}")
                print(f"\nJumlah uang toko: Rp{jumlah_uang}")
            else:
                print("Belum ada penjualan hari ini.")

        elif pilihan_manage == "5":
            print("\n=== Data Karyawan ===")
            for i, k in enumerate(data_karyawan, start=1):
                status = "Sudah digaji" if k["sudah_digaji"] else "Belum digaji"
                print(f"{i}. {k['nama']} - {k['posisi']} - Rp{k['gaji']} ({status})")
            idx = int(input("Pilih karyawan yang ingin digaji (0 untuk batal): "))
            if 1 <= idx <= len(data_karyawan):
                karyawan = data_karyawan[idx - 1]
                if not karyawan["sudah_digaji"]:
                    if jumlah_uang >= karyawan["gaji"]:
                        jumlah_uang -= karyawan["gaji"]
                        karyawan["sudah_digaji"] = True
                        print(f"Karyawan {karyawan['nama']} sudah digaji.")
                    else:
                        print("Uang toko tidak cukup untuk gaji!")
                else:
                    print("Karyawan ini sudah digaji.")
        elif pilihan_manage == "6":
            break
        else:
            print("Opsi tidak valid.")
    return jumlah_uang

def proses_pembelian(data_barang, index, jumlah, keranjang, total, jumlah_uang):
    barang = data_barang[index]
    if jumlah > barang['stok']:
        print("Stok tidak mencukupi!")
        return total, jumlah_uang

    subtotal = barang['harga'] * jumlah
    total += subtotal
    barang['stok'] -= jumlah
    jumlah_uang += subtotal

    keranjang.append({"nama": barang['nama'], "jumlah": jumlah, "subtotal": subtotal})
    print(f"{barang['nama']} x {jumlah} ditambahkan ke keranjang. Subtotal: Rp{subtotal}")
    return total, jumlah_uang

def cetak_struk(keranjang, total):
    print("\n=== Struk Belanja ===")
    for item in keranjang:
        print(f"{item['nama']} x {item['jumlah']} = Rp{item['subtotal']}")
    print(f"Total belanja: Rp{total}")
    print("Terima kasih sudah berbelanja!")

def mulai_belanja(data_barang, data_karyawan, jumlah_uang, data_penjualan):
    keranjang = []
    total = 0
    kotak_saran = []

    while True:
        tampilkan_barang(data_barang)
        pilihan = input("\nPilih nomor barang (ketik 'checkout', 'tambahkan barang', atau 'manage'): ")

        if pilihan.lower() == "tambahkan barang":
            proses_kotak_saran(kotak_saran)
            continue

        elif pilihan.lower() == "checkout":
            break

        elif pilihan.lower() == "manage":
            jumlah_uang = proses_manage(data_barang, kotak_saran, data_karyawan, keranjang, total, jumlah_uang, data_penjualan)
            continue

        elif not pilihan.isdigit() or int(pilihan) < 1 or int(pilihan) > len(data_barang):
            print("Pilihan tidak valid.")
            continue

        index = int(pilihan) - 1
        try:
            jumlah = int(input(f"Masukkan jumlah {data_barang[index]['nama']} yang ingin dibeli: "))
        except ValueError:
            print("Input harus berupa angka.")
            continue

        total, jumlah_uang = proses_pembelian(data_barang, index, jumlah, keranjang, total, jumlah_uang)

    cetak_struk(keranjang, total)
    data_penjualan.append({"keranjang": keranjang.copy(), "total": total})
    return jumlah_uang

# ================================
# === DATA & EKSEKUSI PROGRAM ===
# ================================

data_barang = [
    {"nama": "Pensil", "harga": 2000, "stok": 100},
    {"nama": "Buku", "harga": 5000, "stok": 50},
    {"nama": "Penghapus", "harga": 1000, "stok": 200},
    {"nama": "Spidol", "harga": 3000, "stok": 80},
    {"nama": "Penggaris", "harga": 1500, "stok": 120},
    {"nama": "Tas", "harga": 150000, "stok": 30},
    {"nama": "Sepatu", "harga": 250000, "stok": 20},
    {"nama": "Topi", "harga": 75000, "stok": 40}
]

data_karyawan = [
    {"nama": "kipin", "posisi": "kasir", "gaji": 3000000, "sudah_digaji": False},
    {"nama": "budi", "posisi": "staf gudang", "gaji": 2500000, "sudah_digaji": True}
]

jumlah_uang = 0 
data_penjualan = []

# === Mulai Aplikasi ===
while True:
    jumlah_uang = mulai_belanja(data_barang, data_karyawan, jumlah_uang, data_penjualan)
    lagi = input("\nApakah Anda ingin berbelanja lagi? (ya/tidak): ").lower()
    if lagi != "ya":
        print("\nTerima kasih! Sampai jumpa lagi.")
        break
