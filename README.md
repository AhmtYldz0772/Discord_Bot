# Discord Görev Botu

Merhaba! Bu proje tamamen eğlence amaçlı yazılmıştır :) 

## Nasıl Çalıştırılır

Önce gereken paketleri kurun:
```
pip install -r requirements.txt
```

Sonra `.env` dosyasına Discord bot tokeninizi yazın:
```
DISCORD_TOKEN=buraya_tokeninizi_yazin
DATABASE_PATH=tasks.db
```

Botu başlatmak için:
```
python bot.py
```

## Komutlar

- `!add_task <görev açıklaması>` - Yeni görev ekler
- `!show_tasks` - Bütün görevleri gösterir
- `!complete_task <görev id>` - Görevi tamamlar
- `!celebrate <görev id>` - Tamamlanan görev için kutlama resmi yapar
- `!delete_task <görev id>` - Görevi siler

## Örnek Kullanım

```
!add_task Proje raporunu bitir
!show_tasks
!complete_task 1
!celebrate 1
```

## Testler

Testleri çalıştırmak için:
```
python run_tests.py
```

## Dosyalar

- `bot.py` - Ana bot kodu
- `database.py` - Veritabanı işlemleri (SQLite kullanıyor)
- `tests/` - Test dosyaları
- `images/` - Kutlama resimleri buraya kaydediliyor

## Kullanılan Kütüphaneler

- discord.py - Discord botu için
- SQLite - Görevleri saklamak için
- Pillow - Kutlama resimlerini yapmak için
- pytest - Testler için

## Not

.env dosyasını GitHub'a yüklemeyin! Token'ınız gizli kalmalı.
