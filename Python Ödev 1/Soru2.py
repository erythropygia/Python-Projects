for i in range(0,50): 
    giris=input("Buyuk Harfli Metin veya Sayi Giriniz:")
    giris1=giris.upper()
 
    if giris1==giris1[::-1]:
        print("Polindromdur")
    else:
        print("Polindrom Degildir")