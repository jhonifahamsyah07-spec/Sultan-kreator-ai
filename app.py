import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Sultan Kreator AI Studio", layout="centered")

st.title("Sultan Kreator AI Studio")
st.write("Pencetak storyboard & skrip video affiliate otomatis, cepat, dan siap pakai.")

uploaded_file = st.file_uploader("Upload Foto Produk di Sini", type=["png", "jpg", "jpeg"])
product_name_input = st.text_input("Nama Produk (Opsional)", placeholder="Contoh: Serum Glowing X")
promo_style = st.selectbox("Pilih Gaya Promosi", ["Soft Selling", "Hard Selling", "UGC Unboxing", "Problem-Solution", "Before-After", "FOMO", "POV"])
duration = st.selectbox("Pilih Durasi Video", ["10 Detik (1 Frame)", "20 Detik (2 Frame)", "30 Detik (3 Frame)"])

if st.button("Generate Storyboard"):
    if uploaded_file is not None:
        with st.spinner("Sedang menganalisis produk dan meracik skrip..."):
            try:
                system_instruction = """
                Kamu adalah AI Content Director profesional untuk affiliate marketer. 
                Tugasmu adalah menganalisis foto produk yang diunggah dan merumuskan storyboard video short-form.
                
                ATURAN FORMAT OUTPUT (WAJIB DIPATUHI):
                - JANGAN gunakan teks pengantar, basa-basi, atau penutup.
                - Format output WAJIB HANYA berisi dua elemen inti per frame agar bisa disalin sekali klik:
                  1. Prompt Visual & Sinematik
                  2. Naskah & Dialog (Sekali Copy)
                - WAJIB menyebutkan nama produk secara spesifik di dalam prompt visual dan naskah dialog. Jangan gunakan template kosong.
                """

                user_prompt = f"""
                Buatkan storyboard untuk produk di foto ini.
                - Nama Produk Tambahan: {product_name_input if product_name_input else "Deteksi otomatis dari foto"}
                - Gaya Promosi: {promo_style}
                - Durasi Target: {duration}
                """

                model = genai.GenerativeModel(
                    model_name="gemini-2.5-flash",
                    system_instruction=system_instruction
                )
                
                image_bytes = uploaded_file.getvalue()
                image_part = {
                    "mime_type": uploaded_file.type,
                    "data": image_bytes
                }
                
                response = model.generate_content([image_part, user_prompt])
                
                st.success("Foto produk berhasil dianalisis! Silakan salin naskah di bawah:")
                st.markdown("---")
                st.markdown(response.text)
                
            except Exception as e:
                st.error(f"Terjadi kesalahan saat memproses: {e}")
    else:
        st.warning("Silakan upload foto produk terlebih dahulu!")
