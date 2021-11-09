def topla(liste):
    toplam=0
    for i in liste:
        toplam=toplam+i
    return toplam

def carp(liste):
    carpim=1
    for i in liste:
        carpim=carpim*i
    return carpim

def enbuyuk(liste):
    temp=0
    for i in range(len(liste)):
        for j in range(len(liste)):
            if(liste[i]<liste[j]):
                temp=liste[i]
                liste[i]=liste[j]
                liste[j]=temp
    return liste[len(liste)-1]

def enkucuk(liste):
     temp=0
     for i in range(len(liste)):
        for j in range(len(liste)):
            if(liste[i]<liste[j]):
                temp=liste[i]
                liste[i]=liste[j]
                liste[j]=temp
     return liste[0]
    
def ortalama(liste):
    toplam=0
    for i in liste:
        toplam=toplam+i
    return toplam/len(liste)

def elemanara(liste,aranan):
    temp=0
    for i in range(len(liste)):
        if(liste[i]==aranan):
            temp=temp+1
    return temp

def eseleman(liste):
    list1 = []
    for i in liste:
        if i not in list1:
            list1.append(i)
    return list1
    
            

def sort(liste):
    for i in range(len(liste)):
        for j in range(len(liste)):
            if(liste[i]<liste[j]):
                temp=liste[i]
                liste[i]=liste[j]
                liste[j]=temp
    return liste
    
    
            
            