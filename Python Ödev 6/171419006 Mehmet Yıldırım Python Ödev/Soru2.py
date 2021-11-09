# DİZİNİN EN KÜÇÜK 2. ELEMANINI EŞİTLİK ŞARTINA BAĞLI OLMADAN YAZDIRAN PROGRAM

import sys

liste=[]
ikinci_liste=[]
ucuncu_liste=[]
kucuk_1=0
kucuk_2=0


while(1):
    sayilar=input("")
    
    if str(sayilar).lower()=="quit":
        break
    else:
        liste.append(int(sayilar))
        
liste.sort()
kucuk_1=liste[0]
sayac=0

#Dizi 1 elemanlıysa boş liste döndürüyor
if(len(liste)==1):
        print("")
        print(ucuncu_liste)
        sys.exit()
        
#Dizinin tüm elemanları aynıysa boş liste döndürüyor
dizi_kontrol=liste[0]
counter=0
for sayi in liste:
    if dizi_kontrol == sayi:
        counter+=1

if counter == len(liste):
    print("")
    print(ucuncu_liste)
    sys.exit()


#Dizideki en küçük ikileri yazdırıyor ve diziye atıyor
i=0
while(1):
    if liste[i]!=kucuk_1:
        kucuk_2=liste[i]
        break
    i+=1
    
for kontrol in liste:
    if kontrol==kucuk_2:
        ikinci_liste.append(kontrol)

print("")     
print(ikinci_liste)
        






