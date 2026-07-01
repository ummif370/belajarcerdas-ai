import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="BelajarCerdas AI",
    page_icon="📚",
    layout="wide"
)

api_key = os.getenv("GEMINI_API_KEY")

if api_key:
    genai.configure(api_key=api_key)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #eef6ff 0%, #ffffff 45%, #eaf3ff 100%);
}
.hero {
    padding: 55px 45px;
    border-radius: 28px;
    background: linear-gradient(135deg, #0f4c81, #1e88e5);
    color: white;
    margin-bottom: 30px;
}
.hero h1 {
    font-size: 52px;
    margin-bottom: 10px;
}
.hero p {
    font-size: 20px;
}
.card {
    background: white;
    padding: 25px;
    border-radius: 22px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}
.small-title {
    color: #0f4c81;
    font-weight: 700;
    font-size: 22px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>📚 BelajarCerdas AI</h1>
    <p>Setiap murid berhak mendapatkan cara belajar yang tepat.</p>
    <p>Landing page berbasis AI untuk membantu murid SMP menemukan strategi belajar yang sesuai dengan kebutuhannya.</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <div class="small-title">🎯 Target Pengguna</div>
        <p>Murid SMP, orang tua, dan guru pendamping belajar.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <div class="small-title">🤖 Bantuan AI</div>
        <p>AI memberi saran belajar, motivasi, dan jadwal belajar sederhana.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <div class="small-title">🌱 Dampak Sosial</div>
        <p>Membantu murid belajar lebih percaya diri dan terarah.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("## Mengapa proyek ini penting?")
st.write("""
Banyak murid mengalami kesulitan belajar, tetapi belum mengetahui cara belajar yang cocok.
Sebagian murid juga malu bertanya atau kehilangan motivasi ketika menghadapi pelajaran yang dianggap sulit.

**BelajarCerdas AI** hadir sebagai media sederhana untuk membantu murid memperoleh saran belajar awal
yang lebih personal, mudah dipahami, dan dapat langsung dicoba.
""")

st.markdown("## Cara Kerja")
c1, c2, c3 = st.columns(3)

with c1:
    st.info("1️⃣ Murid menuliskan kesulitan belajar.")

with c2:
    st.info("2️⃣ AI membaca kebutuhan murid.")

with c3:
    st.info("3️⃣ AI memberi saran belajar.")

st.markdown("## 🎓 Coba Asisten Belajar AI")

kesulitan = st.text_area(
    "Tuliskan kelas, mata pelajaran, dan kesulitan belajarmu:",
    placeholder="Contoh: Saya kelas VIII, sulit memahami pecahan dalam Matematika, dan hanya punya waktu belajar 1 jam setiap malam."
)

if st.button("Dapatkan Saran Belajar dari AI"):
    if not api_key:
        st.error("API Key belum terbaca. Pastikan file .env berisi GEMINI_API_KEY=API_KEY_ANDA")
    elif kesulitan.strip() == "":
        st.warning("Silakan tuliskan kesulitan belajar terlebih dahulu.")
    else:
        with st.spinner("AI sedang menyusun saran belajar..."):
            try:
                model = genai.GenerativeModel("gemini-2.5-flash")
                prompt = f"""
                Kamu adalah asisten belajar untuk murid SMP.
                Berikan jawaban dalam bahasa Indonesia yang ramah, sederhana, dan memotivasi.

                Masalah murid:
                {kesulitan}

                Susun jawaban dengan format rapi berikut:

# 📌 Ringkasan Masalah
Jelaskan inti kesulitan murid secara singkat.

# 🔍 Analisis Kebutuhan Belajar
Jelaskan kemungkinan penyebab kesulitan belajar dengan bahasa sederhana.

# 🎯 Strategi Belajar yang Disarankan
Berikan 5 strategi belajar yang mudah dilakukan murid SMP.

# 📅 Jadwal Belajar 7 Hari
Buat jadwal belajar sederhana selama 7 hari, maksimal 1 jam per hari.

# 💡 Tips Tambahan
Berikan tips agar murid tidak mudah bosan dan tetap semangat.

# ❤️ Motivasi
Berikan kalimat penyemangat yang lembut dan membangun percaya diri.

# 🤲 Doa Sebelum Belajar
Tuliskan doa pendek sebelum belajar.
                """

                response = model.generate_content(prompt)
                st.success("Berikut saran dari AI:")
                st.markdown(response.text)

            except Exception as e:
                st.error("Terjadi kendala saat menghubungi Gemini AI.")
                st.write(e)

st.divider()
st.caption("Proyek Akhir Basic AI | Perempuan Inovasi x IBM SkillsBuild | Dibuat oleh Hj. Ummi Salmah")
