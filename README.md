# Otomatik Doğum Günü Kutlayıcı

Bu Python programı, belirtilen tarihte belirli bir kişiye Instagram üzerinden doğum günü mesajı gönderir. Selenium kütüphanesi kullanılarak, kullanıcının giriş yapması ve bir mesaj göndermesi otomatikleştirilir. Eklediğiniz kullanıcıların doğum günlerini sizin yerinize kutlar

## Kurulum

Projeyi çalıştırmak için gereken adımların listesi:

0. Projeyi bulut sunucunuza kurmanız önerilir bu sayede 7/24 çalışabilir
1. Python 3.6 veya daha yüksek bir sürümün yüklü olduğundan emin olun
2. Selenium kütüphanesi yüklü olmalıdır. Eğer yüklü değilse, pip install selenium komutunu kullanarak yükleyebilirsiniz
3. Google Chrome veya başka bir tarayıcıda çalışması için, uygun sürümdeki tarayıcı sürücüsünü indirmelisiniz. Bu programda ChromeDriver kullanıldı. İndirme bağlantısı: https://chromedriver.chromium.org/downloads
4. hesap.py dosyasına gidin, account ve password'u Instagram kullanıcı adı ve şifrenizle değiştirin.
5. kisi_ekle.py dosyasını çalıştırın ve istediğiniz kullanıcıları ekleyin

## Kullanım

Projeyi nasıl kullanabileceğinize dair bir kılavuz:

1. Yukarıdaki adımları uyguladıktan sonra postaci.py dosyasını çalıştırın
2. Program 24 saatte bir çalışır, tarihleri kontrol eder ve doğum günü olan kişiye mesaj gönderir
3. Eğer sonradan yeni kullanıcı eklemek isterseniz postaci.py programını durdurmanız gerekmektedir

## İletişim

Projeyle ilgili herhangi bir sorunuz varsa bana şu adresten ulaşabilirsiniz: telegram.me/KontDragonSuat
