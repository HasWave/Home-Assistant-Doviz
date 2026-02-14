# 💱 HasWave Döviz

<div align="center">

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Home Assistant](https://img.shields.io/badge/Home%20Assistant-2023.6%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

**TRTHaber ekonomi çubuğu verilerini kullanan Home Assistant entegrasyonu.**

Dolar, Euro, Altın ve BIST kurları [TRTHaber](https://www.trthaber.com/) ana sayfasından alınır.

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)

<a href="https://my.home-assistant.io/redirect/hacs_repository/?owner=HasWave&repository=Home-Assistant-Doviz&category=Integration" target="_blank">
  <img src="https://my.home-assistant.io/badges/hacs_repository.svg" alt="Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.">
</a>

</div>

---

## 📋 Özellikler

* 💱 **Döviz Kurları** – Dolar, Euro, Altın ve BIST (TRTHaber ekonomi çubuğu)
* ✅ **Config Flow** – Kolay kurulum ve yapılandırma
* 📊 **Sensörler** – Güncel değer, `değişim` (yüzde) ve `yön` (up/down) attribute'ları
* 🔄 **Güncelleme Sıklığı** – Ayarlardan 30 dakika, 1 saat, 4 saat veya 24 saat
* 🔘 **Güncelle Butonu** – Cihaz sayfası Kontroller sekmesinden anında veri yenileme
* 📊 **Statistics** – Home Assistant statistics sayfasında görünür

## 🚀 Hızlı Başlangıç

### 1️⃣ HACS ile Kurulum

1. Home Assistant → **HACS** → **Integrations**
2. Sağ üstteki **⋮** menüsünden **Custom repositories** seçin
3. Repository URL: `https://github.com/HasWave/Home-Assistant-Doviz`
4. Category: **Integration** seçin
5. **Add** butonuna tıklayın
6. HACS → Integrations → **HasWave Döviz**'i bulun
7. **Download** butonuna tıklayın
8. Home Assistant'ı yeniden başlatın

### 2️⃣ Manuel Kurulum

1. Bu repository'yi klonlayın veya indirin
2. `custom_components/haswave_doviz` klasörünü Home Assistant'ın `config/custom_components/` klasörüne kopyalayın
3. Home Assistant'ı yeniden başlatın

### 3️⃣ Integration Ekleme

1. Home Assistant → **Settings** → **Devices & Services**
2. Sağ alttaki **+ ADD INTEGRATION** butonuna tıklayın
3. **HasWave Döviz** arayın ve seçin
4. **Submit** butonuna tıklayın

**✅ Sensörler otomatik oluşturulur:** Entegrasyon eklendiğinde Dolar, Euro, Altın ve BIST sensörleri eklenir.

## 📖 Kullanım

### Sensörler

| Entity | Açıklama |
|--------|----------|
| `sensor.haswave_doviz_dolar` | Dolar kuru (örn. 34,50) |
| `sensor.haswave_doviz_euro` | Euro kuru |
| `sensor.haswave_doviz_altin` | Altın fiyatı |
| `sensor.haswave_doviz_bist` | BIST endeksi |

Her sensörde:
- **State:** Güncel değer
- **değişim:** Yüzde değişim
- **yön:** `up` veya `down`

### Güncelleme

- **Yapılandır** (entegrasyon kartı) → Güncelleme sıklığı: 30 dk / 1 saat / 4 saat / 24 saat
- Cihaz sayfası → **Kontroller** → **Güncelle** butonu ile anında yenileme

### Dashboard Örneği

```yaml
type: entities
title: Döviz Kurları
entities:
  - entity: sensor.haswave_doviz_dolar
    name: Dolar
  - entity: sensor.haswave_doviz_euro
    name: Euro
  - entity: sensor.haswave_doviz_altin
    name: Altın
  - entity: sensor.haswave_doviz_bist
    name: BIST
```

## 🔗 Kaynak

Veri kaynağı: [TRTHaber](https://www.trthaber.com/) ana sayfa ekonomi çubuğu.

## 📦 Gereksinimler

- `requests`
- `beautifulsoup4`

## 📝 Lisans

Bu proje MIT lisansı altında lisanslanmıştır.

## 👨‍💻 Geliştirici

**HasWave**

🌐 [HasWave](https://haswave.com) | 📱 [Telegram](https://t.me/HasWave) | 📦 [GitHub](https://github.com/HasWave)

---

⭐ Bu projeyi beğendiyseniz yıldız vermeyi unutmayın!

Made with ❤️ by HasWave

