import streamlit as st

# Konfigurasi Halaman Web
st.set_page_config(
    page_title="Pabrik Konten AI - Affiliate Studio",
    page_icon="🎬",
    layout="centered"
)

# Perbaikan Styling: Kotak kontras terang & teks jelas terbaca
st.markdown("""
    <style>
    .main {
        background-color: #0f1117;
        color: #ffffff;
    }
    .stButton>button {
        background: linear-gradient(90deg, #7c3aed, #a855f7);
        color: white;
        border: none;
        border-radius: 8px;
        font-weight: bold;
        padding: 0.6rem 1rem;
        width: 100%;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #6d28d9, #9333ea);
        color: #fff;
    }
    /* Kotak kartu hasil frame dengan latar terang agar teks sangat jelas */
    .frame-card {
        background-color: #ffffff;
        color: #1f2937;
        padding: 20px;
        border-radius: 12px;
        border: 2px solid #7c3aed;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .frame-card h4 {
        color: #6d28d9;
        margin-top: 0;
    }
    </style>
""", unsafe_allow_html=True)

# Judul Aplikasi
st.title("🎬 Pabrik Konten AI Studio")
st.markdown("Pencetak storyboard & skrip video affiliate otomatis, cepat, dan siap pakai.")
st.markdown("---")

# --- INPUT UTAMA ---
uploaded_file = st.file_uploader("📸 Upload Foto Produk di Sini", type=["jpg", "jpeg", "png"])

col1, col2 = st.columns(2)
with col1:
    ad_style = st.selectbox(
        "Pilih Gaya Promosi",
        [
            "Soft Selling",
            "Hard Selling",
            "UGC Unboxing Fast",
            "Problem-Solution",
            "Before-After",
            "FOMO / Urgensi Ekstrem",
            "POV (Point of View)",
            "Educational / Racun Edukasi"
        ]
    )
    
    duration = st.selectbox(
        "Pilih Durasi Video",
        ["10 Detik (1 Frame)", "20 Detik (2 Frame Bersambung)", "30 Detik (3 Frame Bersambung)"]
    )

with col2:
    location_type = st.selectbox(
        "Pilih Lokasi Syuting (Opsional)",
        ["Auto / Menyesuaikan Produk", "Indoor (Kamar / Studio Estetik)", "Outdoor (Alam / Jalanan / Kafe)"]
    )
    
    talent_ref = st.text_input(
        "Referensi Talent Kustom (Opsional)",
        placeholder="Contoh: Model wanita lokal, hijab pastel..."
    )

st.markdown("<br>", unsafe_allow_html=True)
generate_btn = st.button("✨ Generate Storyboard Sekarang")

# --- PROSES & HASIL OUTPUT ---
if generate_btn:
    if uploaded_file is not None:
        st.success("✅ Foto produk berhasil dianalisis! Silakan salin naskah di bawah:")
        st.markdown("---")
        
        loc_desc = f"Setting lokasi: {location_type}." if location_type != "Auto / Menyesuaikan Produk" else ""
        
        if "10 Detik" in duration:
            st.markdown(f"""
            <div class="frame-card">
                <h4><b>Frame 1 (0-10s) — Format Padat Tunggal</b></h4>
                <p><b>🎬 Prompt Visual & Sinematik:</b><br>
                Cinematic 4k, close up product, professional lighting, clean aesthetic. {loc_desc} Talent menunjukkan produk dengan ekspresi antusias.</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.text_area("📋 Naskah & Dialog (Sekali Copy - Frame 1):", 
                         "Wah gila sih ini, bener-bener penyelamat banget buat atasi masalah kita sehari-hari! Kualitasnya juara dan gampang banget dipakai. Mumpung lagi ada promo, buruan chekout sekarang sebelum kehabisan di keranjang kuning!", 
                         height=100)
            
            st.code("Google Flow Video Prompt:\nDynamic product showcase, fast paced transition, 4k resolution, smooth camera movement.", language="text")
            
        elif "20 Detik" in duration:
            st.markdown(f"""
            <div class="frame-card">
                <h4><b>Frame 1 (0-10s) — Hook & Masalah Awal</b></h4>
                <p><b>🎬 Prompt Visual & Sinematik:</b><br>
                Unboxing package moment, aesthetic desk setup, bright lighting. {loc_desc} Talent membuka paket dengan ekspresi penasaran.</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.text_area("📋 Naskah & Dialog (Sekali Copy - Frame 1):", 
                         "Sumpah kaget banget pas paket ini datang, sebagus itu! Buat kalian yang sering punya masalah sama hal kayak gini, wajib banget tonton video ini sampai habis.", 
                         height=90)
            st.code("Google Flow Prompt 1:\nUnboxing package, close up hands opening box, bright aesthetic lighting.", language="text")
            
            st.markdown(f"""
            <div class="frame-card" style="margin-top: 20px;">
                <h4><b>Frame 2 (10-20s) — Solusi & Call to Action (CTA)</b></h4>
                <p><b>🎬 Prompt Visual & Sinematik:</b><br>
                Product in action, happy expression, smooth transition. {loc_desc} Talent menunjukkan hasil produk dan menunjuk keranjang kuning.</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.text_area("📋 Naskah & Dialog (Sekali Copy - Frame 2):", 
                         "Setelah dicoba, hasilnya beneran di luar dugaan! Gampang dipakai, hemat waktu, dan awet banget. Mumpung stok masih ada dan lagi diskon, langsung klik keranjang kuning di bawah ya!", 
                         height=90)
            st.code("Google Flow Prompt 2:\nProduct demonstration, smiling model pointing down, high conversion e-commerce style.", language="text")
            
        else: # 30 Detik
            st.markdown(f"""
            <div class="frame-card">
                <h4><b>Frame 1 (0-10s) — Hook & Unboxing</b></h4>
                <p><b>🎬 Prompt Visual & Sinematik:</b><br>
                Dynamic hook scene, aesthetic opening. {loc_desc} Talent memegang produk dengan ekspresi takjub.</p>
            </div>
            """, unsafe_allow_html=True)
            st.text_area("📋 Naskah & Dialog (Frame 1):", "Jangan beli barang ini sebelum kalian tahu rahasia kelebihannya! Paketnya udah nyampe dan kita langsung buktikan sekarang.", height=80)
            
            st.markdown(f"""
            <div class="frame-card" style="margin-top: 20px;">
                <h4><b>Frame 2 (10-20s) — Ulasan & Bukti Keunggulan</b></h4>
                <p><b>🎬 Prompt Visual & Sinematik:</b><br>
                Detailed product close-up, functional demonstration. {loc_desc}</p>
            </div>
            """, unsafe_allow_html=True)
            st.text_area("📋 Naskah & Dialog (Frame 2):", "Tekstur dan kualitasnya beda banget dari pasaran. Pas dicoba, langsung terasa bedanya dalam hitungan detik aja.", height=80)
            
            st.markdown(f"""
            <div class="frame-card" style="margin-top: 20px;">
                <h4><b>Frame 3 (20-30s) — Solusi Tuntas & CTA</b></h4>
                <p><b>🎬 Prompt Visual & Sinematik:</b><br>
                Satisfied closing, pointing gesture to yellow basket. {loc_desc}</p>
            </div>
            """, unsafe_allow_html=True)
            st.text_area("📋 Naskah & Dialog (Frame 3):", "Udah harganya ramah di kantong, garansi kualitas pula. Yuk buruan amankan stoknya, klik keranjang kuning sekarang juga!", height=80)
            st.code("Google Flow Video Prompt (Full 30s):\nHigh conversion e-commerce video sequence, smooth transitions, professional color grading.", language="text")
            
    else:
        st.warning("⚠️ Silakan upload foto produk terlebih dahulu di atas, Boss!")
else:
    st.info("👆 Silakan lengkapi pilihan di atas, upload foto produk, lalu klik tombol **Generate Storyboard**.")
