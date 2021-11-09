import soru1modul
liste=[6,3,30,2,27,99,67,5,5,30,2,27]
print("Listeniz = " + str(liste))

print("Listedeki Elemanların Toplamı:" + str(soru1modul.topla(liste)))
print("Listedeki Elemanların Çarpımı:" + str(soru1modul.carp(liste)))
print("Listedeki En Büyük Eleman:" + str(soru1modul.enbuyuk(liste)))
print("Listedeki En Küçük Eleman:" + str(soru1modul.enkucuk(liste)))
print("Liste Ortalaması:" + str(soru1modul.ortalama(liste)))

giris=int(input("Lutfen Listede Aranacak Sayiyi Giriniz:"))
if(soru1modul.elemanara(liste,giris)!=0):
    print("Listede Aranan " + str(giris) + " Listede " + str(soru1modul.elemanara(liste,giris)) + " Kere Tekrar Etmektedir")
else:
    print("Listede Aranan " + str(giris) + " Listede Bulunmamaktadır")
    
print("Dizi Eşsiz Hale Getirildi (Aynı Elemanlar Çıkarıldı):" + str(soru1modul.eseleman(liste)))
    

print("Liste Sıralanıyor:" + str(soru1modul.sort(liste)))

