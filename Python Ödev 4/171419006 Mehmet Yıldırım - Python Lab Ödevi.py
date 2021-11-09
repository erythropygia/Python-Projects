import sys


def sirala(okunan,max_deger,sayac,i):

    if (int(okunan[i])>max_deger):
        okunan[i]=str(max_deger)
        sayac+=1
    i+=1
    if (i >= len(okunan)):
        print("Listedeki Toplam Değiştirilen Sayı:"+str(sayac))
        print("Yeni Liste Yazdırılıyor:")
        for s in range(0,len(okunan)):
            print(int(okunan[s]))
        return None
    sirala(okunan,max_deger,sayac,i)
        
        
print("Text Dosyasındaki Sayılar Alt Alta Sıralı Olmalı")
text_dosyasi = input("Text Dosyasinin adini giriniz(.txt ile):")
try:
    file = open(text_dosyasi)
except:
    print("Girilen txt Dosyası Bulunamadı")
    sys.exit()

okunan = file.readlines()
print("Text'deki Toplam Sayi:"+str(len(okunan)))
print("Text'deki Veriler Yazdırılıyor.")

for i in range(0,len(okunan)):
    print(int(okunan[i]))
    
file.close()

try:
    max_deger=int(input("Maksimum Değeri Giriniz:"))
except:
    print("Lütfen Tam Sayi Giriniz")
    sys.exit()
sayac=0
i=0
sirala(okunan,max_deger,sayac,i)



    
    
    