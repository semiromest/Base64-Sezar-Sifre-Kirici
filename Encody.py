# -*- encoding: utf-8 -*-
import base64
from caesarcipher import CaesarCipher

print("############################    BASE 64        ##############################" + "\n" +
      "############################    SEZAR          ##############################" + "\n" +
      "############################    ŞİFRELEYİCİ    ##############################" + "\n" +
      "############################    ŞİFRE ÇÖZÜCÜ   ##############################" + "\n" +
      "############################    by semiromest  ##############################" + "\n" +
      "############################    Lib3rty0rD3ath ##############################")
print("[1] Base64 Şifre Çözücü Ve Şifreleyici" + "\n" + "[2] Sezar Şifre Çözücü Ve Şifreleyici")
secenek_1 = int(input("## Lütfen Yapmak İstediğiniz İşlemi Seçiniz ## "))
if secenek_1 == 1 :
   print("[1] Metin Şifreleme" + "\n" + "[2] Şifre Çözücü ")
   secenek = int(input("## Lütfen Yapmak İstediğiniz İşlemi Seçiniz ## "))

   if secenek == 1:
      metin = input("Şifrelemek İstediğiniz Metni Giriniz :  ").encode('utf-8')
      encoded = base64.b64encode(metin)
      print("Şifrelenmiş Metin : " + encoded.decode('utf-8'))
   elif secenek == 2:
      hash =  input("Şifrelenmiş Metini Giriniz :  ")
      decoded = base64.b64decode(hash).decode('utf-8')
      print("Şifre Çözüldü : "+ decoded)
   else :
      print("Hata! Lütfen Seçeneklerden Birini Giriniz :  ")
elif secenek_1 == 2 :
   print("[1] Metin Şifreleme" + "\n" + "[2] Şifre Çözücü " + "[3] Brute Force ile Şifre Çözücü")
   secenek = int(input("Lütfen Yapmak İstediğiniz İşlemi Seçiniz :  "))
   if secenek == 1:
      metin = input("Şifrelemek İstediğiniz Metni Giriniz :  ")
      harf_sayı = int(input("Atlanan Harf Sayısını Giriniz :  "))
      cipher = CaesarCipher(metin,offset=harf_sayı)
      print(cipher.encoded)
   elif secenek == 2:
      hash = input("Şifrelenmiş Metini Giriniz :  ")
      harf_sayı = int(input("Atlanan Harf Sayısını Giriniz :  "))
      cipher = CaesarCipher(hash,offset=harf_sayı)
      print(cipher.decoded)
   elif secenek == 3:
      hash = input("Şifrelenmiş Metini Giriniz :  ")
      for i in range(26):
         cipher = CaesarCipher(hash, offset=i)
         print(str(i) + ":" + cipher.decoded)
   else :
      print("Hatalı Seçim")
