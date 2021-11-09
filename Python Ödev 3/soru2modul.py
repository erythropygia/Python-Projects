def kontrol(giris, ara):
    sayac=0
    uzunluk=int(len(giris))
    giris1=giris.lower()
    ara1=ara.lower()
    for i in range (uzunluk):
        if(giris1[i]==ara1[0]):
            sayac=sayac+1
    if(sayac!=0): 
        print("Aranan " + str(ara[0]) + " Harfi Girilen " + str(giris) + " Kelimesinde " + str(sayac) + " Kez Tekrar Etmektedir" )
    else:
        print("Aranan " + str(ara[0]) + " Harfi Girilen " + str(giris) + " Kelimesinde " + "Bulunmamaktadır" )


    
    

