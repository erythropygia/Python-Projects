# -*- coding: utf-8 -*-
ogrenciler={"ahmet":"100", "ayşe":"105", "kemal":"203"}
kayit_sorgu=""

while(kayit_sorgu != "H" or kayit_sorgu != "h"):
    kayit_sorgu=input("Yeni Ogrenci Kaydi İstiyor Musunuz[E/H]:")
    if(kayit_sorgu=="E" or kayit_sorgu=="e"):
        kayit_isim=input("Ogrenci Ismi Giriniz:")
        kayit_no=input("Ogreneci Numarasi Giriniz:")
        ogrenciler[kayit_isim]=kayit_no
        
    else:
        break

print("Liste Yaziliyor\n")
print(ogrenciler)
        






