import streamlit as st

# ─────────────────────────────────────────────
#  SAYFA AYARLARI
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Asansör Sistem Seçici v1.0",
    page_icon="🛗",
    layout="wide"
)

# ─────────────────────────────────────────────
#  ASANSÖR VERİTABANI (Orijinal Veriler Birebir Korundu)
# ─────────────────────────────────────────────
ASANSOR_DB = [
    {
        "id": "MR_GR_11_UP",
        "ad": "Makine Daireli · Dişlili · 1:1 · Üstten Palanga",
        "kisa": "MR Dişlili 1:1",
        "hiz_max": 2.5,
        "kapasite_max": 2000,
        "kapasite_min": 200,
        "kat_max": 20,
        "mr": True, "mrl": False, "disli": True, "dishisiz": False,
        "oran_11": True, "oran_21": False, "ustten": True, "alttan": False,
        "cw_yan": True, "cw_arka": True, "pit_min": 1200, "overhead_min": 3600,
        "mrdairesi": True,
        "avantajlar": ["Düşük ilk maliyet", "Yaygın yedek parça bulunabilirliği", "Basit mekanik yapı"],
        "dezavantajlar": ["Makine dairesi gerektirir (+15–25 m²)", "Yağ ve bakım yoğun", "Hız sınırlı (≤2,5 m/s)"],
        "tipik": "Orta katlı konut, alışveriş malleri, hastane (orta trafik)",
    },
    {
        "id": "MR_GR_21_UP",
        "ad": "Makine Daireli · Dişlili · 2:1 · Üstten Palanga",
        "kisa": "MR Dişlili 2:1",
        "hiz_max": 1.6,
        "kapasite_max": 5000,
        "kapasite_min": 500,
        "kat_max": 15,
        "mr": True, "mrl": False, "disli": True, "dishisiz": False,
        "oran_11": False, "oran_21": True, "ustten": True, "alttan": False,
        "cw_yan": True, "cw_arka": True, "pit_min": 1400, "overhead_min": 4200,
        "mrdairesi": True,
        "avantajlar": ["Yüksek yük kapasitesi (≤5.000 kg)", "Daha küçük motor gücü yeterli", "Endüstriyel/kargo uygulamaları için ideal"],
        "dezavantajlar": ["Makine dairesi gerektirir", "Daha yüksek overhead boşluğu", "Hız düşük (≤1,6 m/s)"],
        "tipik": "Yük asansörü, büyük alışveriş merkezi servis asansörü, hastane yatak asansörü",
    },
    {
        "id": "MR_GL_11_UP",
        "ad": "Makine Daireli · Dişlisiz · 1:1 · Üstten Palanga",
        "kisa": "MR Dişlisiz 1:1",
        "hiz_max": 10.0,
        "kapasite_max": 2500,
        "kapasite_min": 400,
        "kat_max": 100,
        "mr": True, "mrl": False, "disli": False, "dishisiz": True,
        "oran_11": True, "oran_21": False, "ustten": True, "alttan": False,
        "cw_yan": True, "cw_arka": True, "pit_min": 1500, "overhead_min": 4000,
        "mrdairesi": True,
        "avantajlar": ["Çok yüksek hız (≤10 m/s)", "Düşük bakım", "Sessiz ve konforlu"],
        "dezavantajlar": ["Makine dairesi gerektirir", "Yüksek ilk maliyet", "Özel kontrol sistemi"],
        "tipik": "Yüksek/çok katlı ofis kuleleri, oteller, rezidanslar",
    },
    {
        "id": "MRL_GL_11_UP",
        "ad": "Makine Dairesiz · Dişlisiz · 1:1 · Üstten Palanga",
        "kisa": "MRL Dişlisiz 1:1",
        "hiz_max": 4.0,
        "kapasite_max": 2000,
        "kapasite_min": 200,
        "kat_max": 40,
        "mr": False, "mrl": True, "disli": False, "dishisiz": True,
        "oran_11": True, "oran_21": False, "ustten": True, "alttan": False,
        "cw_yan": True, "cw_arka": True, "pit_min": 1100, "overhead_min": 3500,
        "mrdairesi": False,
        "avantajlar": ["Makine dairesi gerekmez → bina alanı tasarrufu", "Enerji verimli (VF sürücü)", "Düşük işletme maliyeti"],
        "dezavantajlar": ["Kuyu başı yeterli olmalı (≥3.500 mm)", "Motor kuyu içinde → bakım zor", "Isı yönetimi önemli"],
        "tipik": "Konut, ofis, AVM, hastane — modern binaların büyük çoğunluğu",
    },
    {
        "id": "MRL_GL_21_UP",
        "ad": "Makine Dairesiz · Dişlisiz · 2:1 · Üstten Palanga",
        "kisa": "MRL Dişlisiz 2:1",
        "hiz_max": 2.0,
        "kapasite_max": 3500,
        "kapasite_min": 400,
        "kat_max": 20,
        "mr": False, "mrl": True, "disli": False, "dishisiz": True,
        "oran_11": False, "oran_21": True, "ustten": True, "alttan": False,
        "cw_yan": True, "cw_arka": True, "pit_min": 1200, "overhead_min": 3800,
        "mrdairesi": False,
        "avantajlar": ["Makine dairesi gerekmez", "Yüksek yük + enerji verimliliği", "Daha küçük motor"],
        "dezavantajlar": ["Daha fazla kasnak ve halat", "Kuyu üst yüksekliği kritik"],
        "tipik": "Orta-yüksek kapasiteli konut ve ticari, hastane servis asansörleri",
    },
    {
        "id": "MRL_GL_11_BACK",
        "ad": "Makine Dairesiz · Dişlisiz · 1:1 · Alttan Palanga (Backpack)",
        "kisa": "MRL Backpack 1:1",
        "hiz_max": 2.5,
        "kapasite_max": 1600,
        "kapasite_min": 200,
        "kat_max": 20,
        "mr": False, "mrl": True, "disli": False, "dishisiz": True,
        "oran_11": True, "oran_21": False, "ustten": False, "alttan": True,
        "cw_yan": False, "cw_arka": True, "pit_min": 1200, "overhead_min": 2800,
        "mrdairesi": False,
        "avantajlar": ["Çok düşük kuyu üst yüksekliği (≥2.800 mm)", "Mevcut binalarda renovasyon için ideal", "Panoramik kabin uyumlu"],
        "dezavantajlar": ["Kapasite sınırlı (≤1.600 kg)", "Karmaşık alt çerçeve yapısı"],
        "tipik": "Tarihi bina yenileme, dar kuyu, konut (villa, butik otel)",
    },
    {
        "id": "MR_GL_21_UP",
        "ad": "Makine Daireli · Dişlisiz · 2:1 · Üstten Palanga",
        "kisa": "MR Dişlisiz 2:1",
        "hiz_max": 6.0,
        "kapasite_max": 5000,
        "kapasite_min": 800,
        "kat_max": 60,
        "mr": True, "mrl": False, "disli": False, "dishisiz": True,
        "oran_11": False, "oran_21": True, "ustten": True, "alttan": False,
        "cw_yan": True, "cw_arka": True, "pit_min": 1600, "overhead_min": 4500,
        "mrdairesi": True,
        "avantajlar": ["Çok yüksek yük + yüksek hız", "Büyük ticari projeler", "Uzun seyir mesafesi"],
        "dezavantajlar": ["Makine dairesi gerektirir", "Yüksek kuyu başı gereksinimi", "Yüksek maliyet"],
        "tipik": "Yüksek katlı AVM, ofis kuleleri, büyük hastaneler",
    },
    {
        "id": "HYD_DIRECT",
        "ad": "Hidrolik · Doğrudan Tahrik",
        "kisa": "Hidrolik Doğrudan",
        "hiz_max": 0.8,
        "kapasite_max": 5000,
        "kapasite_min": 200,
        "kat_max": 5,
        "mr": False, "mrl": False, "disli": False, "dishisiz": False,
        "oran_11": True, "oran_21": False, "ustten": False, "alttan": True,
        "cw_yan": False, "cw_arka": False, "pit_min": 400, "overhead_min": 2500,
        "mrdairesi": True,
        "avantajlar": ["Çok düşük kuyu dibi ve üst yüksekliği", "Karşı ağırlık gerekmez", "Yüksek yük kapasitesi"],
        "dezavantajlar": ["Sadece düşük kat sayısı (≤5 kat)", "Hız düşük (≤0,8 m/s)", "Yüksek enerji tüketimi"],
        "tipik": "Villa, 2–5 katlı küçük bina, engelli platformu",
    }
]

# ─────────────────────────────────────────────
#  FİLTRELEME VE PUAN MA MOTORU (Orijinal Mantık Birebir Korundu)
# ─────────────────────────────────────────────
def asansor_filtrele_ve_puanla(cevaplar: dict) -> list:
    sonuclar = []
    for a in ASANSOR_DB:
        puan = 0
        max_p = 0
        
        # ZORUNLU ELİMİNASYON KURALLARI
        if cevaplar["hiz"] > a["hiz_max"]: continue
        if cevaplar["kapasite"] < a["kapasite_min"] or cevaplar["kapasite"] > a["kapasite_max"]: continue
        if cevaplar["kat_sayisi"] > a["kat_max"]: continue
        
        if cevaplar["mr_var"] is False and a["mrdairesi"] is True and a["id"] not in ("HYD_DIRECT",):
            if a["mr"] is True: continue
        if cevaplar["mr_var"] is True and a["mrl"] is True and cevaplar["mrl_tercih"] is False: continue
        
        if cevaplar["pit_derinligi"] is not None and cevaplar["pit_derinligi"] < a["pit_min"]: continue
        if cevaplar["overhead"] is not None and cevaplar["overhead"] < a["overhead_min"]: continue
        
        if cevaplar["cw_pozisyon"] == "Sadece yandan" and not a["cw_yan"]: continue
        if cevaplar["cw_pozisyon"] == "Sadece arkadan" and not a["cw_arka"]: continue

        # PUANLAMA MANTIĞI
        max_p += 2
        if cevaplar["enerji_onceligi"] == "Yüksek":
            puan += 2 if a["dishisiz"] else (1 if a["disli"] else 0)
        elif cevaplar["enerji_onceligi"] == "Orta":
            puan += 1

        max_p += 2
        if cevaplar["butce"] == "Ekonomik":
            puan += 2 if a["disli"] else 0
        elif cevaplar["butce"] == "Orta":
            puan += 2 if (a["mrl"] and not a["disli"]) else 1
        else:
            puan += 2 if a["dishisiz"] else 1

        max_p += 1
        if cevaplar["bakim_kolay"] and a["mr"]: puan += 1
        elif not cevaplar["bakim_kolay"] and a["mrl"]: puan += 1

        max_p += 2
        oran = cevaplar["hiz"] / a["hiz_max"]
        if 0.5 <= oran <= 1.0: puan += 2
        elif oran < 0.5: puan += 1

        max_p += 2
        kap_oran = cevaplar["kapasite"] / a["kapasite_max"]
        if 0.4 <= kap_oran <= 0.9: puan += 2
        elif kap_oran < 0.4: puan += 1

        max_p += 2
        tipik_lower = a["tipik"].lower()
        uyg = cevaplar["uygulama"]
        if uyg == "Konut" and any(x in tipik_lower for x in ["konut", "villa", "rezidans"]): puan += 2
        elif uyg == "Ofis/Ticari" and any(x in tipik_lower for x in ["ofis", "ticari", "avm"]): puan += 2
        elif uyg == "Hastane" and "hastane" in tipik_lower: puan += 2
        elif uyg == "Endüstriyel/Yük" and any(x in tipik_lower for x in ["yük", "endüstri", "servis"]): puan += 2
        elif uyg == "Otel/Turizm" and any(x in tipik_lower for x in ["otel", "butik"]): puan += 2
        else: puan += 1

        max_p += 1
        if cevaplar["modern_tercih"] and a["mrl"]: puan += 1
        elif not cevaplar["modern_tercih"] and a["mr"] and a["disli"]: puan += 1

        sonuclar.append((puan, max_p, a))
        
    sonuclar.sort(key=lambda x: x[0], reverse=True)
    return sonuclar

# ─────────────────────────────────────────────
#  STREAMLIT ARAYÜZ AKIŞI (Tüm Sorular Buraya Taşındı)
# ─────────────────────────────────────────────
st.title("🛗 Asansör Sistem Seçici Mühendislik Paneli")
st.caption("Avrupa Asansör Yönetmeliği (2014/33/EU) ve EN 81-20/50 Standartları Ön Değerlendirme Altyapısı")

# Sol Panel: Soruların Giriş Alanı
st.sidebar.header("📋 PROJE PARAMETRELERİ")

# 1 / 6 — Proje Tanımı
st.sidebar.subheader("1. Proje Tanımı")
uygulama = st.sidebar.selectbox("Kullanım Amacı", ["Konut", "Ofis/Ticari", "Hastane", "Endüstriyel/Yük", "Otel/Turizm"])
kat_sayisi = st.sidebar.number_input("Toplam Kat Sayısı (Zemin Dahil)", min_value=2, max_value=150, value=8)
seyir_yuksekligi = st.sidebar.number_input("Toplam Seyir Yüksekliği (m)", min_value=3.0, max_value=500.0, value=float(kat_sayisi * 3.0))

# 2 / 6 — Performans Gereksinimleri
st.sidebar.subheader("2. Performans")
kapasite = st.sidebar.number_input("İstenen Taşıma Kapasitesi (kg)", min_value=100, max_value=10000, value=630)

hiz_Haritasi = {
    "0,63 m/s — Villa / küçük konut": 0.63,
    "1,00 m/s — Konut standardı": 1.00,
    "1,60 m/s — Orta hız (konut/ofis)": 1.60,
    "2,50 m/s — Hızlı (ofis/AVM)": 2.50,
    "4,00 m/s — Yüksek hız": 4.00,
    "6,00+ m/s — Çok yüksek kule": 6.00
}
hiz_secim = st.sidebar.selectbox("İstenen Nominal Kabin Hızı", list(hiz_Haritasi.keys()), index=1)
hiz = hiz_Haritasi[hiz_secim]

kabin_genislik = st.sidebar.number_input("Kabin İç Genişliği (mm)", min_value=600, max_value=3000, value=1100)
kabin_derinlik = st.sidebar.number_input("Kabin İç Derinliği (mm)", min_value=800, max_value=3000, value=1400)

# 3 / 6 — Kuyu Koşulları
st.sidebar.subheader("3. Kuyu Koşulları")
pit_biliniyor = st.sidebar.checkbox("Kuyu dibi (pit) derinliği biliniyor mu?", value=False)
pit_derinligi = st.sidebar.number_input("Mevcut Kuyu Dibi Boşluğu (mm)", min_value=200, max_value=3000, value=1200) if pit_biliniyor else None

oh_biliniyor = st.sidebar.checkbox("Kuyu üst boşluğu (overhead) biliniyor mu?", value=False)
overhead = st.sidebar.number_input("Mevcut Kuyu Üst Boşluğu (mm)", min_value=2000, max_value=8000, value=3600) if oh_biliniyor else None

cw_pozisyon = st.sidebar.selectbox("Karşı Ağırlık Konum Kısıtı", ["Fark etmez", "Sadece yandan", "Sadece arkadan"])

# 4 / 6 — Makine Dairesi Durumu
st.sidebar.subheader("4. Makine Dairesi")
mr_durum = st.sidebar.radio("Makine Dairesi Durumu", [
    "Mevcut / planlanmış makine dairesi var",
    "Makine dairesi yok, MRL tercih edilir",
    "Hidrolik düşünülüyor",
    "Fark etmez"
], index=1)

if "yok" in mr_durum.lower() or "mrl" in mr_durum.lower():
    mr_var = False
    mrl_tercih = True
elif "var" in mr_durum.lower():
    mr_var = True
    mrl_tercih = False
else:
    mr_var = None
    mrl_tercih = None

# 5 / 6 — Proje Öncelikleri
st.sidebar.subheader("5. Öncelikler")
butce_secim = st.sidebar.selectbox("Bütçe Önceliği", ["Ekonomik (ilk maliyet düşük)", "Orta (denge)", "Premium (en iyi teknoloji)"], index=1)
butce = "Ekonomik" if "Ekonomik" in butce_secim else ("Premium" if "Premium" in butce_secim else "Orta")

enerji_secim = st.sidebar.selectbox("Enerji Verimliliği Önceliği", ["Düşük (standart)", "Orta", "Yüksek (yeşil bina / LEED)"], index=1)
enerji_onceligi = "Düşük" if "Düşük" in enerji_secim else ("Yüksek" if "Yüksek" in enerji_secim else "Orta")

bakim_kolay = st.sidebar.checkbox("Bakım kolaylığı öncelikli mi?", value=False)
modern_tercih = st.sidebar.checkbox("Modern kontrol sistemi (MRL/gearless) tercih edilsin mi?", value=True)

# 6 / 6 — Ek Özellikler
st.sidebar.subheader("6. Ek Özellikler")
acil_enerji = st.sidebar.checkbox("Acil durum / ARD gerekli mi?", value=True)
deprem_bolgesi = st.sidebar.checkbox("Deprem bölgesi (sismik kısıt) var mı?", value=False)
yangin_servisi = st.sidebar.checkbox("İtfaiyeci servisi (EN 81-72) gerekli mi?", value=False)

# Cevapları Paketleme
cevaplar = {
    "uygulama": uygulama, "kat_sayisi": kat_sayisi, "seyir_yuksekligi": seyir_yuksekligi,
    "kapasite": kapasite, "hiz": hiz, "kabin_genislik": kabin_genislik, "kabin_derinlik": kabin_derinlik,
    "pit_derinligi": pit_derinligi, "overhead": overhead, "cw_pozisyon": cw_pozisyon,
    "mr_var": mr_var, "mrl_tercih": mrl_tercih, "butce": butce, "enerji_onceligi": enerji_onceligi,
    "bakim_kolay": bakim_kolay, "modern_tercih": modern_tercih, "deprem_bolgesi": deprem_bolgesi,
    "yangin_servisi": yangin_servisi
}

# ─────────────────────────────────────────────
#  SAĞ PANEL: SONUÇLARI GÖSTERME ALANI
# ─────────────────────────────────────────────
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📊 Girilen Parametre Özeti")
    st.info(f"""
    * **Kullanım:** {uygulama}
    * **Kat / Seyir:** {kat_sayisi} Kat / {seyir_yuksekligi} m
    * **Yük / Hız:** {kapasite} kg / {hiz} m/s
    * **Kabin:** {kabin_genislik}x{kabin_derinlik} mm
    * **Kuyu Dibi:** {f"{pit_derinligi} mm" if pit_derinligi else "Belirtilmedi"}
    * **Kuyu Üstü:** {f"{overhead} mm" if overhead else "Belirtilmedi"}
    """)

with col2:
    st.subheader("🏗️ Uygun Konfigürasyon Önerileri")
    sonuclar = asansor_filtrele_ve_puanla(cevaplar)
    
    if not sonuclar:
        st.error("✖ Girilen sert kısıtlara uygun bir asansör modeli bulunamadı. Lütfen kuyu dibi veya hız kriterlerini esnetin.")
    else:
        goster_sayisi = min(4, len(sonuclar))
        for sira, (puan, max_p, asansor) in enumerate(sonuclar[:goster_sayisi], 1):
            with st.expander(f"#{sira} - {asansor['ad']} (Uyum: {puan}/{max_p})", expanded=(sira==1)):
                # İlerleme çubuğu (Uyum Puanı)
                st.progress(puan / max_p)
                
                # Özellik sütunları
                c1, c2 = st.columns(2)
                with c1:
                    st.markdown("**Teknik Limitler:**")
                    st.write(f"⚡ Hız Maks: {asansor['hiz_max']} m/s")
                    st.write(f"⚖ Kapasite: {asansor['kapasite_min']}-{asansor['kapasite_max']} kg")
                    st.write(f"🏢 Kat Limiti: {asansor['kat_max']} Kat")
                with c2:
                    st.markdown("**Kuyu İhtiyaçları:**")
                    st.write(f"↕ Kuyu Dibi Min: {asansor['pit_min']} mm")
                    st.write(f"↑ Kuyu Üstü Min: {asansor['overhead_min']} mm")
                
                st.write(f"💡 *Tipik Kullanım:* {asansor['tipik']}")
                
                # Avantaj / Dezavantaj
                av_col, dez_col = st.columns(2)
                with av_col:
                    st.success("**✔️ Avantajlar:**\n" + "\n".join([f"* {v}" for v in asansor['avantajlar']]))
                with dez_col:
                    st.warning("**⚠️ Dikkat Edilecekler:**\n" + "\n".join([f"* {d}" for d in asansor['dezavantajlar']]))

st.divider()
st.subheader("📋 Önemli Mühendislik Notları")
st.warning("""
* Bu analiz tamamen ön değerlendirme amacıyla yazılımsal algoritmayla hesaplanmıştır. 
* Kesin yapısal tasarım ve imalat için **lisanslı bir asansör mühendisi (SMM)** onayı zorunludur.
* EN 81-20, EN 81-50 ve asansörün kurulacağı yerel imar yönetmeliklerine tam uyumluluk sahada doğrulanmalıdır.
""")

if deprem_bolgesi:
    st.error("⚠️ **Sismik Bölge Modu Aktif:** EN 81-77 sismik gereksinimleri uyarınca karşı ağırlık ray kilitleri, halat fırlatma önleyiciler ve sismik sensör yerleşimleri tasarıma dahil edilmelidir.")
if yangin_servisi:
    st.error("⚠️ **İtfaiyeci Asansörü Aktif:** EN 81-72 kapsamında yangına dayanıklı kuyu kapıları, acil durum güç beslemesi (jeneratör) ve kabin üstü kurtarma kapağı zorunludur.")
