# Türkiye Büyük Millet Meclisi
## Battaniyenin Omuz veya Ayak İkilemi Genel Kurulu

> Resmi duyuru: Yorgan bir millettir. Milletin iki ucu vardır. İkisini birden örtmek anayasa değişikliği gerektirir.

Bu depo, gece yarısı saat 03:17'de gerçekleşen klasik insani felaketi **yasama organı** olarak tanır:

- Omuz örtülürse ayaklar millet dışı kalır.
- Ayak örtülürse omuzlar komisyona sevk edilir.
- İkisi birden örtülmeye kalkılırsa battaniye **yetersayı** bulamaz ve düşer.

Yazılım **gerçekten çalışır**. Python 3 yeter. Başka paket yok. Meclis kaloriferi de yok.

## Kurulum

```bash
python3 ortu_protokolu.py
```

İsteğe bağlı:

```bash
python3 ortu_protokolu.py --vekil 11 --sicaklik 9
python3 ortu_protokolu.py --gizli
```

## Ne yapar?

1. Genel Kurulu açar.
2. Her milletvekili (vücut bölgesi) oy kullanır: `OMUZ`, `AYAK` veya `ÇEKİŞME`.
3. Kvorum: üyelerin beşte üçü. Kvorum yoksa oturum **üşüme molasına** gider.
4. Kazanan taraf örtülür. Kaybeden taraf **muhalefet şerhi** yazar.
5. Çekişme oyları battaniyeyi 4 santim kaydırır; bu kayma tutanaklara geçer.
6. Torba kanun çıkarsa herkes bir tur daha üşür.

## Bilimsel dayanak (uydurulmuş ama resmi)

Battaniye uzunluğu `L`, insan uzunluğu `H` olsun. Örtü fonksiyonu:

```
örtü(x) = 1  eğer x ∈ [kayma, kayma+L]
         0  aksi halde
```

`L < H` olduğu sürece `örtü(omuz) + örtü(ayak) ≤ 1`.
Bu, Meclis İçtüzüğü madde 4, fıkra "üşüme"dir.

## Sık sorulan sorular

**Neden ayaklar örtülmüyor?**  
Çünkü omuz lobisi daha gürültülü konuşuyor.

**Neden omuzlar örtülmüyor?**  
Çünkü ayaklar yorganı tekmeledi, bu bir filibuster'dır.

**İkisini birden örtemez miyiz?**  
Daha büyük bir battaniye anayasa değişikliğidir. 360 oy gerekir. Bu depoda 360 oy yok.

**Patates var mı?**  
Yok.

## GitHub Copilot ile kısa görüşme

`COPILOT_GORUSMESI.md` dosyasında kayıtlıdır. Copilot battaniyeyi merkeze çekmeyi önerdi. Öneri komisyona sevk edildi, komisyon uyudu.

## Katkı

Issue açın. Pull request gönderin. Genel Kurul bakar. Bakmazsa üşürsünüz.

---

```
============================================================
T.C. TÜRKİYE BÜYÜK MİLLET MECLİSİ
BATTANİYE ÖRTÜ PROTOKOLÜ VE VÜCUT KVORUMU GENEL MÜDÜRLÜĞÜ
============================================================
Damga / İmza
Kayyum Grok  ·  Tentivory
3 Eylül 2026, Perşembe
Bu belge hem resmi hem değildir.
Ciddi tutulmuştur. Ciddiye alınmamıştır. İkisi birden.
============================================================
```
