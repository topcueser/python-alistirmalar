print("""
***********************************************************************
2 Basamaklı sayının okunuşu
***********************************************************************
""")

birler =  ["","Bir","İki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"]
onlar  =  ["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]

def okunus(sayi):
    birinci = sayi % 10  # sayinin 10 a bolumunden kalani verir
    ikinci  = sayi // 10 # sayinin 10 a bolunmesi
    return onlar[ikinci] + " " + birler[birinci]

sayi = int(input("Sayı: "))

print(okunus(sayi))