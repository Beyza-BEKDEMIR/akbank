Bu Python projesi, bir metro ağı üzerinde en az aktarmalı ve en hızlı rotaların bulunmasını amaçlamaktadır. 
MetroAgi sınıfı, metro hatları arasındaki bağlantıları ve istasyonları modelleyerek, BFS ve A* algoritmalarını kullanarak en az aktarmalı ve en hızlı rotaları hesaplar.

Kurulum
Bu projeyi kullanmak için herhangi bir ek kurulum yapmanıza gerek yoktur. Ancak, Python ortamında çalıştırmak için aşağıdaki bağımlılıkları yüklemeniz gerekebilir.

Gereksinimler
  Python 3.x
  heapq (Python'un standart kütüphanesinde mevcuttur)
  collections (Python'un standart kütüphanesinde mevcuttur)
  typing (Python 3.5+)

Kod Yapısı

Istasyon Sınıfı
  idx: İstasyonun benzersiz ID'si.
  ad: İstasyonun adı.
  hat: İstasyonun bulunduğu metro hattı.
  komsular: İstasyonun komşu istasyonları ile olan bağlantıları.
  
MetroAgi Sınıfı
  istasyonlar: Tüm istasyonların bir sözlüğü.
  hatlar: Her hattın içindeki istasyonları listeleyen bir sözlük.
  istasyon_ekle: Yeni bir istasyon ekler.
  baglanti_ekle: İki istasyon arasında bir bağlantı ekler.
  en_az_aktarma_bul: BFS algoritmasını kullanarak en az aktarmalı rotayı bulur.
  en_hizli_rota_bul: A* algoritmasını kullanarak en hızlı rotayı bulur.

Test Senaryoları
Proje, birkaç test senaryosu ile birlikte gelir. Bu testler, başlangıç ve hedef istasyonları vererek, en az aktarmalı ve en hızlı rotaların doğru şekilde hesaplanıp hesaplanmadığını kontrol eder.

Test 1: "M1" -> "K4"
Bu senaryo, "AŞTİ" istasyonundan "OSB" istasyonuna en az aktarmalı ve en hızlı rotaların bulunmasını test eder.
Test 2: "T1" -> "T4"
Bu senaryo, "Batıkent" istasyonundan "Keçiören" istasyonuna en az aktarmalı ve en hızlı rotaları test eder.
Test 3: "T4" -> "M1"
Bu senaryo, "Keçiören" istasyonundan "AŞTİ" istasyonuna en az aktarmalı ve en hızlı rotaları test eder.
