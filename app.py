import streamlit as st

# Konfigurasi Halaman Web
st.set_page_config(
    page_title="Pabrik Konten AI - Ultimate Studio",
    page_icon="🔥",
    layout="centered"
)

# Styling CSS Biar Tampilan Makin Gahar & Nyaman Dibaca
st.markdown("""
    <style>
    .main {
        background-color: #0b0f19;
        color: #ffffff;
    }
    .stButton>button {
        background: linear-gradient(90deg, #7c3aed, #ec4899);
        color: white;
        border: none;
        border-radius: 10px;
        font-weight: bold;
        padding: 0.7rem 1rem;
        width: 100%;
        box-shadow: 0 4px 12px rgba(124, 58, 237, 0.3);
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #6d28d9, #db2777);
        color: #fff;
    }
    .frame-card {
        background-color: #ffffff;
        color: #111827;
        padding: 22px;
        border-radius: 14px;
        border: 2px solid #7c3aed;
        margin-bottom: 20px;
        box-shadow: 0 6px 15px rgba(0,0,0,0.15);
    }
    .frame-card h4 {
        color: #7c3aed;
        margin-top: 0;
        font-weight: 800;
    }
    </style>
""", unsafe_allow_html=True)

# Judul Utama Aplikasi
st.title("🔥 Pabrik Konten AI Ultimate Studio")
st.markdown("Mesin pencetak storyboard, skrip sinematik, dan prompt video affiliate otomatis paling gacor.")
st.markdown("---")

# --- AREA UTAMA: INPUT LANGSUNG DI MUKA ---
uploaded_file = st.file_uploader("📸 Upload Foto Produk Utama", type=["jpg", "jpeg", "png"])

col1, col2 = st.columns(2)
with col1:
    ad_style = st.selectbox(
        "🎯 Pilih Gaya Promosi (Marketing Style)",
        [
            "Soft Selling (Natural & Emosional)",
            "Hard Selling (Tegas & Diskon Kilat)",
            "UGC Unboxing Fast (Review Cepat & Asli)",
            "Problem-Solution (Nembak Masalah)",
            "Before-After (Transformasi Nyata)",
            "FOMO / Urgensi Ekstrem (Takut Kehabisan)",
            "POV (Point of View Pengguna)",
            "Educational / Racun Edukasi"
        ]
    )
    
    duration = st.selectbox(
        "⏱️ Pilih Durasi Video",
        [
            "10 Detik (1 Frame Padat)", 
            "20 Detik (2 Frame Bersambung)", 
            "30 Detik (3 Frame Bersambung)"
        ]
    )

with col2:
    location_type = st.selectbox(
        "📍 Pilih Lokasi Syuting (Opsional)",
        [
            "Auto / Menyesuaikan Karakter Produk",
            "Indoor (Kamar Minimalis / Studio Estetik)",
            "Outdoor (Kafe Hits / Alam Terbuka / Jalanan)"
        ]
    )
    
    talent_ref = st.text_input(
        "👤 Referensi Talent Kustom (Opsional)",
        placeholder="Cth: Model lokal, casual, hijab pastel..."
    )

st.markdown("<br>", unsafe_allow_html=True)
generate_btn = st.button("🚀 GENERATE STORYBOARD SEKARANG")

# --- PROSES & HASIL OUTPUT ---
if generate_btn:
    if uploaded_file is not None:
        st.success(f"✅ Analisis produk sukses! Gaya: **{ad_style.split(' ')[0]}** | Durasi: **{duration}**")
        st.markdown("---")
        
        loc_desc = f"Setting lokasi syuting di {location_type}." if "Auto" not in location_type else "Setting lokasi natural sesuai produk."
        talent_desc = f"Karakter talent: {talent_ref}." if talent_ref else "Karakter talent profesional standar."
        
        # Logika Berdasarkan Pilihan Durasi
        if "10 Detik" in duration:
            st.markdown(f"""
            <div class="frame-card">
                <h4><b>🎬 Frame 1 (0-10s) — Format Padat & Menusuk</b></h4>
                <p><b>Visual & Sinematik:</b><br>
                {loc_desc} {talent_desc} Kamera menyorot produk dengan sudut pandang dinamis, pencahayaan terang dan estetik, ekspresi sangat antusias.</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.text_area("📋 Naskah & Dialog (Sekali Copy - Frame 1):", 
                         "Wah gila sih ini, bener-bener penyelamat banget buat atasi masalah kita sehari-hari! Kualitasnya juara, praktis, dan gampang banget dipakai. Mumpung lagi ada promo spesial, buruan checkout sekarang sebelum kehabisan di keranjang kuning!", 
                         height=110)
            
            st.code("Google Flow Video Prompt:\nCinematic 4k e-commerce shot, dynamic product showcase, fast paced transition, perfect lighting.", language="text")
            
        elif "20 Detik" in duration:
            st.markdown(f"""
            <div class="frame-card">
                <h4><b>🎬 Frame 1 (0-10s) — Hook Kuat & Masalah Awal</b></h4>
                <p><b>Visual & Sinematik:</b><br>
                {loc_desc} {talent_desc} Adegan awal unboxing cepat, memperlihatkan ekspresi penasaran dan menyorot masalah yang sering dialami penonton.</p>
            </div>
            """, unsafe_allow_html=True)
            st.text_area("📋 Naskah & Dialog (Sekali Copy - Frame 1):", 
                         "Sumpah kaget banget pas paket ini datang, sebagus itu aslinya! Buat kalian yang sering banget ngalamin masalah ini, wajib banget tonton video ini sampai habis.", 
                         height=95)
            st.code("Google Flow Video Prompt 1:\nUnboxing package moment, close up hands opening box, bright aesthetic room, curious facial expression.", language="text")
            
            st.markdown(f"""
            <div class="frame-card" style="margin-top: 25px;">
                <h4><b>🎬 Frame 2 (10-20s) — Solusi Tuntas & CTA</b></h4>
                <p><b>Visual & Sinematik:</b><br>
                {loc_desc} {talent_desc} Demonstrasi produk beraksi secara nyata, hasil instan yang memuaskan, ditutup gestur menunjuk ke keranjang kuning.</p>
            </div>
            """, unsafe_allow_html=True)
            st.text_area("📋 Naskah & Dialog (Sekali Copy - Frame 2):", 
                         "Setelah dicoba sendiri, hasilnya beneran di luar dugaan! Gampang dipakai, hemat waktu, dan awet banget. Mumpung stok masih ada dan lagi diskon kilat, langsung klik keranjang kuning di bawah ya!", 
                         height=95)
            st.code("Google Flow Video Prompt 2:\nProduct in action demonstration, happy smiling model pointing down, high conversion e-commerce style, smooth cut.", language="text")
            
        else: # 30 Detik
            st.markdown(f"""
            <div class="frame-card">
                <h4><b>🎬 Frame 1 (0-10s) — Hook & Unboxing Perdana</b></h4>
                <p><b>Visual & Sinematik:</b><br>{loc_desc} {talent_desc} Pembuka sinematik yang memancing rasa penasaran penonton.</p>
            </div>
            """, unsafe_allow_html=True)
            st.text_area("📋 Naskah & Dialog (Frame 1):", "Jangan beli barang ini sebelum kalian tahu rahasia kelebihannya! Paketnya udah nyampe dan kita langsung buktikan sekarang.", height=85)
            
            st.markdown(f"""
            <div class="frame-card" style="margin-top: 25px;">
                <h4><b>🎬 Frame 2 (10-20s) — Ulasan Mendalam & Bukti</b></h4>
                <p><b>Visual & Sinematik:</b><br>{loc_desc} {talent_desc} Close-up detail keunggulan produk secara fungsional.</p>
            </div>
            """, unsafe_allow_html=True)
            st.text_area("📋 Naskah & Dialog (Frame 2):", "Tekstur dan kualitas bahannya beda banget dari pasaran. Pas dicoba, langsung terasa bedanya dalam hitungan detik aja.", height=85)
            
            st.markdown(f"""
            <div class="frame-card" style="margin-top: 25px;">
                <h4><b>🎬 Frame 3 (20-30s) — Solusi Akhir & CTA Keranjang Kuning</b></h4>
                <p><b>Visual & Sinematik:</b><br>{loc_desc} {talent_desc} Penutup manis dengan gestur kuat mengarah ke keranjang kuning.</p>
            </div>
            """, unsafe_allow_html=True)
            st.text_area("📋 Naskah & Dialog (Frame 3):", "Udah harganya ramah di kantong, garansi kualitas pula. Yuk buruan amankan stoknya sebelum kehabisan, klik keranjang kuning sekarang juga!", height=85)
            
            st.code("Google Flow Video Prompt (Full 30s Sequence):\nHigh conversion e-commerce video sequence, smooth multi-angle transitions, professional color grading, 4k.", language="text")
            
    else:
        st.warning("⚠️ Boss, silakan upload foto produknya dulu di bagian atas sebelum pencet tombol generate!")
else:
    st.info("👆 Lengkapi pilihan gaya, durasi, lokasi, lalu upload foto produk dan klik tombol **GENERATE STORYBOARD SEKARANG**.")
