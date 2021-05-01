# -*- coding: utf-8 -*-
import getpass, hashlib, json, mechanize, random, re, smtplib, sys, threading, time
from mechanize import Browser, URLError
from multiprocessing.pool import ThreadPool
from os import chdir, mkdir, system
from requests import delete, get, post, Session
from requests.exceptions import ConnectionError
from shutil import copy, move
from time import sleep
from urllib import urlopen
reload (sys)
sys.setdefaultencoding ("UTF-8")


### Except
# EOFError = CTRL + D
# IOError = Open On File Not Found
# KeyError = Word On File Not Found
# KeyboardInterrupt = CTRL + C


berhasil = []
gagal = []


def hapus():
	del berhasil [:]
	del gagal [:]
	print ""


def enter():
	raw_input (n +"\n›"+ h +"›"+ k +"›"+ m +"›"+ b +" Tekan Tombol Enter "+ n)


def jalan(nalaj):
	for i in nalaj + "\n":
		sys.stdout.write (i)
		sys.stdout.flush ()
		sleep (0.01)


def koneksi():
	titik = ["    ", "•   ", "••  ", "••• "]
	for i in titik:
		print m + tebal +"\r!!! Aktifkan Koneksi Internet "+ n + i,
		sys.stdout.flush ()
		sleep (1)


def salah():
	system ("clear")
	jalan (m +"!!! Nomor Yang Anda Masukkan Salah !!!")
	system ("termux-tts-speak Nomor Yang Anda Masukkan Salah")
	jalan (m +"!!! Silahkan Hubungi Pembuat Script Ini !!!")
	system ("termux-tts-speak Silahkan Hubungi Pembuat Script Ini")










# Warna
n = "\033[0m" # Normal


# Teks
miring = "\033[3m" # Miring
gb = "\033[4m" # Garis Bawah
tebal = "\033[5m" # Tebal
gt = "\033[9m" # Garis Tengah


hitam = "\033[30m" # Hitam
c = "\033[90m" # Coklat
m = "\033[91m" # Merah
h = "\033[92m" # Hijau
k = "\033[93m" # Kuning
u = "\033[94m" # Ungu
p = "\033[95m" # Pink
b = "\033[96m" # Biru


# Latar Belakang
ba = "\033[100m" # Background Abu-Abu
bm = "\033[101m" # Background Merah
bh = "\033[102m" # Background Hijau
bk = "\033[103m" # Background Kuning
bu = "\033[104m" # Background Ungu
bp = "\033[105m" # Background Pink
bb = "\033[106m" # Background Biru
bputih = "\033[107m" # Background Putih


# Urutkan
u0 = n;   u8 = n;   ug = n;   uo = n;   uw = n
u1 = c;   u9 = c;   uh = c;   up = c;   ux = c
u2 = m;   ua = m;   ui = m;   uq = m;   uy = m
u3 = h;   ub = h;   uj = h;   ur = h;   uz = h
u4 = k;   uc = k;   uk = k;   us = k
u5 = u;   ud = u;   ul = u;   ut = u
u6 = p;   ue = p;   um = p;   uu = p
u7 = b;   uf = b;   un = b;   uv = b