nama_file = "data_keuangan.txt"

def file_ada ():
    f = open(nama_file, "a")
    f.close ()
    f = open(nama_file, "r")
    ada = False
    if f.read() != "":
        ada = True
    f.close()
    return ada

def load_data ():
    data = []
    f = open(nama_file, "r")
    baris = f.readlines()
    for line in baris:
        line = line.strip()
        if line:
            bagian = line.split('|')
            if len(bagian) == 4:
                tanggal, keterangan, jumlah, tipe = bagian
                data.append({
                    'Tanggal': tanggal,
                    'Keterangan': keterangan,
                    'Jumlah': jumlah,
                    'Tipe': tipe
                })
    f.close()
    return data

def simpan_data (data):
    f = open(nama_file, "w")
    for item in data:
        line = item['Tanggal'] + '|' + item['Keterangan'] + '|' + item['Jumlah'] + '|' + item['Tipe'] + '\n'
        f.write(line)
    f.close()

def tampilkan_data(data):
    if len(data) == 0:
        print("\nTidak ada data yang tersimpan")
    else:
        print("\n============================DATA KEUANGAN============================")
        print(f"{'No':<4} {'Tanggal':<14} {'Keterangan':<25} {'Jumlah':>12} {'Tipe':<12}")
        print("-" * 70)
        for i in range(len(data)):
            item = data[i]
            nomor = i + 1
            print(f"{nomor:<4} {item['Tanggal']:<14} {item['Keterangan']:<25} {item['Jumlah']:>12} {item['Tipe']:<12}")
        
        print("-" * 70)

def tambah_data(data):
    tanggal = input("Masukkan tanggal : ")
    keterangan = input("Masukkan keterangan         : ")
    jumlah = input("Masukkan jumlah uang        : ")
    tipe = input("Masukkan tipe (pengeluaran/pemasukan) : ").lower()

    if tipe == 'pengeluaran' or tipe == 'pemasukan':
        item = {
            'Tanggal': tanggal,
            'Keterangan': keterangan,
            'Jumlah': jumlah,
            'Tipe': tipe
        }
        data.append(item)
        simpan_data(data)
        print("Data berhasil disimpan!")
    else:
        print("Tipe tidak valid. Data tidak disimpan.")

def hapus_data(data):
    tampilkan_data(data)
    if len(data) == 0:
        return

    index = input("Masukkan nomor data yang ingin dihapus : ")
    if index.isdigit():
        idx = int(index) - 1
        if idx >= 0 and idx < len(data):
            keterangan = data[idx]['Keterangan']
            data.pop(idx)
            simpan_data(data)
            print("Data dengan keterangan '" + keterangan + "' berhasil dihapus!")
        else:
            print("Nomor data tidak valid.")
    else:
        print("Input tidak valid.")


file_ada()
data = load_data()

while True:
    print("\n=== Menu Keuangan ===")
    print("1. Tambah data keuangan")
    print("2. Hapus data keuangan")
    print("3. Tampilkan semua data")
    print("4. Keluar")

    pilihan = input("Pilih menu (1-4): ")

    if pilihan == '1':
        tambah_data(data)
    elif pilihan == '2':
        hapus_data(data)
    elif pilihan == '3':
        tampilkan_data(data)
    elif pilihan == '4':
        print("Terima kasih! Sampai jumpa.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih 1-4.")
