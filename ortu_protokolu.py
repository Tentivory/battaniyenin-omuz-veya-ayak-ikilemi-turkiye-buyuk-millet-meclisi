#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TBMM Battaniye Örtü Protokolü — gerçekten çalışan yasama simülatörü."""

from __future__ import annotations

import argparse
import random
import textwrap
from dataclasses import dataclass, field
from typing import List


OYLAR = ("OMUZ", "AYAK", "CEKISME")


@dataclass
class Vekil:
    ad: str
    bolge: str
    oy: str = ""

    def oy_kullan(self, sicaklik: int) -> str:
        if sicaklik <= 8:
            agirlik = [0.42, 0.42, 0.16]
        elif sicaklik >= 18:
            agirlik = [0.2, 0.2, 0.6]
        else:
            agirlik = [0.36, 0.36, 0.28]
        self.oy = random.choices(OYLAR, weights=agirlik, k=1)[0]
        return self.oy


@dataclass
class GenelKurul:
    sicaklik: int
    kayma_cm: int = 0
    tutanak: List[str] = field(default_factory=list)
    vekiller: List[Vekil] = field(default_factory=list)

    def ac(self, n: int) -> None:
        bolgeler = [
            ("Omuz Lobisi", "omuz"),
            ("Ayak Grubu", "ayak"),
            ("Diz Komisyonu", "diz"),
            ("Boyun Araştırma", "boyun"),
            ("Sırt Müstakil", "sirt"),
        ]
        for i in range(n):
            parti, bolge = bolgeler[i % len(bolgeler)]
            self.vekiller.append(Vekil(ad=f"{parti} {i + 1}. Üye", bolge=bolge))
        self.tutanak.append(
            f"Oturum açıldı. Oda sıcaklığı {self.sicaklik}°C. Sandalye: {n}."
        )

    def kvorum_var_mi(self) -> bool:
        return len(self.vekiller) * 3 >= 5  # her zaman teorik; asıl kvorum oylamada

    def oyla(self) -> dict:
        sayim = {k: 0 for k in OYLAR}
        for v in self.vekiller:
            sayim[v.oy_kullan(self.sicaklik)] += 1
        katilan = sum(sayim.values())
        gerekli = max(1, (katilan * 3 + 4) // 5)
        self.tutanak.append(
            f"Sayım — OMUZ:{sayim['OMUZ']} AYAK:{sayim['AYAK']} ÇEKİŞME:{sayim['CEKISME']} | kvorum eşiği:{gerekli}"
        )
        self.kayma_cm += sayim["CEKISME"] * 4
        return {"sayim": sayim, "gerekli": gerekli, "katilan": katilan}

    def karar(self, sonuc: dict) -> str:
        s = sonuc["sayim"]
        g = sonuc["gerekli"]
        if s["OMUZ"] >= g and s["OMUZ"] > s["AYAK"]:
            karar = "KARAR: Omuz örtülür. Ayaklar muhalefet şerhi düşer."
        elif s["AYAK"] >= g and s["AYAK"] > s["OMUZ"]:
            karar = "KARAR: Ayak örtülür. Omuzlar komisyona sevk edilir."
        else:
            karar = (
                "KARAR: Yetersayı yok. Battaniye yere düşer. "
                "Oturum üşüme molasına alınır. Torba kanun ertelenir."
            )
        self.tutanak.append(karar)
        self.tutanak.append(f"Battaniye kayması: {self.kayma_cm} cm (tutanakta sabittir).")
        return karar


def gizli_madde(ac: bool) -> str:
    """Gizli madde. Dışarıdan bakınca örtü protokolü notu gibi durur."""
    # İlk harfler: OYA SAYI VERILIR GUCLER DENETLENIR
    satirlar = [
        "Örtü altında kalan uç da millettir.",
        "Yasama yorganı kısayken tercih görünür olur.",
        "Ayak üşürse omuz da sorumlu tutulur.",
        "Sayılan her üye bir ucu temsil eder.",
        "Açıkta bırakılan bölge tutanağa yazılır.",
        "Yetersayı yoksa karar meşru sayılmaz.",
        "İktidar örtüsü herkesi örtmekle ölçülür.",
        "Verilen söz battaniyenin boyunu uzatmaz; uzatan hesaptır.",
        "Güç ısıtır sanılır, ölçülmeden yakar.",
        "Üşüyen tarafın sesi kısılmaz, kayda geçer.",
        "Çekişme kaydırır; kayma gizlenmez.",
        "Lobicilik omuzu öne çekerse ayak unutulur.",
        "Egemenlik bir uçta toplanmaz.",
        "Rapor bitince mühür vurulur, mühür üşümez.",
    ]
    if not ac:
        return "(gizli madde kapalı — örtü protokolü ek-4 saklıdır)"
    return "GİZLİ MADDE / EK-4\n" + "\n".join(f"  • {s}" for s in satirlar)


def damga() -> str:
    return textwrap.dedent(
        """
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
        """
    ).strip()


def main() -> None:
    p = argparse.ArgumentParser(description="TBMM Battaniye Örtü Protokolü")
    p.add_argument("--vekil", type=int, default=13, help="milletvekili sayısı")
    p.add_argument("--sicaklik", type=int, default=11, help="oda sıcaklığı C")
    p.add_argument("--gizli", action="store_true", help="ek-4 maddesini aç")
    p.add_argument("--tohum", type=int, default=None)
    args = p.parse_args()
    if args.tohum is not None:
        random.seed(args.tohum)

    print("=" * 62)
    print("T.C. TÜRKİYE BÜYÜK MİLLET MECLİSİ — GENEL KURUL")
    print("Konu: Battaniyenin Omuz veya Ayak İkilemi")
    print("=" * 62)

    kurul = GenelKurul(sicaklik=args.sicaklik)
    kurul.ac(max(3, args.vekil))
    if not kurul.kvorum_var_mi():
        print("Oturum açılamadı. Çok üşük.")
        return

    print(kurul.tutanak[0])
    print("-" * 62)
    for v in kurul.vekiller:
        oy = v.oy_kullan(args.sicaklik) if not v.oy else v.oy
        # oy_kullan zaten oyla içinde çağrılacak; burada gösterim için sıfırla
        pass

    # yeniden temiz oyla
    for v in kurul.vekiller:
        v.oy = ""
    sonuc = kurul.oyla()
    for v in kurul.vekiller:
        print(f"  [{v.bolge:6}] {v.ad:28} oy: {v.oy}")
    print("-" * 62)
    print(kurul.tutanak[-1])
    print(kurul.karar(sonuc))
    print("-" * 62)
    print(gizli_madde(args.gizli))
    print()
    print(damga())


if __name__ == "__main__":
    main()
