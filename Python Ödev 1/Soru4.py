toplam=0
carpim=1

giris=int(input("Bir Tam Sayi Giriniz:"))

while(1):
    if(giris<0):
        print("Programdan Cikiliyor")
        break
    else:
        strgiris=str(giris)
        basamak=len(strgiris)
        if basamak==1:
            print("Toplamsal Kalicilik 0'dir")
            print("Çarpımsal Kalıcılık 0'dir")
            print("Toplamali Kok:",giris)
            print("Çarpımsal Kök:",giris)
            giris=int(input("Bir Tam Sayi Giriniz:"))
            if(giris<0):
                print("Programdan Cikiliyor")
                break
        else:
            list=strgiris
            for i in range(len(list)):
                if(len(str(toplam))<2):
                    toplam+=int(list[i])
                    carpim*=int(list[i])         
            print("Toplamsal Kalicilik",toplam)
            print("Çarpımsal Kalicilik",carpim)
            toplam=0
            carpim=1
            giris=int(input("Bir Tam Sayi Giriniz:"))
            if(giris<0):
                 print("Programdan Cikiliyor")
                 break
                
                      
        
        
       
    
