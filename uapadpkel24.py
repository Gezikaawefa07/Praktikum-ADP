import os
import random
from datetime import datetime, timedelta
from termcolor import cprint
from rich.console import Console
from rich.table import Table
from rich.theme import Theme
from rich import box
from time import sleep
import threading
from pyfiglet import Figlet
from rich.text import Text
# Tema warna
custom_theme = Theme({
    "warna": "bold #6B4226 on #BFA6A0"
})
console = Console(theme=custom_theme)
pasangan_warna = {
    "pink": "bold #C77A86 on #F7C5CC",
    "purple": "bold #A98DAF on #DCC6E0",
    "blue": "bold #5DA9B5 on #AED9E0",
    "green": "bold #4C9A6A on #C2EDCE" }
motivasi_list = [
    "Disiplin itu mengerjakan hal hal yang kita benci seolah kita suka",
    "Kalau kamu merasa salah jurusan, ingat pesan Zipy ini. “Jika nasi sudah jadi bubur, buatlah bubur yang enak. Tidak ada gunanya menangisi hal yang sudah terjadi”",
    "Kamu gak butuh jadi sempurna besok. Kamu cuma butuh jadi 1% lebih baik hari ini daripada kemarin. Itu saja",
    "Yang terpenting adalah jumlah bangun mu lebih banyak daripada jumlah jatuh mu",
    "Ambil resikonya!! Berhasil kita rayakan, gagal kita setting ulang",
    "Jangan berhenti karena sulit, justru disitulah cerita hebat mu dimulai",
    "Konsisten itu jauh lebih mahal daripada ide cemerlang",
    "Langkah kecil yang kamu lakukan setiap hari, suatu saat akan menjadi langkah yang besar",
    "Walaupun hari ini terasa berat, jangan menyerah yaa..",
    "Nanti kita rayakan perjalanan yang hebat ini. Jangan menyerah dulu!!",
    "Peluk manis untuk kamu yang gak pernah nyerah dan selalu mengusahakan yang terbaik disetiap harinya. Semoga nilai UAS mu tinggi yaa",
    "Hasil yang indah tidak terlahir dari langkah yang mudah",
    "Jangan bandingkan dirimu dengan orang lain, karena itu tak akan pernah sama. Cukup bandingkan dirimu yang sekarang dengan dirimu yang sebelumnya",
    "Kadang kita terlalu fokus melihat betapa luar biasanya orang-orang diluar sana. Padahal disaat yang bersamaan, kita tak kalah hebat",
    "Kalau gak berusaha hari ini, siap siap aja jadi penonton kesuksesan orang lain besok"
]
def print_berjalan(teks):
    hasil = ""
    for huruf in teks:
        hasil += huruf
        print(f"{hasil}", end="\r")
        sleep(0.05)
    print(f"{hasil}")  # Cetak akhir
def countdown_terminal(durasi_menit, kegiatan, motivasi=None):
    os.system('cls')
    print_berjalan(f"⏰ Kegiatan: {kegiatan}")
    if motivasi:
        sleep(1)
        warna = random.choice(list(pasangan_warna.values()))
        console.print(f"[{warna}]💌 Motivasi: {motivasi}")
    sleep(1)
    input("\nTekan Enter untuk mulai timer...")
    total_detik = durasi_menit * 60
    skip_flag = [False]
    def tunggu_enter():
        input("\nTekan Enter untuk skip waktu...")
        skip_flag[0] = True
    # Jalankan listener Enter di thread terpisah
    t = threading.Thread(target=tunggu_enter)
    t.daemon = True
    t.start()
    while total_detik > 0:
        if skip_flag[0]:
            print(f"\n⏩ Waktu diskip untuk: {kegiatan}")
            break
        os.system('cls')
        print(f"⏰ Kegiatan: {kegiatan}")
        menit = total_detik // 60
        detik = total_detik % 60
        f = Figlet(font='big')
        timer_ascii = f.renderText(f"{menit:02}:{detik:02}")
        text_obj = Text(timer_ascii, style="bold #FF4C4C")  # Paksa semuanya merah
        console.print(text_obj)
        print("Tekan enter untuk lanjut...")
        sleep(1)
        total_detik -= 1
    if not skip_flag[0]:
        print(f"\n✅ Selesai: {kegiatan}")
        input("Tekan Enter untuk lanjut...")
# Waktu-waktu penting
jadwal_break = {
    "04:53": ("Sholat Subuh", 15),
    "07:00": ("Mandi & Sarapan", 45),
    "12:19": ("Sholat Zuhur & Makan Siang", 30),
    "15:44": ("Sholat Ashar & Mandi Sore", 30),
    "18:21": ("Sholat Maghrib & Makan Malam", 30),
    "19:36": ("Sholat Isya", 15)
}
# Fungsi cek azan di tengah sesi
def cek_ada_azan_di_tengah(start_time, durasi):
    hasil = []
    end_time = start_time + timedelta(minutes=durasi)
    for waktu_str, (label, durasi_azan) in jadwal_break.items():
        waktu_obj = datetime.strptime(waktu_str, "%H:%M").replace(
            year=start_time.year, month=start_time.month, day=start_time.day
        )
        if start_time < waktu_obj < end_time:
            hasil.append((waktu_obj, label, durasi_azan))
    return hasil if hasil else None
# Mulai program
os.system('cls')
print("Hai, Selamat datang di aplikasi UAS Master. Aku Zipy yang akan menemani persiapan UAS kamu hari ini.")
cprint("\nTekan Enter untuk melanjutkan...", "yellow")
input()
os.system('cls')
print("Siapa nama murid Zipy kali ini?")
nama = input()
os.system('cls')
print(f"Salam kenal {nama}! {nama}, mau belajar apa nih hari ini?")
matkul = input()
os.system('cls')
print(f"Asikkk😍 Sebelum mulai belajar, Zipy mau tau dulu nih. Nilai UTS {matkul} {nama} kemaren berapa?")
nilai_uts = int(input())
# Materi
os.system('cls')
print("Masukkan materi-materi yang akan kita pelajari (ketik 'selesai' jika sudah):")
materi_list = []
i = 1
while True:
    materi = input(f"Materi {i}: ")
    i += 1
    if materi.lower() == "selesai":
        break
    materi_list.append(materi)
# Pembagian waktu
os.system('cls')
max_waktu_belajar = 480  # 8 jam
def bagi_per_8(lst):
    hasil = []
    for i in range(0, len(lst), 8):
        hasil.append(lst[i:i+8])
    return hasil
if len(materi_list) > 8:
    console.print(f"Materi kamu ada {len(materi_list)}. Lebih dari 8 materi.", style="red")
    pilihan = input("Mau selesaikan semua hari ini atau lanjut besok? (ya/tidak): ")
    if pilihan.lower() == 'ya':
        waktu_per_materi = max_waktu_belajar // len(materi_list)
        grup_materi = [materi_list]
    else:
        print("\nBaik! Kita fokus belajar 8 materi dulu hari ini ya.")
        grup_materi = bagi_per_8(materi_list)
        waktu_per_materi = 60
else:
    waktu_per_materi = 60
    grup_materi = [materi_list]
# Pola belajar dan break
os.system('cls')
if 75 <= nilai_uts <= 100:
    belajar_menit = waktu_per_materi * 5 // 6
    break_menit = waktu_per_materi - belajar_menit
    pola = [(belajar_menit, break_menit)]
    print(f"Kita akan gunakan pola belajar {pola[0][0]}-{pola[0][1]}. {pola[0][0]} menit belajar kemudian {pola[0][1]} menit break")
elif 50 <= nilai_uts < 75:
    if waktu_per_materi == 60:
        pola = [(25, 5), (25, 5)]
        print("Kita akan gunakan pola belajar 25-5-25-5. 25 menit pertama akan digunakan untuk belajar. Lalu 5 menit setelahnya istirahat. Setelahnya, lanjut lagi belajar 25 menit, kemudian istirahat lagi 5 menit")
    else:
        belajar = int((25/60)*waktu_per_materi)
        istirahat = int((5/60)*waktu_per_materi)
        pola = [(belajar, istirahat), (belajar, istirahat)]
        print(f"Kita akan gunakan pola belajar {pola[0][0]}-{pola[0][1]}-{pola[1][0]}-{pola[1][1]}. {pola[0][0]} menit pertama akan digunakan untuk belajar. Lalu {pola[0][1]} menit setelahnya istirahat. Setelahnya, lanjut lagi belajar {pola[1][0]} menit, kemudian istirahat lagi {pola[1][1]} menit")
else:
    if waktu_per_materi == 60:
        pola = [(25, 5), (20, 10)]
        print("Kita akan gunakan pola belajar 25-5-20-10. 25 menit pertama akan digunakan untuk belajar. Lalu 5 menit setelahnya istirahat. Setelahnya, lanjut belajar 20 menit, kemudian istirahat 10 menit")
    else:
        belajar1 = int((25/60)*waktu_per_materi)
        istirahat1 = int((5/60)*waktu_per_materi)
        belajar2 = int((20/60)*waktu_per_materi)
        istirahat2 = int((10/60)*waktu_per_materi)
        pola = [(belajar1, istirahat1), (belajar2, istirahat2)]
        print(f"Kita akan gunakan pola belajar {pola[0][0]}-{pola[0][1]}-{pola[1][0]}-{pola[1][1]}. {pola[0][0]} menit pertama akan digunakan untuk belajar. Lalu {pola[0][1]} menit setelahnya istirahat. Setelahnya, lanjut belajar {pola[1][0]} menit, kemudian istirahat {pola[1][1]} menit")
# Input jam mulai
console.print("Sekarang ayo kita atur jam mulai belajar Hari 1.", style="cyan")
jam_mulai_str = input("Masukkan jam mulai belajar Hari 1 (format Jam:Menit, contoh 08:00): ")
jam_mulai = datetime.strptime(jam_mulai_str, "%H:%M")
# Loop tiap hari
os.system('cls')
for hari, materi_hari_ini in enumerate(grup_materi, 1):
    list_sesi = []
    if hari > 1:
        os.system('cls')
        console.print(f"Sekarang ayo kita atur jam mulai belajar Hari {hari}.", style="cyan")
        jam_mulai_str = input(f"Masukkan jam mulai belajar Hari {hari} (format Jam:Menit, contoh 08:00): ")
        jam_mulai = datetime.strptime(jam_mulai_str, "%H:%M")
    current_time = jam_mulai
    table = Table(
        title=f"📚 Hari {hari} - Rencana Belajar {nama} untuk {matkul} 📚",
        title_style="bold white on #6B4226",
        box=box.DOUBLE,
        show_lines=True,
        border_style="white"
    )
    table.add_column("Kegiatan", header_style="warna", justify="left", no_wrap=True)
    table.add_column("Waktu", header_style="warna", justify="center")
    table.add_column("Ceklis", header_style="warna", justify="center")
    sesi = 1
    row_index = 0
    for materi in materi_hari_ini:
        for belajar, istirahat in pola:
            azan_di_tengah = cek_ada_azan_di_tengah(current_time, belajar)
            if azan_di_tengah:
                for waktu_azan, label, durasi in azan_di_tengah:
                    sebelum_azan = int((waktu_azan - current_time).total_seconds() // 60)
                    jam_selesai_1 = current_time + timedelta(minutes=sebelum_azan)
                    waktu_format_1 = f"{current_time.strftime('%H:%M')} - {jam_selesai_1.strftime('%H:%M')}"
                    table.add_row(f"Materi {sesi}: {materi}", waktu_format_1, "☐", style="warna")
                    list_sesi.append((f"Belajar Materi {sesi}: {materi}", current_time, jam_selesai_1, False))
                    row_index += 1
                    waktu_azan_beres = jam_selesai_1 + timedelta(minutes=durasi)
                    waktu_format_azan = f"{jam_selesai_1.strftime('%H:%M')} - {waktu_azan_beres.strftime('%H:%M')}"
                    table.add_row(f"{label} (break)", waktu_format_azan, "☐", style="warna")
                    list_sesi.append((f"{label} (break)", jam_selesai_1, waktu_azan_beres, False))
                    row_index += 1
                    current_time = waktu_azan_beres
                    sisa = belajar - sebelum_azan
                    if sisa > 0:
                        jam_selesai_2 = current_time + timedelta(minutes=sisa)
                        waktu_format_2 = f"{current_time.strftime('%H:%M')} - {jam_selesai_2.strftime('%H:%M')}"
                        table.add_row(f"Materi {sesi}: {materi}", waktu_format_2, "☐", style="warna")
                        list_sesi.append((f"Belajar Materi {sesi}: {materi}", current_time, jam_selesai_2, False))
                        row_index += 1
                        current_time = jam_selesai_2
            else:
                jam_selesai = current_time + timedelta(minutes=belajar)
                waktu_format = f"{current_time.strftime('%H:%M')} - {jam_selesai.strftime('%H:%M')}"
                table.add_row(f"Materi {sesi}: {materi}", waktu_format, "☐", style="warna")
                list_sesi.append((f"Belajar Materi {sesi}: {materi}", current_time, jam_selesai, False))
                row_index += 1
                current_time = jam_selesai
            # ✅ FIXED: Break yang bisa kena azan
            azan_di_tengah_break = cek_ada_azan_di_tengah(current_time, istirahat)
            if azan_di_tengah_break:
                for waktu_azan, label, durasi in azan_di_tengah_break:
                    sebelum_azan = int((waktu_azan - current_time).total_seconds() // 60)
                    jam_selesai_1 = current_time + timedelta(minutes=sebelum_azan)
                    waktu_format_1 = f"{current_time.strftime('%H:%M')} - {jam_selesai_1.strftime('%H:%M')}"
                    table.add_row(f"(break)", waktu_format_1, "☐", style="warna")
                    list_sesi.append(("Istirahat", current_time, jam_selesai_1, False))
                    row_index += 1
                    waktu_azan_beres = jam_selesai_1 + timedelta(minutes=durasi)
                    waktu_format_azan = f"{jam_selesai_1.strftime('%H:%M')} - {waktu_azan_beres.strftime('%H:%M')}"
                    table.add_row(f"{label} (break)", waktu_format_azan, "☐", style="warna")
                    list_sesi.append((f"{label} (break)", jam_selesai_1, waktu_azan_beres, False))
                    row_index += 1
                    current_time = waktu_azan_beres
                    sisa = istirahat - sebelum_azan
                    if sisa > 0:
                        jam_selesai_2 = current_time + timedelta(minutes=sisa)
                        waktu_format_2 = f"{current_time.strftime('%H:%M')} - {jam_selesai_2.strftime('%H:%M')}"
                        table.add_row(f"(break)", waktu_format_2, "☐", style="warna")
                        list_sesi.append(("Istirahat", current_time, jam_selesai_2, False))
                        row_index += 1
                        current_time = jam_selesai_2
            else:
                jam_selesai_break = current_time + timedelta(minutes=istirahat)
                waktu_break = f"{current_time.strftime('%H:%M')} - {jam_selesai_break.strftime('%H:%M')}"
                table.add_row("(break)", waktu_break, "☐", style="warna")
                list_sesi.append(("Istirahat", current_time, jam_selesai_break, False))
                row_index += 1
                current_time = jam_selesai_break
        sesi += 1
    os.system('cls')
    console.print(table)
    cprint("\nSesi Hari ini akan segera dimulai!", "cyan")
    input("Tekan Enter jika kamu siap...")
    for i, (kegiatan, mulai, selesai_waktu, status_selesai) in enumerate(list_sesi):
        durasi = int((selesai_waktu - mulai).total_seconds() // 60)
        if "Belajar Materi" in kegiatan:
            motivasi = random.choice(motivasi_list)
        else:
            motivasi = None
        countdown_terminal(durasi, kegiatan, motivasi)
        # Setelah sesi selesai, tandai sebagai selesai ✅
        list_sesi[i] = (kegiatan, mulai, selesai_waktu, True)
        # Cetak ulang tabel dengan ceklis terupdate
        os.system('cls')
        table = Table(
            title=f"📚 Hari {hari} - Progress Belajar {nama} untuk {matkul} 📚",
            title_style="bold white on #6B4226",
            box=box.DOUBLE,
            show_lines=True,
            border_style="white"
        )
        table.add_column("Kegiatan", header_style="warna", justify="left", no_wrap=True)
        table.add_column("Waktu", header_style="warna", justify="center")
        table.add_column("Ceklis", header_style="warna", justify="center")
        for k, mulai, selesai_waktu, s in list_sesi:
            waktu_format = f"{mulai.strftime('%H:%M')} - {selesai_waktu.strftime('%H:%M')}"
            table.add_row(k, waktu_format, "✅" if s else "☐", style="warna")
        console.print(table)
        input("\nTekan Enter untuk melanjutkan ke sesi berikutnya...")
