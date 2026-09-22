import streamlit as st
import pandas as pd
import numpy as np
import math

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent



def statistika_masyarakat():
    st.header("📊 Statistika dalam Kehidupan Masyarakat")
    st.info("Materi akan dikembangkan.")


def matematika_ekonomi():
    st.header("💰 Matematika Ekonomi dan Budaya")
    st.info("Materi akan dikembangkan.")



def geometri_budaya():

    st.markdown(
        '<div class="content-title">📐 Geometri dalam Budaya</div>',
        unsafe_allow_html=True
    )

    # ==========================================================
    # MATERI
    # ==========================================================

    st.header("🌿 Mengenal Geometri dalam Budaya")

    st.markdown("""
    Geometri tidak hanya ditemukan dalam buku matematika.
    Berbagai bentuk geometri dapat ditemukan dalam **karya seni,
    arsitektur, kerajinan, teknologi tradisional, dan kehidupan
    masyarakat**.

    Kajian hubungan antara matematika dan budaya dapat menjadi bagian
    dari **etnomatematika**.

    Dalam budaya Indonesia, konsep geometri dapat ditemukan pada:

    - motif tenun;
    - motif batik;
    - rumah tradisional;
    - arsitektur kesultanan;
    - bubu atau alat tangkap tradisional;
    - perahu tradisional;
    - ornamen dan kerajinan masyarakat.
    """)

    st.header("🔷 Bentuk Geometri dalam Budaya")

    st.markdown("""
    Berbagai bangun geometri dapat ditemukan pada objek budaya.

    **Persegi**  
    Dapat ditemukan pada pola motif, lantai, atau ornamen.

    **Persegi panjang**  
    Dapat digunakan untuk memodelkan kain, lantai rumah,
    pintu, jendela, atau bagian perahu.

    **Segitiga**  
    Dapat ditemukan pada motif, ornamen, dan bentuk atap.

    **Lingkaran**  
    Dapat ditemukan pada penampang bubu, ornamen, dan berbagai
    pola budaya.

    **Segi banyak**  
    Misalnya segi delapan pada unsur arsitektur tertentu.

    **Bangun ruang**  
    Balok, prisma, tabung, dan kerucut dapat digunakan sebagai
    model sederhana berbagai benda budaya.
    """)

    st.header("🧵 Geometri pada Tenun")

    st.markdown("""
    Motif tenun dapat mengandung garis, titik, bidang, dan pola
    yang berulang.

    Pola geometris dapat dibentuk melalui pengulangan suatu motif
    secara horizontal, vertikal, atau diagonal.

    Contoh konsep matematika yang dapat dipelajari:

    - panjang dan lebar;
    - luas;
    - keliling;
    - sudut;
    - simetri;
    - pola berulang;
    - transformasi geometri.
    """)

    st.header("🎨 Geometri pada Batik")

    st.markdown("""
    Banyak motif batik memiliki bentuk geometris dan pola yang teratur.

    Motif dapat dianalisis menggunakan:

    **Translasi** → menggeser motif.

    **Rotasi** → memutar motif.

    **Refleksi** → mencerminkan motif.

    **Dilatasi** → memperbesar atau memperkecil motif.

    Penggunaan transformasi tersebut dapat menghasilkan pola yang
    berulang dan memenuhi bidang kain.
    """)

    st.header("🏠 Geometri pada Rumah Tradisional")

    st.markdown("""
    Rumah tradisional dapat digunakan sebagai objek pengukuran.

    Contohnya:

    - lantai → persegi panjang;
    - jendela → persegi atau persegi panjang;
    - tiang → balok atau tabung;
    - atap → segitiga atau prisma;
    - tangga → dapat dimodelkan sebagai segitiga siku-siku.

    Dengan demikian, siswa dapat mempelajari luas, keliling, volume,
    panjang, tinggi, sudut, dan skala melalui objek budaya.
    """)

    st.header("🕌 Geometri pada Arsitektur Kesultanan")

    st.markdown("""
    Arsitektur kesultanan juga memiliki berbagai unsur geometris.

    Contohnya dapat berupa:

    - persegi;
    - persegi panjang;
    - segitiga;
    - lingkaran;
    - segi banyak;
    - bentuk ruang;
    - pola ornamen;
    - simetri.

    Sebagai contoh, gerbang berbentuk segi delapan dapat digunakan
    untuk mempelajari jumlah sisi, jumlah sudut, keliling, dan
    simetri.
    """)

    st.header("🐟 Geometri pada Bubu")

    st.markdown("""
    Bubu merupakan contoh teknologi tradisional yang dapat dimodelkan
    menggunakan geometri ruang.

    Bagian badan bubu dapat disederhanakan sebagai:

    - tabung;
    - kerucut;
    - kerucut terpancung;
    - gabungan beberapa bangun ruang.

    Pola anyaman juga dapat dianalisis menggunakan garis, sudut,
    jarak, pengulangan, dan simetri.
    """)

    st.header("🛶 Geometri pada Perahu")

    st.markdown("""
    Perahu tradisional memiliki bentuk yang kompleks sehingga dapat
    disederhanakan menjadi model matematika.

    Bagian tertentu dapat dimodelkan menggunakan:

    - persegi panjang;
    - segitiga;
    - trapesium;
    - prisma;
    - gabungan bangun ruang.

    Pengukuran panjang, lebar, tinggi, kedalaman, luas, volume,
    dan perbandingan dapat digunakan untuk menganalisis bentuk perahu.
    """)

    st.header("🔄 Transformasi Geometri dalam Budaya")

    st.markdown("""
    Salah satu konsep penting dalam geometri budaya adalah
    **transformasi geometri**.

    Transformasi dapat digunakan untuk menjelaskan bagaimana suatu
    motif atau bentuk menghasilkan pola baru.

    **Translasi** → pergeseran.

    **Rotasi** → perputaran.

    **Refleksi** → pencerminan.

    **Dilatasi** → perubahan ukuran dengan faktor skala.
    """)

    st.latex(r"T(x,y)=(x+a,y+b)")

    st.markdown("""
    Persamaan tersebut merupakan contoh translasi titik sebesar
    $(a,b)$.

    Misalnya titik $(2,3)$ ditranslasikan 4 satuan ke kanan dan
    2 satuan ke atas.
    """)

    st.latex(r"(2,3)\rightarrow(2+4,3+2)=(6,5)")

    st.header("🪞 Simetri dalam Budaya")

    st.markdown("""
    Simetri merupakan keteraturan bentuk yang dapat ditemukan pada
    banyak objek budaya.

    Dua konsep yang mudah diamati adalah:

    **Simetri lipat**  
    Suatu bentuk dapat dilipat sehingga dua bagiannya berimpit.

    **Simetri putar**  
    Suatu bentuk dapat diputar dengan sudut tertentu dan kembali
    berimpit dengan bentuk awal.
    """)

    st.header("📏 Skala dalam Budaya")

    st.markdown("""
    Skala digunakan ketika objek budaya dibuat dalam bentuk gambar,
    maket, miniatur, atau model.

    Misalnya sebuah rumah memiliki panjang sebenarnya 20 m dan
    dibuat dengan skala 1 : 100.
    """)

    st.latex(r"Panjang\ model=\frac{20}{100}=0,2\text{ m}=20\text{ cm}")

    st.markdown("""
    Dengan demikian, panjang rumah pada model adalah **20 cm**.
    """)

    st.header("📊 Perbandingan dalam Bentuk Budaya")

    st.markdown("""
    Perbandingan dapat digunakan untuk membandingkan ukuran bagian
    suatu objek budaya.

    Misalnya sebuah perahu memiliki panjang 8 m dan lebar 1 m.
    """)

    st.latex(r"Panjang:Lebar=8:1")

    st.markdown("""
    Perbandingan tersebut menunjukkan bahwa bentuk perahu lebih
    panjang daripada lebarnya.
    """)

    st.header("🧮 Contoh Perhitungan Geometri")

    st.markdown("""
    Sebuah motif budaya berbentuk persegi dengan sisi 10 cm.
    """)
    st.latex(r"L=s^2=10^2=100\text{ cm}^2")

    st.markdown("""
    Kelilingnya:
    """)
    st.latex(r"K=4s=4(10)=40\text{ cm}")

    st.markdown("""
    Contoh sederhana tersebut menunjukkan bahwa objek budaya dapat
    digunakan untuk mempelajari konsep luas dan keliling.
    """)

    st.header("🌏 Etnomatematika")

    st.markdown("""
    Etnomatematika memandang matematika sebagai sesuatu yang dapat
    dipelajari melalui aktivitas dan praktik budaya masyarakat.

    Dalam konteks pembelajaran, siswa dapat:

    1. mengamati objek budaya;
    2. mengidentifikasi bentuk geometris;
    3. melakukan pengukuran;
    4. menemukan pola;
    5. membuat model matematika;
    6. menghitung ukuran;
    7. menjelaskan hubungan matematika dengan budaya.
    """)

    st.info(
        "💡 Intinya: budaya dapat menjadi sumber belajar matematika, "
        "sedangkan matematika dapat digunakan untuk mendeskripsikan "
        "dan memahami bentuk serta pola budaya."
    )

    # ==========================================================
    # SOAL INTERAKTIF
    # ==========================================================

    st.divider()
    st.header("🧠 Latihan Interaktif — 20 Soal")

    st.info(
        "Pilih jawaban. Hasil benar atau salah akan langsung muncul. "
        "Setelah selesai, gunakan tombol **Periksa Semua Jawaban**."
    )

    soal = [

        {
            "soal": "1. Bangun datar yang memiliki empat sisi sama panjang dan empat sudut siku-siku adalah...",
            "pilihan": ["Persegi", "Segitiga", "Lingkaran", "Trapesium"],
            "jawaban": "Persegi",
            "pembahasan": "Persegi memiliki empat sisi sama panjang dan empat sudut siku-siku."
        },

        {
            "soal": "2. Sebuah motif persegi memiliki sisi 8 cm. Luasnya adalah...",
            "pilihan": ["16 cm²", "32 cm²", "64 cm²", "128 cm²"],
            "jawaban": "64 cm²",
            "pembahasan": "Luas = 8 × 8 = 64 cm²."
        },

        {
            "soal": "3. Sebuah motif persegi memiliki sisi 8 cm. Kelilingnya adalah...",
            "pilihan": ["16 cm", "24 cm", "32 cm", "64 cm"],
            "jawaban": "32 cm",
            "pembahasan": "Keliling = 4 × 8 = 32 cm."
        },

        {
            "soal": "4. Motif batik digeser 5 cm ke kanan. Transformasi tersebut disebut...",
            "pilihan": ["Rotasi", "Refleksi", "Translasi", "Dilatasi"],
            "jawaban": "Translasi",
            "pembahasan": "Translasi adalah transformasi berupa pergeseran."
        },

        {
            "soal": "5. Motif diputar sebesar 90°. Transformasi tersebut disebut...",
            "pilihan": ["Translasi", "Rotasi", "Refleksi", "Dilatasi"],
            "jawaban": "Rotasi",
            "pembahasan": "Rotasi adalah transformasi berupa perputaran."
        },

        {
            "soal": "6. Motif dicerminkan terhadap garis tengah. Transformasi tersebut disebut...",
            "pilihan": ["Translasi", "Rotasi", "Refleksi", "Dilatasi"],
            "jawaban": "Refleksi",
            "pembahasan": "Refleksi merupakan pencerminan terhadap suatu garis."
        },

        {
            "soal": "7. Motif diperbesar dengan faktor skala 2. Jika panjang awal 5 cm, panjang barunya adalah...",
            "pilihan": ["2,5 cm", "5 cm", "7 cm", "10 cm"],
            "jawaban": "10 cm",
            "pembahasan": "Ukuran baru = 2 × 5 = 10 cm."
        },

        {
            "soal": "8. Sebuah rumah memiliki panjang 20 m. Jika dibuat dengan skala 1 : 100, panjang modelnya adalah...",
            "pilihan": ["10 cm", "20 cm", "50 cm", "100 cm"],
            "jawaban": "20 cm",
            "pembahasan": "20 m = 2.000 cm. 2.000 ÷ 100 = 20 cm."
        },

        {
            "soal": "9. Sebuah bubu memiliki diameter 40 cm. Jari-jarinya adalah...",
            "pilihan": ["10 cm", "20 cm", "30 cm", "40 cm"],
            "jawaban": "20 cm",
            "pembahasan": "Jari-jari = diameter ÷ 2 = 20 cm."
        },

        {
            "soal": "10. Jika jari-jari penampang bubu 10 cm dan π = 3,14, luas penampangnya adalah...",
            "pilihan": ["31,4 cm²", "62,8 cm²", "314 cm²", "628 cm²"],
            "jawaban": "314 cm²",
            "pembahasan": "Luas = πr² = 3,14 × 10² = 314 cm²."
        },

        {
            "soal": "11. Sebuah perahu memiliki panjang 8 m dan lebar 2 m. Luas model bagian dasarnya adalah...",
            "pilihan": ["10 m²", "16 m²", "20 m²", "32 m²"],
            "jawaban": "16 m²",
            "pembahasan": "Luas = 8 × 2 = 16 m²."
        },

        {
            "soal": "12. Sebuah gerbang berbentuk segi delapan memiliki jumlah sisi...",
            "pilihan": ["6", "7", "8", "10"],
            "jawaban": "8",
            "pembahasan": "Segi delapan atau oktagon memiliki 8 sisi."
        },

        {
            "soal": "13. Jika setiap sisi segi delapan beraturan panjangnya 3 m, kelilingnya adalah...",
            "pilihan": ["11 m", "18 m", "24 m", "30 m"],
            "jawaban": "24 m",
            "pembahasan": "Keliling = 8 × 3 = 24 m."
        },

        {
            "soal": "14. Sebuah lantai rumah berukuran 12 m × 8 m. Luasnya adalah...",
            "pilihan": ["20 m²", "40 m²", "96 m²", "192 m²"],
            "jawaban": "96 m²",
            "pembahasan": "Luas = 12 × 8 = 96 m²."
        },

        {
            "soal": "15. Susunan motif yang terus berulang disebut...",
            "pilihan": [
                "Pola berulang",
                "Peluang",
                "Median",
                "Persamaan linear"
            ],
            "jawaban": "Pola berulang",
            "pembahasan": "Pola yang mengulang bentuk atau susunan tertentu disebut pola berulang."
        },

        {
            "soal": "16. Jika titik (2, 3) ditranslasikan 4 satuan ke kanan dan 2 satuan ke atas, koordinat bayangannya adalah...",
            "pilihan": ["(4, 5)", "(6, 5)", "(6, 1)", "(2, 5)"],
            "jawaban": "(6, 5)",
            "pembahasan": "x bertambah 4 dan y bertambah 2, sehingga (2,3) → (6,5)."
        },

        {
            "soal": "17. Jika panjang dan lebar sebuah bangun masing-masing diperbesar 2 kali, luasnya menjadi...",
            "pilihan": ["2 kali", "3 kali", "4 kali", "8 kali"],
            "jawaban": "4 kali",
            "pembahasan": "Luas baru = (2p)(2l) = 4pl."
        },

        {
            "soal": "18. Konsep yang paling tepat untuk menganalisis kesamaan bagian kiri dan kanan sebuah ornamen adalah...",
            "pilihan": [
                "Simetri",
                "Peluang",
                "Statistika",
                "Barisan"
            ],
            "jawaban": "Simetri",
            "pembahasan": "Kesamaan bentuk terhadap garis atau pusat tertentu berkaitan dengan simetri."
        },

        {
            "soal": "19. Benda budaya yang bentuknya dapat dimodelkan menggunakan tabung adalah...",
            "pilihan": [
                "Penampang badan bubu",
                "Motif segitiga",
                "Pintu persegi",
                "Kain persegi panjang"
            ],
            "jawaban": "Penampang badan bubu",
            "pembahasan": "Bagian badan bubu dengan diameter relatif tetap dapat dimodelkan sebagai tabung."
        },

        {
            "soal": "20. Mengapa objek budaya dapat digunakan dalam pembelajaran geometri?",
            "pilihan": [
                "Karena objek budaya tidak memiliki bentuk",
                "Karena objek budaya mengandung bentuk, ukuran, pola, dan ruang yang dapat dianalisis secara matematis",
                "Karena matematika tidak membutuhkan pengukuran",
                "Karena semua budaya berbentuk sama"
            ],
            "jawaban": "Karena objek budaya mengandung bentuk, ukuran, pola, dan ruang yang dapat dianalisis secara matematis",
            "pembahasan": "Objek budaya dapat menjadi konteks nyata untuk mempelajari konsep geometri."
        }
    ]

    jawaban_user = []

    for i, item in enumerate(soal):

        st.markdown(f"{item['soal']}")

        jawaban = st.radio(
            "Pilih jawaban:",
            item["pilihan"],
            index=None,
            key=f"geometri_budaya_q_{i}",
            label_visibility="collapsed"
        )

        jawaban_user.append(jawaban)

        if jawaban is not None:

            if jawaban == item["jawaban"]:

                st.success(
                    f"✅ Benar! {item['pembahasan']}"
                )

            else:

                st.error(
                    f"❌ Salah. Jawaban yang benar adalah "
                    f"**{item['jawaban']}**. {item['pembahasan']}"
                )

    # ==========================================================
    # PERIKSA SEMUA JAWABAN
    # ==========================================================

    st.divider()

    if st.button(
        "✅ Periksa Semua Jawaban",
        key="cek_semua_geometri_budaya",
        use_container_width=True
    ):

        jumlah_dijawab = sum(
            jawaban is not None
            for jawaban in jawaban_user
        )

        jumlah_benar = sum(
            jawaban_user[i] == soal[i]["jawaban"]
            for i in range(len(soal))
            if jawaban_user[i] is not None
        )

        jumlah_belum = len(soal) - jumlah_dijawab

        nilai = jumlah_benar / len(soal) * 100

        st.subheader("📊 Hasil Latihan")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Benar", jumlah_benar)
        col2.metric("Dijawab", jumlah_dijawab)
        col3.metric("Belum Dijawab", jumlah_belum)
        col4.metric("Nilai", f"{nilai:.0f}")

        if jumlah_dijawab < len(soal):

            st.warning(
                f"⚠️ Masih ada {jumlah_belum} soal yang belum dijawab."
            )

        elif nilai >= 80:

            st.success(
                "🎉 Semua soal sudah dijawab. "
                "Pemahaman geometri dalam budaya sudah baik!"
            )

        elif nilai >= 60:

            st.info(
                "👍 Semua soal sudah dijawab. "
                "Pelajari kembali konsep yang masih belum dikuasai."
            )

        else:

            st.warning(
                "📚 Pelajari kembali konsep bangun datar, "
                "transformasi, simetri, skala, dan bangun ruang."
            )

    # ==========================================================
    # SOAL ESSAY
    # ==========================================================

    st.divider()

    st.header("✍️ Soal Essay")

    st.markdown(
        "Kerjakan terlebih dahulu. Klik **Tampilkan Jawaban** "
        "untuk melihat pembahasan."
    )

    essay = [

        (
            "Essay 1",
            "Sebutkan minimal lima objek budaya yang dapat digunakan "
            "sebagai sumber belajar geometri.",
            "Contohnya adalah tenun, batik, rumah tradisional, "
            "arsitektur kesultanan, bubu, perahu, ornamen, dan kerajinan."
        ),

        (
            "Essay 2",
            "Sebuah motif budaya berbentuk persegi dengan sisi 12 cm. "
            "Hitung luas dan kelilingnya.",
            "Luas = 12² = 144 cm². "
            "Keliling = 4 × 12 = 48 cm."
        ),

        (
            "Essay 3",
            "Jelaskan perbedaan translasi, rotasi, refleksi, "
            "dan dilatasi.",
            "Translasi adalah pergeseran, rotasi adalah perputaran, "
            "refleksi adalah pencerminan, sedangkan dilatasi adalah "
            "perubahan ukuran berdasarkan faktor skala."
        ),

        (
            "Essay 4",
            "Sebuah rumah memiliki panjang sebenarnya 25 m. "
            "Jika dibuat dengan skala 1 : 100, berapa panjang "
            "pada model?",
            "25 m = 2.500 cm. "
            "Panjang model = 2.500 ÷ 100 = 25 cm."
        ),

        (
            "Essay 5",
            "Sebuah bubu berbentuk tabung memiliki jari-jari 20 cm "
            "dan panjang 100 cm. Hitung volumenya menggunakan "
            "π = 3,14.",
            "V = πr²t = 3,14 × 20² × 100 = 125.600 cm³."
        ),

        (
            "Essay 6",
            "Sebuah perahu memiliki panjang 10 m dan lebar 2 m. "
            "Tentukan perbandingan panjang terhadap lebarnya.",
            "10 : 2 = 5 : 1."
        ),

        (
            "Essay 7",
            "Jelaskan bagaimana pola budaya dapat digunakan untuk "
            "mempelajari konsep simetri.",
            "Pola budaya dapat diamati untuk menemukan kesamaan bentuk "
            "terhadap suatu garis atau pusat. Kesamaan tersebut dapat "
            "digunakan untuk mempelajari simetri lipat maupun simetri putar."
        ),

        (
            "Essay 8",
            "Jelaskan hubungan geometri dan etnomatematika.",
            "Geometri mempelajari bentuk, ukuran, ruang, dan hubungan "
            "antarobjek. Etnomatematika dapat menggunakan objek budaya "
            "sebagai konteks untuk menemukan dan mempelajari konsep "
            "geometri yang terdapat dalam kehidupan masyarakat."
        )
    ]

    for judul, pertanyaan, jawaban in essay:

        st.markdown(f"{judul}")

        st.markdown(pertanyaan)

        with st.expander("👁️ Tampilkan Jawaban"):

            st.success(jawaban)

    # ==========================================================
    # REFLEKSI
    # ==========================================================

    st.divider()

    st.header("💭 Refleksi")

    st.markdown("""
    Setelah mempelajari geometri dalam budaya, coba pikirkan:

    - Bentuk geometri apa yang paling sering kamu temukan dalam budaya?
    - Di mana kamu menemukan simetri?
    - Di mana kamu menemukan pola berulang?
    - Objek budaya apa yang paling mudah dimodelkan secara matematis?
    - Bagaimana matematika dapat membantu mendokumentasikan budaya lokal?
    - Bagaimana pembelajaran geometri dapat dibuat lebih dekat dengan
      kehidupan masyarakat?
    """)

    st.success(
        "📐 Geometri tidak hanya berada di dalam buku matematika. "
        "Ia juga hadir dalam kain, rumah, istana, alat tangkap, "
        "perahu, dan berbagai karya budaya masyarakat."
    )



def perahu():
    st.markdown(
        '<div class="content-title">🛶 Perahu Tradisional</div>',
        unsafe_allow_html=True
    )

    # ==========================================================
    # MATERI
    # ==========================================================

    st.header("🌊 Mengenal Perahu Tradisional")

    st.markdown("""
    Perahu tradisional merupakan bagian penting dari kehidupan masyarakat
    yang tinggal di sekitar sungai dan wilayah perairan.

    Di Kalimantan Barat, **sampan/perahu** telah digunakan sebagai sarana
    transportasi air, termasuk di kawasan Sungai Kapuas di Pontianak.

    Bentuk perahu yang memanjang dan ramping dapat menjadi objek menarik
    untuk mempelajari **geometri, pengukuran, perbandingan, skala,
    luas, volume, dan pemodelan matematika**.
    """)

    st.image(
        "https://www.liputan6.com/photo/read/2299439/menikmati-asyiknya-naik-perahu-sampan-di-sungai-kapuas",
        caption="Perahu sampan di Sungai Kapuas, Pontianak — Sumber: Liputan6",
        use_container_width=True
    )

    st.caption(
        "Sumber gambar: Liputan6 — Menikmati Asyiknya Naik Perahu Sampan "
        "di Sungai Kapuas."
    )

    st.header("🛶 Sampan di Sungai Kapuas")

    st.markdown("""
    Sampan masih menjadi bagian dari aktivitas transportasi air di
    Pontianak. Perahu digunakan untuk menyeberangi sungai maupun
    melakukan perjalanan di sepanjang kawasan perairan.

    Bentuk perahu yang panjang dan relatif sempit membantu perahu bergerak
    di permukaan air.

    Dalam pembelajaran matematika, bentuk tersebut dapat disederhanakan
    menjadi model geometri.
    """)

    st.image(
        "https://media.zenfs.com/en_SG/News/jackposttravel/7ijlrjtjs6wwkkw48o04o88kg.JPG",
        caption="Sampan tradisional di Sungai Kapuas — Sumber: Yahoo News Singapore",
        use_container_width=True
    )

    st.caption(
        "Sumber gambar: Yahoo News Singapore — River Crossing in Pontianak."
    )

    st.header("📐 Bentuk Geometri Perahu")

    st.markdown("""
    Perahu tradisional memiliki bentuk yang kompleks. Untuk mempelajarinya
    secara matematis, bentuk tersebut dapat disederhanakan menjadi beberapa
    bagian.

    - **Persegi panjang** → lantai atau bagian dasar tertentu.
    - **Segitiga** → bagian ujung atau penampang sederhana.
    - **Trapesium** → penampang badan perahu.
    - **Balok** → model sederhana bagian tertentu.
    - **Prisma** → model ruang badan perahu.
    - **Gabungan bangun** → model keseluruhan perahu.

    Penyederhanaan ini disebut **pemodelan matematika**.
    """)

    st.header("📏 Mengukur Perahu")

    st.markdown("""
    Beberapa ukuran yang dapat diamati pada sebuah perahu antara lain:

    - panjang perahu;
    - lebar perahu;
    - tinggi badan perahu;
    - kedalaman bagian dalam;
    - panjang tempat duduk;
    - jarak antarbagian perahu.

    Pengukuran tersebut dapat digunakan untuk menghitung luas,
    volume, perbandingan, maupun membuat model berskala.
    """)

    st.header("📊 Contoh Luas Dasar")

    st.markdown("""
    Misalkan bagian dasar sebuah perahu dimodelkan sebagai persegi panjang
    dengan panjang 6 m dan lebar 1,5 m.
    """)

    st.latex(r"L = p \times l = 6 \times 1,5 = 9\text{ m}^2")

    st.markdown("""
    Jadi, luas model bagian dasar perahu adalah **9 m²**.
    """)

    st.header("📦 Contoh Volume")

    st.markdown("""
    Misalkan badan perahu disederhanakan sebagai balok dengan panjang
    6 m, lebar 1,5 m, dan tinggi 0,5 m.
    """)

    st.latex(r"V = p \times l \times t = 6 \times 1,5 \times 0,5 = 4,5\text{ m}^3")

    st.markdown("""
    Jadi, volume model tersebut adalah **4,5 m³**.

    Perhitungan ini merupakan model matematika sederhana. Bentuk perahu
    sebenarnya tidak berbentuk balok sempurna.
    """)

    st.header("🔺 Penampang Perahu")

    st.markdown("""
    Penampang badan perahu dapat dimodelkan menggunakan trapesium.

    Misalnya sebuah penampang memiliki sisi sejajar 1,2 m dan 0,8 m
    dengan tinggi 0,5 m.
    """)

    st.latex(r"L = \frac{1}{2}(a+b)t")

    st.latex(r"L = \frac{1}{2}(1,2+0,8)(0,5) = 0,5\text{ m}^2")

    st.markdown("""
    Dengan model tersebut, luas penampang adalah **0,5 m²**.
    """)

    st.header("⚖️ Perbandingan Ukuran")

    st.markdown("""
    Perbandingan panjang dan lebar merupakan salah satu karakteristik
    penting dalam mempelajari bentuk perahu.

    Misalnya panjang perahu 8 m dan lebarnya 1 m.
    """)

    st.latex(r"Panjang:Lebar = 8:1")

    st.markdown("""
    Perbandingan tersebut menunjukkan bahwa perahu jauh lebih panjang
    daripada lebarnya.

    Perbandingan seperti ini dapat digunakan untuk membandingkan bentuk
    beberapa jenis perahu.
    """)

    st.header("📐 Skala dan Miniatur Perahu")

    st.markdown("""
    Perahu tradisional dapat dibuat menjadi miniatur atau maket.

    Misalnya panjang perahu sebenarnya 8 m dan dibuat dengan skala 1 : 20.
    """)

    st.latex(r"Panjang\ model = \frac{8}{20} = 0,4\text{ m} = 40\text{ cm}")

    st.markdown("""
    Jadi, panjang model perahu adalah **40 cm**.

    Konsep skala juga dapat digunakan untuk membuat gambar teknik,
    denah, maupun model 3D.
    """)

    st.header("🔄 Simetri pada Perahu")

    st.markdown("""
    Jika dilihat dari bagian depan atau atas, beberapa perahu memiliki
    bentuk yang mendekati simetris terhadap garis tengah.

    Konsep tersebut dapat dikaji menggunakan **simetri refleksi**.

    Misalnya bagian kiri dan kanan badan perahu memiliki bentuk yang
    hampir sama terhadap garis tengah.
    """)

    st.header("🏞️ Perahu dan Lingkungan Sungai")

    st.markdown("""
    Bentuk perahu tradisional tidak terlepas dari lingkungan tempat
    perahu digunakan.

    Pada wilayah sungai, ukuran, bentuk, kedalaman, dan kemampuan
    manuver perahu menjadi bagian penting dalam penggunaannya.

    Kajian kebudayaan di Kalimantan juga menunjukkan bahwa teknologi
    perahu berkembang berkaitan dengan aktivitas manusia di sungai.
    Pada masa awal, perahu dibuat dari batang kayu yang dipahat bagian
    tengahnya dan kemudian berkembang dengan penambahan papan pada
    bagian badan perahu. :contentReference[oaicite:1]{index=1}
    """)

    st.header("🧮 Kecepatan Perahu")

    st.markdown("""
    Matematika juga dapat digunakan untuk menghitung kecepatan perjalanan.

    Jika sebuah perahu menempuh jarak 6 km dalam waktu 30 menit,
    terlebih dahulu waktu diubah menjadi jam.
    """)

    st.latex(r"30\text{ menit} = 0,5\text{ jam}")

    st.latex(r"v = \frac{s}{t} = \frac{6}{0,5} = 12\text{ km/jam}")

    st.markdown("""
    Jadi, kecepatan rata-rata perahu adalah **12 km/jam**.
    """)

    # ==========================================================
    # SOAL INTERAKTIF
    # ==========================================================

    st.divider()
    st.header("🧠 Latihan Interaktif — 20 Soal")

    st.info(
        "Pilih jawaban. Hasil benar atau salah akan langsung muncul. "
        "Setelah selesai, gunakan tombol **Periksa Semua Jawaban**."
    )

    soal = [

        {
            "soal": "1. Sebuah perahu memiliki panjang 6 m dan lebar 1,5 m. Berapa luas model bagian dasarnya?",
            "pilihan": ["7 m²", "9 m²", "12 m²", "15 m²"],
            "jawaban": "9 m²",
            "pembahasan": "Luas = 6 × 1,5 = 9 m²."
        },

        {
            "soal": "2. Sebuah perahu memiliki panjang 8 m dan lebar 1 m. Perbandingan panjang : lebar adalah...",
            "pilihan": ["1 : 8", "2 : 1", "8 : 1", "8 : 2"],
            "jawaban": "8 : 1",
            "pembahasan": "8 : 1 = 8 : 1."
        },

        {
            "soal": "3. Sebuah model perahu berbentuk balok dengan panjang 6 m, lebar 1,5 m, dan tinggi 0,5 m. Volumenya adalah...",
            "pilihan": ["3 m³", "4 m³", "4,5 m³", "6 m³"],
            "jawaban": "4,5 m³",
            "pembahasan": "V = 6 × 1,5 × 0,5 = 4,5 m³."
        },

        {
            "soal": "4. Panjang perahu sebenarnya 8 m. Jika dibuat dengan skala 1 : 20, panjang modelnya adalah...",
            "pilihan": ["20 cm", "30 cm", "40 cm", "80 cm"],
            "jawaban": "40 cm",
            "pembahasan": "8 m = 800 cm. 800 ÷ 20 = 40 cm."
        },

        {
            "soal": "5. Bagian badan perahu dapat dimodelkan sebagai gabungan beberapa bangun. Proses tersebut disebut...",
            "pilihan": [
                "Pemodelan matematika",
                "Pengurangan",
                "Pengkodean",
                "Pencacahan"
            ],
            "jawaban": "Pemodelan matematika",
            "pembahasan": "Bentuk nyata disederhanakan menjadi model matematika."
        },

        {
            "soal": "6. Sebuah penampang perahu berbentuk trapesium memiliki sisi sejajar 1,2 m dan 0,8 m serta tinggi 0,5 m. Luasnya adalah...",
            "pilihan": ["0,25 m²", "0,5 m²", "1 m²", "1,5 m²"],
            "jawaban": "0,5 m²",
            "pembahasan": "L = 1/2(1,2 + 0,8) × 0,5 = 0,5 m²."
        },

        {
            "soal": "7. Jika sebuah perahu menempuh 6 km dalam 30 menit, kecepatan rata-ratanya adalah...",
            "pilihan": ["6 km/jam", "10 km/jam", "12 km/jam", "18 km/jam"],
            "jawaban": "12 km/jam",
            "pembahasan": "30 menit = 0,5 jam. v = 6 ÷ 0,5 = 12 km/jam."
        },

        {
            "soal": "8. Jika panjang perahu 10 m dan lebarnya 2 m, perbandingan panjang : lebar adalah...",
            "pilihan": ["2 : 10", "5 : 1", "10 : 2", "1 : 5"],
            "jawaban": "5 : 1",
            "pembahasan": "10 : 2 disederhanakan menjadi 5 : 1."
        },

        {
            "soal": "9. Perahu yang memiliki bagian kiri dan kanan hampir sama terhadap garis tengah menunjukkan konsep...",
            "pilihan": [
                "Simetri refleksi",
                "Translasi",
                "Peluang",
                "Barisan"
            ],
            "jawaban": "Simetri refleksi",
            "pembahasan": "Kesamaan bentuk terhadap garis tengah merupakan contoh simetri refleksi."
        },

        {
            "soal": "10. Sebuah perahu panjangnya 12 m. Jika dibuat model dengan skala 1 : 30, panjang modelnya adalah...",
            "pilihan": ["20 cm", "30 cm", "40 cm", "60 cm"],
            "jawaban": "40 cm",
            "pembahasan": "12 m = 1200 cm. 1200 ÷ 30 = 40 cm."
        },

        {
            "soal": "11. Bagian lantai perahu berukuran 5 m × 1,2 m. Luasnya adalah...",
            "pilihan": ["5 m²", "6 m²", "7 m²", "8 m²"],
            "jawaban": "6 m²",
            "pembahasan": "Luas = 5 × 1,2 = 6 m²."
        },

        {
            "soal": "12. Sebuah perahu memiliki panjang 10 m. Jika bertambah 2 m, panjang barunya adalah...",
            "pilihan": ["8 m", "10 m", "12 m", "20 m"],
            "jawaban": "12 m",
            "pembahasan": "10 + 2 = 12 m."
        },

        {
            "soal": "13. Sebuah perahu menempuh 10 km dengan kecepatan 5 km/jam. Waktu yang diperlukan adalah...",
            "pilihan": ["1 jam", "2 jam", "3 jam", "5 jam"],
            "jawaban": "2 jam",
            "pembahasan": "t = s ÷ v = 10 ÷ 5 = 2 jam."
        },

        {
            "soal": "14. Sebuah perahu panjangnya 8 m. Jika setiap 1 m terdapat satu tempat duduk, jumlah tempat duduk secara sederhana adalah...",
            "pilihan": ["4", "6", "8", "10"],
            "jawaban": "8",
            "pembahasan": "8 m ÷ 1 m = 8 tempat."
        },

        {
            "soal": "15. Bentuk yang paling sesuai untuk memodelkan penampang badan perahu yang melebar di bagian atas adalah...",
            "pilihan": [
                "Trapesium",
                "Lingkaran",
                "Persegi sempurna",
                "Segi enam beraturan"
            ],
            "jawaban": "Trapesium",
            "pembahasan": "Penampang yang memiliki dua sisi sejajar dengan panjang berbeda dapat dimodelkan sebagai trapesium."
        },

        {
            "soal": "16. Jika panjang sebuah perahu diperbesar 2 kali dan lebarnya tetap, luas model lantai menjadi...",
            "pilihan": ["1/2 kali", "2 kali", "3 kali", "4 kali"],
            "jawaban": "2 kali",
            "pembahasan": "Luas persegi panjang sebanding dengan panjang jika lebar tetap."
        },

        {
            "soal": "17. Jika panjang dan lebar sebuah model perahu masing-masing diperbesar 2 kali, luasnya menjadi...",
            "pilihan": ["2 kali", "3 kali", "4 kali", "8 kali"],
            "jawaban": "4 kali",
            "pembahasan": "Luas baru = (2p)(2l) = 4pl."
        },

        {
            "soal": "18. Salah satu fungsi utama perahu tradisional di wilayah sungai adalah...",
            "pilihan": [
                "Transportasi air",
                "Tempat menyimpan tanah",
                "Alat ukur suhu",
                "Bangunan permanen"
            ],
            "jawaban": "Transportasi air",
            "pembahasan": "Sampan/perahu digunakan sebagai sarana transportasi di wilayah perairan."
        },

        {
            "soal": "19. Konsep matematika yang dapat digunakan untuk membuat miniatur perahu adalah...",
            "pilihan": [
                "Skala",
                "Median",
                "Modus",
                "Peluang"
            ],
            "jawaban": "Skala",
            "pembahasan": "Skala digunakan untuk mengubah ukuran sebenarnya menjadi ukuran model secara proporsional."
        },

        {
            "soal": "20. Mengapa perahu tradisional dapat menjadi objek pembelajaran etnomatematika?",
            "pilihan": [
                "Karena hanya memiliki nilai sejarah",
                "Karena mengandung bentuk, ukuran, pola, dan teknik pembuatan yang dapat dikaji secara matematis",
                "Karena tidak memiliki bentuk geometris",
                "Karena hanya digunakan untuk perlombaan"
            ],
            "jawaban": "Karena mengandung bentuk, ukuran, pola, dan teknik pembuatan yang dapat dikaji secara matematis",
            "pembahasan": "Perahu menghubungkan konsep matematika dengan teknologi dan budaya masyarakat."
        }
    ]

    jawaban_user = []

    for i, item in enumerate(soal):

        st.markdown(f"{item['soal']}")

        jawaban = st.radio(
            "Pilih jawaban:",
            item["pilihan"],
            index=None,
            key=f"perahu_q_{i}",
            label_visibility="collapsed"
        )

        jawaban_user.append(jawaban)

        if jawaban is not None:

            if jawaban == item["jawaban"]:

                st.success(
                    f"✅ Benar! {item['pembahasan']}"
                )

            else:

                st.error(
                    f"❌ Salah. Jawaban yang benar adalah "
                    f"**{item['jawaban']}**. {item['pembahasan']}"
                )

    # ==========================================================
    # PERIKSA SEMUA JAWABAN
    # ==========================================================

    st.divider()

    if st.button(
        "✅ Periksa Semua Jawaban",
        key="cek_semua_perahu",
        use_container_width=True
    ):

        jumlah_dijawab = sum(
            jawaban is not None
            for jawaban in jawaban_user
        )

        jumlah_benar = sum(
            jawaban_user[i] == soal[i]["jawaban"]
            for i in range(len(soal))
            if jawaban_user[i] is not None
        )

        jumlah_belum = len(soal) - jumlah_dijawab

        nilai = jumlah_benar / len(soal) * 100

        st.subheader("📊 Hasil Latihan")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Benar", jumlah_benar)
        col2.metric("Dijawab", jumlah_dijawab)
        col3.metric("Belum Dijawab", jumlah_belum)
        col4.metric("Nilai", f"{nilai:.0f}")

        if jumlah_dijawab < len(soal):

            st.warning(
                f"⚠️ Masih ada {jumlah_belum} soal yang belum dijawab."
            )

        elif nilai >= 80:

            st.success(
                "🎉 Semua soal sudah dijawab. "
                "Pemahaman matematika pada perahu tradisional sudah baik!"
            )

        elif nilai >= 60:

            st.info(
                "👍 Semua soal sudah dijawab. "
                "Pelajari kembali konsep yang masih belum dikuasai."
            )

        else:

            st.warning(
                "📚 Pelajari kembali konsep geometri, skala, "
                "perbandingan, luas, volume, dan kecepatan."
            )

    # ==========================================================
    # SOAL ESSAY
    # ==========================================================

    st.divider()

    st.header("✍️ Soal Essay")

    st.markdown(
        "Kerjakan terlebih dahulu. Klik **Tampilkan Jawaban** "
        "untuk melihat pembahasan."
    )

    essay = [

        (
            "Essay 1",
            "Sebuah perahu memiliki panjang 8 m dan lebar 1,5 m. "
            "Hitung luas model bagian dasarnya.",
            "Luas = 8 × 1,5 = 12 m²."
        ),

        (
            "Essay 2",
            "Sebuah perahu dimodelkan sebagai balok dengan panjang "
            "6 m, lebar 1,5 m, dan tinggi 0,5 m. Hitung volumenya.",
            "V = 6 × 1,5 × 0,5 = 4,5 m³."
        ),

        (
            "Essay 3",
            "Panjang sebuah perahu sebenarnya 10 m. Jika dibuat "
            "dengan skala 1 : 25, berapa panjang modelnya?",
            "10 m = 1000 cm. Panjang model = 1000 ÷ 25 = 40 cm."
        ),

        (
            "Essay 4",
            "Sebuah perahu menempuh jarak 12 km dalam waktu 1,5 jam. "
            "Hitung kecepatan rata-ratanya.",
            "v = s ÷ t = 12 ÷ 1,5 = 8 km/jam."
        ),

        (
            "Essay 5",
            "Sebuah penampang perahu berbentuk trapesium dengan sisi "
            "sejajar 1,2 m dan 0,8 m serta tinggi 0,5 m. Hitung luasnya.",
            "L = 1/2(1,2 + 0,8) × 0,5 = 0,5 m²."
        ),

        (
            "Essay 6",
            "Jelaskan bagaimana konsep simetri dapat digunakan untuk "
            "menganalisis bentuk perahu.",
            "Jika bagian kiri dan kanan perahu memiliki bentuk yang "
            "hampir sama terhadap garis tengah, bentuk tersebut dapat "
            "dikaji menggunakan konsep simetri refleksi."
        ),

        (
            "Essay 7",
            "Sebutkan minimal lima konsep matematika yang dapat "
            "digunakan untuk mengkaji perahu tradisional.",
            "Contohnya panjang, lebar, tinggi, luas, volume, skala, "
            "perbandingan, sudut, simetri, kecepatan, dan geometri."
        ),

        (
            "Essay 8",
            "Jelaskan hubungan antara perahu tradisional dan "
            "etnomatematika.",
            "Perahu merupakan teknologi budaya yang memiliki bentuk, "
            "ukuran, pola, proporsi, dan teknik pembuatan. Unsur tersebut "
            "dapat dihubungkan dengan berbagai konsep matematika."
        )
    ]

    for judul, pertanyaan, jawaban in essay:

        st.markdown(f"### {judul}")

        st.markdown(pertanyaan)

        with st.expander("👁️ Tampilkan Jawaban"):

            st.success(jawaban)

    # ==========================================================
    # REFLEKSI
    # ==========================================================

    st.divider()

    st.header("💭 Refleksi")

    st.markdown("""
    Setelah mempelajari perahu tradisional, coba pikirkan:

    - Bentuk geometri apa yang dapat digunakan untuk memodelkan badan perahu?
    - Bagaimana cara menghitung luas dan volume sebuah perahu?
    - Mengapa perahu dibuat dengan bentuk yang panjang dan relatif sempit?
    - Bagaimana skala dapat digunakan untuk membuat miniatur perahu?
    - Bagaimana matematika dapat membantu mendokumentasikan teknologi
      perahu tradisional?
    """)

    st.success(
        "🛶 Perahu tradisional menunjukkan bahwa matematika hadir "
        "dalam teknologi, lingkungan sungai, dan kehidupan masyarakat."
    )


def bubu():
    st.markdown(
        '<div class="content-title">🐟 Bubu dan Alat Tangkap Tradisional</div>',
        unsafe_allow_html=True
    )

    # ==========================================================
    # MATERI
    # ==========================================================

    st.header("🌿 Mengenal Bubu")

    st.markdown("""
    **Bubu** merupakan alat tangkap ikan tradisional berbentuk perangkap.
    Bubu dibuat dari bahan alami seperti **bambu atau rotan** yang
    dianyam dan disusun membentuk ruang dengan lubang masuk bagi ikan.

    Bubu merupakan alat tangkap yang bersifat pasif. Ikan masuk melalui
    bagian mulut bubu dan kemudian sulit keluar kembali.

    Dalam pembelajaran etnomatematika, bubu menarik dikaji karena bentuknya
    dapat dimodelkan menggunakan **geometri dan pengukuran**.
    """)

    st.image(
        "https://berkatnewstv.com/wp-content/uploads/2023/03/SALI-PENANGKAP-IKAN-DI-TEBAS-KABUPATEN-SAMBAS-GUNAKAN-BUBU-TRADISIONAL-UNTUK-MENANGKAP-IKAN.jpeg",
        caption="Pembuatan bubu tradisional di Kabupaten Sambas — Sumber: Berkatnews TV",
        use_container_width=True
    )

    st.caption(
        "Sumber gambar: Berkatnews TV — Lestarikan Kearifan Lokal, "
        "Penangkap Ikan Gunakan Bubu Tradisional."
    )

    st.header("🧺 Bubu Kapuas Hulu")

    st.markdown("""
    Bubu juga digunakan oleh masyarakat di Kabupaten Kapuas Hulu,
    Kalimantan Barat.

    Salah satu kajian tentang pemanfaatan rotan di Desa Landau Mentail,
    Kecamatan Boyan Tanjung, mencatat bahwa perangkap ikan atau bubu
    dibuat dari **rotan tapah**, dengan **rotan segak sebagai bahan
    pengikat**.

    Ukurannya sekitar:

    - Diameter: **35–45 cm**
    - Panjang: **45 cm–1,5 m**
    - Bahan utama: **rotan**
    - Lokasi pemasangan: **parit atau sungai kecil**

    Bubu dibuat dengan cara menganyam rotan sehingga membentuk keranjang
    atau perangkap dengan lubang masuk ikan.
    """)

    st.image(
        "https://img.antaranews.com/cache/730x487/2020/07/25/Screenshot_2020-07-25-WhatsApp-1.png",
        caption="Pembuatan bubu bambu secara tradisional — Sumber: ANTARA",
        use_container_width=True
    )

    st.caption(
        "Sumber gambar: ANTARA News Kalimantan Barat — "
        "Satgas TMMD belajar membuat perangkap ikan."
    )

    st.header("📐 Bentuk Geometri Bubu")

    st.markdown("""
    Bentuk bubu dapat disederhanakan menjadi beberapa bentuk geometri.

    **1. Lingkaran**

    Penampang bubu dapat berbentuk lingkaran.

    **2. Tabung**

    Bagian badan bubu yang memiliki diameter relatif tetap dapat
    dimodelkan sebagai tabung.

    **3. Kerucut terpancung**

    Bubu yang semakin mengecil ke salah satu ujung dapat dimodelkan
    sebagai kerucut terpancung.

    **4. Kerucut**

    Bagian ujung tertentu dapat dimodelkan sebagai kerucut.

    **5. Pola anyaman**

    Susunan rotan atau bambu dapat membentuk pola garis horizontal,
    vertikal, diagonal, atau kombinasi di antaranya.
    """)

    st.header("🔵 Diameter dan Jari-jari")

    st.markdown("""
    Jika diameter sebuah bubu adalah 40 cm, maka jari-jarinya adalah:
    """)

    st.latex(r"r = \frac{d}{2} = \frac{40}{2} = 20\text{ cm}")

    st.markdown("""
    Jika penampang bubu dianggap berbentuk lingkaran, luas penampangnya
    dapat dihitung dengan:
    """)

    st.latex(r"L = \pi r^2")

    st.markdown("""
    Dengan $r = 20$ cm dan $\pi = 3,14$:
    """)

    st.latex(r"L = 3,14 \times 20^2 = 1.256\text{ cm}^2")

    st.header("📦 Volume Bubu")

    st.markdown("""
    Jika badan bubu dimodelkan sebagai tabung, volume dapat dihitung
    menggunakan:
    """)

    st.latex(r"V = \pi r^2t")

    st.markdown("""
    Misalnya diameter bubu 40 cm dan panjangnya 100 cm.
    Maka $r = 20$ cm dan $t = 100$ cm.
    """)

    st.latex(r"V = 3,14 \times 20^2 \times 100 = 125.600\text{ cm}^3")

    st.markdown("""
    Jadi, volume model bubu tersebut sekitar **125.600 cm³**.

    Perhitungan ini merupakan model matematika. Bentuk bubu sebenarnya
    tidak selalu merupakan tabung sempurna.
    """)

    st.header("🔺 Bubu sebagai Kerucut Terpancung")

    st.markdown("""
    Banyak bubu memiliki bentuk yang mengecil ke arah ujung.
    Bentuk tersebut dapat dimodelkan sebagai **kerucut terpancung**.

    Jika jari-jari besar adalah $R$, jari-jari kecil adalah $r$, dan
    tinggi bubu adalah $t$, maka volumenya dapat dihitung dengan:
    """)

    st.latex(r"V = \frac{1}{3}\pi t(R^2+Rr+r^2)")

    st.markdown("""
    Model ini membantu kita memahami bahwa benda tradisional yang dibuat
    secara manual dapat dipelajari menggunakan konsep geometri ruang.
    """)

    st.header("🧶 Pola Anyaman")

    st.markdown("""
    Anyaman pada bubu juga memiliki pola matematika.

    Batang rotan atau bambu dapat disusun secara:

    - horizontal;
    - vertikal;
    - diagonal;
    - melingkar;
    - berulang.

    Jarak antarbatang dapat diukur dan dibandingkan. Dengan demikian,
    pola anyaman dapat dikaji menggunakan **pengukuran, perbandingan,
    pola, simetri, dan geometri**.
    """)

    st.header("📏 Skala Bubu")

    st.markdown("""
    Bubu juga dapat dibuat menjadi model atau miniatur.

    Misalnya panjang bubu sebenarnya 100 cm dan dibuat dengan skala
    1 : 5.
    """)

    st.latex(r"Panjang\ model = \frac{100}{5} = 20\text{ cm}")

    st.markdown("""
    Dengan demikian, panjang model bubu adalah **20 cm**.

    Konsep skala dapat digunakan ketika siswa membuat **maket bubu,
    gambar teknik, atau model 3D menggunakan GeoGebra**.
    """)

    st.header("🌿 Bubu dan Kearifan Lokal")

    st.markdown("""
    Bubu bukan hanya objek matematika. Bubu juga menunjukkan keterampilan
    masyarakat dalam memanfaatkan bahan alam dan menyesuaikan alat dengan
    lingkungan perairan.

    Di Kapuas Hulu, penggunaan bubu tercatat dalam aktivitas perikanan
    masyarakat. Pemerintah daerah juga mencatat keberadaan bubu sebagai
    salah satu alat penangkap ikan di perairan umum. :contentReference[oaicite:2]{index=2}

    Dengan demikian, bubu dapat menjadi contoh nyata bahwa matematika
    dapat dipelajari melalui **budaya, lingkungan, teknologi tradisional,
    dan kehidupan masyarakat**.
    """)

    # ==========================================================
    # SOAL INTERAKTIF
    # ==========================================================

    st.divider()
    st.header("🧠 Latihan Interaktif — 20 Soal")

    st.info(
        "Pilih jawaban. Hasil benar atau salah akan langsung muncul. "
        "Setelah selesai, gunakan tombol **Periksa Semua Jawaban**."
    )

    soal = [

        {
            "soal": "1. Jika diameter bubu 40 cm, berapa jari-jarinya?",
            "pilihan": ["10 cm", "20 cm", "30 cm", "40 cm"],
            "jawaban": "20 cm",
            "pembahasan": "Jari-jari = diameter ÷ 2 = 40 ÷ 2 = 20 cm."
        },

        {
            "soal": "2. Sebuah bubu memiliki diameter 50 cm. Jari-jarinya adalah...",
            "pilihan": ["15 cm", "20 cm", "25 cm", "50 cm"],
            "jawaban": "25 cm",
            "pembahasan": "Jari-jari = 50 ÷ 2 = 25 cm."
        },

        {
            "soal": "3. Jika jari-jari penampang bubu 10 cm, luas penampang dengan π = 3,14 adalah...",
            "pilihan": ["31,4 cm²", "62,8 cm²", "314 cm²", "628 cm²"],
            "jawaban": "314 cm²",
            "pembahasan": "Luas = πr² = 3,14 × 10² = 314 cm²."
        },

        {
            "soal": "4. Sebuah bubu dimodelkan sebagai tabung dengan r = 10 cm dan t = 50 cm. Dengan π = 3,14, volumenya adalah...",
            "pilihan": ["1.570 cm³", "3.140 cm³", "15.700 cm³", "31.400 cm³"],
            "jawaban": "15.700 cm³",
            "pembahasan": "V = πr²t = 3,14 × 10² × 50 = 15.700 cm³."
        },

        {
            "soal": "5. Bubu yang diameter badannya semakin mengecil ke salah satu ujung dapat dimodelkan sebagai...",
            "pilihan": [
                "Kerucut terpancung",
                "Kubus",
                "Bola",
                "Prisma segi enam"
            ],
            "jawaban": "Kerucut terpancung",
            "pembahasan": "Bentuk yang memiliki dua ukuran jari-jari berbeda dapat dimodelkan sebagai kerucut terpancung."
        },

        {
            "soal": "6. Dalam kajian bubu di Desa Landau Mentail, bahan utama bubu adalah...",
            "pilihan": ["Besi", "Rotan", "Plastik", "Kaca"],
            "jawaban": "Rotan",
            "pembahasan": "Kajian tersebut mencatat bubu dibuat menggunakan rotan tapah dengan rotan segak sebagai pengikat."
        },

        {
            "soal": "7. Diameter bubu yang dicatat dalam kajian Desa Landau Mentail sekitar...",
            "pilihan": ["5–10 cm", "15–25 cm", "35–45 cm", "60–80 cm"],
            "jawaban": "35–45 cm",
            "pembahasan": "Ukuran diameter yang dicatat sekitar 35–45 cm."
        },

        {
            "soal": "8. Panjang bubu yang dicatat dalam kajian tersebut sekitar...",
            "pilihan": [
                "5–15 cm",
                "20–30 cm",
                "45 cm–1,5 m",
                "3–5 m"
            ],
            "jawaban": "45 cm–1,5 m",
            "pembahasan": "Panjang bubu yang dicatat sekitar 45 cm sampai 1,5 m."
        },

        {
            "soal": "9. Jika panjang bubu 100 cm dibuat dengan skala 1 : 5, panjang modelnya adalah...",
            "pilihan": ["5 cm", "10 cm", "20 cm", "50 cm"],
            "jawaban": "20 cm",
            "pembahasan": "Panjang model = 100 ÷ 5 = 20 cm."
        },

        {
            "soal": "10. Jika diameter bubu 40 cm, keliling penampang dengan π = 3,14 adalah...",
            "pilihan": ["62,8 cm", "100 cm", "125,6 cm", "251,2 cm"],
            "jawaban": "125,6 cm",
            "pembahasan": "Keliling = πd = 3,14 × 40 = 125,6 cm."
        },

        {
            "soal": "11. Jika sebuah bubu memiliki panjang 80 cm dan diameter 40 cm, perbandingan panjang : diameter adalah...",
            "pilihan": ["1 : 2", "2 : 1", "3 : 1", "4 : 1"],
            "jawaban": "2 : 1",
            "pembahasan": "80 : 40 = 2 : 1."
        },

        {
            "soal": "12. Pola batang rotan yang berulang pada badan bubu merupakan contoh...",
            "pilihan": [
                "Pola berulang",
                "Peluang",
                "Median",
                "Persamaan kuadrat"
            ],
            "jawaban": "Pola berulang",
            "pembahasan": "Susunan bentuk atau garis yang terus diulang merupakan pola berulang."
        },

        {
            "soal": "13. Jika jarak antarbatang anyaman adalah 2 cm dan terdapat 20 jarak yang sama, panjang susunannya adalah...",
            "pilihan": ["10 cm", "20 cm", "40 cm", "60 cm"],
            "jawaban": "40 cm",
            "pembahasan": "Panjang = 20 × 2 = 40 cm."
        },

        {
            "soal": "14. Jika sebuah bubu memiliki diameter 40 cm, luas penampang dengan π = 22/7 adalah...",
            "pilihan": [
                "1.200 cm²",
                "1.257 cm²",
                "1.400 cm²",
                "2.800 cm²"
            ],
            "jawaban": "1.257 cm²",
            "pembahasan": "r = 20 cm. Luas = 22/7 × 20² ≈ 1.257 cm²."
        },

        {
            "soal": "15. Rumus volume tabung adalah...",
            "pilihan": [
                "V = 2πr",
                "V = πr²t",
                "V = πd",
                "V = 2πr²"
            ],
            "jawaban": "V = πr²t",
            "pembahasan": "Volume tabung = luas alas × tinggi = πr²t."
        },

        {
            "soal": "16. Jika ukuran panjang bubu diperbesar 2 kali tetapi jari-jari tetap, volumenya menjadi...",
            "pilihan": ["1/2 kali", "2 kali", "3 kali", "4 kali"],
            "jawaban": "2 kali",
            "pembahasan": "Volume tabung sebanding dengan tinggi. Jika tinggi menjadi 2 kali, volume juga menjadi 2 kali."
        },

        {
            "soal": "17. Jika jari-jari bubu diperbesar 2 kali sementara tinggi tetap, volume menjadi...",
            "pilihan": ["2 kali", "3 kali", "4 kali", "8 kali"],
            "jawaban": "4 kali",
            "pembahasan": "Volume sebanding dengan r². Jika r menjadi 2r, volume menjadi 4 kali."
        },

        {
            "soal": "18. Salah satu fungsi lubang masuk pada bubu adalah...",
            "pilihan": [
                "Memperbesar berat bubu",
                "Memungkinkan ikan masuk ke perangkap",
                "Mengubah warna bubu",
                "Mengurangi panjang bubu"
            ],
            "jawaban": "Memungkinkan ikan masuk ke perangkap",
            "pembahasan": "Bagian mulut atau lubang masuk merupakan jalan ikan masuk ke dalam perangkap."
        },

        {
            "soal": "19. Konsep matematika yang dapat digunakan untuk menganalisis bentuk bubu adalah...",
            "pilihan": [
                "Geometri dan pengukuran",
                "Hanya statistika",
                "Hanya peluang",
                "Hanya logika"
            ],
            "jawaban": "Geometri dan pengukuran",
            "pembahasan": "Bentuk, diameter, panjang, luas, volume, dan skala dapat dianalisis dengan geometri dan pengukuran."
        },

        {
            "soal": "20. Bubu dapat menjadi objek pembelajaran etnomatematika karena...",
            "pilihan": [
                "Hanya memiliki nilai ekonomi",
                "Mengandung bentuk, ukuran, pola, dan teknik tradisional",
                "Tidak memiliki bentuk geometris",
                "Hanya digunakan sebagai hiasan"
            ],
            "jawaban": "Mengandung bentuk, ukuran, pola, dan teknik tradisional",
            "pembahasan": "Bubu menghubungkan konsep matematika dengan budaya dan teknologi tradisional masyarakat."
        }
    ]

    jawaban_user = []

    for i, item in enumerate(soal):

        st.markdown(f"{item['soal']}")

        jawaban = st.radio(
            "Pilih jawaban:",
            item["pilihan"],
            index=None,
            key=f"bubu_q_{i}",
            label_visibility="collapsed"
        )

        jawaban_user.append(jawaban)

        if jawaban is not None:

            if jawaban == item["jawaban"]:

                st.success(
                    f"✅ Benar! {item['pembahasan']}"
                )

            else:

                st.error(
                    f"❌ Salah. Jawaban yang benar adalah "
                    f"**{item['jawaban']}**. {item['pembahasan']}"
                )

    # ==========================================================
    # PERIKSA SEMUA JAWABAN
    # ==========================================================

    st.divider()

    if st.button(
        "✅ Periksa Semua Jawaban",
        key="cek_semua_bubu",
        use_container_width=True
    ):

        jumlah_dijawab = sum(
            jawaban is not None
            for jawaban in jawaban_user
        )

        jumlah_benar = sum(
            jawaban_user[i] == soal[i]["jawaban"]
            for i in range(len(soal))
            if jawaban_user[i] is not None
        )

        jumlah_belum = len(soal) - jumlah_dijawab

        nilai = jumlah_benar / len(soal) * 100

        st.subheader("📊 Hasil Latihan")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Benar", jumlah_benar)
        col2.metric("Dijawab", jumlah_dijawab)
        col3.metric("Belum Dijawab", jumlah_belum)
        col4.metric("Nilai", f"{nilai:.0f}")

        if jumlah_dijawab < len(soal):

            st.warning(
                f"⚠️ Masih ada {jumlah_belum} soal yang belum dijawab."
            )

        elif nilai >= 80:

            st.success(
                "🎉 Semua soal sudah dijawab. "
                "Pemahaman tentang bubu dan geometri sudah baik!"
            )

        elif nilai >= 60:

            st.info(
                "👍 Semua soal sudah dijawab. "
                "Pelajari kembali konsep yang masih belum dikuasai."
            )

        else:

            st.warning(
                "📚 Pelajari kembali konsep diameter, luas, volume, "
                "skala, dan bentuk geometri."
            )

    # ==========================================================
    # SOAL ESSAY
    # ==========================================================

    st.divider()

    st.header("✍️ Soal Essay")

    st.markdown(
        "Kerjakan terlebih dahulu. Klik **Tampilkan Jawaban** "
        "untuk melihat pembahasan."
    )

    essay = [

        (
            "Essay 1",
            "Sebuah bubu memiliki diameter 40 cm. Tentukan jari-jari "
            "dan keliling penampangnya dengan π = 3,14.",
            "Jari-jari = 40 ÷ 2 = 20 cm. "
            "Keliling = 2πr = 2 × 3,14 × 20 = 125,6 cm."
        ),

        (
            "Essay 2",
            "Sebuah bubu dimodelkan sebagai tabung dengan jari-jari "
            "20 cm dan tinggi 100 cm. Hitung volumenya dengan π = 3,14.",
            "V = πr²t = 3,14 × 20² × 100 = 125.600 cm³."
        ),

        (
            "Essay 3",
            "Sebuah bubu memiliki panjang sebenarnya 120 cm. "
            "Jika dibuat model dengan skala 1 : 6, berapa panjang model?",
            "Panjang model = 120 ÷ 6 = 20 cm."
        ),

        (
            "Essay 4",
            "Jelaskan mengapa bentuk bubu dapat dimodelkan menggunakan "
            "kerucut terpancung.",
            "Bubu tertentu memiliki bagian yang lebih besar dan bagian "
            "yang lebih kecil sehingga bentuknya menyerupai kerucut "
            "yang dipotong. Model tersebut disebut kerucut terpancung."
        ),

        (
            "Essay 5",
            "Sebuah bubu memiliki diameter 40 cm dan panjang 80 cm. "
            "Tentukan perbandingan panjang terhadap diameter.",
            "80 : 40 = 2 : 1."
        ),

        (
            "Essay 6",
            "Jelaskan hubungan antara pola anyaman bubu dan matematika.",
            "Pola anyaman dapat dianalisis menggunakan konsep garis, "
            "jarak, pengulangan, simetri, sudut, pola, dan pengukuran."
        ),

        (
            "Essay 7",
            "Sebutkan minimal lima konsep matematika yang dapat "
            "digunakan untuk mengkaji bubu.",
            "Contohnya diameter, jari-jari, keliling, luas, volume, "
            "skala, perbandingan, pola, simetri, dan geometri ruang."
        ),

        (
            "Essay 8",
            "Jelaskan mengapa bubu dapat dijadikan objek pembelajaran "
            "etnomatematika.",
            "Bubu merupakan teknologi tradisional masyarakat yang "
            "mengandung unsur bentuk, ukuran, pola anyaman, ruang, "
            "dan teknik pembuatan. Unsur tersebut dapat dihubungkan "
            "dengan konsep matematika."
        )
    ]

    for judul, pertanyaan, jawaban in essay:

        st.markdown(f"{judul}")

        st.markdown(pertanyaan)

        with st.expander("👁️ Tampilkan Jawaban"):

            st.success(jawaban)

    # ==========================================================
    # REFLEKSI
    # ==========================================================

    st.divider()

    st.header("💭 Refleksi")

    st.markdown("""
    Setelah mempelajari bubu, coba pikirkan:

    - Bentuk geometri apa yang paling sesuai untuk memodelkan bubu?
    - Bagaimana cara menentukan volume sebuah bubu?
    - Bagaimana pola anyaman dapat dianalisis menggunakan matematika?
    - Mengapa ukuran bubu perlu disesuaikan dengan lingkungan penggunaannya?
    - Bagaimana teknologi tradisional seperti bubu dapat digunakan
      sebagai sumber belajar matematika?
    """)

    st.success(
        "🐟 Bubu menunjukkan bahwa matematika dapat ditemukan "
        "dalam teknologi tradisional, keterampilan menganyam, "
        "dan kehidupan masyarakat di sekitar perairan."
    )



def arsitektur_kesultanan():

    st.markdown(
        '<div class="content-title">🕌 Arsitektur Kesultanan</div>',
        unsafe_allow_html=True
    )

    # ==========================================================
    # MATERI
    # ==========================================================

    st.header("🏛️ Mengenal Arsitektur Kesultanan")

    st.markdown("""
    Istana atau keraton merupakan bagian penting dari sejarah dan budaya
    masyarakat Indonesia. Selain sebagai tempat tinggal dan pusat
    pemerintahan kesultanan, kompleks istana juga memiliki bentuk ruang,
    bangunan, dan ornamen yang dapat dikaji menggunakan matematika.

    Dalam pembelajaran etnomatematika, arsitektur kesultanan dapat digunakan
    untuk mempelajari **geometri, ukuran, luas, keliling, volume, simetri,
    pola, perbandingan, dan tata ruang**.
    """)

    st.image(
        "https://images.bisnis.com/photos/2023/01/31/187275/antarafoto-wisata-sejarah-istana-sambas-300123-aez-3.jpg",
        caption="Istana Alwatzikhoebillah Kesultanan Sambas — Sumber: Bisnis.com/Antara",
        use_container_width=True
    )

    st.caption(
        "Sumber gambar: Bisnis.com/Antara — Kompleks Istana Sambas."
    )

    st.header("👑 Istana Alwatzikhoebillah Sambas")

    st.markdown("""
    Istana Alwatzikhoebillah merupakan istana Kesultanan Sambas di
    Kalimantan Barat. Kompleks istana berada di kawasan pertemuan
    Sungai Subah, Sungai Sambas Kecil, dan Sungai Teberau.

    Istana yang ada sekarang dibangun pada masa Sultan Muhammad Mulia
    Ibrahim Syafiuddin. Kompleks tersebut memiliki berbagai elemen
    arsitektur seperti gerbang, alun-alun, balairung, paseban, paviliun,
    masjid, dan bangunan pendukung.

    Salah satu ciri menariknya adalah **gerbang berbentuk segi delapan
    (oktagon)**. Bentuk tersebut dapat menjadi konteks pembelajaran
    geometri.
    """)

    st.header("🔷 Gerbang Segi Delapan")

    st.markdown("""
    Segi delapan atau oktagon merupakan bangun datar yang memiliki
    **8 sisi dan 8 sudut**.

    Jika sebuah gerbang berbentuk segi delapan beraturan memiliki panjang
    setiap sisi 2 m, maka kelilingnya dapat dihitung dengan:
    """)

    st.latex(r"K = 8 \times 2 = 16\text{ m}")

    st.markdown("""
    Jadi, keliling gerbang tersebut adalah **16 m**.

    Bentuk segi delapan juga dapat digunakan untuk mengenalkan konsep
    **simetri putar dan simetri lipat**.
    """)

    st.header("📐 Ruang Geometris Istana")

    st.markdown("""
    Penelitian mengenai arsitektur Istana Alwatzikhoebillah menunjukkan
    adanya ruang geometris dan ruang fungsional dalam kompleks istana.

    Ruang tersebut terbentuk melalui hubungan antara bangunan, pagar,
    pepohonan, permukaan tanah, dan tata massa bangunan.

    **Alun-alun dan balairung** merupakan ruang yang memiliki karakter
    ruang yang kuat dalam kompleks istana. :contentReference[oaicite:1]{index=1}
    """)

    st.header("🏛️ Bentuk Geometri pada Arsitektur")

    st.markdown("""
    Beberapa bentuk matematika yang dapat diamati pada arsitektur
    kesultanan antara lain:

    - **Persegi dan persegi panjang** → lantai, pintu, jendela, dinding.
    - **Segitiga** → bagian tertentu pada atap dan ornamen.
    - **Segi delapan** → gerbang utama Istana Alwatzikhoebillah.
    - **Lingkaran** → beberapa unsur ornamen dan dekorasi.
    - **Balok** → model sederhana ruang atau bagian bangunan.
    - **Prisma/piramida** → model sederhana bagian atap.
    """)

    st.header("🔄 Simetri dan Ornamen")

    st.markdown("""
    Ornamen pada bangunan kesultanan dapat dianalisis menggunakan
    konsep **titik, garis, bidang, dan volume**.

    Penelitian terhadap Istana Kadriyah Pontianak dan Istana
    Alwatzikhoebillah Sambas juga mengkaji karakteristik bentuk ornamen
    bangunan bersejarah di Kalimantan Barat. :contentReference[oaicite:2]{index=2}

    Jika bagian kiri dan kanan sebuah ornamen memiliki bentuk yang
    berpasangan terhadap suatu garis, kita dapat mengaitkannya dengan
    **simetri refleksi**.
    """)

    st.image(
        "https://awsimages.detik.net.id/community/media/visual/2021/02/05/dev-megahnya-istana-kadriyah-pontianak-2.jpeg?q=90&w=600",
        caption="Interior Istana Kadriyah Pontianak — Sumber: detikTravel",
        use_container_width=True
    )

    st.caption(
        "Sumber gambar: detikTravel — Megahnya Istana Kadriyah Pontianak."
    )

    st.header("🏰 Istana Kadriyah Pontianak")

    st.markdown("""
    Selain Istana Alwatzikhoebillah, Kalimantan Barat juga memiliki
    Istana Kadriyah di Pontianak.

    Istana Kadriyah didirikan pada tahun 1771 dan sebagian besar struktur
    bangunannya menggunakan kayu belian. Bangunan ini merupakan bagian
    penting dari sejarah Kesultanan Pontianak. :contentReference[oaicite:3]{index=3}

    Dari sudut pandang matematika, bangunan istana dapat dikaji melalui
    **bentuk, ukuran, proporsi, simetri, luas, dan hubungan antar-ruang**.
    """)

    st.header("📏 Contoh Perhitungan Luas")

    st.markdown("""
    Misalkan sebuah balairung berbentuk persegi panjang dengan panjang
    20 m dan lebar 10 m.
    """)

    st.latex(r"L = p \times l = 20 \times 10 = 200\text{ m}^2")

    st.markdown("""
    Jadi, luas lantai balairung tersebut adalah **200 m²**.

    Jika panjang dan lebar sebuah ruang masing-masing diperbesar 2 kali,
    maka luasnya menjadi 4 kali lebih besar.
    """)

    st.latex(r"L' = (2p)(2l) = 4pl = 4L")

    st.header("📊 Perbandingan dan Skala")

    st.markdown("""
    Arsitektur istana juga dapat dipelajari menggunakan skala.

    Misalnya, sebuah bangunan memiliki panjang sebenarnya 20 m dan dibuat
    dalam gambar dengan skala 1 : 100.
    """)

    st.latex(r"Panjang\ gambar = \frac{20}{100} = 0,2\text{ m} = 20\text{ cm}")

    st.markdown("""
    Dengan demikian, panjang bangunan pada gambar adalah **20 cm**.

    Skala sangat berguna ketika arsitektur bangunan dibuat dalam bentuk
    denah, maket, atau model 3D.
    """)

    st.header("🌿 Arsitektur, Lingkungan, dan Budaya")

    st.markdown("""
    Kompleks Istana Alwatzikhoebillah berada pada lingkungan yang berkaitan
    erat dengan sungai. Penelitian arsitektur menunjukkan bahwa tata ruang
    dan bentuk kompleks istana dipengaruhi oleh konteks lingkungan serta
    perkembangan pemerintahan Kesultanan Sambas dan Hindia Belanda.
    :contentReference[oaicite:4]{index=4}

    Karena itu, arsitektur kesultanan dapat dipelajari tidak hanya sebagai
    bentuk bangunan, tetapi juga sebagai hubungan antara **ruang, manusia,
    lingkungan, sejarah, dan budaya**.
    """)

    # ==========================================================
    # SOAL INTERAKTIF
    # ==========================================================

    st.divider()
    st.header("🧠 Latihan Interaktif — 20 Soal")

    st.info(
        "Pilih jawaban. Hasil benar atau salah akan langsung muncul. "
        "Setelah selesai, gunakan tombol **Periksa Semua Jawaban**."
    )

    soal = [

        {
            "soal": "1. Gerbang segi delapan memiliki berapa sisi?",
            "pilihan": ["6", "7", "8", "10"],
            "jawaban": "8",
            "pembahasan": "Segi delapan atau oktagon memiliki 8 sisi."
        },

        {
            "soal": "2. Jika setiap sisi gerbang segi delapan panjangnya 2 m, berapa kelilingnya?",
            "pilihan": ["8 m", "12 m", "16 m", "20 m"],
            "jawaban": "16 m",
            "pembahasan": "Keliling = 8 × 2 = 16 m."
        },

        {
            "soal": "3. Transformasi yang menghasilkan pencerminan suatu ornamen disebut...",
            "pilihan": ["Translasi", "Rotasi", "Refleksi", "Dilatasi"],
            "jawaban": "Refleksi",
            "pembahasan": "Refleksi adalah transformasi berupa pencerminan."
        },

        {
            "soal": "4. Segi delapan beraturan memiliki jumlah sudut sebesar...",
            "pilihan": ["360°", "720°", "900°", "1080°"],
            "jawaban": "1080°",
            "pembahasan": "Jumlah sudut dalam segi-n adalah (n − 2) × 180°. Untuk n = 8, diperoleh 1080°."
        },

        {
            "soal": "5. Besar setiap sudut dalam segi delapan beraturan adalah...",
            "pilihan": ["90°", "120°", "135°", "150°"],
            "jawaban": "135°",
            "pembahasan": "1080° ÷ 8 = 135°."
        },

        {
            "soal": "6. Sebuah balairung berukuran 20 m × 10 m. Berapa luas lantainya?",
            "pilihan": ["30 m²", "100 m²", "200 m²", "400 m²"],
            "jawaban": "200 m²",
            "pembahasan": "Luas = 20 × 10 = 200 m²."
        },

        {
            "soal": "7. Sebuah ruang berbentuk persegi panjang memiliki panjang 15 m dan lebar 8 m. Kelilingnya adalah...",
            "pilihan": ["23 m", "46 m", "120 m", "240 m"],
            "jawaban": "46 m",
            "pembahasan": "Keliling = 2(15 + 8) = 46 m."
        },

        {
            "soal": "8. Sebuah ruangan berukuran 12 m × 8 m. Luasnya adalah...",
            "pilihan": ["20 m²", "40 m²", "96 m²", "192 m²"],
            "jawaban": "96 m²",
            "pembahasan": "Luas = 12 × 8 = 96 m²."
        },

        {
            "soal": "9. Jika sebuah bangunan panjang sebenarnya 20 m dan dibuat dengan skala 1 : 100, panjang pada gambar adalah...",
            "pilihan": ["2 cm", "10 cm", "20 cm", "200 cm"],
            "jawaban": "20 cm",
            "pembahasan": "20 m = 2000 cm. 2000 ÷ 100 = 20 cm."
        },

        {
            "soal": "10. Jika panjang dan lebar suatu ruangan masing-masing diperbesar 2 kali, luas menjadi...",
            "pilihan": ["2 kali", "3 kali", "4 kali", "8 kali"],
            "jawaban": "4 kali",
            "pembahasan": "Luas baru = (2p)(2l) = 4pl."
        },

        {
            "soal": "11. Bangun yang paling sesuai untuk memodelkan lantai berbentuk panjang dan lebar adalah...",
            "pilihan": ["Lingkaran", "Persegi panjang", "Segitiga", "Segi enam"],
            "jawaban": "Persegi panjang",
            "pembahasan": "Lantai ruangan umumnya dapat dimodelkan sebagai persegi panjang."
        },

        {
            "soal": "12. Jika sebuah ornamen kiri dan kanan berimpit ketika dicerminkan terhadap garis tengah, ornamen tersebut memiliki...",
            "pilihan": ["Simetri refleksi", "Translasi", "Dilatasi", "Barisan"],
            "jawaban": "Simetri refleksi",
            "pembahasan": "Kesamaan dua bagian terhadap suatu garis merupakan simetri refleksi."
        },

        {
            "soal": "13. Istana Alwatzikhoebillah berada di wilayah pertemuan beberapa sungai. Salah satu sungai yang disebut dalam sumber adalah...",
            "pilihan": [
                "Sungai Kapuas",
                "Sungai Subah",
                "Sungai Mahakam",
                "Sungai Barito"
            ],
            "jawaban": "Sungai Subah",
            "pembahasan": "Kompleks istana berada di kawasan pertemuan Sungai Subah, Sungai Sambas Kecil, dan Sungai Teberau."
        },

        {
            "soal": "14. Salah satu ruang yang memiliki karakter ruang kuat dalam penelitian arsitektur Istana Alwatzikhoebillah adalah...",
            "pilihan": [
                "Alun-alun dan balairung",
                "Gudang dan dapur",
                "Kamar dan gudang",
                "Garasi dan gudang"
            ],
            "jawaban": "Alun-alun dan balairung",
            "pembahasan": "Penelitian arsitektur mengidentifikasi alun-alun dan balairung sebagai ruang dengan sense of place yang kuat."
        },

        {
            "soal": "15. Sebuah tiang berbentuk balok memiliki panjang 2 m, lebar 0,5 m, dan tinggi 4 m. Volumenya adalah...",
            "pilihan": ["2 m³", "3 m³", "4 m³", "8 m³"],
            "jawaban": "4 m³",
            "pembahasan": "Volume = 2 × 0,5 × 4 = 4 m³."
        },

        {
            "soal": "16. Sebuah atap dimodelkan sebagai prisma segitiga. Konsep matematika yang digunakan untuk menghitung ruangnya adalah...",
            "pilihan": ["Volume", "Median", "Modus", "Peluang"],
            "jawaban": "Volume",
            "pembahasan": "Bangun ruang seperti prisma dapat dianalisis menggunakan konsep volume."
        },

        {
            "soal": "17. Jika sebuah denah memiliki panjang 30 m dan lebar 10 m, perbandingan panjang : lebar adalah...",
            "pilihan": ["1 : 3", "2 : 1", "3 : 1", "3 : 2"],
            "jawaban": "3 : 1",
            "pembahasan": "30 : 10 = 3 : 1."
        },

        {
            "soal": "18. Jika sebuah motif pada ornamen diputar 90°, transformasi tersebut disebut...",
            "pilihan": ["Translasi", "Rotasi", "Refleksi", "Dilatasi"],
            "jawaban": "Rotasi",
            "pembahasan": "Rotasi adalah transformasi berupa perputaran."
        },

        {
            "soal": "19. Penelitian tentang ornamen bangunan bersejarah di Kalimantan Barat mengkaji unsur bentuk berupa...",
            "pilihan": [
                "Titik, garis, bidang, dan volume",
                "Hanya angka",
                "Hanya warna",
                "Hanya panjang"
            ],
            "jawaban": "Titik, garis, bidang, dan volume",
            "pembahasan": "Elemen arsitektur dapat dianalisis melalui konsep titik, garis, bidang, dan volume."
        },

        {
            "soal": "20. Konsep matematika yang paling sesuai untuk mengkaji arsitektur kesultanan adalah...",
            "pilihan": [
                "Geometri, pengukuran, simetri, dan skala",
                "Hanya peluang",
                "Hanya statistika",
                "Hanya aritmetika"
            ],
            "jawaban": "Geometri, pengukuran, simetri, dan skala",
            "pembahasan": "Arsitektur dapat dikaji melalui bentuk, ukuran, simetri, proporsi, skala, luas, keliling, dan volume."
        }
    ]

    jawaban_user = []

    for i, item in enumerate(soal):

        st.markdown(f"##### {item['soal']}")

        jawaban = st.radio(
            "Pilih jawaban:",
            item["pilihan"],
            index=None,
            key=f"arsitektur_q_{i}",
            label_visibility="collapsed"
        )

        jawaban_user.append(jawaban)

        if jawaban is not None:

            if jawaban == item["jawaban"]:

                st.success(
                    f"✅ Benar! {item['pembahasan']}"
                )

            else:

                st.error(
                    f"❌ Salah. Jawaban yang benar adalah "
                    f"**{item['jawaban']}**. {item['pembahasan']}"
                )

    # ==========================================================
    # PERIKSA SEMUA
    # ==========================================================

    st.divider()

    if st.button(
        "✅ Periksa Semua Jawaban",
        key="cek_semua_arsitektur",
        use_container_width=True
    ):

        jumlah_dijawab = sum(
            jawaban is not None
            for jawaban in jawaban_user
        )

        jumlah_benar = sum(
            jawaban_user[i] == soal[i]["jawaban"]
            for i in range(len(soal))
            if jawaban_user[i] is not None
        )

        jumlah_belum = len(soal) - jumlah_dijawab

        nilai = jumlah_benar / len(soal) * 100

        st.subheader("📊 Hasil Latihan")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Benar", jumlah_benar)
        col2.metric("Dijawab", jumlah_dijawab)
        col3.metric("Belum Dijawab", jumlah_belum)
        col4.metric("Nilai", f"{nilai:.0f}")

        if jumlah_dijawab < len(soal):

            st.warning(
                f"⚠️ Masih ada {jumlah_belum} soal yang belum dijawab."
            )

        elif nilai >= 80:

            st.success(
                "🎉 Semua soal sudah dijawab. Pemahaman geometri "
                "pada arsitektur kesultanan sudah baik."
            )

        elif nilai >= 60:

            st.info(
                "👍 Semua soal sudah dijawab. Pelajari kembali "
                "konsep yang masih belum dikuasai."
            )

        else:

            st.warning(
                "📚 Pelajari kembali materi geometri, simetri, "
                "pengukuran, dan skala."
            )

    # ==========================================================
    # ESSAY
    # ==========================================================

    st.divider()

    st.header("✍️ Soal Essay")

    st.markdown(
        "Kerjakan terlebih dahulu. Klik **Tampilkan Jawaban** "
        "untuk melihat pembahasan."
    )

    essay = [

        (
            "Essay 1",
            "Sebuah gerbang berbentuk segi delapan beraturan memiliki "
            "panjang setiap sisi 3 m. Hitung kelilingnya.",
            "Keliling = 8 × 3 = 24 m."
        ),

        (
            "Essay 2",
            "Sebuah balairung berbentuk persegi panjang berukuran "
            "24 m × 12 m. Hitung luas dan kelilingnya.",
            "Luas = 24 × 12 = 288 m². "
            "Keliling = 2(24 + 12) = 72 m."
        ),

        (
            "Essay 3",
            "Sebuah denah istana dibuat dengan skala 1 : 200. "
            "Jika panjang sebenarnya 40 m, berapa panjang pada denah?",
            "40 m = 4000 cm. "
            "Panjang denah = 4000 ÷ 200 = 20 cm."
        ),

        (
            "Essay 4",
            "Jelaskan apa yang dimaksud dengan simetri refleksi "
            "pada ornamen arsitektur.",
            "Simetri refleksi adalah keadaan ketika suatu bentuk "
            "memiliki bagian yang saling mencerminkan terhadap "
            "suatu garis."
        ),

        (
            "Essay 5",
            "Sebutkan minimal empat bentuk geometri yang dapat "
            "ditemukan atau dimodelkan pada arsitektur kesultanan.",
            "Contohnya persegi, persegi panjang, segitiga, lingkaran, "
            "segi delapan, balok, prisma, dan bentuk geometris lainnya."
        ),

        (
            "Essay 6",
            "Sebuah ruang berukuran 15 m × 8 m. Jika seluruh lantai "
            "akan dipasang ubin berukuran 1 m², berapa ubin yang "
            "dibutuhkan?",
            "Luas ruangan = 15 × 8 = 120 m². "
            "Jika setiap ubin luasnya 1 m², diperlukan 120 ubin."
        ),

        (
            "Essay 7",
            "Jelaskan bagaimana skala dapat digunakan dalam "
            "pembuatan maket istana.",
            "Skala digunakan untuk mengecilkan ukuran sebenarnya "
            "secara proporsional sehingga bangunan dapat dibuat "
            "dalam bentuk model atau maket."
        ),

        (
            "Essay 8",
            "Jelaskan hubungan antara arsitektur kesultanan "
            "dan etnomatematika.",
            "Arsitektur kesultanan merupakan objek budaya yang "
            "mengandung bentuk, ukuran, pola, simetri, proporsi, "
            "dan tata ruang. Unsur tersebut dapat dikaji menggunakan "
            "konsep matematika sehingga menjadi objek pembelajaran "
            "etnomatematika."
        )
    ]

    for judul, pertanyaan, jawaban in essay:

        st.markdown(f"### {judul}")

        st.markdown(pertanyaan)

        with st.expander("👁️ Tampilkan Jawaban"):

            st.success(jawaban)

    # ==========================================================
    # REFLEKSI
    # ==========================================================

    st.divider()

    st.header("💭 Refleksi")

    st.markdown("""
    Setelah mempelajari arsitektur kesultanan, coba pikirkan:

    - Bentuk geometri apa yang paling menarik perhatianmu?
    - Di mana kamu dapat menemukan simetri pada bangunan istana?
    - Bagaimana skala digunakan dalam membuat denah atau maket?
    - Bagaimana tata ruang istana dapat dipelajari menggunakan matematika?
    - Mengapa arsitektur kesultanan penting sebagai sumber belajar
      etnomatematika?
    """)

    st.success(
        "🕌 Arsitektur kesultanan memperlihatkan bahwa matematika "
        "dapat ditemukan dalam bentuk, ruang, pola, ukuran, dan tata "
        "bangunan warisan budaya."
    )

def rumah_tradisional():
    st.markdown(
        '<div class="content-title">🏠 Rumah Tradisional Kalimantan Barat</div>',
        unsafe_allow_html=True
    )

    # ==========================================================
    # MATERI
    # ==========================================================

    st.header("🌿 Mengenal Rumah Tradisional")

    st.markdown(r"""
    Rumah tradisional merupakan bagian penting dari kebudayaan masyarakat
    Indonesia. Bentuk rumah tidak hanya berkaitan dengan tempat tinggal,
    tetapi juga menunjukkan **adaptasi terhadap lingkungan, kehidupan
    sosial, dan nilai budaya masyarakat**.

    Di Kalimantan Barat terdapat berbagai rumah tradisional, antara lain
    **Rumah Radakng** (rumah panjang masyarakat Dayak) dan
    **Rumah Adat Melayu Pontianak**.
    """)

     # ==========================================================
    # GAMBAR 1: RUMAH ADAT MELAYU PONTIANAK
    # ==========================================================

    st.header("🏡 Rumah Adat Melayu Pontianak")

    #st.image(
    #    "https://github.com/havizul/PKM-Streamlit-2026/blob/main/images/Rumah-Adat-Melayu-Pontianak.jpg",
    #    caption="Rumah Adat Melayu Pontianak, Kalimantan Barat — Rumah panggung dengan atap limasan. Sumber: salsawisata.com",
    #    use_container_width=True
    #)

    st.image(
    str(BASE_DIR / "images" / "Rumah-Adat-Melayu-Pontianak.jpg"),
    caption="Rumah Adat Melayu Pontianak, Kalimantan Barat — Rumah panggung dengan atap limasan. Sumber: salsawisata.com",
    use_container_width=True
    )

    st.markdown(r"""
    **Rumah Adat Melayu Pontianak** terletak di Jalan Sutan Syahrir,
    Komplek Perkampungan Budaya Kota Pontianak. Pembangunan rumah ini
    dimulai pada 17 Mei 2003 dan diresmikan pada 9 November 2005

    Bangunan ini berbentuk **rumah panggung** dengan luas 25,62 m × 17,85 m.
    Atapnya berbentuk **limasan** yang memiliki makna sebagai pelindung,
    mengundang, dan menerima [citation:20]. Rumah ini berfungsi sebagai
    pusat kegiatan Majelis Adat Budaya Melayu (MABM) Kalimantan Barat
    """)

    st.markdown(r"""
    **Ciri khas Rumah Adat Melayu Pontianak:**

    - Berbentuk rumah panggung dengan tiang tinggi.
    - Atap limasan dengan kemiringan sekitar 30 derajat.
    - Ornamen khas keraton Kalimantan Barat.
    - Terdapat ruang pustaka, ruang budaya, dan area pertemuan.
    - Dibangun untuk menghindari banjir dan binatang liar.
    """)
    
    # ==========================================================
    # GAMBAR 2: RUMAH RADAKNG
    # ==========================================================

    st.header("🏠 Rumah Radakng (Rumah Panjang Dayak)")

    st.image(
    str(BASE_DIR / "images" / "Rumah-Radakng-Pontianak.jpg"),
    caption="Rumah Radakng di Pontianak, Kalimantan Barat — Rumah panjang masyarakat Dayak Kanayatn.",
    use_container_width=True
    )

    st.markdown(r"""
    **Rumah Radakng** adalah rumah panjang tradisional masyarakat Dayak
    Kanayatn di Kalimantan Barat. Dalam bahasa Dayak, *radakng* berarti
    rumah panjang. Bangunan ini berfungsi sebagai hunian bersama banyak
    keluarga dalam satu komunitas.

    Rumah Radakng yang berdiri di Pontianak merupakan rumah adat terbesar
    dan terpanjang di Indonesia, dengan panjang sekitar **138 meter** dan
    tinggi sekitar **7 meter**. Rumah ini diresmikan pada 2 Juli 2013 dan
    kini berfungsi sebagai pusat kegiatan seni, budaya, dan wisata edukasi.
    """)

    st.markdown(r"""
    **Ciri khas Rumah Radakng:**

    - Berbentuk rumah panggung dengan tiang setinggi 3–5 meter.
    - Memiliki ornamen burung Enggang sebagai simbol masyarakat Dayak.
    - Dibangun menghadap matahari terbit, melambangkan kerja keras sejak pagi.
    - Terdapat kolong rumah untuk menyimpan hasil panen dan alat pertanian.
    - Tangga masuk (*hejot*) berjumlah ganjil sesuai kepercayaan Dayak.
    """)

   

    # ==========================================================
    # BENTUK GEOMETRI
    # ==========================================================

    st.header("📐 Bentuk Geometri pada Rumah Tradisional")

    st.markdown(r"""
    Dalam rumah tradisional Kalimantan Barat, kita dapat menemukan
    berbagai bentuk geometri:

    - **Lantai** dapat dimodelkan sebagai **persegi panjang**.
    - **Tiang** dapat dimodelkan sebagai **balok atau tabung**.
    - **Atap** dapat dimodelkan menggunakan **segitiga atau limasan**.
    - **Jendela dan pintu** dapat berbentuk **persegi atau persegi panjang**.
    - **Denah rumah** dapat dianalisis menggunakan **luas dan keliling**.
    """)

    # ==========================================================
    # CONTOH PERHITUNGAN
    # ==========================================================

    st.header("🔢 Contoh Perhitungan")

    st.markdown(r"""
    Misalkan sebuah ruang pada rumah tradisional berbentuk persegi panjang
    dengan panjang 12 m dan lebar 8 m.
    """)

    st.latex(r"L = p \times l = 12 \times 8 = 96\text{ m}^2")

    st.markdown(r"""
    Jadi, luas ruang tersebut adalah **96 m²**.

    Jika panjang sebuah rumah 20 m dan lebarnya 8 m, maka keliling denah
    rumah adalah:
    """)

    st.latex(r"K = 2(p+l) = 2(20+8) = 56\text{ m}")

    st.markdown(r"""
    Dengan demikian, rumah tradisional dapat menjadi konteks nyata untuk
    mempelajari geometri dan pengukuran.
    """)

    # ==========================================================
    # SOAL INTERAKTIF
    # ==========================================================

    st.divider()
    st.header("🧠 Latihan Interaktif — 20 Soal")

    st.info(
        "Pilih jawaban. Hasil benar atau salah akan langsung muncul. "
        "Setelah selesai, gunakan tombol **Periksa Semua Jawaban**."
    )

    soal = [

        {
            "soal": "1. Sebuah lantai rumah berbentuk persegi panjang dengan panjang 12 m dan lebar 8 m. Berapa luasnya?",
            "pilihan": ["20 m²", "40 m²", "96 m²", "192 m²"],
            "jawaban": "96 m²",
            "pembahasan": "Luas = 12 × 8 = 96 m²."
        },

        {
            "soal": "2. Sebuah denah rumah memiliki panjang 20 m dan lebar 8 m. Berapa kelilingnya?",
            "pilihan": ["28 m", "40 m", "56 m", "160 m"],
            "jawaban": "56 m",
            "pembahasan": "Keliling = 2(20 + 8) = 56 m."
        },

        {
            "soal": "3. Jika sebuah ruangan berbentuk persegi memiliki sisi 6 m, luasnya adalah...",
            "pilihan": ["12 m²", "24 m²", "36 m²", "48 m²"],
            "jawaban": "36 m²",
            "pembahasan": "Luas persegi = 6 × 6 = 36 m²."
        },

        {
            "soal": "4. Sebuah rumah memiliki panjang 30 m dan lebar 10 m. Luas denah rumah adalah...",
            "pilihan": ["40 m²", "100 m²", "300 m²", "600 m²"],
            "jawaban": "300 m²",
            "pembahasan": "Luas = 30 × 10 = 300 m²."
        },

        {
            "soal": "5. Rumah Radakng di Pontianak memiliki panjang sekitar...",
            "pilihan": ["38 m", "88 m", "138 m", "204 m"],
            "jawaban": "138 m",
            "pembahasan": "Rumah Radakng Pontianak memiliki panjang sekitar 138 meter [citation:16]."
        },

        {
            "soal": "6. Tinggi tiang Rumah Betang Sungai Uluk Palin yang disebutkan dalam sumber adalah sekitar...",
            "pilihan": ["4 m", "6 m", "8 m", "12 m"],
            "jawaban": "8 m",
            "pembahasan": "Tinggi tiang yang tercatat adalah sekitar 8 m [citation:3]."
        },

        {
            "soal": "7. Jika panjang rumah 20 m dan dibuat model dengan skala 1 : 10, panjang modelnya adalah...",
            "pilihan": ["0,2 m", "2 m", "10 m", "200 m"],
            "jawaban": "2 m",
            "pembahasan": "Panjang model = 20 ÷ 10 = 2 m."
        },

        {
            "soal": "8. Sebuah tiang rumah berbentuk balok dengan panjang 2 m, lebar 0,5 m, dan tinggi 3 m. Volumenya adalah...",
            "pilihan": ["1 m³", "2 m³", "3 m³", "6 m³"],
            "jawaban": "3 m³",
            "pembahasan": "Volume = 2 × 0,5 × 3 = 3 m³."
        },

        {
            "soal": "9. Atap rumah dimodelkan sebagai segitiga dengan alas 10 m dan tinggi 4 m. Luasnya adalah...",
            "pilihan": ["20 m²", "40 m²", "50 m²", "80 m²"],
            "jawaban": "20 m²",
            "pembahasan": "Luas segitiga = 1/2 × 10 × 4 = 20 m²."
        },

        {
            "soal": "10. Sebuah rumah memiliki 10 bilik. Jika setiap bilik memiliki luas 24 m², total luas bilik adalah...",
            "pilihan": ["34 m²", "120 m²", "240 m²", "340 m²"],
            "jawaban": "240 m²",
            "pembahasan": "Total luas = 10 × 24 = 240 m²."
        },

        {
            "soal": "11. Rumah Betang Sungai Uluk Palin memiliki 53 bilik/ruang. Jika dibagi menjadi 5 kelompok sama banyak, hasil pembagian mendekati...",
            "pilihan": ["8,6", "10,6", "12,6", "15,6"],
            "jawaban": "10,6",
            "pembahasan": "53 ÷ 5 = 10,6."
        },

        {
            "soal": "12. Sebuah tangga memiliki tinggi 3 m dan panjang mendatar 4 m. Jika dianggap sebagai segitiga siku-siku, panjang sisi miringnya adalah...",
            "pilihan": ["4 m", "5 m", "6 m", "7 m"],
            "jawaban": "5 m",
            "pembahasan": "Dengan Teorema Pythagoras: √(3² + 4²) = √25 = 5 m."
        },

        {
            "soal": "13. Sebuah jendela berbentuk persegi panjang berukuran 2 m × 1,5 m. Luasnya adalah...",
            "pilihan": ["2 m²", "3 m²", "3,5 m²", "4 m²"],
            "jawaban": "3 m²",
            "pembahasan": "Luas = 2 × 1,5 = 3 m²."
        },

        {
            "soal": "14. Sebuah rumah memiliki dua bagian lantai yang masing-masing berukuran 10 m × 5 m. Total luas lantainya adalah...",
            "pilihan": ["50 m²", "75 m²", "100 m²", "150 m²"],
            "jawaban": "100 m²",
            "pembahasan": "Satu bagian = 50 m², sehingga dua bagian = 100 m²."
        },

        {
            "soal": "15. Sebuah rumah dibuat dengan bentuk panggung. Salah satu fungsi bentuk tersebut dalam konteks lingkungan adalah...",
            "pilihan": [
                "Mengurangi luas rumah",
                "Menghindari kondisi lingkungan tertentu seperti banjir",
                "Membuat rumah selalu berbentuk lingkaran",
                "Menghilangkan kebutuhan tangga"
            ],
            "jawaban": "Menghindari kondisi lingkungan tertentu seperti banjir",
            "pembahasan": "Rumah panggung dapat menjadi bentuk adaptasi terhadap kondisi lingkungan [citation:3]."
        },

        {
            "soal": "16. Sebuah denah rumah berbentuk persegi panjang memiliki panjang 25 m dan lebar 10 m. Perbandingan panjang : lebar adalah...",
            "pilihan": ["1 : 2", "2 : 5", "5 : 2", "25 : 10"],
            "jawaban": "5 : 2",
            "pembahasan": "25 : 10 disederhanakan menjadi 5 : 2."
        },

        {
            "soal": "17. Jika tinggi sebuah rumah 8 m kemudian dibuat model dengan skala 1 : 4, tinggi model adalah...",
            "pilihan": ["1 m", "2 m", "4 m", "32 m"],
            "jawaban": "2 m",
            "pembahasan": "Tinggi model = 8 ÷ 4 = 2 m."
        },

        {
            "soal": "18. Bentuk lantai rumah yang memiliki panjang dan lebar dapat dimodelkan menggunakan bangun...",
            "pilihan": ["Lingkaran", "Segitiga", "Persegi panjang", "Trapesium"],
            "jawaban": "Persegi panjang",
            "pembahasan": "Denah lantai rumah sering dapat dimodelkan sebagai persegi panjang."
        },

        {
            "soal": "19. Jika sebuah rumah memiliki dua bagian yang sama besar dan simetris terhadap garis tengah, konsep geometri yang digunakan adalah...",
            "pilihan": [
                "Refleksi",
                "Translasi",
                "Dilatasi",
                "Barisan"
            ],
            "jawaban": "Refleksi",
            "pembahasan": "Kesimetrian terhadap garis dapat dikaji menggunakan konsep refleksi."
        },

        {
            "soal": "20. Konsep matematika yang paling banyak digunakan untuk mengkaji ukuran rumah tradisional adalah...",
            "pilihan": [
                "Geometri dan pengukuran",
                "Peluang saja",
                "Statistika saja",
                "Logika saja"
            ],
            "jawaban": "Geometri dan pengukuran",
            "pembahasan": "Bentuk, panjang, lebar, tinggi, luas, keliling, dan volume berkaitan dengan geometri dan pengukuran."
        }
    ]

    jawaban_user = []

    for i, item in enumerate(soal):

        st.markdown(f"###### {item['soal']}")

        jawaban = st.radio(
            "Pilih jawaban:",
            item["pilihan"],
            index=None,
            key=f"rumah_q_{i}",
            label_visibility="collapsed"
        )

        jawaban_user.append(jawaban)

        if jawaban is not None:

            if jawaban == item["jawaban"]:

                st.success(
                    f"✅ Benar! {item['pembahasan']}"
                )

            else:

                st.error(
                    f"❌ Salah. Jawaban yang benar adalah "
                    f"**{item['jawaban']}**. {item['pembahasan']}"
                )

    # ==========================================================
    # PERIKSA SEMUA JAWABAN
    # ==========================================================

    st.divider()

    if st.button(
        "✅ Periksa Semua Jawaban",
        key="cek_semua_rumah",
        use_container_width=True
    ):

        jumlah_dijawab = sum(
            jawaban is not None
            for jawaban in jawaban_user
        )

        jumlah_benar = sum(
            jawaban_user[i] == soal[i]["jawaban"]
            for i in range(len(soal))
            if jawaban_user[i] is not None
        )

        jumlah_belum = len(soal) - jumlah_dijawab

        nilai = jumlah_benar / len(soal) * 100

        st.subheader("📊 Hasil Latihan")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Benar",
            jumlah_benar
        )

        col2.metric(
            "Dijawab",
            jumlah_dijawab
        )

        col3.metric(
            "Belum Dijawab",
            jumlah_belum
        )

        col4.metric(
            "Nilai",
            f"{nilai:.0f}"
        )

        if jumlah_dijawab < len(soal):

            st.warning(
                f"⚠️ Masih ada {jumlah_belum} soal yang belum dijawab."
            )

        elif nilai >= 80:

            st.success(
                "🎉 Semua soal sudah dijawab. Pertahankan pemahamanmu!"
            )

        elif nilai >= 60:

            st.info(
                "👍 Semua soal sudah dijawab. Pelajari kembali konsep "
                "yang masih belum dikuasai."
            )

        else:

            st.warning(
                "📚 Pelajari kembali materi geometri dan pengukuran."
            )

    # ==========================================================
    # SOAL ESSAY
    # ==========================================================

    st.divider()

    st.header("✍️ Soal Essay")

    st.markdown(
        "Kerjakan terlebih dahulu. Klik **Tampilkan Jawaban** "
        "untuk melihat pembahasan."
    )

    essay = [

        (
            "Essay 1",
            "Sebuah lantai rumah berbentuk persegi panjang dengan "
            "panjang 15 m dan lebar 8 m. Hitung luasnya.",
            "Luas = 15 × 8 = 120 m²."
        ),

        (
            "Essay 2",
            "Sebuah denah rumah memiliki panjang 20 m dan lebar 10 m. "
            "Hitung luas dan kelilingnya.",
            "Luas = 20 × 10 = 200 m². "
            "Keliling = 2(20 + 10) = 60 m."
        ),

        (
            "Essay 3",
            "Sebuah rumah dibuat dengan skala 1 : 10. Jika panjang "
            "rumah sebenarnya 30 m, berapa panjang modelnya?",
            "Panjang model = 30 ÷ 10 = 3 m."
        ),

        (
            "Essay 4",
            "Sebuah rumah memiliki 12 bilik dengan luas masing-masing "
            "20 m². Berapa total luas seluruh bilik?",
            "Total luas = 12 × 20 = 240 m²."
        ),

        (
            "Essay 5",
            "Sebuah tangga memiliki tinggi 3 m dan panjang mendatar "
            "4 m. Hitung panjang sisi miringnya.",
            "Dengan Teorema Pythagoras: "
            "√(3² + 4²) = √25 = 5 m."
        ),

        (
            "Essay 6",
            "Jelaskan mengapa rumah tradisional tertentu dibuat "
            "berbentuk panggung.",
            "Rumah panggung dapat menjadi bentuk adaptasi terhadap "
            "kondisi lingkungan, misalnya untuk menghadapi banjir "
            "atau kondisi permukaan tanah tertentu [citation:3]."
        ),

        (
            "Essay 7",
            "Sebutkan minimal lima konsep matematika yang dapat "
            "digunakan untuk mempelajari rumah tradisional.",
            "Contohnya adalah panjang, lebar, tinggi, luas, keliling, "
            "volume, perbandingan, skala, sudut, dan geometri."
        ),

        (
            "Essay 8",
            "Jelaskan bagaimana rumah tradisional dapat digunakan "
            "sebagai konteks pembelajaran matematika.",
            "Rumah tradisional dapat digunakan untuk mempelajari "
            "pengukuran, bangun datar, bangun ruang, skala, "
            "perbandingan, luas, keliling, volume, dan bentuk geometri "
            "melalui objek budaya yang nyata."
        )
    ]

    for judul, pertanyaan, jawaban in essay:

        st.markdown(f"### {judul}")

        st.markdown(pertanyaan)

        with st.expander("👁️ Tampilkan Jawaban"):

            st.success(jawaban)

    # ==========================================================
    # REFLEKSI
    # ==========================================================

    st.divider()

    st.header("💭 Refleksi")

    st.markdown(r"""
    Setelah mempelajari rumah tradisional, coba pikirkan:

    - Bentuk geometri apa yang dapat ditemukan pada rumah tradisional?
    - Bagaimana cara menghitung luas sebuah denah rumah?
    - Mengapa ukuran dan bentuk rumah dapat berkaitan dengan lingkungan?
    - Bagaimana matematika dapat membantu mendokumentasikan bentuk
      rumah tradisional?
    - Apa yang dapat dilakukan generasi muda untuk mengenal dan
      melestarikan rumah tradisional?
    """)

    st.success(
        "🏠 Rumah tradisional bukan hanya warisan budaya, "
        "tetapi juga sumber belajar matematika yang dekat dengan kehidupan."
    )
    



def batik_geometri():
    st.markdown(
        '<div class="content-title">🎨 Batik dan Pola Geometri</div>',
        unsafe_allow_html=True
    )

    # ==========================================================
    # MATERI
    # ==========================================================

    st.header("🌺 Mengenal Batik dan Geometri")

    st.markdown("""
    Batik merupakan salah satu warisan budaya Indonesia yang memiliki
    beragam motif. Banyak motif batik dapat dikaji menggunakan konsep
    matematika, khususnya **geometri dan pola**.

    Pada beberapa motif dapat ditemukan bentuk seperti **persegi,
    persegi panjang, segitiga, belah ketupat, lingkaran, garis diagonal,
    serta pola yang berulang**.
    """)

    st.image(
        "https://commons.wikimedia.org/wiki/Special:Redirect/file/Motif_Tapak_Kebo.jpg",
        caption="Motif Batik Baduy Tapak Kebo — Sumber: Wikimedia Commons, CC BY-SA 4.0",
        use_container_width=True
    )

    st.caption(
        "Sumber gambar: Wikimedia Commons — Motif Batik Tapak Kebo."
    )

    st.header("📐 Unsur Geometri pada Motif Batik")

    st.markdown("""
    Beberapa unsur matematika yang dapat diamati pada motif batik:

    **1. Titik dan garis**  
    Garis horizontal, vertikal, diagonal, maupun lengkung dapat menjadi
    bagian dasar pembentukan motif.

    **2. Bangun datar**  
    Motif dapat membentuk persegi, segitiga, lingkaran, belah ketupat,
    dan bentuk geometris lainnya.

    **3. Simetri**  
    Sebagian motif memiliki simetri lipat atau simetri putar.

    **4. Transformasi geometri**  
    Pola dapat terbentuk melalui translasi, rotasi, dan refleksi.

    **5. Pola berulang**  
    Satu motif dasar dapat diulang sehingga menghasilkan pola yang
    memenuhi permukaan kain.
    """)

    st.image(
        "https://commons.wikimedia.org/wiki/Special:Redirect/file/Batik_jumputan_motif_persegi.png",
        caption="Contoh pola batik berbentuk persegi — Sumber: Wikimedia Commons, CC BY-SA 4.0",
        use_container_width=True
    )

    st.caption(
        "Sumber gambar: Wikimedia Commons — Batik Jumputan Motif Persegi."
    )

    st.header("🔷 Contoh Motif Geometris")

    st.markdown("""
    Motif geometris dapat dijumpai dalam berbagai tradisi batik Indonesia.
    Misalnya, batik Cirebon memiliki kelompok ragam hias geometris yang
    mencakup motif seperti **tambal sewu, liris, kawung, dan
    lengko-lengko**.

    Motif tumpal juga memiliki bentuk geometris yang jelas, yaitu
    susunan segitiga yang berulang.

    Dalam matematika, pola tersebut dapat digunakan untuk mempelajari
    **bentuk, ukuran, sudut, simetri, transformasi, dan keteraturan pola**.
    """)

    st.image(
        "https://commons.wikimedia.org/wiki/Special:Redirect/file/Batik_Motif_Pasisiran.jpg",
        caption="Contoh kain batik bermotif — Sumber: Wikimedia Commons, CC0",
        use_container_width=True
    )

    st.caption(
        "Sumber gambar: Wikimedia Commons — Batik Motif Pasisiran."
    )

    st.header("🔄 Transformasi pada Motif Batik")

    st.markdown("""
    Pola batik dapat dipahami menggunakan transformasi geometri.

    **Translasi** → menggeser motif tanpa mengubah bentuk dan ukurannya.

    **Rotasi** → memutar motif terhadap suatu titik.

    **Refleksi** → mencerminkan motif terhadap suatu garis.

    **Dilatasi** → memperbesar atau memperkecil motif dengan faktor skala.

    Contoh sederhana: jika sebuah motif persegi berukuran $4 \\times 4$ cm
    diperbesar dengan faktor skala 2, maka panjang sisinya menjadi 8 cm.
    """)

    st.header("📊 Batik sebagai Pola Matematika")

    st.markdown("""
    Misalkan sebuah motif memiliki lebar 5 cm dan motif tersebut diulang
    sebanyak 12 kali.

    Panjang pola yang terbentuk:

    """)
    st.latex(r"P = 12 \times 5 = 60\text{ cm}")

    st.markdown("""
    Dengan demikian, matematika dapat membantu kita menganalisis
    keteraturan motif sekaligus memahami bagaimana pola budaya dapat
    dimodelkan secara matematis.
    """)

    # ==========================================================
    # SOAL INTERAKTIF
    # ==========================================================

    st.divider()
    st.header("🧠 Latihan Interaktif — 20 Soal")

    st.info(
        "Pilih jawaban. Setelah pilihan diklik, hasil benar/salah akan "
        "langsung ditampilkan. Setelah selesai, gunakan tombol "
        "**Periksa Semua Jawaban** di bagian bawah."
    )

    soal = [
        {
            "soal": "1. Sebuah motif persegi memiliki sisi 6 cm. Berapa luasnya?",
            "pilihan": ["12 cm²", "24 cm²", "36 cm²", "42 cm²"],
            "jawaban": "36 cm²",
            "pembahasan": "Luas persegi = sisi × sisi = 6 × 6 = 36 cm²."
        },
        {
            "soal": "2. Sebuah pola batik berbentuk persegi panjang berukuran 10 cm × 4 cm. Berapa luasnya?",
            "pilihan": ["14 cm²", "28 cm²", "40 cm²", "80 cm²"],
            "jawaban": "40 cm²",
            "pembahasan": "Luas = panjang × lebar = 10 × 4 = 40 cm²."
        },
        {
            "soal": "3. Persegi panjang berukuran 10 cm × 4 cm. Berapa kelilingnya?",
            "pilihan": ["14 cm", "20 cm", "28 cm", "40 cm"],
            "jawaban": "28 cm",
            "pembahasan": "Keliling = 2(10 + 4) = 28 cm."
        },
        {
            "soal": "4. Motif digeser 5 cm ke kanan tanpa mengubah bentuknya. Transformasi tersebut disebut...",
            "pilihan": ["Rotasi", "Refleksi", "Translasi", "Dilatasi"],
            "jawaban": "Translasi",
            "pembahasan": "Translasi adalah perpindahan atau penggeseran suatu objek."
        },
        {
            "soal": "5. Sebuah motif diputar 90° terhadap titik pusat. Transformasi tersebut disebut...",
            "pilihan": ["Translasi", "Rotasi", "Refleksi", "Dilatasi"],
            "jawaban": "Rotasi",
            "pembahasan": "Rotasi adalah transformasi berupa perputaran."
        },
        {
            "soal": "6. Motif dicerminkan terhadap garis vertikal. Transformasi tersebut disebut...",
            "pilihan": ["Rotasi", "Translasi", "Refleksi", "Dilatasi"],
            "jawaban": "Refleksi",
            "pembahasan": "Refleksi adalah pencerminan terhadap suatu garis."
        },
        {
            "soal": "7. Sebuah motif berukuran 4 cm diulang sebanyak 15 kali. Berapa panjang susunan motif?",
            "pilihan": ["19 cm", "45 cm", "60 cm", "75 cm"],
            "jawaban": "60 cm",
            "pembahasan": "Panjang = 15 × 4 = 60 cm."
        },
        {
            "soal": "8. Sebuah motif berukuran 20 cm diperbesar dengan skala 2. Berapa ukurannya?",
            "pilihan": ["10 cm", "22 cm", "40 cm", "60 cm"],
            "jawaban": "40 cm",
            "pembahasan": "Ukuran baru = 2 × 20 = 40 cm."
        },
        {
            "soal": "9. Sebuah motif memiliki panjang 30 cm dan lebar 10 cm. Perbandingan panjang : lebar adalah...",
            "pilihan": ["1 : 3", "2 : 1", "3 : 1", "3 : 2"],
            "jawaban": "3 : 1",
            "pembahasan": "30 : 10 = 3 : 1."
        },
        {
            "soal": "10. Sebuah kain batik berukuran 200 cm × 80 cm. Luas kain adalah...",
            "pilihan": ["280 cm²", "800 cm²", "16.000 cm²", "28.000 cm²"],
            "jawaban": "16.000 cm²",
            "pembahasan": "Luas = 200 × 80 = 16.000 cm²."
        },
        {
            "soal": "11. Sebanyak 25% dari luas kain 16.000 cm² digunakan untuk motif utama. Berapa luasnya?",
            "pilihan": ["2.000 cm²", "4.000 cm²", "6.000 cm²", "8.000 cm²"],
            "jawaban": "4.000 cm²",
            "pembahasan": "25% × 16.000 = 4.000 cm²."
        },
        {
            "soal": "12. Pola motif memiliki jumlah 3, 6, 9, 12, ... Pola tersebut memiliki beda...",
            "pilihan": ["2", "3", "4", "6"],
            "jawaban": "3",
            "pembahasan": "Setiap suku bertambah 3."
        },
        {
            "soal": "13. Jika pola jumlah motif adalah 3, 6, 9, 12, ..., berapa suku ke-10?",
            "pilihan": ["27", "30", "33", "36"],
            "jawaban": "30",
            "pembahasan": "Suku ke-n = 3n, sehingga suku ke-10 = 30."
        },
        {
            "soal": "14. Sebuah motif memiliki simetri lipat. Artinya...",
            "pilihan": [
                "Motif dapat digeser",
                "Motif dapat dibagi menjadi bagian yang saling berimpit ketika dilipat",
                "Motif selalu berbentuk lingkaran",
                "Motif harus memiliki warna yang sama"
            ],
            "jawaban": "Motif dapat dibagi menjadi bagian yang saling berimpit ketika dilipat",
            "pembahasan": "Simetri lipat terjadi ketika dua bagian objek dapat berimpit setelah dilipat."
        },
        {
            "soal": "15. Sebuah motif diputar dan kembali tepat ke posisi semula setelah 180°. Konsep yang berkaitan adalah...",
            "pilihan": ["Simetri putar", "Keliling", "Luas", "Translasi"],
            "jawaban": "Simetri putar",
            "pembahasan": "Simetri putar berkaitan dengan posisi objek yang kembali berimpit setelah diputar."
        },
        {
            "soal": "16. Sebuah motif segitiga memiliki alas 10 cm dan tinggi 8 cm. Berapa luasnya?",
            "pilihan": ["18 cm²", "40 cm²", "80 cm²", "160 cm²"],
            "jawaban": "40 cm²",
            "pembahasan": "Luas segitiga = 1/2 × 10 × 8 = 40 cm²."
        },
        {
            "soal": "17. Sebuah motif lingkaran memiliki jari-jari 7 cm. Dengan π = 22/7, luasnya adalah...",
            "pilihan": ["44 cm²", "88 cm²", "154 cm²", "308 cm²"],
            "jawaban": "154 cm²",
            "pembahasan": "Luas = πr² = 22/7 × 7² = 154 cm²."
        },
        {
            "soal": "18. Sebuah pola terdiri dari motif A-B-C yang berulang. Setelah C, motif berikutnya adalah...",
            "pilihan": ["A", "B", "C", "D"],
            "jawaban": "A",
            "pembahasan": "Pola A-B-C berulang sehingga setelah C kembali ke A."
        },
        {
            "soal": "19. Motif batik berupa deretan belah ketupat yang sama dan berulang. Konsep matematika yang paling tepat adalah...",
            "pilihan": [
                "Pola berulang",
                "Persamaan kuadrat",
                "Peluang",
                "Statistika bivariat"
            ],
            "jawaban": "Pola berulang",
            "pembahasan": "Pengulangan bentuk yang sama merupakan contoh pola berulang."
        },
        {
            "soal": "20. Dalam menganalisis motif batik, kombinasi konsep yang paling sesuai adalah...",
            "pilihan": [
                "Geometri dan transformasi",
                "Hanya aritmetika",
                "Hanya statistika",
                "Hanya peluang"
            ],
            "jawaban": "Geometri dan transformasi",
            "pembahasan": "Motif batik dapat dianalisis melalui bentuk geometri dan transformasi seperti translasi, rotasi, refleksi, dan dilatasi."
        }
    ]

    jawaban_user = []

    for i, item in enumerate(soal):

        st.markdown(f"### {item['soal']}")

        jawaban = st.radio(
            "Pilih jawaban:",
            item["pilihan"],
            index=None,
            key=f"batik_q_{i}",
            label_visibility="collapsed"
        )

        jawaban_user.append(jawaban)

        if jawaban is not None:

            if jawaban == item["jawaban"]:
                st.success(
                    f"✅ Benar! {item['pembahasan']}"
                )

            else:
                st.error(
                    f"❌ Salah. Jawaban yang benar adalah **{item['jawaban']}**. "
                    f"{item['pembahasan']}"
                )

    # ==========================================================
    # PERIKSA SEMUA
    # ==========================================================

    st.divider()

    if st.button(
        "✅ Periksa Semua Jawaban",
        key="cek_semua_batik",
        use_container_width=True
    ):

        jumlah_dijawab = sum(
            jawaban is not None
            for jawaban in jawaban_user
        )

        jumlah_benar = sum(
            jawaban_user[i] == soal[i]["jawaban"]
            for i in range(len(soal))
            if jawaban_user[i] is not None
        )

        jumlah_belum = len(soal) - jumlah_dijawab

        nilai = jumlah_benar / len(soal) * 100

        st.subheader("📊 Hasil Latihan")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Benar",
            jumlah_benar
        )

        col2.metric(
            "Dijawab",
            jumlah_dijawab
        )

        col3.metric(
            "Belum Dijawab",
            jumlah_belum
        )

        col4.metric(
            "Nilai",
            f"{nilai:.0f}"
        )

        if jumlah_dijawab < len(soal):

            st.warning(
                f"⚠️ Masih ada {jumlah_belum} soal yang belum dijawab."
            )

        elif nilai >= 80:

            st.success(
                "🎉 Semua soal sudah dijawab. Pertahankan pemahamanmu!"
            )

        elif nilai >= 60:

            st.info(
                "👍 Semua soal sudah dijawab. Coba pelajari kembali "
                "materi yang masih belum dikuasai."
            )

        else:

            st.warning(
                "📚 Pelajari kembali konsep geometri dan pola sebelum "
                "mengerjakan latihan berikutnya."
            )

    # ==========================================================
    # ESSAY
    # ==========================================================

    st.divider()

    st.header("✍️ Soal Essay")

    st.markdown(
        "Kerjakan terlebih dahulu. Klik bagian **Tampilkan Jawaban** "
        "untuk melihat pembahasan."
    )

    essay = [
        (
            "Essay 1",
            "Sebuah motif batik berbentuk persegi panjang berukuran "
            "25 cm × 12 cm. Hitung luasnya.",
            "Luas = panjang × lebar = 25 × 12 = 300 cm²."
        ),
        (
            "Essay 2",
            "Sebuah motif berbentuk persegi memiliki sisi 15 cm. "
            "Hitung luas dan kelilingnya.",
            "Luas = 15 × 15 = 225 cm². Keliling = 4 × 15 = 60 cm."
        ),
        (
            "Essay 3",
            "Sebuah motif memiliki titik A(2, 3). Motif tersebut "
            "ditranslasikan 5 satuan ke kanan. Tentukan koordinat "
            "bayangan titik A.",
            "Translasi ke kanan 5 satuan: A'(2 + 5, 3) = A'(7, 3)."
        ),
        (
            "Essay 4",
            "Sebuah pola motif memiliki lebar 6 cm dan diulang "
            "sebanyak 20 kali. Berapa panjang pola seluruhnya?",
            "Panjang pola = 6 × 20 = 120 cm."
        ),
        (
            "Essay 5",
            "Jelaskan perbedaan translasi, rotasi, dan refleksi "
            "dalam pola batik.",
            "Translasi adalah pergeseran, rotasi adalah perputaran, "
            "sedangkan refleksi adalah pencerminan terhadap suatu garis."
        ),
        (
            "Essay 6",
            "Sebuah motif memiliki pola jumlah 4, 8, 12, 16, ... "
            "Tentukan suku ke-10.",
            "Barisan memiliki beda 4. Suku ke-10 = 4 × 10 = 40."
        ),
        (
            "Essay 7",
            "Sebuah kain batik berukuran 200 cm × 80 cm. "
            "Jika 25% luas kain digunakan untuk motif utama, "
            "berapa luas bagian tersebut?",
            "Luas kain = 200 × 80 = 16.000 cm². "
            "Bagian motif = 25% × 16.000 = 4.000 cm²."
        ),
        (
            "Essay 8",
            "Sebutkan minimal tiga konsep matematika yang dapat "
            "digunakan untuk menganalisis pola batik.",
            "Contohnya adalah bangun datar, simetri, translasi, "
            "rotasi, refleksi, dilatasi, pola berulang, luas, "
            "keliling, dan perbandingan."
        )
    ]

    for judul, pertanyaan, jawaban in essay:

        st.markdown(f"### {judul}")

        st.markdown(pertanyaan)

        with st.expander("👁️ Tampilkan Jawaban"):

            st.success(jawaban)

    # ==========================================================
    # REFLEKSI
    # ==========================================================

    st.divider()

    st.header("💭 Refleksi")

    st.markdown("""
    Setelah mempelajari materi ini, coba pikirkan:

    - Bentuk geometri apa yang paling sering kamu temukan pada motif batik?
    - Apakah kamu dapat menemukan pola pengulangan pada kain batik?
    - Transformasi geometri apa yang dapat digunakan untuk menjelaskan
      pengulangan motif?
    - Bagaimana matematika dapat membantu mendokumentasikan dan
      mengembangkan motif budaya Indonesia?
    """)

    st.success(
        "🌺 Matematika tidak hanya ditemukan di dalam buku, "
        "tetapi juga dapat ditemukan dalam seni, budaya, dan kehidupan masyarakat."
    )


def tenun_motif():

    st.markdown(
        '<div class="content-title">🧵 Tenun dan Motif Tradisional</div>',
        unsafe_allow_html=True
    )

    # =========================================================
    # MATERI RINGKAS
    # =========================================================

    st.header("🌿 Mengenal Tenun Sambas")

    st.markdown("""
    Tenun Sambas merupakan salah satu warisan budaya dari Kalimantan Barat.
    Kain tenun Sambas memiliki beragam motif, antara lain motif tumbuhan,
    geometris, dan motif yang berkaitan dengan budaya masyarakat Sambas.

    Dalam matematika, motif tenun dapat digunakan untuk mempelajari
    **pola, geometri, simetri, transformasi, pengukuran, perbandingan,
    dan statistika sederhana**.
    """)

    st.image(
        "https://indonesiakaya.com/wp-content/uploads/2020/10/4__IMG_1729_Harga_tenun_Sambas_biasanya_tergantung_dari_kain_bahan_dan_motif_apa_yang_dibuat.jpg",
        caption="Proses pembuatan Tenun Sambas — Sumber: Indonesia Kaya",
        use_container_width=True
    )

    st.caption(
        "Sumber: Indonesia Kaya — Tenun Sambas: Kain Tradisional Kalimantan Barat yang Mendunia."
    )

    st.header("🧵 Motif dan Pola")

    st.markdown("""
    Motif pada kain tenun dapat disusun secara berulang sehingga
    membentuk pola yang teratur.

    Dalam matematika, pengulangan tersebut dapat dikaitkan dengan:

    - pola bilangan,
    - translasi,
    - refleksi,
    - rotasi,
    - bangun datar,
    - simetri.
    """)

    st.image(
        "https://awsimages.detik.net.id/community/media/visual/2021/02/03/dev-kain-tenun-songket-khas-sambas.jpeg?w=1200",
        caption="Alat tenun Songket Sambas — Sumber: detikTravel",
        use_container_width=True
    )

    st.caption(
        "Sumber: detikTravel — Kain Tenun Songket Khas Sambas."
    )

    st.info("""
    💡 **Konteks matematika**

    Motif yang berulang dapat dipandang sebagai suatu unit pola yang
    digeser, diputar, atau dicerminkan.
    """)

    st.header("📐 Contoh Matematika")

    st.markdown("""
    Misalkan satu unit motif memiliki panjang 8 cm dan diulang 10 kali.
    """)

    st.latex(r"L=n\times p")

    st.latex(r"L=10\times8=80\text{ cm}")

    st.success("Panjang keseluruhan pola adalah 80 cm.")

    st.markdown("""
    Jika sebuah unit motif berbentuk persegi panjang dengan panjang 8 cm
    dan lebar 5 cm:
    """)

    st.latex(r"L=p\times l")

    st.latex(r"L=8\times5=40\text{ cm}^2")

    st.markdown("""
    Jadi, konsep matematika dapat ditemukan melalui bentuk, ukuran,
    pengulangan, dan susunan motif.
    """)

    st.header("🔄 Transformasi pada Motif")

    st.markdown("""
    Motif dapat mengalami beberapa transformasi geometri:

    **Translasi** → motif digeser.

    **Refleksi** → motif dicerminkan.

    **Rotasi** → motif diputar.
    """)

    st.latex(r"T(x,y)=(x+a,y)")

    st.header("📏 Skala")

    st.markdown("""
    Skala digunakan ketika motif digambar lebih kecil atau lebih besar
    daripada ukuran sebenarnya.

    Jika panjang motif sebenarnya 40 cm dan skala 1 : 4:
    """)

    st.latex(r"\text{Ukuran gambar}=\frac{40}{4}=10\text{ cm}")

    st.header("💰 Matematika dalam Produksi Tenun")

    st.markdown("""
    Matematika juga digunakan dalam kegiatan produksi dan penjualan.

    Misalnya:

    Biaya produksi = Rp250.000

    Harga jual = Rp350.000

    Maka:
    """)

    st.latex(r"\text{Keuntungan}=\text{Harga Jual}-\text{Biaya Produksi}")

    st.latex(r"\text{Keuntungan}=350000-250000=100000")

    st.success("Keuntungan per kain adalah Rp100.000.")

    st.header("📊 Statistika Sederhana")

    st.markdown("""
    Jumlah motif pada beberapa kain juga dapat dianalisis menggunakan
    statistika.

    Misalnya data jumlah motif:

    **12, 15, 10, 18, 15**
    """)

    st.latex(r"\bar{x}=\frac{12+15+10+18+15}{5}=14")

    st.success("Rata-rata jumlah motif adalah 14.")

    st.header("🌿 Inti Pembelajaran")

    st.markdown("""
    Dari Tenun Sambas kita dapat mempelajari:

    - **Pola** → pengulangan motif.
    - **Geometri** → bentuk motif.
    - **Simetri** → keteraturan motif.
    - **Transformasi** → translasi, refleksi, dan rotasi.
    - **Pengukuran** → panjang, luas, dan keliling.
    - **Skala** → perbandingan ukuran.
    - **Statistika** → analisis data motif.
    - **Aritmetika** → biaya dan keuntungan produksi.
    """)

    st.info("""
    🎯 **Matematika tidak hanya terdapat dalam rumus, tetapi juga dapat
    ditemukan dalam artefak dan aktivitas budaya masyarakat.**
    """)

    # =========================================================
    # 20 SOAL INTERAKTIF
    # =========================================================

    st.divider()
    st.header("📝 20 Soal Interaktif")

    st.markdown("""
    Pilih jawaban pada setiap soal.

    **Setelah memilih jawaban, hasilnya langsung ditampilkan.**

    Setelah menyelesaikan soal nomor 20, tekan tombol
    **Periksa Semua Jawaban** untuk melihat nilai akhir.
    """)

    soal = [
        {
            "q": "1. Jika satu unit motif panjangnya 8 cm dan diulang 10 kali, berapa panjang seluruh pola?",
            "opsi": ["18 cm", "40 cm", "80 cm", "100 cm"],
            "jawaban": "80 cm",
            "pembahasan": "10 × 8 = 80 cm."
        },
        {
            "q": "2. Motif berbentuk persegi dengan sisi 6 cm. Berapa luasnya?",
            "opsi": ["12 cm²", "24 cm²", "36 cm²", "48 cm²"],
            "jawaban": "36 cm²",
            "pembahasan": "Luas persegi = 6 × 6 = 36 cm²."
        },
        {
            "q": "3. Persegi panjang memiliki panjang 10 cm dan lebar 4 cm. Kelilingnya adalah...",
            "opsi": ["14 cm", "20 cm", "28 cm", "40 cm"],
            "jawaban": "28 cm",
            "pembahasan": "K = 2(10 + 4) = 28 cm."
        },
        {
            "q": "4. Motif digeser 8 cm ke kanan. Transformasi tersebut disebut...",
            "opsi": ["Rotasi", "Refleksi", "Translasi", "Dilatasi"],
            "jawaban": "Translasi",
            "pembahasan": "Translasi adalah pergeseran suatu objek."
        },
        {
            "q": "5. Motif diputar sebesar 90°. Transformasi tersebut disebut...",
            "opsi": ["Translasi", "Rotasi", "Refleksi", "Dilatasi"],
            "jawaban": "Rotasi",
            "pembahasan": "Rotasi adalah transformasi berupa perputaran."
        },
        {
            "q": "6. Motif dicerminkan terhadap suatu garis. Transformasi tersebut disebut...",
            "opsi": ["Rotasi", "Translasi", "Refleksi", "Dilatasi"],
            "jawaban": "Refleksi",
            "pembahasan": "Refleksi berarti pencerminan."
        },
        {
            "q": "7. Panjang kain 240 cm. Setiap motif membutuhkan 8 cm. Berapa motif yang dapat disusun?",
            "opsi": ["20", "24", "30", "32"],
            "jawaban": "30",
            "pembahasan": "240 ÷ 8 = 30 motif."
        },
        {
            "q": "8. Ukuran sebenarnya motif 40 cm. Jika skala 1 : 4, ukuran pada gambar adalah...",
            "opsi": ["5 cm", "10 cm", "20 cm", "160 cm"],
            "jawaban": "10 cm",
            "pembahasan": "40 ÷ 4 = 10 cm."
        },
        {
            "q": "9. Perbandingan panjang dan lebar motif adalah 12 : 8. Bentuk sederhananya adalah...",
            "opsi": ["2 : 1", "3 : 2", "4 : 3", "6 : 5"],
            "jawaban": "3 : 2",
            "pembahasan": "12 : 8 dibagi 4 menjadi 3 : 2."
        },
        {
            "q": "10. Kain berukuran 200 cm × 80 cm. Berapa luas kain?",
            "opsi": ["280 cm²", "2.800 cm²", "16.000 cm²", "28.000 cm²"],
            "jawaban": "16.000 cm²",
            "pembahasan": "200 × 80 = 16.000 cm²."
        },
        {
            "q": "11. Jika 60% dari luas kain 16.000 cm² merupakan area bermotif, berapa luasnya?",
            "opsi": ["6.000 cm²", "9.600 cm²", "10.000 cm²", "12.000 cm²"],
            "jawaban": "9.600 cm²",
            "pembahasan": "60% × 16.000 = 9.600 cm²."
        },
        {
            "q": "12. Barisan 4, 8, 12, 16, ... memiliki beda...",
            "opsi": ["2", "3", "4", "8"],
            "jawaban": "4",
            "pembahasan": "Setiap suku bertambah 4."
        },
        {
            "q": "13. Suku ke-10 dari barisan 4, 8, 12, 16, ... adalah...",
            "opsi": ["36", "40", "44", "48"],
            "jawaban": "40",
            "pembahasan": "U₁₀ = 4 + (10 − 1) × 4 = 40."
        },
        {
            "q": "14. Biaya bahan Rp150.000 dan tenaga kerja Rp100.000. Total biaya produksi adalah...",
            "opsi": ["Rp200.000", "Rp250.000", "Rp300.000", "Rp350.000"],
            "jawaban": "Rp250.000",
            "pembahasan": "150.000 + 100.000 = 250.000."
        },
        {
            "q": "15. Biaya produksi Rp250.000 dan harga jual Rp350.000. Keuntungannya adalah...",
            "opsi": ["Rp50.000", "Rp75.000", "Rp100.000", "Rp150.000"],
            "jawaban": "Rp100.000",
            "pembahasan": "350.000 − 250.000 = 100.000."
        },
        {
            "q": "16. Jika keuntungan satu kain Rp100.000 dan dibuat 10 kain, total keuntungan adalah...",
            "opsi": ["Rp100.000", "Rp500.000", "Rp1.000.000", "Rp1.500.000"],
            "jawaban": "Rp1.000.000",
            "pembahasan": "10 × 100.000 = 1.000.000."
        },
        {
            "q": "17. Data jumlah motif adalah 12, 15, 10, 18, 15. Berapa rata-ratanya?",
            "opsi": ["12", "13", "14", "15"],
            "jawaban": "14",
            "pembahasan": "(12 + 15 + 10 + 18 + 15) ÷ 5 = 14."
        },
        {
            "q": "18. Median dari data 12, 15, 10, 18, 15 adalah...",
            "opsi": ["10", "12", "14", "15"],
            "jawaban": "15",
            "pembahasan": "Data diurutkan menjadi 10, 12, 15, 15, 18. Median = 15."
        },
        {
            "q": "19. Satu unit motif memiliki luas 40 cm². Jika terdapat 20 unit, berapa luas seluruh unit?",
            "opsi": ["400 cm²", "600 cm²", "800 cm²", "1.000 cm²"],
            "jawaban": "800 cm²",
            "pembahasan": "20 × 40 = 800 cm²."
        },
        {
            "q": "20. Konsep matematika yang paling sesuai untuk motif yang berulang secara teratur adalah...",
            "opsi": [
                "Pola dan transformasi",
                "Logaritma saja",
                "Integral saja",
                "Matriks saja"
            ],
            "jawaban": "Pola dan transformasi",
            "pembahasan": "Pengulangan motif dapat dianalisis menggunakan pola dan transformasi."
        }
    ]

    jawaban_user = []

    for i, item in enumerate(soal):

        st.markdown(f"**{item['q']}**")

        jawaban = st.radio(
            "Pilih jawaban:",
            item["opsi"],
            key=f"tenun_soal_{i}",
            index=None
        )

        jawaban_user.append(jawaban)

        if jawaban is not None:

            if jawaban == item["jawaban"]:

                st.success(
                    f"✅ Benar! {item['pembahasan']}"
                )

            else:

                st.error(
                    f"❌ Salah. Jawaban yang benar adalah **{item['jawaban']}**. "
                    f"{item['pembahasan']}"
                )

        if i < len(soal) - 1:
            st.divider()

    # =========================================================
    # PERIKSA SEMUA JAWABAN
    # =========================================================

    st.divider()

    st.subheader("📊 Hasil Akhir")

    if st.button(
        "✅ Periksa Semua Jawaban",
        key="cek_semua_tenun",
        use_container_width=True
    ):

        jumlah_benar = sum(
            jawaban_user[i] == soal[i]["jawaban"]
            for i in range(len(soal))
            if jawaban_user[i] is not None
        )

        jumlah_dijawab = sum(
            jawaban is not None
            for jawaban in jawaban_user
        )

        jumlah_belum = 20 - jumlah_dijawab
        nilai = jumlah_benar / 20 * 100

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "Benar",
                jumlah_benar
            )

        with col2:
            st.metric(
                "Salah",
                jumlah_dijawab - jumlah_benar
            )

        with col3:
            st.metric(
                "Belum dijawab",
                jumlah_belum
            )

        with col4:
            st.metric(
                "Nilai",
                f"{nilai:.0f}"
            )

        if jumlah_belum > 0:

            st.warning(
                f"Masih ada {jumlah_belum} soal yang belum dijawab."
            )

        if nilai >= 85:

            st.success(
                "🎉 Hasil sangat baik."
            )

        elif nilai >= 70:

            st.info(
                "👍 Hasil baik. Beberapa konsep masih dapat diperdalam."
            )

        elif nilai >= 60:

            st.warning(
                "📚 Cukup. Pelajari kembali materi yang belum dikuasai."
            )

        else:

            st.error(
                "💡 Pelajari kembali materi sebelum mengulang kuis."
            )

    # =========================================================
    # SOAL ESSAY
    # =========================================================

    st.divider()

    st.header("✍️ Soal Essay")

    st.markdown("""
    Jawablah pertanyaan berikut dengan menggunakan konsep matematika
    dan hubungkan dengan konteks tenun atau motif tradisional.
    """)

    st.markdown("### Essay 1")
    st.markdown("""
    Sebuah kain memiliki motif berulang dengan panjang satu unit motif
    12 cm. Jika terdapat 25 unit motif, tentukan panjang seluruh pola.
    Jelaskan langkah perhitungannya.
    """)

    with st.expander("👁️ Tampilkan Jawaban Essay 1"):
        st.markdown("""
        Diketahui:

        - Panjang satu motif = 12 cm.
        - Jumlah motif = 25.
        """)
        st.latex(r"L=25\times12=300\text{ cm}")
        st.markdown("Jadi, panjang seluruh pola adalah **300 cm**.")

    st.markdown("### Essay 2")
    st.markdown("""
    Sebuah unit motif berbentuk persegi panjang dengan panjang 15 cm
    dan lebar 8 cm. Tentukan luas dan keliling unit motif tersebut.
    """)

    with st.expander("👁️ Tampilkan Jawaban Essay 2"):
        st.latex(r"L=15\times8=120\text{ cm}^2")
        st.latex(r"K=2(15+8)=46\text{ cm}")
        st.markdown("Jadi luasnya **120 cm²** dan kelilingnya **46 cm**.")

    st.markdown("### Essay 3")
    st.markdown("""
    Jelaskan bagaimana konsep translasi dapat digunakan untuk menjelaskan
    pengulangan motif pada kain tenun.
    """)

    with st.expander("👁️ Tampilkan Jawaban Essay 3"):
        st.markdown("""
        Translasi merupakan transformasi berupa pergeseran suatu objek
        tanpa mengubah bentuk dan ukurannya.

        Pada motif tenun, satu unit motif dapat digeser dengan jarak
        tertentu secara berulang.
        """)
        st.latex(r"T(x,y)=(x+8,y)")

    st.markdown("### Essay 4")
    st.markdown("""
    Sebuah kain berukuran 200 cm × 80 cm. Sebanyak 60% permukaannya
    merupakan area bermotif. Hitung luas area bermotif.
    """)

    with st.expander("👁️ Tampilkan Jawaban Essay 4"):
        st.latex(r"A=200\times80=16000\text{ cm}^2")
        st.latex(r"A_{\text{motif}}=0.60\times16000=9600\text{ cm}^2")

    st.markdown("### Essay 5")
    st.markdown("""
    Jelaskan bagaimana matematika dapat digunakan untuk membantu
    pengrajin menentukan harga jual kain tenun.
    """)

    with st.expander("👁️ Tampilkan Jawaban Essay 5"):
        st.latex(r"\text{Keuntungan}=\text{Harga Jual}-\text{Biaya Produksi}")
        st.markdown("""
        Matematika dapat digunakan untuk menghitung biaya bahan,
        tenaga kerja, biaya produksi, keuntungan, dan harga jual.
        """)

    st.markdown("### Essay 6")
    st.markdown("""
    Jelaskan hubungan antara pola motif tenun dengan konsep barisan
    atau pola bilangan.
    """)

    with st.expander("👁️ Tampilkan Jawaban Essay 6"):
        st.markdown("""
        Pengulangan motif yang tersusun secara teratur dapat dimodelkan
        menggunakan pola bilangan atau barisan.
        """)
        st.latex(r"4,\ 8,\ 12,\ 16,\ldots")

    st.markdown("### Essay 7")
    st.markdown("""
    Sebuah kain memiliki biaya bahan Rp150.000 dan biaya tenaga kerja
    Rp100.000. Jika dijual Rp350.000, tentukan keuntungan per kain.
    """)

    with st.expander("👁️ Tampilkan Jawaban Essay 7"):
        st.latex(r"B=150000+100000=250000")
        st.latex(r"K=350000-250000=100000")
        st.markdown("Keuntungan per kain adalah **Rp100.000**.")

    st.markdown("### Essay 8")
    st.markdown("""
    Jelaskan minimal tiga konsep matematika yang dapat ditemukan pada
    motif dan proses pembuatan kain tenun.
    """)

    with st.expander("👁️ Tampilkan Jawaban Essay 8"):
        st.markdown("""
        Contohnya:

        1. Geometri → bentuk motif.
        2. Simetri → keteraturan motif.
        3. Transformasi → translasi, rotasi, dan refleksi.
        4. Perbandingan dan skala.
        5. Luas dan keliling.
        6. Barisan dan pola.
        7. Statistika.
        8. Aritmetika ekonomi.
        """)

    st.header("🌿 Refleksi")

    st.markdown("""
    1. Konsep matematika apa yang paling mudah ditemukan pada motif tenun?
    2. Bagaimana pola matematika membantu menghasilkan motif yang teratur?
    3. Bagaimana transformasi geometri dapat digunakan untuk membuat
       pengulangan motif?
    4. Bagaimana matematika dapat membantu pengrajin menghitung biaya
       produksi?
    5. Mengapa budaya lokal dapat digunakan sebagai konteks pembelajaran
       matematika?
    """)

    st.success("🎉 Materi Tenun dan Motif Tradisional selesai dipelajari.")





def tampilkan(materi):
    if materi == "Tenun dan Motif Tradisional":
        tenun_motif()

    elif materi == "Batik dan Pola Geometri":
        batik_geometri()

    elif materi == "Rumah Tradisional":
        rumah_tradisional()

    elif materi == "Arsitektur Kesultanan":
        arsitektur_kesultanan()

    elif materi == "Bubu dan Alat Tangkap Tradisional":
        bubu()

    elif materi == "Perahu Tradisional":
        perahu()

    elif materi == "Geometri dalam Budaya":
        geometri_budaya()

    elif materi == "Statistika dalam Kehidupan Masyarakat":
        statistika_masyarakat()

    elif materi == "Matematika Ekonomi dan Budaya":
        matematika_ekonomi()
