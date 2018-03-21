# coding=utf-8

"""
        Tv kanalları yayın akışı
"""
import time
import requests

from bs4 import BeautifulSoup

Kanal_d = "http://www.tvyayinakisi.com/kanal-d-tv"
Fox = "http://www.tvyayinakisi.com/fox"
Show = "http://www.tvyayinakisi.com/show-tv"
Star = "http://www.tvyayinakisi.com/star-tv"
Atv = "http://www.tvyayinakisi.com/atv"
Trt_1 = "http://www.tvyayinakisi.com/trt-1"
Tv8 = "http://www.tvyayinakisi.com/tv-8"
Kanal_7 = "http://www.tvyayinakisi.com/kanal-7"


def kanal(soup, kanal_adi):
    print("Yükleniyor... Lütfen bekleyiniz.\n")
    time.sleep(3)

    tarih = soup.find("span", {"class": "date"}).text # tek bir tane oldugu icin find kullandik
    kanal = soup.find("div",  {"class": "seven columns"}).find("h1").text

    # strip() ile bosluklar varsa silinir daha guzel goruntu icin
    kanal = kanal.strip();
    tarih = tarih.strip();

    print("*" * len(kanal)*2 + "\n")
    print(kanal + "\n")
    print(tarih + "\n")
    print("*" * len(kanal)*2 + "\n")

    saatler  = soup.find_all("div", {"class": "two columns time"})
    yayinlar = soup.find_all("div", {"class": "ten columns"})

    for saat,yayin in zip(saatler,yayinlar):
        print(saat.text.strip(),yayin.text.strip())

    time.sleep(5)
    s = int(input("\nDiğer kanalları da görmek istiyor musunuz?(Evet: 1, Hayır: -1)"))
    if s == 1:
        main()
    else:
        print("Güle güle :)")
        time.sleep(2)

def main():
    print(
        """
                1 - Kanal D
                2 - Fox Tv
                3 - Show Tv
                4 - Star
                5 - Atv
                6 - Trt 1
                7 - Tv8
                8 - Kanal 7
            """)
    time.sleep(1)

    secim = int(input("\nkanal seçiniz: "))

    if secim == 1:
        soup_kanald = BeautifulSoup(requests.get(Kanal_d).content,"html.parser")
        kanal(soup_kanald, "Kanal D")
    elif secim == 2:
        soup_fox = BeautifulSoup(requests.get(Fox).content, "html.parser")
        kanal(soup_fox, "Fox Tv")
    elif secim == 3:
        soup_show = BeautifulSoup(requests.get(Show).content, "html.parser")
        kanal(soup_show, "Show Tv")
    elif secim == 4:
        soup_star = BeautifulSoup(requests.get(Star).content, "html.parser")
        kanal(soup_star, "Star Tv")
    elif secim == 5:
        soup_atv = BeautifulSoup(requests.get(Atv).content, "html.parser")
        kanal(soup_atv, "Atv")
    elif secim == 6:
        soup_trt1 = BeautifulSoup(requests.get(Trt_1).content, "html.parser")
        kanal(soup_trt1, "Trt 1")
    elif secim == 7:
        soup_tv8 = BeautifulSoup(requests.get(Tv8).content, "html.parser")
        kanal(soup_tv8, "Tv8")
    elif secim == 8:
        soup_kanal7 = BeautifulSoup(requests.get(Kanal_7).content, "html.parser")
        kanal(soup_kanal7, "Kanal 7")
    else:
        print("kanal seçmediniz :(")
        time.sleep(2)
        main()


if __name__ == '__main__':
    main()