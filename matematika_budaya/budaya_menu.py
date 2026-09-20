import streamlit as st
import pandas as pd
import numpy as np
import math


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



    


def batik_geometri():
    st.header("🎨 Batik dan Pola Geometri")
    st.info("Materi akan dikembangkan.")


def rumah_tradisional():
    st.header("🏠 Rumah Tradisional")
    st.info("Materi akan dikembangkan.")


def arsitektur_kesultanan():
    st.header("🕌 Arsitektur Kesultanan")
    st.info("Materi akan dikembangkan.")


def bubu():
    st.header("🐟 Bubu dan Alat Tangkap Tradisional")
    st.info("Materi akan dikembangkan.")


def perahu():
    st.header("🛶 Perahu Tradisional")
    st.info("Materi akan dikembangkan.")


def geometri_budaya():
    st.header("📐 Geometri dalam Budaya")
    st.info("Materi akan dikembangkan.")


def statistika_masyarakat():
    st.header("📊 Statistika dalam Kehidupan Masyarakat")
    st.info("Materi akan dikembangkan.")


def matematika_ekonomi():
    st.header("💰 Matematika Ekonomi dan Budaya")
    st.info("Materi akan dikembangkan.")


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
