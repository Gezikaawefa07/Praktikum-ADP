print("---------------------------------------")
print("----RINCIAN PEMESANAN TIKET PESAWAT----")
print("---------------------------------------\n")


nama = input("Nama               : ")
umur = input("Umur               : ")
jenis_kelamin = input("Jenis Kelamin      : ")

print("\n---------------------------------------")
print("----------MENU JENIS MASKAPAI----------")
print("---------------------------------------\n")

kode_1 = 3012
kode_2 = 4015
kode_3 = 4050

kode = int(input("Kode Maskapai      : "))        

if kode == kode_1:
    print("Kelas Ekonomi      : Rp.800.000")
    print("Kelas Bisnis       : Rp.850.000")
    print("Kelas First Class  : Rp.900.000")
    print("\n---------------------------------------")
    print("-----------DETAIL PEMESANAN------------")
    print("---------------------------------------\n")
    tp = "Padang-Jakarta"
    jenis = input("Jenis Maskapai     : ")
    jumlah = int(input("Jumlah Tiket       : "))
    e_3012 = 800000
    b_3012 = 850000
    fc_3012 = 900000
    if jenis == "Kelas Ekonomi":
        if jumlah <= 3:
             total = e_3012 * jumlah
        else:
             print("Anda mendapat diskon 20%")
             total = e_3012 * jumlah - (e_3012 * jumlah * 20/100)
    if jenis == "Kelas Bisnis":
        if jumlah <= 3: 
             total = b_3012 * jumlah
        else:
             print("Anda mendapat diskon 20%")
             total = b_3012 * jumlah - (b_3012 * jumlah * 20/100)
    if jenis == "Kelas First Class":
        if jumlah <= 3:
             total = fc_3012 * jumlah
        else:
             print("Anda mendapat diskon 20%")
             total = fc_3012 * jumlah - (fc_3012 * jumlah * 20/100) 

elif kode == kode_2:
      print("Kelas Ekonomi      : Rp.500.000")
      print("Kelas Bisnis       : Rp.550.000")
      print("Kelas First Class  : Rp.700.000")
      print("\n---------------------------------------")
      print("-----------DETAIL PEMESANAN------------")
      print("---------------------------------------\n")
      tp = "Padang-Batam"
      jenis = input("Jenis Maskapai     : ")
      jumlah = int(input("Jumlah Tiket       : "))
      e_4015 = 500000
      b_4015 = 550000
      fc_4015 = 700000
      if jenis == "Kelas Ekonomi":
        if jumlah <= 3:
             total = e_4015 * jumlah
        else:
             print("Anda mendapat diskon 20%")
             total = e_4015 * jumlah - (e_4015 * jumlah * 20/100)
      if jenis == "Kelas Bisnis":
        if jumlah <= 3: 
             total = b_4015 * jumlah
        else:
             print("Anda mendapat diskon 20%")
             total = b_4015 * jumlah - (b_4015 * jumlah * 20/100)
      if jenis == "Kelas First Class":
        if jumlah <= 3:
             total = fc_4015 * jumlah
        else:
             print("Anda mendapat diskon 20%")
             total = fc_4015 * jumlah - (fc_4015 * jumlah * 20/100)

elif kode == kode_3:
      print("Kelas Ekonomi      : Rp.700.000")
      print("Kelas Bisnis       : Rp.750.000")
      print("Kelas First Class  : Rp.850.000") 
      print("\n---------------------------------------")
      print("-----------DETAIL PEMESANAN------------")
      print("---------------------------------------\n")
      tp = "Padang-Bandung"
      jenis = input("Jenis Maskapai     : ")
      jumlah = int(input("Jumlah Tiket       : "))
      e_4050 = 700000
      b_4050 = 750000
      fc_4050 = 850000
      if jenis == "Kelas Ekonomi":
        if jumlah <= 3:
             total = e_4050 * jumlah
        else:
             print("Anda mendapat diskon 20%")
             total = e_4050 * jumlah - (e_4050 * jumlah * 20/100)
      if jenis == "Kelas Bisnis":
        if jumlah <= 3: 
             total = b_4050 * jumlah
        else:
             print("Anda mendapat diskon 20%")
             total = b_4050 * jumlah - (b_4050 * jumlah * 20/100)
      if jenis == "Kelas First Class":
        if jumlah <= 3:
             total = fc_4050 * jumlah
        else:
             print("Anda mendapat diskon 20%")
             total = fc_4050 * jumlah - (fc_4050 * jumlah * 20/100)

else: 
     print("Kode maskapai tidak valid") 
     kode = "Tidak Valid" 
     tp = "-"
     jenis = "-"
     jumlah = "-" 
     total = "-"   

print("\n---------------------------------------")  
print("------------STRUK PEMBELIAN------------")
print("---------------------------------------\n")  
print("1. Nama                 : ", nama)
print("2. Umur                 : ", umur, "Tahun")
print("3. Jenis Kelamin        : ", jenis_kelamin)
print("4. Kode Maskapai        : ", kode)
print("5. Tujuan Penerbangan   : ", tp)
print("6. Jenis Maskapai       : ", jenis)
print("7. Jumlah Tiket         : ", jumlah)
print("8. Total Harga          : ", total)

print("\n---------------------------------------")  
print("--------------TERIMAKASIH--------------")
print("---------------------------------------\n")  


            




    