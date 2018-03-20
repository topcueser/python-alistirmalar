import requests

url = "https://api.fixer.io/latest?base="

#birinci = input("Elinizdeki para birimi : ")
#ikinci  = input("Çevirmek istediğiniz para birimi : ")
#miktar  = input("Tutar giriniz : ")

birinci = "USD"
ikinci  = "TRY"
miktar  = 100  # DOLAR olarak. Yani 100 DOLAR kaç TL ?

response = requests.get(url + birinci)

json_verisi = response.json()

ceviri_tutar = json_verisi['rates'][ikinci] * float(miktar)

print("\n" + birinci + " durumu : ",json_verisi['rates'][ikinci])

print("\n" + str(miktar) + " " + birinci + " --------> " + str(ceviri_tutar) + " " + ikinci)
