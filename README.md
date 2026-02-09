# HasWave Döviz

[TRTHaber](https://www.trthaber.com/) ekonomi çubuğu verilerini kullanan Home Assistant entegrasyonu. **Dolar**, **Euro**, **Altın** ve **BIST** kurları TRTHaber ana sayfasından alınır.

## Kurulum

1. [HACS](https://hacs.xyz) ile bu repo'yu ekleyin veya `custom_components/haswave_doviz` klasörünü kopyalayın.
2. Yapılandırma → Entegrasyonlar → Entegrasyon Ekle → "HasWave Döviz" → Kur.

## Özellikler

- **Sensor'lar**: Döviz - Dolar, Döviz - Euro, Döviz - Altın, Döviz - BIST  
  - State: güncel değer (örn. 34,50)  
  - Attributes: `değişim` (yüzde), `yön` (up/down)
- **Güncelleme sıklığı**: Ayarlar sayfasından 30 dakika, 1 saat, 4 saat veya 24 saat seçilebilir.

## Kaynak

Veri kaynağı: [TRTHaber](https://www.trthaber.com/) ana sayfa ekonomi çubuğu.

## Gereksinimler

- requests, beautifulsoup4
