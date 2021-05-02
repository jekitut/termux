# -*- coding: utf-8 -*-
from warna import *


def jekitut():
	koneksi()
	print u +"╔══╗"
	print u +"║"+ n +"No"+ u +"║"+ b +" Menu Yang Tersedia :"
	print u +"║  ║"
	print u +"║"+ n +"00"+ u +"║"+ n +" Update"
	print u +"║"+ c +"01"+ u +"║"+ c +" Spam"
	print u +"║"+ k +"99"+ u +"║"+ k +" Keluar"
	print u +"╚══╝\n"
	irul = raw_input (n +"›"+ h +"›"+ k +"›"+ m +"›"+ b +" Pilih Nomor "+ n +": ")
	if irul == "00" or irul == "0":
		system ("sh update")
	elif irul == "01" or irul == "1":
		spam()
	elif irul == "99":
		system ("clear")
		system ("pwd")
		system ("exit")
	else:
		salah()
		jekitut()


def spam():
	system ("clear")
	print u +"╔══╗"
	print u +"║"+ n +"No"+ u +"║"+ b +" Menu Yang Tersedia :"
	print u +"║  ║"
	print u +"║"+ h +"01"+ u +"║"+ c +" Kode OTP"
	print u +"║"+ n +"99"+ u +"║"+ n +" Kembali"
	print u +"╚══╝\n"
	irul = raw_input (n +"›"+ h +"›"+ k +"›"+ m +"›"+ b +" Pilih Nomor "+ n +": ")
	print ""
	if irul == "01" or irul == "1":
		chdir ("spam")
		def start():
			try:
				jl = json.load (open ("nomor.json"))
				print k +"Nomor Tujuan"+ n +" : "+ h + jl["nomor"]
				print h +"Jumlah Pesan"+ n +" : "+ k + jl["jumlah"]
				print p +"Jeda Pesan"+ n +"   : "+ b + jl["jeda"]
				bs()
			except IOError:
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
	elif irul == "99":
		jekitut()
	else:
		salah()
		spam()


jekitut()