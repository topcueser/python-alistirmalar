print("""
***********************************************************************
Floyd üçgeni, her satırda satır değeri kadar ardışık sayma sayılarının
sola yaslı sırasıyla dizilmesi sayesinde oluşan bir dik üçgendir.
***********************************************************************
""")


satir_sayisi = int(input("Satır sayısını giriniz : "))

s = 1

for satir in range(1,(satir_sayisi + 1)):
    for j in range(satir):
        print(s,end="\t")
        s += 1
    print("\n")