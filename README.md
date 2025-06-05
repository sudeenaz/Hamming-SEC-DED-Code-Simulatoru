# Hamming SEC-DED Code Simülatörü

Bu proje, Hamming SEC-DED (Single Error Correction, Double Error Detection) kodlama sisteminin simülasyonunu yapan bir Python uygulamasıdır. Kullanıcılar 8-bitlik veri girebilir, Hamming kodu hesaplayabilir, yapay hata oluşturabilir ve bu hataları düzeltebilirler.

## 🎯 Özellikler

- 8-bitlik veri girişi (0-255 arası)
- SEC-DED Hamming kodu hesaplama
- Yapay hata oluşturma (1-12 arası pozisyonlarda)
- Hata tespiti ve düzeltme
- Kullanıcı dostu grafiksel arayüz

## 📋 Gereksinimler

- Python 3.x
- tkinter (Python ile birlikte gelir)

## 🚀 Kurulum

1. Projeyi klonlayın:
git clone https://github.com/kullaniciadi/hamming-code-simulator.git
cd hamming-code-simulator

2. Gerekli bağımlılıkları yükleyin:
pip install -r requirements.txt

3. Uygulamayı çalıştırın:
python src/main.py


## 💻 Kullanım

1. **Veri Girişi**
   - 0-255 arası bir sayı girin
   - "Hamming Kodu Hesapla" butonuna tıklayın

2. **Hata Oluşturma**
   - 1-12 arası bir pozisyon seçin
   - "Hata Oluştur" butonuna tıklayın

3. **Hata Düzeltme**
   - "Hata Düzelt" butonuna tıklayın
   - Düzeltilmiş kod otomatik olarak gösterilecektir

## 🔧 Teknik Detaylar

### Hamming Kodu Yapısı
- 8-bit veri + 4 kontrol biti = 12-bit Hamming kodu
- Kontrol bitleri: p1, p2, p3, p4 (pozisyonlar: 1,2,4,8)
- Veri bitleri: d1-d8 (diğer pozisyonlar)

### Hata Düzeltme Mekanizması
1. Sendrom hesaplama
2. Hata pozisyonunu belirleme
3. Hatalı biti düzeltme

## 📁 Proje Yapısı

HammingSimulator/
│
├── src/
│   ├── main.py          # Ana uygulama dosyası
│   ├── hamming_code.py  # Hamming kodu hesaplama ve hata düzeltme
│   └── gui.py          # Kullanıcı arayüzü
│
├── tests/              # Test dosyaları
│   └── test_hamming_code.py
│
└── README.md          # Bu dosya


## 🧪 Test

Test dosyalarını çalıştırmak için:
python -m unittest tests/test_hamming_code.py


## 👥 Katkıda Bulunma

1. Bu depoyu fork edin
2. Yeni bir branch oluşturun (`git checkout -b feature/yeniOzellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik: Açıklama'`)
4. Branch'inizi push edin (`git push origin feature/yeniOzellik`)
5. Pull Request oluşturun

## 📞 İletişim

Sorularınız veya önerileriniz için:
- GitHub Issues
- E-posta: sudedogdu33@gmail.com
