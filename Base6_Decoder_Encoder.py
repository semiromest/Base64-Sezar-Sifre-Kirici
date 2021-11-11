# -*- encoding: utf-8 -*-
import base64

print("[1] Metin Şifreleme" + "\n" + "[2] Şifre Çözücü ")
secenek = int(input("Lütfen Yapmak İstediğiniz İşlemi Seçiniz"))

if secenek == 1:
   metin = input("Şifrelemek İstediğiniz Metni Giriniz").encode('utf-8')
   encoded = base64.b64encode(metin)
   print("Şifrelenmiş Metin : " + encoded.decode('utf-8'))


elif secenek == 2:
   hash =  input("Şifrelenmiş Metini Giriniz")
   decoded = base64.b64decode(hash).decode('utf-8')
   print("Şifre Çözüldü : "+ decoded)
