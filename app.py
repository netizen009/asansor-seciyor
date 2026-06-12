import streamlit as st

# Sayfa Ayarları (Tarayıcı sekmesinde görünecek kısım)
st.set_page_config(page_title="Asansör Sistem Seçici", page_icon="🛗", layout="wide")

# ─────────────────────────────────────────────
#  ASANSÖR VERİTABANI
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
        "mr": True,
        "mrl": False,
        "disli": True,
        "dishisiz": False,
        "oran_11": True,
        "oran_21": False,
        "ustten": True,
        "alttan": False,
        "cw_yan": True,
        "cw_arka": True,
        "pit_min": 1200,
        "overhead_min": 3600,
        "mrdairesi": True,
        "avantajlar": ["Düşük ilk maliyet", "Yaygın yedek parça bulunabilirliği", "Basit mekanik yapı"],
        "dezavantajlar": ["Makine dairesi gerektirir (+15–25 m²)", "Yağ ve bakım yoğun", "Hız sınırlı (≤2,5 m/s)"],
        "tipik": "Orta katlı konut, alışveriş merkezi, hastane (orta trafik)",
    },
    {
        "id": "MR_GR_21_UP",
        "ad": "Makine Daireli · Dişlili · 2:1 · Üstten Palanga",
        "kisa": "MR Dişlili 2:1",
        "hiz_max": 1.6,
        "kapasite_max": 5000,
        "kapasite_min": 500,
        "kat_max": 15,
        "mr": True,
        "mrl": False,
        "disli": True,
        "dishisiz": False,
        "oran_11": False,
        "oran_21": True,
        "ustten": True,
        "alttan": False,
        "cw_yan": True,
        "cw_arka": True,
        "pit_min": 1400,
        "overhead_min": 4200,
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
        "mr": True,
        "mrl": False,
        "disli": False,
        "dishisiz": True,
        "oran_11": True,
        "oran_21": False,
        "ustten": True,
        "alttan": False,
        "cw_yan": True,
        "cw_arka": True,
        "pit_min": 1500,
        "overhead_min": 4000,
        "mrdairesi": True,
        "avantajlar": ["Çok yüksek hız (≤10 m/s)", "Düşük bakım", "Sessiz ve konforlu"],
        "dezavantajlar": ["Makine dairesi gerektirir", "Yüksek ilk maliyet"],
        "tipik": "Yükse/çok katlı ofis kuleleri, oteller, rezidanslar",
    },
    {
        "id": "MRL_GL_11_UP",
        "ad": "Makine Dairesiz · Dişlisiz · 1:1 · Üstten Palanga",
        "kisa": "MRL Dişlisiz 1:1",
        "hiz_max": 4.0,
        "kapasite_max": 2000,
        "kapasite_min": 200,
        "kat_max": 40,
        "mr": False,
        "mrl": True,
        "disli": False,
        "dishisiz": True,
        "oran_11": True,
        "oran_21": False,
        "ustten": True,
        "alttan": False,
        "cw_yan": True,
        "cw_arka": True,
        "pit_min": 1100,
        "overhead_min": 3500,
        "mrdairesi": False,
        "avantajlar": ["Makine dairesi gerekmez → alan tasarrufu", "Enerji verimli (VF sürücü)", "Düşük işletme maliyeti"],
        "dezavantajlar": ["Kuyu başı yeterli olmalı (≥3.500 mm)", "Motor kuyu içinde → bakım zorluğu"],
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
        "mr": False,
        "mrl": True,
        "disli": False,
        "dishisiz": True,
        "oran_11": False,
        "oran_21": True,
        "ustten": True,
        "alttan": False,
        "cw_yan": True,
        "cw_arka": True,
        "pit_min": 1200,
        "overhead_min": 3800,
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
        "mr": False,
        "mrl": True,
        "disli": False,
        "dishisiz": True,
        "oran_11": True,
        "oran_21": False,
        "ustten": False,
        "alttan": True,
        "cw_yan": False,
        "cw_arka": True,
        "pit_min": 1200,
        "overhead_min": 2800,
        "mrdairesi": False,
        "avantajlar": ["Çok düşük kuyu üst yüksekliği (≥2.800 mm)", "Mevcut binalarda renovasyon için ideal", "Panoramik kabin uyumlu"],
        "dezavantajlar": ["Kapasite sınırlı (≤1.600 kg)", "Karmaşık alt çerçeve yapısı"],
        "tipik": "Tarihi bina yenileme, dar kuyu, konut (villa, butik otel)",
    },
    {
        "id": "HYD_DIRECT",
        "ad": "Hidrolik · Doğrudan Tahrik",
        "kisa": "Hidrolik Doğrudan",
        "hiz_max": 0.8,
        "kapasite_max": 5000,
        "kapasite_min": 200,
        "kat_max": 5,
        "mr": False,
        "mrl": False,
        "disli": False,
        "dishisiz": False,
        "oran_11": True,
        "oran_21": False,
        "ustten": False,
        "alttan": True,
        "cw_yan": False,
        "cw_arka": False,
        "pit_min": 400,
        "overhead_min": 2500,
        "mrdairesi": True,
        "avantajlar": ["Çok düşük kuyu dibi ve üst yüksekliği", "Karşı ağırlık gerekmez", "Yüksek yük kapasitesi"],
        "dezavantajlar": ["Sadece düşük kat sayısı (≤5 kat)", "Yüksek enerji tüketimi", "Çevre riski (yağ sızıntısı)"],
        "tipik": "Villa, 2–5 katlı küçük bina, engelli platformu",
    }
]

# ─────────────────────────────────────────────
#  FİLTRELEME MOTORU
# ─────────────────────────────────────────────
def asansor_filtrele_ve_puanla(cevaplar):
    sonuclar = []
    for a in ASANSOR_DB:
        puan = 0
        max_p = 0
        
        # Filtreleme Kuralları
        if cevaplar["hiz"] > a["hiz_max"]: continue
        if cevaplar["kapasite"] < a["kapasite_min"] or cevaplar["kapasite"] > a["kapasite_max"]: continue
        if cevaplar["kat_sayisi"] > a["kat_max"]: continue
        
        if cevaplar["mr_var"] is False and a["mrdairesi"] is True and a["id"] != "HYD_DIRECT": continue
        if cevaplar["mr_var"] is True and a["mrl"] is True and cevaplar["mrl_tercih"] is False: continue
        
        if cevaplar["pit_derinligi"] and cevaplar["pit_derinligi"] < a["pit_min"]: continue
        if cevaplar["overhead"] and cevaplar["overhead"] < a["overhead_min"]: continue
        
        if cevaplar["cw_pozisyon"] == "Sadece yandan" and not a["cw_yan"]: continue
        if cevaplar["cw_pozisyon"] == "Sadece arkadan" and not a["cw_arka"]: continue

        # Puanlama Kuralları
        max_p += 2
        if cevaplar["enerji_onceligi"] == "Yüksek" and a["dishisiz"]: puan += 2
        elif cevaplar["enerji_onceligi"] == "Orta": puan += 1

        max_p += 2
        if cevaplar["butce"] == "Ekonomik" and a["disli"]: puan += 2
        elif cevaplar["butce"] == "Orta": puan += 1
        elif cevaplar["butce"] == "Premium" and a["dishisiz"]: puan += 2

        max_p += 2
        if 0.5 <= (cevaplar["hiz"] / a["hiz_max"]) <= 1.0: puan += 2
        else: puan += 1

        tipik_lower = a["tipik"].lower()
        if cevaplar["uygulama"].lower() in tipik_lower: puan += 2
        else: puan += 1
        max_p += 2

        sonuclar.append((puan, max_p, a))
    
    sonuclar.sort(key=lambda x: x[0], reverse=True)
    return sonuclar

# ─────────────────────────────────────────────
#  STREAMLIT ARAYÜZÜ (UI)
# ─────────────────────────────────────────────
st.title("🛗 Asansör Sistem Seçici v1.0")
st.caption("Avrupa Asansör Yönetmeliği (2014/33/EU) ve EN 81-20/50 standartları temel alınmıştır.")

# Yan Menü (Sidebar) - Giriş Parametreleri
st.sidebar.header("📋 Proje Parametreleri")

cevaplar = {}
cevaplar["uygulama"] = st.sidebar.selectbox("Kullanım Amacı", ["Konut", "Ofis/Ticari", "Hastane", "Endüstriyel/Yük", "Otel/Turizm"])
cevaplar["kat_sayisi"] = st.sidebar.number_input("Toplam Kat Sayısı", min_value=2, max_value=150, value=8)
cevaplar["kapasite"] = st.sidebar.slider("İstenen Kapasite (kg)", min_value=100, max_value=5000, value=630, step=10)
cevaplar["hiz"] = st.sidebar.select_slider("İstenen Nominal Hız (m/s)", options=[0.63, 1.0, 1.6, 2.5, 4.0, 6.0], value=1.0)

# Kuyu Ölçüleri
st.sidebar.subheader("📐 Kuyu Ölçüleri")
pit_biliniyor = st.sidebar.checkbox("Kuyu Dibi (Pit) Derinliği Biliniyor")
cevaplar["pit_derinligi"] = st.sidebar.number_input("Pit Derinliği (mm)", min_value=200, max_value=3000, value=1200) if pit_biliniyor else None

oh_biliniyor = st.sidebar.checkbox("Kuyu Üst Boşluğu (Overhead) Biliniyor")
cevaplar["overhead"] = st.sidebar.number_input("Overhead (mm)", min_value=2000, max_value=8000, value=3600) if oh_biliniyor else None

cevaplar["cw_pozisyon"] = st.sidebar.radio("Karşı Ağırlık Konum Kısıtı", ["Fark etmez", "Sadece yandan", "Sadece arkadan"])

# Öncelikler
st.sidebar.subheader("🎯 Öncelikler ve Kısıtlar")
mr_durum = st.sidebar.selectbox("Makine Dairesi Durumu", ["Mevcut / Planlanmış var", "Makine dairesi yok (MRL)", "Fark etmez"])
cevaplar["mr_var"] = True if "var" in mr_durum.lower() else (False if "yok" in mr_durum.lower() else None)
cevaplar["mrl_tercih"] = True if "yok" in mr_durum.lower() else False

cevaplar["butce"] = st.sidebar.select_slider("Bütçe Önceliği", options=["Ekonomik", "Orta", "Premium"], value="Orta")
cevaplar["enerji_onceligi"] = st.sidebar.select_slider("Enerji Verimliliği Önceliği", options=["Düşük", "Orta", "Yüksek"], value="Orta")

# Ekstra Seçenekler
st.sidebar.subheader("🛡️ Sismik & Yangın")
cevaplar["deprem_bolgesi"] = st.sidebar.checkbox("Deprem Bölgesi (Sismik Kısıt var)")
cevaplar["yangin_servisi"] = st.sidebar.checkbox("İtfaiyeci Servisi (EN 81-72)")

# ─────────────────────────────────────────────
#  SONUÇLARI EKRANA BASMA
# ─────────────────────────────────────────────
sonuclar = asansor_filtrele_ve_puanla(cevaplar)

if not sonuclar:
    st.error("✖ Girilen parametrelerle uyumlu standart sistem bulunamadı. Lütfen kısıtları gevşetiniz.")
else:
    st.subheader("📊 Önerilen Asansör Sistemleri")
    
    # En iyi 3 sonucu yan yana kartlar halinde gösterelim
    goster_sayisi = min(3, len(sonuclar))
    cols = st.columns(goster_sayisi)
    
    for sira, (puan, max_p, asansor) in enumerate(sonuclar[:goster_sayisi]):
        with cols[sira]:
            st.markdown(f"### #{sira+1} {asansor['kisa']}")
            st.info(f"**Uyum Puanı:** {puan} / {max_p}")
            
            # İlerleme Çubuğu (Progress Bar) ile puanı gösterelim
            st.progress(puan / max_p)
            
            st.write(f"**Tam Tanım:** {asansor['ad']}")
            st.write(f"⚡ **Maks Hız:** {asansor['hiz_max']} m/s")
            st.write(f"⚖️ **Kapasite:** {asansor['kapasite_min']}-{asansor['kapasite_max']} kg")
            st.write(f"↕️ **Min Pit:** {asansor['pit_min']} mm | **Min OH:** {asansor['overhead_min']} mm")
            
            st.success("**✔ Avantajlar:**\n" + "\n".join([f"- {av}" for av in asansor['avantajlar']]))
            st.warning("**⚠️ Dikkat Edilecekler:**\n" + "\n".join([f"- {dez}" for dez in asansor['dezavantajlar']]))
            st.help(f"💡 **Tipik Kullanım:** {asansor['tipik']}")

st.divider()
st.subheader("📋 Mühendislik Notları")
st.caption("- Bu analiz ön değerlendirme amacıyla hazırlanmıştır. Kesin seçim için lisanslı mühendis onayı gerekir.")
if cevaplar["deprem_bolgesi"]:
    st.warning("⚠ Sismik bölge aktif: EN 81-77 gereğince karşı ağırlık kilitleri ve kabin paten mukavemetleri artırılmalıdır.")
if cevaplar["yangin_servisi"]:
    st.warning("⚠ İtfaiyeci asansörü aktif: EN 81-72 kapsamında ayrı kuyu duvarı ve yangına dayanıklı kapı seçilmelidir.")