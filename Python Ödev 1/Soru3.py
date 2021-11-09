import random
dizi=[]
toplam=0
cift=0
for j in range(20):
    dizi.append(random.randint(1,100))
print('Random Liste: ',dizi)
for i in range(0,len(dizi)):
    toplam+=dizi[i]
ortalama=toplam/len(dizi)    
print('Dizi Ortalamasi : ',ortalama)
print("En Buyuk Sayi:", max(dizi))
print("En Kucuk Sayi:", min(dizi))
dizi.sort()
print("Listedeki 2. En Buyuk Sayi:", dizi[-2])
print("Listedeki 2. En Kucuk Sayi:", dizi[2])
for k in range(0,19):
    if (dizi[k]%2==0):
        cift=cift+1
print("Listedeki Cift Sayi Sayisi:",cift)