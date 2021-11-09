from collections import Counter 




def palindrom_olustur(string):
    print(string + " Kelimesinin Kombinasyonlarının Palindrom Olup Olmadığı Kontrol Ediliyor:")
    harfleri_al = [i for i in string.lower() if i.isalpha()]
    counts = Counter(harfleri_al)
    tek= sum(1 for letter, counter in counts.items() if counter%2)
    return string and tek <= 1


def palindrom_kontrol(string):
    print(string + " Kelimesinin Kendisinin Palindrom Olup Olmadığı Kontrol Ediliyor:")
    if len(string)<=1:
        return "string" and True
    else:
        return "string" and string[0]==string[-1] and palindrom_kontrol(string[1:-1])
    
    
def yaz(sayac,durum,uzunluk,string):
    
    harfleri_al = [i for i in string.lower() if i.isalpha()]
    counts = Counter(harfleri_al)
    tek= sum(1 for letter, counter in counts.items() if counter%2)
    palindrom = []
    
    for i in range (uzunluk):
        palindrom.append(" ")
    
    cift=0
    tek=0
    
    for i in kontrol:
        if cift == uzunluk:
            break
        if sayac[i]%2 == 0:
            palindrom[durum[i]]=i
            palindrom[(uzunluk -1) - durum[i]]=i
            durum[i]+=1
            cift+=2
        
        elif sayac[i]%2 == 1 and tek==0:
            palindrom[uzunluk//2]=i
            durum[i]=uzunluk//2
            tek+=1
            cift+=1
        
    string= ""
    for i in palindrom:
        string+=i

    return string

    

string=input("Lütfen İçerisinde Palindrom Aranacak Kelime veya Cümleyi Giriniz Kucuk Harfle Giriniz(EN AZ 5 HARF!):")
string.replace(" ","") 
kontrol=[]

for i in string:
    if i not in kontrol:
        kontrol.append(i)

sayac={}
durum={}
sayac1=0
uzunluk=5


for i in kontrol:
    sayac[i]=string.count(i)
    durum[i]=sayac1
    sayac1+=1



print(palindrom_kontrol(string))
print(palindrom_olustur(string))

print("Oluşturulabiliyorsa ilk 5 Harften Oluşturulan Palindrom:" + yaz(sayac,durum,uzunluk,string[0::5]))





