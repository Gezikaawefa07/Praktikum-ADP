n = int(input("Jumlah Mahasiswa : "))
data = []
jumlah = 0

for i in range (1,n+1):
    nama = input(f"Mahasiswa ke-{i}: ")
    pretest = float(input("pretest : "))
    postest = float(input("postest : "))
    makalah = float(input("makalah : "))
    na = 0.4 * pretest + 0.4 * postest + 0.2 * makalah
    jumlah += na
    data.append(nama)
    data.append(na)

print("\n__________________________________")
print(f"NAMA MAHASISWA    | NILAI AKHIR   ")
print("__________________________________")
for objek in range (n):
    nama = data[2 * objek]
    nilai = data[2 * objek + 1]
    print(f"{nama:<17} | {nilai:.2f}")

rata_rata = jumlah / n
print(f"\nRata rata nilai akhir kelas adalah {rata_rata:.2f}")

nilai_tertinggi = data[1]
nama_tertinggi = data[0]
nilai_terendah = data[1]
nama_terendah = data[0]

for objek in range(n):
    if data[2 * objek + 1] > nilai_tertinggi:
        nilai_tertinggi = data[2 * objek + 1]
        nama_tertinggi = data[2 * objek]
    if data[2 * objek + 1] < nilai_terendah:
        nilai_terendah = data[2 * objek + 1]
        nama_terendah = data[2 * objek]

print(f"Nilai tertinggi diraih oleh {nama_tertinggi} dengan nilai {nilai_tertinggi:2f} ")
print(f"Nilai terendah diraih oleh {nama_terendah} dengan nilai {nilai_terendah:2f} ")  
print("\nMAHASISWA YANG NILAINYA DIATAS RATA-RATA:")
for objek in range (n):
    nama = data[2 * objek]
    nilai = data [2 * objek + 1]
    if nilai >= rata_rata:
        print(nama)
