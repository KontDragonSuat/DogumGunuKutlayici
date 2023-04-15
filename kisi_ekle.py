# -*- coding: utf-8 -*-

from time import sleep
bilgi = "Bilgileri yazarken hata yapmamaya dikkat edin. Aksi takdirde programda çökmelere yol açabilir"
nasil = "\nFormları doldururken tarihlerde sıfır (0) yazmayin\nYANLIŞ KULLANIM: 05/07/2006\nDOĞRU KULLANIM: 5/7/2006"
print(bilgi)
sleep(5)
print(nasil)
sleep(5)

def sorular():
    kim = input("\nKişinin Instagram kullanıcı adı\n: @")
    sleep(1)
    ay = int(input("\nKişinin doğduğu AY (Tek sayı ise sıfır koymayın!)\n: "))
    sleep(1)
    gun = int(input("\nKişinin doğduğu GÜN (Tek sayı ise sıfır koymayın!)\n: "))
    sleep(1)
    message = input("\nDoğum günü mesajınız\n: ")
    sleep(1)
    dogru = int(input("\nYazdıklarınızı onaylıyor musunuz?\n(Onaylıyorsanız 1'e basın onaylamıyorsanız 2'ye)\n: "))
    sleep(1)
    if dogru == 1:
        with open("postaci.py", "a", encoding="utf-8") as f:
            f.write(f"""

    if zaman.month == {ay} and zaman.day == {gun}:
        kime = "{kim}"
        dgkomsj = "{message}"
        calistir()""")

        print("\nKişi başarıyla kaydedildi!")
    else:
        print("\nYazdıklarınız kaydedilmedi!")

while True:
    sleep(1)
    sorular()
    sleep(2)
    devam = int(input("\nYeni kişi oluşturmak istiyor musunuz?\n1-Evet 2-Hayır\n: "))
    if devam == 1:
        continue
    else:
        print("\nProgram sonlandırıldı...")
        sleep(1)
        break