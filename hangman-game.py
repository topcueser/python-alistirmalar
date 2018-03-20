import time

#oyuncu adı alınıyor.
name = input("Adınız : ")

print ("Merhaba, " + name, "Hangman oyununa hoşgeldin!")

#program bekliyor
time.sleep(1)

print ("Tahminlerinize başlayabilirsiniz...")
time.sleep(0.5)

#aranılan kelime
word = "secret"

#kullanıcının tahmin ettiği kelimeler
guesses = ''

#tahmin hakkımız
turns = 10

while turns > 0:

    bosluk = 0

    for char in word:  # stringler de liste olmadan da direk for ile donebilirsin
        if char in guesses:
            print(char,end=" ")
        else:
            print("___",end=" ")
            bosluk += 1

    if (bosluk == 0):
        print("Kazandınız...")
        break

    guess = input("\nKarakter tahmin ediniz : ")

    guesses += guess

    if (guess not in word): # belirtilen harfi direk string icinde arayabilirsin
        turns -= 1
        print("Hatalı seçim yaptınız. " + str(turns) + " hakkınız kaldı...")

    if (turns == 0):
        print("Kaybettiniz....")
