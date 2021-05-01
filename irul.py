# -*- coding: utf-8 -*-
from warna import *


def jekitut():
	print u +"╔══╗"
	print u +"║"+ n +"No"+ u +"║"+ b +" Menu Yang Tersedia :"
	print u +"║  ║"
	print u +"║"+ n +"00"+ u +"║"+ n +" Pembaruan"
	print u +"║"+ c +"01"+ u +"║"+ c +" Bot"
	print u +"║"+ m +"02"+ u +"║"+ m +" Download Musik Di Spotify"
	print u +"║"+ h +"03"+ u +"║"+ h +" Facebook"
	print u +"║"+ k +"04"+ u +"║"+ k +" Hack Kamera"
	print u +"║"+ p +"05"+ u +"║"+ p +" Live Streaming Cctv"
	print u +"║"+ b +"06"+ u +"║"+ b +" Nomor NIK Dan Nomor KK"
	print u +"║"+ n +"07"+ u +"║"+ n +" Sms Gratis"
	print u +"║"+ c +"08"+ u +"║"+ c +" Spam"
	print u +"║"+ m +"09"+ u +"║"+ m +" Streaming Musik Di Youtube"
	print u +"║"+ h +"10"+ u +"║"+ h +" Beli Pulsa, Paket Data, Dll"
	print u +"║"+ k +"99"+ u +"║"+ k +" Keluar"
	print u +"╚══╝\n"
	irul = raw_input (n +"›"+ h +"›"+ k +"›"+ m +"›"+ b +" Pilih Nomor "+ n +": ")
	if irul == "00" or irul == "0":
		pembaruan()
	elif irul == "01" or irul == "1":
		bot()
	elif irul == "02" or irul == "2":
		spotify()
	elif irul == "03" or irul == "3":
		chdir ("facebook")
		system ("python2 irul.py")
	elif irul == "04" or irul == "4":
		hack_kamera()
	elif irul == "05" or irul == "5":
		cctv()
	elif irul == "06" or irul == "6":
		system ("php n")
		enter()
		system ("xdg-open https://nabila-tools.000webhostapp.com/e-ktp.php")
		menu()
	elif irul == "07" or irul == "7":
		system ("python sg.py")
		enter()
		menu()
	elif irul == "08" or irul == "8":
		spam()
	elif irul == "09" or irul == "9":
		youtube()
	elif irul == "10" or irul == "10":
		system ("xdg-open https://rebrand.ly/daftar-produk")
		menu()
	elif irul == "99" or irul == "99":
		system ("clear")
		system ("pwd")
		system ("exit")
	else:
		salah()
		menu()


def pembaruan():
	system ("clear")
	print u +"                    ╔═══════════╗"
	print u +"                    ║"+ k +" Pembaruan "+ u +"║"
	print u +"                    ╚═══════════╝\n"
	print u +"╔══╗"
	print u +"║"+ n +"No"+ u +"║"+ b +" Menu Yang Tersedia :"
	print u +"║  ║"
	print u +"║"+ h +"01"+ u +"║"+ h +" Memperbarui Data-Data Script"
	print u +"║"+ k +"02"+ u +"║"+ k +" Memperbarui Data-Data Termux"
	print u +"║"+ n +"09"+ u +"║"+ n +" Kembali"
	print u +"╚══╝\n"
	irul = raw_input (n +"›"+ h +"›"+ k +"›"+ m +"›"+ b +" Pilih Nomor "+ n +": ")
	if irul == "01" or irul == "1":
		system ("termux-setup-storage")
		system ("termux-vibrate")
		system ("xdg-open https://api.whatsapp.com/send?phone=6285856232526&text=Ahmad%20Khoirul%20Marzuqin")
		system ("xdg-open https://www.facebook.com/ahmadkhoirulmarzuqin")
		system ("xdg-open https://m.me/ahmadkhoirulmarzuqin")
		system ("xdg-open https://www.instagram.com/ahmad_khoirul_marzuqin")
		system ("clear")
		system ("rm -rf /data/data/com.termux/files/home/irul")
		chdir ("/data/data/com.termux/files/home")
		system ("git clone https://github.com/jekitut/irul")
		chdir ("/data/data/com.termux/files/home/irul")
		system ("unzip /data/data/com.termux/files/home/irul/irul.zip")
		system ("rm -rf /data/data/com.termux/files/home/irul/irul.zip")
		system ("rm -rf /data/data/com.termux/files/home/irul/update")
		system ("rm -rf /data/data/com.termux/files/home/storage/shared/Spotify.txt")
		system ("rm -rf /data/data/com.termux/files/home/.termux")
		system ("rm -rf /data/data/com.termux/files/usr/etc/bash.bashrc")
		move ("/data/data/com.termux/files/home/irul/bash.bashrc", "/data/data/com.termux/files/usr/etc/bash.bashrc")
		move ("/data/data/com.termux/files/home/irul/.termux", "/data/data/com.termux/files/home/.termux")
		move ("/data/data/com.termux/files/home/irul/Spotify.txt", "/data/data/com.termux/files/home/storage/shared/Spotify.txt")
		system ("termux-reload-settings")
		system ("python2 irul.py")
	elif irul == "02" or irul == "2":
		system ("sh update_termux")
		menu()
	elif irul == "09" or irul == "9":
		menu()
	else:
		salah()
		pembaruan()


def bot():
	system ("clear")
	chdir ("bot")
	print u +"                       ╔═════╗"
	print u +"                       ║"+ k +" Bot "+ u +"║"
	print u +"                       ╚═════╝\n"
	print u +"╔══╗"
	print u +"║"+ n +"No"+ u +"║"+ b +" Menu Yang Tersedia :"
	print u +"║  ║"
	print u +"║"+ h +"01"+ u +"║"+ h +" Baca Plus"
	print u +"║"+ k +"02"+ u +"║"+ k +" Caping"
	print u +"║"+ h +"03"+ u +"║"+ h +" Ceki Ceki"
	print u +"║"+ b +"04"+ u +"║"+ b +" Rishort"
	print u +"║"+ k +"05"+ u +"║"+ k +" Yodo"
	print u +"║"+ n +"09"+ u +"║"+ n +" Kembali"
	print u +"╚══╝\n"
	irul = raw_input (n +"›"+ h +"›"+ k +"›"+ m +"›"+ b +" Pilih Nomor "+ n +": ")
	if irul == "01" or irul == "1":
		system ("php bb")
		enter()
		chdir ("..")
		bot()
	elif irul == "02" or irul == "2":
		chdir ("caping")
		system ("php bot_caping")
		enter()
		chdir ("../..")
		bot()
	elif irul == "03" or irul == "3":
		system ("php bc")
		enter()
		chdir ("..")
		bot()
	elif irul == "04" or irul == "4":
		system ("php ddbr")
		enter()
		chdir ("..")
		bot()
	elif irul == "05" or irul == "5":
		chdir ("yodo")
		system ("php bot_yodo")
		enter()
		chdir ("../..")
		bot()
	elif irul == "09" or irul == "9":
		chdir ("..")
		menu()
	else:
		salah()
		chdir ("..")
		bot()


def spotify():
	def logo():
		system ("clear")
		print u +"            ╔═══════════════════════════╗"
		print u +"            ║"+ k +" Download Musik Di Spotify "+ u +"║"
		print u +"            ╚═══════════════════════════╝\n"
	logo()
	print n +"Pastikan Anda Sudah Mengisi Url Di"
	print n +"Memori Internal Dengan Nama "+ h + tebal +"Spotify.txt\n"+ n
	raw_input ( h +"Tekan Tombol Enter Untuk Melanjutkan ")
	logo()
	chdir ("/data/data/com.termux/files/home/storage/shared")
	system ("spotdl -l Spotify.txt -f Spotify")
	logo()
	chdir ("/data/data/com.termux/files/home/irul")
	print h +"✓"+ n +" Berhasil Mendownload Musik Ke"
	print n +"  Memori Internal Dengan Nama "+ h + tebal +"Spotify"+ n
	enter()
	menu()


def hack_kamera():
	system ("clear")
	print u +"                   ╔═════════════╗"
	print u +"                   ║"+ k +" Hack Kamera "+ u +"║"
	print u +"                   ╚═════════════╝\n"
	print n +"Apakah Anda Ingin Mengganti Template Html"
	print h +"Tidak (Tekan Tombol Enter)"+ n +" Atau"
	data = raw_input (m +"Ya (Ketik Ya)"+ n +" : "+ b)
	if data == "Ya" or data == "ya" or data == "YA":
		try:
			open ("/data/data/com.termux/files/home/storage/shared/irul.html", "r")
			system ("rm -rf /data/data/com.termux/files/home/irul/hack_kamera/irul.html")
			copy ("/data/data/com.termux/files/home/storage/shared/irul.html", "/data/data/com.termux/files/home/irul/hack_kamera")
			system ("clear")
			print h +"✓"+ n +" Berhasil Mengganti Template Html"
			enter()
			hack_kamera()
		except IOError:
			system ("clear")
			print m +"!!! Template Html Tidak Ditemukan !!!"
			print n +"Pastikan File Ada Di Memori"
			print n +"Internal Dengan Nama "+ h + tebal +"irul.html"+ n
			enter()
			hack_kamera()
	else:
		chdir ("hack_kamera")
		system ("bash irul.sh")
		chdir ("..")
		menu()


def cctv():
	system ("clear")
	print u +"               ╔═════════════════════╗"
	print u +"               ║"+ k +" Live Streaming Cctv "+ u +"║"
	print u +"               ╚═════════════════════╝\n"
	print u +"╔══╗"
	print u +"║"+ n +"No"+ u +"║"+ b +" Menu Yang Tersedia :"
	print u +"║  ║"
	print u +"║"+ n +"01"+ u +"║"+ n +" Di Dunia"
	print u +"║"+ h +"02"+ u +"║"+ h +" Gerbang Tol Purwodadi"
	print u +"║"+ k +"03"+ u +"║"+ k +" Tol Mapan KM 71+700"
	print u +"║"+ n +"09"+ u +"║"+ n +" Kembali"
	print u +"╚══╝\n"
	livecctv = raw_input (n +"›"+ h +"›"+ k +"›"+ m +"›"+ b +" Pilih Nomor "+ n +": ")
	if livecctv == "01" or livecctv == "1":
		system ("xdg-open http://www.insecam.org")
		cctv()
	elif livecctv == "02" or livecctv == "2":
		system ("xdg-open https://s.id/7PPcN")
		cctv()
	elif livecctv == "03" or livecctv == "3":
		system ("xdg-open https://s.id/7PP9K")
		cctv()
	elif livecctv == "09" or livecctv == "9":
		menu()
	else:
		salah()
		cctv()


def spam():
	system ("clear")
	print u +"                      ╔══════╗"
	print u +"                      ║"+ k +" Spam "+ u +"║"
	print u +"                      ╚══════╝\n"
	print u +"╔══╗"
	print u +"║"+ n +"No"+ u +"║"+ b +" Menu Yang Tersedia :"
	print u +"║  ║"
	print u +"║"+ h +"01"+ u +"║"+ c +" Email "+ h +"02" 
	print u +"║"+ k +"02"+ u +"║"+ c +" Kode OTP "+ k +"29"
	print u +"║"+ p +"03"+ u +"║"+ c +" Kode OTP "+ p +"King Tools"
	print u +"║"+ p +"04"+ u +"║"+ c +" Kode OTP "+ p +"Master Kadal"
	print u +"║"+ p +"05"+ u +"║"+ c +" Kode OTP "+ p +"REV-ZONE.NET"
	print u +"║"+ n +"09"+ u +"║"+ n +" Kembali"
	print u +"╚══╝\n"
	irul = raw_input (n +"›"+ h +"›"+ k +"›"+ m +"›"+ b +" Pilih Nomor "+ n +": ")
	if irul == "01" or irul == "1":
		chdir ("spam")
		def logo():
			system ("clear")
			print u +"               ╔═══════════════════╗"
			print u +"               ║"+ k +" Jumlah Email "+ n +":"+ h +" 02 "+ u +"║"
			print u +"               ╚═══════════════════╝\n"
		def start():
			try:
				logo()
				jl = json.load (open ("e-mail.json"))
				print k +"Email Tujuan"+ n +" : "+ h + jl["email"]
				print h +"Jumlah Pesan"+ n +" : "+ k + jl["jumlah"]
				print p +"Jeda Pesan"+ n +"   : "+ b + jl["jeda"]
				bs()
			except IOError:
				logo()
				email = raw_input (k +"Email Tujuan"+ n +" : "+ h)
				jumlah = raw_input (h +"Jumlah Pesan"+ n +" : "+ k)
				jeda = raw_input (p +"Jeda Pesan  "+ n +" : "+ b)
				json.dump ({"email": email, "jumlah": jumlah, "jeda": jeda}, open ("e-mail.json", "w"))
				bs()
		def bs():
			print n +"\nApakah Data-Data Di Atas Sudah"
			print h +"Benar (Tekan Tombol Enter)"+ n +" Atau"
			data = raw_input (m +"Salah (Ketik Salah)"+ n +" : "+ b)
			print ""
			if data == "Salah" or data == "salah" or data == "SALAH":
				system ("rm -rf e-mail.json")
				start()
			else:
				system ("python2 e-mail.py")
				chdir ("..")
				spam()
		start()
	elif irul == "02" or irul == "2":
		chdir ("spam")
		def logo():
			system ("clear")
			print u +"              ╔══════════════════════╗"
			print u +"              ║"+ k +" Jumlah Kode OTP "+ n +":"+ h +" 29 "+ u +"║"
			print u +"              ╚══════════════════════╝\n"
		def start():
			try:
				logo()
				jl = json.load (open ("nomor.json"))
				print k +"Nomor Tujuan"+ n +" : "+ h + jl["nomor"]
				print h +"Jumlah Pesan"+ n +" : "+ k + jl["jumlah"]
				print p +"Jeda Pesan"+ n +"   : "+ b + jl["jeda"]
				bs()
			except IOError:
				logo()
				nomor = raw_input (k +"Nomor Tujuan"+ n +" : "+ h)
				jumlah = raw_input (h +"Jumlah Pesan"+ n +" : "+ k)
				jeda = raw_input (p +"Jeda Pesan  "+ n +" : "+ b)
				json.dump ({"nomor": nomor, "jumlah": jumlah, "jeda": jeda}, open ("nomor.json", "w"))
				json.dump ([{"nomor": nomor, "jumlah": jumlah, "jeda": jeda}], open ("nomor.php", "w"))
				bs()
		def bs():
			print n +"\nApakah Data-Data Di Atas Sudah"
			print h +"Benar (Tekan Tombol Enter)"+ n +" Atau"
			data = raw_input (m +"Salah (Ketik Salah)"+ n +" : "+ b)
			print ""
			if data == "Salah" or data == "salah" or data == "SALAH":
				system ("rm -rf nomor.json")
				start()
			else:
				system ("python2 kode_otp.py")
				chdir ("..")
				spam()
		start()
	elif irul == "03" or irul == "3":
		system ("xdg-open http://kingtools.id")
		spam()
	elif irul == "04" or irul == "4":
		system ("xdg-open https://masterkadal.com/tools/tokotalk")
		spam()
	elif irul == "05" or irul == "5":
		system ("xdg-open https://www.rev-zone.net")
		spam()
	elif irul == "09" or irul == "9":
		menu()
	else:
		salah()
		spam()


def youtube():
	irul_youtube = raw_input (u +"\n›"+ k +" Judul Lagu "+ n +": "+ h)
	system ("termux-tts-speak "+ irul_youtube)
	system ("mpsyt /"+ irul_youtube)
	menu()


# Ahmad Khoirul Marzuqin


def menu():
	system ("clear")
	hari = ("Senin", "Selasa", "Rabu", "Kamis", "Jum'at", "Sabtu", "Minggu")
	tanggal = ("01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31")
	bulan = ("Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember")
	jam = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23")
	menit = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59")
	emit = time.localtime(time.time())
	print h +"Sekarang"+ n +"     : "+ str(hari[emit[6]]) +", "+ str(tanggal[emit[2]-1]) +" "+ str(bulan[emit[1]-1]) +" "+ str(emit[0]) + u +" ║ "+ n + str(jam[emit[3]]) +":"+ str(menit[emit[4]]) +":"+ str(menit[emit[5]])
	update()


def update():
	try:
		rg = get ("https://raw.githubusercontent.com/jekitut/irul/master/update").text
		exec rg
		print u + 53 * "═"+ m +"\nNama Pembuat"+ n +" : "+ c + miring + tebal +"Ahmad Khoirul Marzuqin\n"+ n
		jekitut()
	except ConnectionError:
		koneksi()
		update()


menu()