print("""
******************************
Mükemmel Sayı Kontrol Programı
******************************

Bir sayının kendisi hariç tüm pozitif bölenlerinin toplamı kendisine eşit ise bu sayıya Mükemmel Sayı denir.

""")
while True: # Bu sayede döngü tamamlandıkça tekrar girdi alıp yeni döngüleri başlatabiliriz.
    sayı = int(input("Sayı:"))

    if sayı <= 0:
        print("Sadece pozitif sayılar mükemmel sayı olabilir.")
        continue
    i = 1
    toplam = 0
    while (i < sayı):
        if (sayı % i == 0):
            toplam += i
        i += 1

    if (toplam == sayı):
        print(sayı, "mükemmel bir sayıdır.")
    else:
        print(sayı, "mükemmel bir sayı değildir.")

