import streamlit as st
import pandas as pd
import numpy as np
import math

def tenun_motif():
    st.markdown(
        '<div class="content-title">🧵 Tenun dan Motif Tradisional</div>',
        unsafe_allow_html=True
    )

    st.header("🎯 Tujuan Pembelajaran")

    st.markdown("""
    Setelah mempelajari materi ini, peserta didik diharapkan mampu:

    - Mengidentifikasi konsep matematika pada pola motif tenun.
    - Menggunakan konsep bangun datar dalam konteks kain tenun.
    - Menghitung luas dan keliling pola.
    - Menggunakan konsep simetri dan transformasi geometri.
    - Menggunakan skala dan perbandingan.
    - Menganalisis pengulangan pola secara matematis.
    - Menggunakan matematika untuk menyelesaikan masalah kontekstual
      yang berkaitan dengan produksi kain tenun.
    """)

    st.header("🌿 Matematika dalam Tenun")

    st.markdown("""
    Kain tenun merupakan salah satu bentuk karya budaya yang memiliki
    berbagai pola dan susunan motif.

    Dalam pembelajaran matematika, pola pada kain dapat digunakan sebagai
    konteks untuk mempelajari berbagai konsep matematika, seperti:

    - titik dan garis,
    - bangun datar,
    - simetri,
    - translasi,
    - rotasi,
    - refleksi,
    - pola berulang,
    - perbandingan,
    - skala,
    - luas dan keliling,
    - serta statistika sederhana.

    Dengan demikian, budaya tidak hanya dipelajari sebagai objek budaya,
    tetapi juga dapat menjadi konteks untuk memahami konsep matematika.
    """)

    st.info("""
    💡 **Catatan**

    Ukuran pada contoh di bawah merupakan ukuran matematis yang
    disederhanakan untuk keperluan pembelajaran. Peserta didik dapat
    menggantinya dengan ukuran atau data dari objek tenun yang diamati
    secara langsung.
    """)

    st.header("1️⃣ Pola Berulang pada Motif")

    st.markdown("""
    Salah satu karakteristik penting dalam pola adalah **pengulangan**.

    Misalnya sebuah unit motif memiliki panjang 8 cm. Jika motif tersebut
    diulang sebanyak 12 kali, panjang bagian kain yang ditempati motif
    adalah:
    """)

    st.latex(r"L=n\times p")

    st.latex(r"L=12\times8=96\text{ cm}")

    st.success("Panjang pola yang terbentuk adalah 96 cm.")

    st.header("2️⃣ Eksplorasi Pengulangan Motif")

    panjang_motif = st.number_input(
        "Panjang satu unit motif (cm)",
        min_value=1.0,
        value=8.0,
        step=1.0,
        key="tenun_panjang_motif"
    )

    jumlah_motif = st.number_input(
        "Jumlah pengulangan motif",
        min_value=1,
        value=12,
        step=1,
        key="tenun_jumlah_motif"
    )

    total_panjang = panjang_motif * jumlah_motif

    st.latex(r"L=n\times p")

    st.success(
        f"Panjang total pola = {total_panjang:.2f} cm"
    )

    st.header("3️⃣ Bangun Datar pada Motif")

    st.markdown("""
    Motif kain dapat dimodelkan menggunakan berbagai bangun datar.

    Misalnya sebuah unit motif berbentuk persegi panjang dengan panjang
    8 cm dan lebar 5 cm.
    """)

    st.latex(r"L=p\times l")

    st.latex(r"L=8\times5=40\text{ cm}^2")

    st.latex(r"K=2(p+l)")

    st.latex(r"K=2(8+5)=26\text{ cm}")

    st.header("4️⃣ Eksplorasi Luas dan Keliling")

    panjang_unit = st.number_input(
        "Panjang unit motif (cm)",
        min_value=1.0,
        value=8.0,
        step=1.0,
        key="tenun_panjang_unit"
    )

    lebar_unit = st.number_input(
        "Lebar unit motif (cm)",
        min_value=1.0,
        value=5.0,
        step=1.0,
        key="tenun_lebar_unit"
    )

    luas_unit = panjang_unit * lebar_unit
    keliling_unit = 2 * (panjang_unit + lebar_unit)

    st.metric("Luas unit motif", f"{luas_unit:.2f} cm²")
    st.metric("Keliling unit motif", f"{keliling_unit:.2f} cm")

    st.header("5️⃣ Simetri pada Motif")

    st.markdown("""
    Motif dapat dianalisis berdasarkan sifat simetrinya.

    Beberapa jenis simetri yang dapat dipelajari:

    - **Simetri refleksi** → pola memiliki pencerminan.
    - **Simetri rotasi** → pola tetap memiliki bentuk yang sama setelah
      diputar dengan sudut tertentu.
    - **Simetri translasi** → pola berulang setelah digeser dengan jarak
      tertentu.
    """)

    st.markdown("""
    Misalnya satu unit motif memiliki panjang 10 cm dan diulang secara
    horizontal. Pergeseran setiap unit sebesar 10 cm merupakan contoh
    **translasi**.
    """)

    st.latex(r"T(x,y)=(x+a,y)")

    st.header("6️⃣ Translasi Motif")

    jarak_translasi = st.slider(
        "Jarak translasi horizontal (cm)",
        min_value=1,
        max_value=20,
        value=8,
        key="tenun_translasi"
    )

    st.latex(r"T(x,y)=(x+a,y)")

    st.success(
        f"Setiap unit motif dapat digeser sejauh {jarak_translasi} cm "
        "secara horizontal."
    )

    st.header("7️⃣ Rotasi Motif")

    st.markdown("""
    Motif tertentu dapat dianalisis menggunakan konsep rotasi.

    Beberapa sudut rotasi yang umum digunakan dalam geometri adalah:
    """)

    st.latex(r"90^\circ,\quad180^\circ,\quad270^\circ,\quad360^\circ")

    sudut_rotasi = st.selectbox(
        "Pilih sudut rotasi",
        [90, 180, 270, 360],
        key="tenun_rotasi"
    )

    st.success(
        f"Motif diputar sebesar {sudut_rotasi}°."
    )

    st.header("8️⃣ Skala Motif")

    st.markdown("""
    Dalam menggambar ulang motif, ukuran gambar dapat dibuat lebih kecil
    atau lebih besar menggunakan konsep skala.

    Misalnya panjang motif sebenarnya 40 cm dan gambar dibuat dengan
    skala 1 : 4.
    """)

    st.latex(r"\text{Panjang gambar}=\frac{\text{Panjang sebenarnya}}{\text{skala}}")

    st.latex(r"\text{Panjang gambar}=\frac{40}{4}=10\text{ cm}")

    st.header("9️⃣ Kalkulator Skala")

    ukuran_sebenarnya = st.number_input(
        "Ukuran sebenarnya (cm)",
        min_value=1.0,
        value=40.0,
        step=1.0,
        key="tenun_ukuran_sebenarnya"
    )

    skala = st.number_input(
        "Skala 1 : n",
        min_value=1.0,
        value=4.0,
        step=1.0,
        key="tenun_skala"
    )

    ukuran_gambar = ukuran_sebenarnya / skala

    st.success(
        f"Ukuran pada gambar = {ukuran_gambar:.2f} cm"
    )

    st.header("🔟 Perbandingan Panjang dan Lebar")

    st.markdown("""
    Perbandingan dapat digunakan untuk membandingkan ukuran dua bagian
    motif.
    """)

    st.latex(r"\text{Perbandingan}=p:l")

    st.markdown("""
    Misalnya panjang motif 12 cm dan lebarnya 8 cm.
    """)

    st.latex(r"12:8=3:2")

    st.success("Perbandingan panjang dan lebar adalah 3 : 2.")

    st.header("1️⃣1️⃣ Banyak Motif pada Kain")

    st.markdown("""
    Misalkan panjang kain 240 cm dan setiap unit motif membutuhkan ruang
    8 cm. Banyak unit motif yang dapat disusun adalah:
    """)

    st.latex(r"n=\frac{L}{p}")

    st.latex(r"n=\frac{240}{8}=30")

    st.success("Terdapat 30 unit motif.")

    st.header("1️⃣2️⃣ Persentase Bagian Bermotif")

    st.markdown("""
    Misalkan sebuah kain berukuran 200 cm × 80 cm.

    Jika 60% permukaannya merupakan area bermotif, maka:
    """)

    st.latex(r"A_{\text{kain}}=200\times80=16000\text{ cm}^2")

    st.latex(r"A_{\text{motif}}=60\%\times16000=9600\text{ cm}^2")

    st.success("Luas area bermotif adalah 9.600 cm².")

    st.header("1️⃣3️⃣ Eksplorasi Persentase Motif")

    panjang_kain = st.number_input(
        "Panjang kain (cm)",
        min_value=1.0,
        value=200.0,
        key="tenun_panjang_kain"
    )

    lebar_kain = st.number_input(
        "Lebar kain (cm)",
        min_value=1.0,
        value=80.0,
        key="tenun_lebar_kain"
    )

    persen_motif = st.slider(
        "Persentase area bermotif (%)",
        min_value=0,
        max_value=100,
        value=60,
        key="tenun_persen_motif"
    )

    luas_kain = panjang_kain * lebar_kain
    luas_motif = luas_kain * persen_motif / 100

    st.metric("Luas kain", f"{luas_kain:.2f} cm²")
    st.metric("Luas area bermotif", f"{luas_motif:.2f} cm²")

    st.header("1️⃣4️⃣ Pola Bilangan pada Pengulangan Motif")

    st.markdown("""
    Jumlah motif yang tersusun dalam beberapa baris dapat membentuk
    barisan bilangan.

    Misalnya:

    4, 8, 12, 16, ...

    merupakan barisan aritmetika dengan beda 4.
    """)

    st.latex(r"U_n=a+(n-1)b")

    st.markdown("""
    Jika $a=4$ dan $b=4$, maka suku ke-10:
    """)

    st.latex(r"U_{10}=4+(10-1)(4)=40")

    st.header("1️⃣5️⃣ Biaya Produksi Tenun")

    st.markdown("""
    Matematika juga dapat digunakan untuk menganalisis biaya produksi.

    Misalnya biaya bahan untuk satu kain adalah Rp150.000 dan biaya
    tenaga kerja Rp100.000.
    """)

    st.latex(r"B=150000+100000")

    st.latex(r"B=250000")

    st.markdown("""
    Jika kain dijual Rp350.000, keuntungan per kain adalah:
    """)

    st.latex(r"K=350000-250000")

    st.latex(r"K=100000")

    st.success("Keuntungan per kain adalah Rp100.000.")

    st.header("1️⃣6️⃣ Simulasi Produksi")

    harga_bahan = st.number_input(
        "Biaya bahan per kain (Rp)",
        min_value=0,
        value=150000,
        step=10000,
        key="tenun_bahan"
    )

    biaya_tenaga = st.number_input(
        "Biaya tenaga kerja per kain (Rp)",
        min_value=0,
        value=100000,
        step=10000,
        key="tenun_tenaga"
    )

    harga_jual = st.number_input(
        "Harga jual per kain (Rp)",
        min_value=0,
        value=350000,
        step=10000,
        key="tenun_jual"
    )

    jumlah_produksi = st.number_input(
        "Jumlah kain",
        min_value=1,
        value=10,
        step=1,
        key="tenun_produksi"
    )

    biaya_per_kain = harga_bahan + biaya_tenaga
    keuntungan_per_kain = harga_jual - biaya_per_kain
    total_keuntungan = keuntungan_per_kain * jumlah_produksi

    st.metric(
        "Biaya produksi per kain",
        f"Rp{biaya_per_kain:,.0f}"
    )

    st.metric(
        "Keuntungan per kain",
        f"Rp{keuntungan_per_kain:,.0f}"
    )

    st.metric(
        "Total keuntungan",
        f"Rp{total_keuntungan:,.0f}"
    )

    st.header("1️⃣7️⃣ Statistika Motif")

    st.markdown("""
    Data jumlah motif yang ditemukan pada beberapa sampel kain dapat
    dianalisis menggunakan statistika.

    Misalnya jumlah motif pada lima sampel kain adalah:
    """)

    data_motif = [12, 15, 10, 18, 15]

    st.dataframe(
        pd.DataFrame({
            "Sampel": [1, 2, 3, 4, 5],
            "Jumlah motif": data_motif
        }),
        use_container_width=True,
        hide_index=True
    )

    mean_motif = np.mean(data_motif)
    median_motif = np.median(data_motif)

    st.metric("Rata-rata", f"{mean_motif:.2f}")
    st.metric("Median", f"{median_motif:.2f}")

    st.header("1️⃣8️⃣ Visualisasi Data Motif")

    df_motif = pd.DataFrame({
        "Sampel": [1, 2, 3, 4, 5],
        "Jumlah motif": data_motif
    })

    st.bar_chart(
        df_motif.set_index("Sampel")
    )

    st.header("1️⃣9️⃣ Integrasi Matematika dan Budaya")

    st.markdown("""
    Dari objek tenun, kita dapat menemukan berbagai konsep matematika:

    | Unsur budaya | Konsep matematika |
    |---|---|
    | Pengulangan motif | Pola dan barisan |
    | Bentuk motif | Geometri |
    | Pencerminan motif | Refleksi |
    | Pemutaran motif | Rotasi |
    | Penggeseran motif | Translasi |
    | Ukuran kain | Luas dan keliling |
    | Perbandingan ukuran | Rasio dan skala |
    | Jumlah motif | Statistika |
    | Produksi kain | Aritmetika dan ekonomi |
    """)

    st.header("🌿 Kesimpulan Kontekstual")

    st.markdown("""
    Tenun dapat menjadi konteks pembelajaran matematika karena pola,
    ukuran, susunan, dan aktivitas produksinya dapat dimodelkan dengan
    konsep matematika.

    Pendekatan ini memungkinkan peserta didik melihat bahwa matematika
    tidak hanya terdapat dalam buku atau rumus, tetapi juga dapat
    ditemukan dalam aktivitas dan artefak budaya.
    """)

    st.divider()

    # =========================================================
    # 20 SOAL INTERAKTIF
    # =========================================================

    st.header("📝 20 Soal Interaktif")

    st.markdown("""
    Pilih satu jawaban untuk setiap soal. Setelah semua soal dijawab,
    tekan tombol **Periksa Semua Jawaban**.
    """)

    soal = [
        {
            "q": "1. Sebuah motif memiliki panjang 8 cm dan diulang 10 kali. Berapa panjang total pola?",
            "opsi": ["18 cm", "40 cm", "80 cm", "100 cm"],
            "jawaban": "80 cm",
            "pembahasan": "Panjang total = 10 × 8 = 80 cm."
        },
        {
            "q": "2. Sebuah motif berbentuk persegi dengan sisi 6 cm. Berapa luasnya?",
            "opsi": ["12 cm²", "24 cm²", "36 cm²", "48 cm²"],
            "jawaban": "36 cm²",
            "pembahasan": "Luas persegi = s² = 6² = 36 cm²."
        },
        {
            "q": "3. Persegi panjang memiliki panjang 10 cm dan lebar 4 cm. Kelilingnya adalah...",
            "opsi": ["14 cm", "20 cm", "28 cm", "40 cm"],
            "jawaban": "28 cm",
            "pembahasan": "K = 2(p + l) = 2(10 + 4) = 28 cm."
        },
        {
            "q": "4. Sebuah motif digeser 8 cm ke kanan. Transformasi tersebut disebut...",
            "opsi": ["Rotasi", "Refleksi", "Translasi", "Dilatasi"],
            "jawaban": "Translasi",
            "pembahasan": "Translasi adalah transformasi berupa pergeseran."
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
            "pembahasan": "Refleksi adalah pencerminan terhadap suatu garis."
        },
        {
            "q": "7. Panjang kain 240 cm. Jika satu motif membutuhkan 8 cm, berapa motif yang dapat disusun?",
            "opsi": ["20", "24", "30", "32"],
            "jawaban": "30",
            "pembahasan": "240 ÷ 8 = 30 motif."
        },
        {
            "q": "8. Ukuran sebenarnya suatu motif 40 cm. Jika dibuat dengan skala 1:4, ukurannya menjadi...",
            "opsi": ["5 cm", "10 cm", "20 cm", "160 cm"],
            "jawaban": "10 cm",
            "pembahasan": "40 ÷ 4 = 10 cm."
        },
        {
            "q": "9. Perbandingan panjang dan lebar motif adalah 12:8. Bentuk sederhananya adalah...",
            "opsi": ["2:1", "3:2", "4:3", "6:5"],
            "jawaban": "3:2",
            "pembahasan": "12:8 dibagi 4 menjadi 3:2."
        },
        {
            "q": "10. Kain berukuran 200 cm × 80 cm. Luas kain adalah...",
            "opsi": ["280 cm²", "2.800 cm²", "16.000 cm²", "28.000 cm²"],
            "jawaban": "16.000 cm²",
            "pembahasan": "Luas = 200 × 80 = 16.000 cm²."
        },
        {
            "q": "11. Jika 60% dari kain seluas 16.000 cm² merupakan area bermotif, luas area bermotif adalah...",
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
            "pembahasan": "U₁₀ = 4 + (10−1)4 = 40."
        },
        {
            "q": "14. Biaya bahan Rp150.000 dan tenaga kerja Rp100.000. Total biaya produksi adalah...",
            "opsi": ["Rp200.000", "Rp250.000", "Rp300.000", "Rp350.000"],
            "jawaban": "Rp250.000",
            "pembahasan": "150.000 + 100.000 = 250.000."
        },
        {
            "q": "15. Jika biaya produksi Rp250.000 dan harga jual Rp350.000, keuntungan per kain adalah...",
            "opsi": ["Rp50.000", "Rp75.000", "Rp100.000", "Rp150.000"],
            "jawaban": "Rp100.000",
            "pembahasan": "350.000 − 250.000 = 100.000."
        },
        {
            "q": "16. Jika keuntungan per kain Rp100.000 dan diproduksi 10 kain, total keuntungan adalah...",
            "opsi": ["Rp100.000", "Rp500.000", "Rp1.000.000", "Rp1.500.000"],
            "jawaban": "Rp1.000.000",
            "pembahasan": "10 × 100.000 = 1.000.000."
        },
        {
            "q": "17. Jumlah motif pada lima kain adalah 12, 15, 10, 18, dan 15. Rata-ratanya adalah...",
            "opsi": ["12", "13", "14", "15"],
            "jawaban": "14",
            "pembahasan": "(12 + 15 + 10 + 18 + 15) ÷ 5 = 14."
        },
        {
            "q": "18. Data jumlah motif 12, 15, 10, 18, 15 memiliki median...",
            "opsi": ["10", "12", "14", "15"],
            "jawaban": "15",
            "pembahasan": "Urutkan menjadi 10, 12, 15, 15, 18. Median = 15."
        },
        {
            "q": "19. Jika satu unit motif memiliki luas 40 cm² dan terdapat 20 unit motif, total luas seluruh unit adalah...",
            "opsi": ["400 cm²", "600 cm²", "800 cm²", "1.000 cm²"],
            "jawaban": "800 cm²",
            "pembahasan": "20 × 40 = 800 cm²."
        },
        {
            "q": "20. Konsep matematika yang paling tepat untuk pola motif yang berulang secara teratur adalah...",
            "opsi": ["Pola dan transformasi", "Logaritma saja", "Matriks saja", "Integral saja"],
            "jawaban": "Pola dan transformasi",
            "pembahasan": "Pengulangan motif dapat dianalisis menggunakan pola dan transformasi seperti translasi, rotasi, dan refleksi."
        }
    ]

    jawaban_pengguna = []

    with st.form("form_kuis_tenun"):

        for i, item in enumerate(soal):

            st.markdown(f"**{item['q']}**")

            jawaban = st.radio(
                "Pilih jawaban:",
                item["opsi"],
                key=f"tenun_soal_{i}",
                index=None
            )

            jawaban_pengguna.append(jawaban)

            if i < len(soal) - 1:
                st.divider()

        periksa = st.form_submit_button(
            "✅ Periksa Semua Jawaban",
            use_container_width=True
        )

    if periksa:

        skor = 0

        for i, item in enumerate(soal):

            if jawaban_pengguna[i] == item["jawaban"]:
                skor += 1

        nilai = skor / len(soal) * 100

        st.divider()

        st.header("📊 Hasil Kuis")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Jawaban Benar", f"{skor}/20")

        with col2:
            st.metric("Jawaban Salah", f"{20 - skor}")

        with col3:
            st.metric("Nilai", f"{nilai:.0f}")

        if nilai >= 85:
            st.success("🎉 Sangat baik! Pemahaman konsep matematika dalam konteks tenun sudah sangat baik.")
        elif nilai >= 70:
            st.info("👍 Baik. Beberapa konsep masih dapat diperdalam.")
        elif nilai >= 60:
            st.warning("📚 Cukup. Silakan pelajari kembali materi yang belum dikuasai.")
        else:
            st.error("💡 Perlu belajar kembali konsep-konsep dasar pada materi.")

        st.subheader("🔎 Pembahasan")

        for i, item in enumerate(soal):

            if jawaban_pengguna[i] == item["jawaban"]:

                st.success(
                    f"Soal {i + 1}: ✅ Benar — {item['pembahasan']}"
                )

            else:

                st.error(
                    f"Soal {i + 1}: ❌ "
                    f"Jawaban benar: **{item['jawaban']}**. "
                    f"{item['pembahasan']}"
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

        Maka:

        """)
        st.latex(r"L=25\times12=300\text{ cm}")

        st.markdown("""
        Jadi, panjang seluruh pola adalah **300 cm**.
        """)

    st.markdown("### Essay 2")
    st.markdown("""
    Sebuah unit motif berbentuk persegi panjang dengan panjang 15 cm
    dan lebar 8 cm. Tentukan luas dan keliling unit motif tersebut.
    """)

    with st.expander("👁️ Tampilkan Jawaban Essay 2"):
        st.latex(r"L=15\times8=120\text{ cm}^2")
        st.latex(r"K=2(15+8)=46\text{ cm}")

        st.markdown("""
        Jadi luas unit motif adalah **120 cm²** dan kelilingnya
        **46 cm**.
        """)

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
        tertentu secara berulang sehingga menghasilkan pola yang
        teratur.

        Misalnya setiap motif digeser 8 cm ke kanan. Secara matematis
        dapat ditulis:
        """)

        st.latex(r"T(x,y)=(x+8,y)")

        st.markdown("""
        Dengan demikian, pengulangan motif dapat dipahami sebagai
        penerapan translasi secara berulang.
        """)

    st.markdown("### Essay 4")
    st.markdown("""
    Sebuah kain berukuran 200 cm × 80 cm. Sebanyak 60% permukaannya
    merupakan area bermotif. Hitung luas area bermotif.
    """)

    with st.expander("👁️ Tampilkan Jawaban Essay 4"):
        st.latex(r"A=200\times80=16000\text{ cm}^2")
        st.latex(r"A_{\text{motif}}=0.60\times16000=9600\text{ cm}^2")

        st.markdown("""
        Jadi luas area bermotif adalah **9.600 cm²**.
        """)

    st.markdown("### Essay 5")
    st.markdown("""
    Jelaskan bagaimana matematika dapat digunakan untuk membantu
    pengrajin menentukan harga jual kain tenun.
    """)

    with st.expander("👁️ Tampilkan Jawaban Essay 5"):
        st.markdown("""
        Matematika dapat digunakan untuk menghitung biaya bahan, biaya
        tenaga kerja, biaya produksi, keuntungan, dan harga jual.

        Secara sederhana:

        """)
        st.latex(r"\text{Keuntungan}=\text{Harga Jual}-\text{Biaya Produksi}")

        st.markdown("""
        Dengan mengetahui biaya produksi dan keuntungan yang diinginkan,
        pengrajin dapat menentukan harga jual secara lebih terukur.
        """)

    st.markdown("### Essay 6")
    st.markdown("""
    Jelaskan hubungan antara pola motif tenun dengan konsep barisan
    atau pola bilangan.
    """)

    with st.expander("👁️ Tampilkan Jawaban Essay 6"):
        st.markdown("""
        Pengulangan motif dapat menghasilkan susunan yang teratur.
        Jika jumlah atau ukuran motif berubah secara teratur, susunan
        tersebut dapat dimodelkan menggunakan pola bilangan atau
        barisan.

        Misalnya jumlah motif bertambah 4 setiap baris:

        """)

        st.latex(r"4,\ 8,\ 12,\ 16,\ldots")

        st.markdown("""
        Pola tersebut merupakan barisan aritmetika dengan beda 4.
        """)

    st.markdown("### Essay 7")
    st.markdown("""
    Sebuah kain memiliki biaya bahan Rp150.000 dan biaya tenaga kerja
    Rp100.000. Jika dijual Rp350.000, tentukan keuntungan per kain dan
    jelaskan bagaimana matematika membantu dalam pengambilan keputusan
    ekonomi.
    """)

    with st.expander("👁️ Tampilkan Jawaban Essay 7"):
        st.latex(r"B=150000+100000=250000")

        st.latex(r"K=350000-250000=100000")

        st.markdown("""
        Keuntungan per kain adalah **Rp100.000**.

        Matematika membantu pengrajin menghitung biaya, keuntungan,
        menentukan harga jual, dan merencanakan jumlah produksi.
        """)

    st.markdown("### Essay 8")
    st.markdown("""
    Jelaskan minimal tiga konsep matematika yang dapat ditemukan pada
    motif dan proses pembuatan kain tenun.
    """)

    with st.expander("👁️ Tampilkan Jawaban Essay 8"):
        st.markdown("""
        Contoh konsep yang dapat digunakan:

        1. **Geometri** → bentuk bangun datar pada motif.
        2. **Simetri** → pencerminan atau keteraturan motif.
        3. **Transformasi** → translasi, rotasi, dan refleksi.
        4. **Perbandingan dan skala** → ukuran motif dan ukuran kain.
        5. **Luas dan keliling** → ukuran bagian kain.
        6. **Barisan** → pengulangan motif.
        7. **Statistika** → analisis jumlah atau variasi motif.
        8. **Aritmetika ekonomi** → biaya dan keuntungan produksi.
        """)

    st.header("🌿 Refleksi")

    st.markdown("""
    Setelah mempelajari Tenun dan Motif Tradisional, renungkan:

    1. Konsep matematika apa yang paling mudah ditemukan pada motif tenun?
    2. Bagaimana pola matematika membantu menghasilkan motif yang teratur?
    3. Bagaimana transformasi geometri dapat digunakan untuk membuat
       pengulangan motif?
    4. Bagaimana matematika dapat membantu pengrajin menghitung biaya
       produksi?
    5. Mengapa budaya lokal dapat digunakan sebagai konteks pembelajaran
       matematika?
    """)

    st.success(
        "🎉 Materi Tenun dan Motif Tradisional selesai dipelajari."
    )
    


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
