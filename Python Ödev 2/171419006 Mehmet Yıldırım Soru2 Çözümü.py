dongu = 1
menu ="Yazmak İçin Y , Çözmek İçin C Giriniz:"
while dongu == 1:
    print(menu)
    sorgu = input(" ")
    if(sorgu == ""):
        print("Lütfen Boş Bırakmayınız")
    elif(sorgu == "Y" or sorgu== "y"):
        gecici = []
        harfler = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        kelime = input("Lütfen Kelimeyi Küçük Harfle Giriniz:")
        sifresayisi = int(input("Şifre Anahtarı Giriniz:"))
        for harf in kelime:
            if(harf in harfler):  
                sira = harfler.index(harf)
                yeni = harfler[(sira+sifresayisi)%len(harfler)]
                gecici.append(yeni)
        print("Şifreleniyor:")
        print(*gecici)
            
    elif(sorgu == "C" or sorgu=="c"):
        gecici = []
        harfler = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        kelime = input("kelime:")
        sifresayisi = int(input("Şifre Anahtarı Giriniz:"))
        for harf in kelime:
            if(harf in harfler):  
                sira = harfler.index(harf)
                yeni = harfler[(sira-sifresayisi)%len(harfler)]
                gecici.append(yeni)
        print("Şifreniz Çözülüyor:")
        print(*gecici)
            
    giris_kontrol=input("Devam Etmek İstiyor Musunuz? [E/H]:")
    if(giris_kontrol == "H" or giris_kontrol == "h"):
        print("Çıkılıyor")
        dongu = 0
    elif():
        print("Hatalı Giriş Lütfen Tekrar Deneyiniz!")