import os
import streamlit as st
from google import genai

# Konfigurasi halaman Streamlit
st.set_page_config(page_title="AI Storyboard Generator", page_icon="🎬", layout="centered")

st.title("🎬 AI Storyboard Generator")
st.write("Buat storyboard otomatis untuk konten video Anda dengan mudah.")

# Ambil API key dari st.secrets (pastikan sudah diset di Streamlit Cloud Settings)
api_key = st.secrets.get("GEMINI_API_KEY")

if not api_key:
    st.error("⚠️ GEMINI_API_KEY belum diset di Streamlit Secrets! Silakan atur terlebih dahulu di pengaturan aplikasi Anda.")
else:
    # Inisialisasi klien Gemini resmi terbaru
    client = genai.Client(api_key=api_key)

    # Input dari user
    user_prompt = st.text_area("Masukkan ide atau topik video Anda:", placeholder="Contoh: Tips hemat bulanan untuk anak kos, gaya santai, durasi 30 detik.")

    if st.button("🚀 Generate Storyboard", type="primary"):
        if not user_prompt.strip():
            st.warning("⚠️ Mohon masukkan ide videonya terlebih dahulu.")
        else:
            # Spinner agar ada indikator proses berjalan (tidak kelihatan nge-hang)
            with st.spinner("⏳ Sedang meracik storyboard terbaik untuk Anda... Mohon tunggu sebentar."):
                try:
                    # Menggunakan model gemini-2.5-flash yang stabil dan cepat
                    response = client.models.generate_content(
                        model="gemini-2.5-flash",
                        contents=f"Buatkan storyboard video yang menarik, terstruktur (Scene, Visual, Audio/Voiceover) berdasarkan ide berikut: {user_prompt}"
                    )
                    
                    st.success("✨ Storyboard berhasil dibuat!")
                    st.markdown("---")
                    st.markdown(response.text)
                    
                except Exception as e:
                    st.error(f"❌ Terjadi kesalahan pada API: {e}")
