from collections import defaultdict, deque
import heapq
from typing import Dict, List, Tuple, Optional

class Istasyon:
    def __init__(self, idx: str, ad: str, hat: str):
        self.idx = idx
        self.ad = ad
        self.hat = hat
        self.komsular: List[Tuple['Istasyon', int]] = []  # (istasyon, süre) tuple'ları

    def komsu_ekle(self, istasyon: 'Istasyon', sure: int):
        self.komsular.append((istasyon, sure))

class MetroAgi:
    def __init__(self):
        self.istasyonlar: Dict[str, Istasyon] = {}
        self.hatlar: Dict[str, List[Istasyon]] = defaultdict(list)

    def istasyon_ekle(self, idx: str, ad: str, hat: str) -> None:
        if idx not in self.istasyonlar:
            istasyon = Istasyon(idx, ad, hat)
            self.istasyonlar[idx] = istasyon
            self.hatlar[hat].append(istasyon)

    def baglanti_ekle(self, istasyon1_id: str, istasyon2_id: str, sure: int) -> None:
        istasyon1 = self.istasyonlar[istasyon1_id]
        istasyon2 = self.istasyonlar[istasyon2_id]
        istasyon1.komsu_ekle(istasyon2, sure)
        istasyon2.komsu_ekle(istasyon1, sure)
    
    def en_az_aktarma_bul(self, baslangic_id: str, hedef_id: str) -> Optional[List[str]]:
        """BFS algoritması ile en az aktarmalı rotayı bulur"""
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None

        kuyruk = deque([(self.istasyonlar[baslangic_id], [baslangic_id])])
        ziyaret_edilen = set()

        while kuyruk:
            mevcut_istasyon, yol = kuyruk.popleft()

            if mevcut_istasyon.idx == hedef_id:
                 return [f"{self.istasyonlar[idx].ad}({idx})" for idx in yol]

            if mevcut_istasyon.idx not in ziyaret_edilen:
                ziyaret_edilen.add(mevcut_istasyon.idx)
                for komsu, _ in mevcut_istasyon.komsular:
                    if komsu.idx not in ziyaret_edilen:
                        kuyruk.append((komsu, yol + [komsu.idx]))

        return None

    def en_hizli_rota_bul(self, baslangic_id: str, hedef_id: str) -> Optional[Tuple[List[str], int]]:
        """A* algoritması ile en hızlı rotayı bulur"""
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None

        pq = [(0, baslangic_id, [baslangic_id])]  # (Toplam süre, istasyon ID, rota)
        ziyaret_edilen = {}

        while pq:
            toplam_sure, mevcut_id, yol = heapq.heappop(pq)

            if mevcut_id == hedef_id:
                 return [f"{self.istasyonlar[idx].ad}({idx})" for idx in yol], toplam_sure

            if mevcut_id not in ziyaret_edilen or toplam_sure < ziyaret_edilen[mevcut_id]:
                ziyaret_edilen[mevcut_id] = toplam_sure
                for komsu, sure in self.istasyonlar[mevcut_id].komsular:
                    heapq.heappush(pq, (toplam_sure + sure, komsu.idx, yol + [komsu.idx]))

        return None

# Örnek Kullanım
if __name__ == "__main__":
    metro = MetroAgi()
    
    # İstasyonlar ekleme
    metro.istasyon_ekle("K1", "Kızılay", "Kırmızı Hat")
    metro.istasyon_ekle("K2", "Ulus", "Kırmızı Hat")
    metro.istasyon_ekle("K3", "Demetevler", "Kırmızı Hat")
    metro.istasyon_ekle("K4", "OSB", "Kırmızı Hat")
    
    metro.istasyon_ekle("M1", "AŞTİ", "Mavi Hat")
    metro.istasyon_ekle("M2", "Kızılay", "Mavi Hat")
    metro.istasyon_ekle("M3", "Sıhhiye", "Mavi Hat")
    metro.istasyon_ekle("M4", "Gar", "Mavi Hat")
    
    metro.istasyon_ekle("T1", "Batıkent", "Turuncu Hat")
    metro.istasyon_ekle("T2", "Demetevler", "Turuncu Hat")
    metro.istasyon_ekle("T3", "Gar", "Turuncu Hat")
    metro.istasyon_ekle("T4", "Keçiören", "Turuncu Hat")

    # Bağlantılar ekleme
    metro.baglanti_ekle("K1", "K2", 4)
    metro.baglanti_ekle("K2", "K3", 6)
    metro.baglanti_ekle("K3", "K4", 8)
    
    metro.baglanti_ekle("M1", "M2", 5)
    metro.baglanti_ekle("M2", "M3", 3)
    metro.baglanti_ekle("M3", "M4", 4)
    
    metro.baglanti_ekle("T1", "T2", 7)
    metro.baglanti_ekle("T2", "T3", 9)
    metro.baglanti_ekle("T3", "T4", 5)
    
    metro.baglanti_ekle("K1", "M2", 2)
    metro.baglanti_ekle("K3", "T2", 3)
    metro.baglanti_ekle("M4", "T3", 2)
    
    # Test senaryoları
    testler = [
        ("M1", "K4"),  
        ("T1", "T4"),  
        ("T4", "M1")  
    ]

    for baslangic, hedef in testler:
        print(f"\n{baslangic} ({metro.istasyonlar[baslangic].ad}) -> {hedef} ({metro.istasyonlar[hedef].ad})")

        en_az_aktarma = metro.en_az_aktarma_bul(baslangic, hedef)
        if en_az_aktarma:
            print("En az aktarmalı rota:", " -> ".join(en_az_aktarma))
        else:
            print("Rota bulunamadı.")

        en_hizli_rota = metro.en_hizli_rota_bul(baslangic, hedef)
        if en_hizli_rota:
            rota, sure = en_hizli_rota
            print(f"En hızlı rota ({sure} dakika):", " -> ".join(rota))
        else:
            print("Hızlı rota bulunamadı.")
