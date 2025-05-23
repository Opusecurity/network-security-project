# MITM Detector & Bettercap Simulation – Network Security Assignment

Bu proje, ağ güvenliği dersi kapsamında geliştirilen bir MITM (Man-in-the-Middle) saldırı tespit aracı ile Bettercap kullanılarak gerçekleştirilen MITM saldırı senaryosuna ait çıktıları içermektedir.

---

## Proje Yapısı

├── mitm_detector.py
├── mitm.pdf 
├── README.md 
└── .gitignore

## MITM Saldırısı Simülasyonu – `mitm.pdf`

Bettercap kullanılarak gerçekleştirilen DNS, HTTP ve HTTPS trafik müdahaleleri ekran görüntüleri ile birlikte PDF dosyasında sunulmuştur.

## MITM Tespit Aracı – `mitm_detector.py`

Python ile geliştirilmiş bu betik, sistemdeki ARP tablosunu analiz ederek şüpheli durumları tespit eder. Eğer birden fazla IP adresi aynı MAC adresine bağlanmışsa, bu bir MITM saldırısı belirtisi olabilir.

### Nasıl Çalışır?

1. Her 10 saniyede bir `arp -a` komutu ile sistemin ARP tablosu okunur.
2. MAC adresi-IP eşleşmeleri kontrol edilir.
3. Aynı MAC adresine sahip birden fazla IP varsa, terminale uyarı basılır.
