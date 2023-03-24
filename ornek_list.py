#verilen listedeki minimum elemanı döndürür
def minimum_deger(liste):
    #listedeki minimum sayıyı bulmayı dener
    try: 
        gecici_liste= liste.copy()
        minimum= min(gecici_liste)
        return minimum
    #ValueError hatasını ele alır
    except ValueError:
        print("uygunsuz veri formatı")

#listedeki maximum değeri verir        
def maximum_deger(liste):
    try:
        gecici_liste= liste.copy()
        maximum= max(gecici_liste)
        return maximum
    except ValueError:
        print("uygunsuz veri formatı")

#listeyi tersine çevirir        
def tersine_cevir(liste):
    gecici_liste= liste.copy()
    gecici_liste.reverse()
    return gecici_liste

#listeyi sıralar
def sirala(liste):
    gecici_liste= liste.copy()
    gecici_liste.sort()
    return gecici_liste

#listede hangi elemandan kaç tane olduğunu verir
def eleman_sayisi(liste):
    #listedeki unique elemanlar bu listede toplanacak
    unique_liste= []
    for eleman in liste:
        if eleman not in unique_liste:
            unique_liste.append(eleman)
    #her elemanın değerini ve listede kaç kere tekrar ettiği 
    #bilgisini saklayacak sözlük 
    eleman_sayilari= {}        
    for eleman in unique_liste:
        sayi = liste.count(eleman)
        #sözlükte eleman değerine karşılık gelen sayı değeri ataması yapılır
        eleman_sayilari[eleman] = sayi
    return eleman_sayilari

#örnek liste
a = [10, 20, 30, 40, 15, 25, 75, 5, 10, 40, 20, 10]

minimum = minimum_deger(a)   
maximum = maximum_deger(a)
ters = tersine_cevir(a)
sira = sirala(a)
elemans = eleman_sayisi(a)

print("Orijinal Liste: ", a)
print("Minimum Değer: ", minimum)
print("Maximum Değer: ", maximum)
print("Listenin Tersi: ", ters)
print("Sıralı Liste: ", sira)
print("Eleman Frekansı: ", elemans)





    
     
                         
        
    

