
giris = ""
liste = []


while(1):  
    giris = input("")
    if giris.lower() !="quit":
        liste.append(giris)
    else:
        break
    
print("")
for i in range(len(liste)):
    print(liste[len(liste)-i-1])
    