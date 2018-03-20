import random
import time

print("""
***********************************************************************
Sayı Tahmin Oyunu

1 ile 40 arasında sayıyı tahmin edin.
***********************************************************************
""")

rastgele_sayi = random.randint(1,40)
tahmin_hakki = 7

while True:

    tahmin = int(input("Tahmininiz: "))

    if (tahmin < rastgele_sayi):
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)
        print("Daha yüksek bir sayı giriniz :)")
        tahmin_hakki -= 1
    elif (tahmin > rastgele_sayi):
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)
        print("Daha küçük bir sayı giriniz :)")
        tahmin_hakki -= 1
    else:
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)
        print("Tebrikler! Sayımız: ",rastgele_sayi)
        break
    if (tahmin_hakki == 0):
        print("Tahmin hakkınız bitmiştir.")
        print("Sayımız: ",rastgele_sayi)
        break