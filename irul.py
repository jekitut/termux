# -*- coding: utf-8 -*-
from warna import *


def jekitut():
	koneksi()
	system ("clear")
	print u +"╔══╗"
	print u +"║"+ n +"No"+ u +"║"+ b +" Menu Yang Tersedia :"
	print u +"║  ║"
	print u +"║"+ n +"00"+ u +"║"+ n +" Update"
	print u +"║"+ c +"01"+ u +"║"+ c +" Spam"
	print u +"║"+ k +"99"+ u +"║"+ k +" Keluar"
	print u +"╚══╝\n"
	irul = raw_input (n +"›"+ h +"›"+ k +"›"+ m +"›"+ b +" Pilih Nomor "+ n +": ")
	if irul == "00" or irul == "0":
		update()
	elif irul == "01" or irul == "1":
		spam()
	elif irul == "99":
		system ("clear")
		system ("pwd")
		system ("exit")
	else:
		salah()
		jekitut()


def update():
	system ("clear")
	print u +"╔══╗"
	print u +"║"+ n +"No"+ u +"║"+ b +" Menu Yang Tersedia :"
	print u +"║  ║"
	print u +"║"+ n +"00"+ u +"║"+ n +" Update Script"
	print u +"║"+ c +"01"+ u +"║"+ c +" Update Package Management"
	print u +"║"+ k +"99"+ u +"║"+ k +" Keluar"
	print u +"╚══╝\n"
	irul = raw_input (n +"›"+ h +"›"+ k +"›"+ m +"›"+ b +" Pilih Nomor "+ n +": ")
	if irul == "01" or irul == "1":
		system ("termux-vibrate")
		system ("clear")
		system ("rm -rf /data/data/com.termux/files/home/irul")
		chdir ("/data/data/com.termux/files/home")
		system ("git clone https://github.com/jekitut/termux")
		chdir ("/data/data/com.termux/files/home/irul")
		system ("rm -rf /data/data/com.termux/files/home/.termux")
		system ("rm -rf /data/data/com.termux/files/usr/etc/bash.bashrc")
		move ("/data/data/com.termux/files/home/irul/bash.bashrc", "/data/data/com.termux/files/usr/etc/bash.bashrc")
		move ("/data/data/com.termux/files/home/irul/.termux", "/data/data/com.termux/files/home/.termux")
		system ("termux-reload-settings")
		system ("termux-vibrate")
		system ("python2 irul.py")
	elif irul == "02" or irul == "2":
		system ("sh update")
		jekitut()
	elif irul == "99":
		jekitut()
	else:
		salah()
		update()


def spam():
	system ("clear")
	print u +"╔══╗"
	print u +"║"+ n +"No"+ u +"║"+ b +" Menu Yang Tersedia :"
	print u +"║  ║"
	print u +"║"+ h +"01"+ u +"║"+ c +" Kode OTP"
	print u +"║"+ n +"99"+ u +"║"+ n +" Kembali"
	print u +"╚══╝\n"
	irul = raw_input (n +"›"+ h +"›"+ k +"›"+ m +"›"+ b +" Pilih Nomor "+ n +": ")
	if irul == "01" or irul == "1":
		chdir ("spam")
		system ("clear")
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