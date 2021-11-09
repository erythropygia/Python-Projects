
denklem=input("Lutfen Denkleminizi Giriniz:")
sayi=int(len(denklem))
sayac=0
sayac1=0
temp=0
for i in range (sayi):
    if(denklem[i]=="("):
        sayac=sayac+1
    if(denklem[i]==")"):
        sayac1=sayac1+1

if(sayac==sayac1):
    print("Parantez Hatası Yok")
    
else:
    print( str(abs(sayac-sayac1)) + " Tane Parantez Hatası Var")
        
            
        


