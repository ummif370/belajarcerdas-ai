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
    background: linear-gradient(135deg, #eef6ff, #ffffff, #eaf3ff);
}
.hero {
    background: linear-gradient(135deg, #0f4c81, #1e88e5);
    color: white;
    padding: 55px;
    border-radius: 30px;
    margin-bottom: 30px;
}
.hero h1 {
    font-size: 56px;
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
    margin-bottom: 18px;
}
.card-title {
    font-size: 22px;
    font-weight: bold;
    color: #0f4c81;
}
.stat {
    background: white;
    text-align: center;
    padding: 25px;
    border-radius: 22px;
    box-shadow: 0 8px 22px rgba(0,0,0,0.07);
}
.stat h2 {
    color: #0f4c81;
    font-size: 34px;
}
.footer {
    text-align: center;
    color: #666;
    padding: 25px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>📚 BelajarCerdas AI</h1>
    <p><b>Setiap murid berhak mendapatkan strategi belajar yang tepat.</b></p>
    <p>Landing page berbasis Artificial Intelligence untuk membantu murid SMP menemukan cara belajar yang sesuai dengan kebutuhan, waktu, dan target belajarnya.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("## 📊 Dampak dan Manfaat")

s1, s2, s3, s4 = st.columns(4)
with s1:
    st.markdown('<div class="stat"><h2>500+</h2><p>Murid Terbantu</p></div>', unsafe_allow_html=True)
with s2:
    st.markdown('<div class="stat"><h2>24 Jam</h2><p>AI Siap Membantu</p></div>', unsafe_allow_html=True)
with s3:
    st.markdown('<div class="stat"><h2>100+</h2><p>Strategi Belajar</p></div>', unsafe_allow_html=True)
with s4:
    st.markdown('<div class="stat"><h2>Gratis</h2><p>Mudah Diakses</p></div>', unsafe_allow_html=True)

st.markdown("## 🎯 Mengapa Proyek Ini Penting?")
st.write("""
Banyak murid SMP mengalami kesulitan belajar, kehilangan motivasi, atau belum mengetahui metode belajar yang sesuai.
Tidak semua murid memiliki akses ke bimbingan belajar atau pendampingan pribadi.

**BelajarCerdas AI** hadir sebagai solusi edukatif berbasis AI untuk memberikan saran belajar yang personal,
mudah dipahami, dan dapat digunakan kapan saja oleh murid, orang tua, maupun guru pendamping.
""")

st.markdown("## ⚙️ Cara Kerja")
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown('<div class="card"><div class="card-title">1️⃣ Isi Data</div><p>Murid mengisi kelas, mata pelajaran, target nilai, waktu belajar, dan kesulitan yang dialami.</p></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="card"><div class="card-title">2️⃣ AI Menganalisis</div><p>AI membaca kebutuhan belajar murid dan memahami masalah yang dihadapi.</p></div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="card"><div class="card-title">3️⃣ Strategi Muncul</div><p>AI memberikan strategi belajar, jadwal, motivasi, dan doa sebelum belajar.</p></div>', unsafe_allow_html=True)

st.markdown("## 🤖 Konsultasi Belajar dengan AI")

with st.form("form_ai"):
    nama = st.text_input("Nama Murid", placeholder="Contoh: Aulia")
    kelas = st.selectbox("Kelas", ["VII", "VIII", "IX"])
    mapel = st.selectbox(
        "Mata Pelajaran",
        ["Matematika", "Bahasa Indonesia", "Bahasa Inggris", "IPA", "IPS", "Pendidikan Pancasila", "Agama", "Informatika"]
    )
    target = st.slider("Target Nilai", 70, 100, 85)
    waktu = st.selectbox("Waktu Belajar per Hari", ["30 menit", "45 menit", "1 jam", "1,5 jam", "2 jam"])
    kesulitan = st.text_area(
        "Tuliskan kesulitan belajar",
        placeholder="Contoh: Saya sulit memahami pecahan dan sering bingung saat mengerjakan soal cerita."
    )

    tombol = st.form_submit_button("🚀 Dapatkan Strategi Belajar dari AI")

if tombol:
    if not api_key:
        st.error("API Key belum terbaca. Pastikan file .env berisi GEMINI_API_KEY=API_KEY_ANDA")
    elif kesulitan.strip() == "":
        st.warning("Silakan isi kesulitan belajar terlebih dahulu.")
    else:
        with st.spinner("AI sedang menyusun strategi belajar terbaik..."):
            try:
                model = genai.GenerativeModel("gemini-2.0-flash")

                prompt = f"""
Kamu adalah Guru Pendamping Belajar AI untuk murid SMP.
Jawab dalam bahasa Indonesia yang ramah, sederhana, sopan, dan memotivasi.

Data murid:
Nama: {nama}
Kelas: {kelas}
Mata pelajaran: {mapel}
Target nilai: {target}
Waktu belajar per hari: {waktu}
Kesulitan belajar: {kesulitan}

Susun jawaban dengan format berikut:

# 📌 Ringkasan Masalah
Jelaskan inti masalah murid secara singkat.

# 🔍 Analisis Kebutuhan Belajar
Jelaskan kemungkinan penyebab kesulitan belajar dengan bahasa sederhana.

# 🎯 Strategi Belajar yang Disarankan
Berikan 5 strategi belajar yang mudah dilakukan murid SMP.

# 🧠 Metode Belajar yang Cocok
Pilih dan jelaskan salah satu metode: Pomodoro, Active Recall, Mind Mapping, Feynman Technique, atau Spaced Repetition.

# 📅 Jadwal Belajar 7 Hari
Buat jadwal belajar sederhana selama 7 hari sesuai waktu belajar murid.

# 📖 Materi yang Perlu Diprioritaskan
Tuliskan bagian materi yang perlu dikuatkan.

# 🔎 Rekomendasi Kata Kunci Belajar
Berikan 3 kata kunci yang bisa dicari di YouTube atau Google.

# 💡 Tips Tambahan
Berikan tips agar murid tidak mudah bosan dan tetap semangat.

# ❤️ Motivasi
Berikan kalimat penyemangat yang lembut dan membangun percaya diri.

# 🤲 Doa Sebelum Belajar
Tuliskan doa pendek sebelum belajar.
"""

                response = model.generate_content(prompt)

                st.success("Berikut strategi belajar dari AI:")
                st.markdown(response.text)

            except Exception as e:
                st.error("Terjadi kendala saat menghubungi Gemini AI.")
                st.write(e)

st.markdown("## 🌱 Manfaat Sosial")
m1, m2, m3 = st.columns(3)
with m1:
    st.markdown('<div class="card"><div class="card-title">👩‍🎓 Untuk Murid</div><p>Membantu murid lebih percaya diri dan memiliki arah belajar yang jelas.</p></div>', unsafe_allow_html=True)
with m2:
    st.markdown('<div class="card"><div class="card-title">👨‍👩‍👧 Untuk Orang Tua</div><p>Membantu orang tua mendampingi anak belajar di rumah.</p></div>', unsafe_allow_html=True)
with m3:
    st.markdown('<div class="card"><div class="card-title">👩‍🏫 Untuk Guru</div><p>Menjadi alat bantu awal untuk memahami kebutuhan belajar murid.</p></div>', unsafe_allow_html=True)

st.divider()

st.markdown("""
<div class="footer">
    <b>BelajarCerdas AI</b><br>
    Proyek Akhir Basic AI - Perempuan Inovasi x IBM SkillsBuild<br>
    Dibuat oleh Hj. Ummi Salmah<br>
    Teknologi: Streamlit + Google Gemini AI
</div>
""", unsafe_allow_html=True)