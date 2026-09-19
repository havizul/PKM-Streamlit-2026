import streamlit as st
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

from textwrap import dedent


def irisan_kerucut():
    st.markdown(
        '<div class="content-title">📕 Irisan Kerucut: Lingkaran dan Elips</div>',
        unsafe_allow_html=True
    )

    # =========================================================
    # TUJUAN PEMBELAJARAN
    # =========================================================

    st.header("🎯 Tujuan Pembelajaran")

    st.markdown(r"""
    Setelah mempelajari materi ini, siswa diharapkan mampu:

    - Menjelaskan konsep dasar irisan kerucut.
    - Menjelaskan pengertian lingkaran dan elips sebagai irisan kerucut.
    - Menentukan pusat dan jari-jari lingkaran.
    - Menentukan bentuk persamaan lingkaran.
    - Menentukan pusat, puncak, dan fokus elips.
    - Menentukan sumbu mayor dan sumbu minor elips.
    - Menentukan eksentrisitas elips.
    - Mengubah persamaan kuadrat ke bentuk standar.
    - Membuat dan membaca grafik lingkaran dan elips.
    - Menerapkan konsep irisan kerucut dalam permasalahan kontekstual.
    """)

    # =========================================================
    # APERSEPSI
    # =========================================================

    st.header("💡 Apersepsi")

    st.markdown(r"""
    Pernahkah kamu melihat bentuk lingkaran pada roda, jam, atau piring?

    Bagaimana dengan bentuk elips pada lintasan orbit planet atau desain
    sebuah stadion?

    Bentuk-bentuk tersebut dapat dipelajari menggunakan konsep **irisan
    kerucut**.
    """)

    # =========================================================
    # 1. KONSEP IRISAN KERUCUT
    # =========================================================

    st.header("1. Konsep Irisan Kerucut")

    st.markdown(r"""
    Irisan kerucut adalah kurva yang diperoleh dari perpotongan sebuah
    bidang dengan permukaan kerucut.

    Beberapa bentuk irisan kerucut adalah:

    - Lingkaran.
    - Elips.
    - Parabola.
    - Hiperbola.

    Pada materi ini kita fokus pada **lingkaran dan elips**.
    """)

    # =========================================================
    # 2. LINGKARAN
    # =========================================================

    st.header("2. Lingkaran")

    st.markdown(r"""
    Lingkaran adalah himpunan semua titik pada bidang yang mempunyai jarak
    sama terhadap suatu titik tetap yang disebut pusat.
    """)

    st.latex(r"(x-h)^2+(y-k)^2=r^2")

    st.markdown(r"""
    dengan:

    - $(h,k)$ = pusat lingkaran.
    - $r$ = jari-jari.
    """)

    st.markdown(r"Jika pusat berada di titik asal $O(0,0)$:")

    st.latex(r"x^2+y^2=r^2")

    # =========================================================
    # 3. CONTOH LINGKARAN
    # =========================================================

    st.header("3. Contoh Persamaan Lingkaran")

    st.markdown("Diberikan:")

    st.latex(r"(x-2)^2+(y+3)^2=25")

    st.markdown(r"""
    Maka:

    - Pusat = $(2,-3)$
    - Jari-jari = $5$
    """)

    # =========================================================
    # 4. BENTUK UMUM LINGKARAN
    # =========================================================

    st.header("4. Bentuk Umum Persamaan Lingkaran")

    st.latex(r"x^2+y^2+Dx+Ey+F=0")

    st.markdown(r"""
    Untuk menentukan pusat dan jari-jari, persamaan dapat diubah ke bentuk
    standar menggunakan **melengkapkan kuadrat**.
    """)

    st.markdown("Contoh:")

    st.latex(r"x^2+y^2-4x+6y-12=0")

    st.markdown(r"Kelompokkan suku $x$ dan $y$:")

    st.latex(r"(x^2-4x)+(y^2+6y)=12")

    st.markdown("Lengkapi kuadrat:")

    st.latex(r"(x-2)^2+(y+3)^2=25")

    st.markdown(r"""
    Jadi pusatnya adalah $(2,-3)$ dan jari-jarinya $5$.
    """)

    # =========================================================
    # 5. KALKULATOR LINGKARAN
    # =========================================================

    st.header("5. Kalkulator Lingkaran")

    col1, col2 = st.columns(2)

    with col1:
        pusat_x = st.number_input(
            "Koordinat pusat h",
            value=2.0,
            key="kerucut_pusat_x"
        )

        pusat_y = st.number_input(
            "Koordinat pusat k",
            value=-3.0,
            key="kerucut_pusat_y"
        )

    with col2:
        radius = st.number_input(
            "Jari-jari r",
            min_value=0.01,
            value=5.0,
            key="kerucut_radius"
        )

    luas_lingkaran = math.pi * radius**2
    keliling_lingkaran = 2 * math.pi * radius

    st.latex(
        rf"(x-({pusat_x:g}))^2+(y-({pusat_y:g}))^2=({radius:g})^2"
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Luas", f"{luas_lingkaran:.4f}")

    with col2:
        st.metric("Keliling", f"{keliling_lingkaran:.4f}")

    # =========================================================
    # 6. VISUALISASI LINGKARAN
    # =========================================================

    st.header("6. Visualisasi Lingkaran")

    theta = np.linspace(0, 2 * math.pi, 400)
    x_circle = pusat_x + radius * np.cos(theta)
    y_circle = pusat_y + radius * np.sin(theta)

    fig, ax = plt.subplots(figsize=(5, 5))
    ax.plot(x_circle, y_circle, "b-")
    ax.plot(pusat_x, pusat_y, "ro", label=f"Pusat ({pusat_x:g}, {pusat_y:g})")
    ax.axhline(0, color="gray", linewidth=0.6)
    ax.axvline(0, color="gray", linewidth=0.6)
    ax.grid(True, linestyle=":", alpha=0.6)
    ax.set_aspect("equal", adjustable="box")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title(
        rf"$(x-{pusat_x:g})^2+(y-{pusat_y:g})^2={radius:g}^2$"
    )
    ax.legend(loc="upper right")
    fig.tight_layout()
    st.pyplot(fig, use_container_width=True)

    # =========================================================
    # 7. ELIPS
    # =========================================================

    st.header("7. Elips")

    st.markdown(r"""
    Elips adalah himpunan titik pada bidang yang jumlah jaraknya terhadap
    dua titik tetap bernilai konstan.

    Dua titik tetap tersebut disebut **fokus**.
    """)

    st.latex(r"PF_1+PF_2=2a")

    # =========================================================
    # 8. PERSAMAAN STANDAR ELIPS
    # =========================================================

    st.header("8. Persamaan Standar Elips")

    st.markdown(r"Jika pusat elips berada di $(h,k)$ dan sumbu mayor horizontal:")

    st.latex(r"\frac{(x-h)^2}{a^2}+\frac{(y-k)^2}{b^2}=1")

    st.markdown(r"""
    dengan $a>b>0$.

    Jika sumbu mayor vertikal:
    """)

    st.latex(r"\frac{(x-h)^2}{b^2}+\frac{(y-k)^2}{a^2}=1")

    # =========================================================
    # 9. UNSUR ELIPS
    # =========================================================

    st.header("9. Unsur-Unsur Elips")

    st.markdown(r"""
    Untuk elips dengan:

    - $a$ = semi-sumbu mayor.
    - $b$ = semi-sumbu minor.
    - $c$ = jarak pusat ke fokus.

    berlaku:
    """)

    st.latex(r"c^2=a^2-b^2")

    st.markdown(r"""
    Unsur penting elips:

    - Pusat = $(h,k)$.
    - Panjang sumbu mayor = $2a$.
    - Panjang sumbu minor = $2b$.
    - Jarak antarfokus = $2c$.
    """)

    # =========================================================
    # 10. FOKUS ELIPS
    # =========================================================

    st.header("10. Fokus Elips")

    st.markdown(r"""
    Untuk elips dengan sumbu mayor horizontal, fokus berada pada:
    """)

    st.latex(r"(h-c,k)\text{ dan }(h+c,k)")

    st.markdown(r"""
    Untuk elips dengan sumbu mayor vertikal:
    """)

    st.latex(r"(h,k-c)\text{ dan }(h,k+c)")

    # =========================================================
    # 11. EKSENTRISITAS
    # =========================================================

    st.header("11. Eksentrisitas Elips")

    st.markdown(r"""
    Eksentrisitas menunjukkan tingkat ke-elips-an suatu elips.
    """)

    st.latex(r"e=\frac{c}{a}")

    st.markdown(r"""
    Untuk elips berlaku:

    $0<e<1$

    Semakin dekat $e$ dengan 0, bentuk elips semakin mendekati lingkaran.
    """)

    # =========================================================
    # 12. CONTOH ELIPS
    # =========================================================

    st.header("12. Contoh Menentukan Unsur Elips")

    st.markdown("Diberikan:")

    st.latex(r"\frac{x^2}{25}+\frac{y^2}{9}=1")

    st.markdown(r"""
    Dari persamaan tersebut:

    - $a^2=25$, sehingga $a=5$.
    - $b^2=9$, sehingga $b=3$.
    """)

    st.latex(r"c^2=25-9=16")
    st.latex(r"c=4")

    st.markdown(r"""
    Jadi:

    - Pusat = $(0,0)$.
    - Fokus = $(-4,0)$ dan $(4,0)$.
    - Panjang sumbu mayor = $10$.
    - Panjang sumbu minor = $6$.
    """)

    st.latex(r"e=\frac{4}{5}")

    # =========================================================
    # 13. EKSPLORASI ELIPS
    # =========================================================

    st.header("13. Eksplorasi Elips")

    col1, col2 = st.columns(2)

    with col1:
        elips_a = st.number_input(
            "Semi-sumbu mayor a",
            min_value=0.1,
            value=5.0,
            key="elips_a"
        )

    with col2:
        elips_b = st.number_input(
            "Semi-sumbu minor b",
            min_value=0.1,
            value=3.0,
            key="elips_b"
        )

    if elips_b > elips_a:
        st.warning(
            "Untuk eksplorasi ini, nilai b sebaiknya tidak lebih besar dari a."
        )
    else:
        elips_c = math.sqrt(max(elips_a**2 - elips_b**2, 0))
        elips_e = elips_c / elips_a if elips_a != 0 else 0

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("c", f"{elips_c:.4f}")

        with col2:
            st.metric("Eksentrisitas", f"{elips_e:.4f}")

        with col3:
            st.metric(
                "Luas Elips",
                f"{math.pi * elips_a * elips_b:.4f}"
            )

        theta_elips = np.linspace(0, 2 * math.pi, 400)
        x_elips = elips_a * np.cos(theta_elips)
        y_elips = elips_b * np.sin(theta_elips)

        fig, ax = plt.subplots(figsize=(5, 5))
        ax.plot(x_elips, y_elips, "g-", label="Elips")
        
        # Tandai fokus (hanya kalau c > 0)
        if elips_c > 1e-9:
            ax.plot(-elips_c, 0, "r*", markersize=12,
                    label=rf"Fokus $(-{elips_c:.2f},\ 0)$")
            ax.plot(elips_c, 0, "r*", markersize=12,
                    label=rf"Fokus $({elips_c:.2f},\ 0)$")
        else:
            st.caption("Karena a = b, elips berbentuk lingkaran (kedua fokus berimpit di pusat).")
        
        ax.plot(0, 0, "ko", markersize=5, label="Pusat")
        
        ax.axhline(0, color="gray", linewidth=0.6)
        ax.axvline(0, color="gray", linewidth=0.6)
        ax.grid(True, linestyle=":", alpha=0.6)
        ax.set_aspect("equal", adjustable="box")
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_title(
            rf"$\dfrac{{x^2}}{{{elips_a:.2f}^2}}+\dfrac{{y^2}}{{{elips_b:.2f}^2}}=1$"
        )
        ax.legend(loc="upper right", fontsize=8, framealpha=0.9)
        
        fig.tight_layout()
        st.pyplot(fig, use_container_width=True)

    # =========================================================
    # 14. LUAS ELIPS
    # =========================================================

    st.header("14. Luas Elips")

    st.markdown(r"""
    Luas elips dengan semi-sumbu mayor $a$ dan semi-sumbu minor $b$ adalah:
    """)

    st.latex(r"L=\pi ab")

    st.markdown("Contoh:")

    st.latex(r"a=5,\quad b=3")
    st.latex(r"L=15\pi")

    # =========================================================
    # 15. PERSAMAAN ELIPS DENGAN PUSAT BERGESER
    # =========================================================

    st.header("15. Elips dengan Pusat (h, k)")

    st.markdown("Misalnya:")

    st.latex(r"\frac{(x-2)^2}{25}+\frac{(y+1)^2}{9}=1")

    st.markdown(r"""
    Maka:

    - Pusat = $(2,-1)$.
    - $a=5$.
    - $b=3$.
    """)

    st.latex(r"c=\sqrt{25-9}=4")

    st.markdown(r"""
    Karena penyebut terbesar berada pada suku $x$, sumbu mayor
    berorientasi horizontal.
    """)

    # =========================================================
    # 16. PERBANDINGAN LINGKARAN DAN ELIPS
    # =========================================================

    st.header("16. Lingkaran vs Elips")

    perbandingan = pd.DataFrame({
        "Aspek": [
            "Bentuk",
            "Parameter utama",
            "Fokus",
            "Eksentrisitas",
            "Persamaan standar"
        ],
        "Lingkaran": [
            "Semua arah simetris",
            "Jari-jari r",
            "Satu pusat",
            "0",
            "(x-h)²+(y-k)²=r²"
        ],
        "Elips": [
            "Memanjang pada satu arah",
            "a dan b",
            "Dua fokus",
            "0 < e < 1",
            "(x-h)²/a²+(y-k)²/b²=1"
        ]
    })

    st.dataframe(
        perbandingan,
        use_container_width=True,
        hide_index=True
    )

    # =========================================================
    # 17. IRISAN KERUCUT DAN GEOMETRI ANALITIK
    # =========================================================

    st.header("17. Hubungan dengan Geometri Analitik")

    st.markdown(r"""
    Persamaan lingkaran dan elips merupakan contoh bagaimana objek
    geometris dapat direpresentasikan menggunakan persamaan aljabar.

    Dengan demikian, geometri dan aljabar dapat digunakan secara bersamaan
    untuk menganalisis suatu objek.
    """)

    # =========================================================
    # 18. APLIKASI
    # =========================================================

    st.header("🌍 Penerapan Irisan Kerucut")

    st.markdown(r"""
    Konsep lingkaran dan elips digunakan dalam:

    - Arsitektur.
    - Desain.
    - Astronomi.
    - Optik.
    - Teknik.
    - Robotika.
    - Pemodelan CAD.
    - Grafika komputer.
    - Sistem navigasi.
    """)

    # =========================================================
    # 19. STUDI KASUS ORBIT
    # =========================================================

    st.header("🪐 Studi Kasus: Orbit Planet")

    st.markdown(r"""
    Dalam model sederhana, lintasan suatu objek langit dapat didekati
    menggunakan bentuk elips.

    Misalnya lintasan dimodelkan:
    """)

    st.latex(r"\frac{x^2}{100}+\frac{y^2}{64}=1")

    st.markdown(r"""
    Maka:

    - $a=10$
    - $b=8$
    """)

    st.latex(r"c=\sqrt{100-64}=6")
    st.latex(r"e=\frac{6}{10}=0.6")

    st.markdown(r"""
    Fokus berada pada $(-6,0)$ dan $(6,0)$.
    """)

    # =========================================================
    # 20. STUDI KASUS ARSITEKTUR
    # =========================================================

    st.header("🏛️ Studi Kasus: Bentuk Elips")

    st.markdown(r"""
    Sebuah desain lengkungan bangunan dimodelkan menggunakan bagian dari
    elips:
    """)

    st.latex(r"\frac{x^2}{16}+\frac{y^2}{9}=1")

    st.markdown(r"""
    Dengan model tersebut, posisi lengkungan dapat dianalisis secara
    matematis sehingga ukuran desain dapat disesuaikan.
    """)

    # =========================================================
    # 21. LATIHAN
    # =========================================================

    st.header("📝 Latihan")

    st.markdown(r"""
    **Soal 1**

    Tentukan pusat dan jari-jari lingkaran:

    $$ (x-3)^2+(y+2)^2=16 $$
    """)

    st.markdown(r"""
    **Soal 2**

    Tentukan bentuk standar dari:

    $$x^2+y^2-6x+4y-12=0$$
    """)

    st.markdown(r"""
    **Soal 3**

    Tentukan pusat, $a$, dan $b$ dari:

    $$\frac{(x-2)^2}{25}+\frac{(y+1)^2}{9}=1$$
    """)

    st.markdown(r"""
    **Soal 4**

    Tentukan fokus elips:

    $$\frac{x^2}{25}+\frac{y^2}{9}=1$$
    """)

    st.markdown(r"""
    **Soal 5**

    Tentukan eksentrisitas elips:

    $$\frac{x^2}{100}+\frac{y^2}{64}=1$$
    """)

    # =========================================================
    # 22. KUIS
    # =========================================================

    st.header("🎯 Kuis")

    jawaban_kerucut = st.radio(
        "Persamaan (x−2)² + (y+3)² = 25 mempunyai pusat:",
        [
            "(2, 3)",
            "(−2, −3)",
            "(2, −3)",
            "(−2, 3)"
        ],
        key="quiz_irisan_kerucut"
    )

    if st.button("Periksa Jawaban", key="cek_quiz_irisan_kerucut"):
        if jawaban_kerucut == "(2, −3)":
            st.success(
                "✅ Benar. Bentuk standar lingkaran adalah "
                "(x−h)²+(y−k)²=r²."
            )
        else:
            st.error(
                "❌ Belum tepat. Perhatikan tanda pada bentuk "
                "(x−h)²+(y−k)²=r²."
            )

    # =========================================================
    # 23. REFLEKSI
    # =========================================================

    st.header("💭 Refleksi")

    st.markdown(r"""
    Setelah mempelajari irisan kerucut, coba jelaskan:

    1. Apa yang dimaksud dengan irisan kerucut?
    2. Bagaimana menentukan pusat dan jari-jari lingkaran?
    3. Apa perbedaan lingkaran dan elips?
    4. Apa hubungan $a$, $b$, dan $c$ pada elips?
    5. Apa yang dimaksud dengan eksentrisitas?
    6. Bagaimana persamaan aljabar dapat merepresentasikan bentuk geometris?
    7. Di mana konsep elips digunakan dalam kehidupan nyata?
    """)

    # =========================================================
    # 24. RANGKUMAN
    # =========================================================

    st.header("📌 Rangkuman")

    st.markdown(r"""
    **Irisan kerucut** merupakan kurva yang diperoleh dari perpotongan
    bidang dengan permukaan kerucut.

    Konsep penting:

    - Lingkaran mempunyai pusat dan jari-jari.
    - Persamaan lingkaran berbentuk $(x-h)^2+(y-k)^2=r^2$.
    - Elips mempunyai dua fokus.
    - Persamaan elips menggunakan parameter $a$ dan $b$.
    - Hubungan antara $a$, $b$, dan $c$ adalah $c^2=a^2-b^2$.
    - Eksentrisitas elips adalah $e=c/a$.
    - Lingkaran dapat dipandang sebagai kasus khusus elips ketika $a=b$.
    - Lingkaran dan elips dapat divisualisasikan serta dianalisis melalui
      koordinat dan persamaan aljabar.
    - Konsep irisan kerucut digunakan dalam astronomi, arsitektur, teknik,
      desain, robotika, dan grafika komputer.
    """)

    st.success("🎉 Materi Irisan Kerucut selesai dipelajari.")


def pemodelan_fungsi():

    st.markdown(
        '<div class="content-title">📕 Pemodelan Fungsi</div>',
        unsafe_allow_html=True
    )

    # =========================================================
    # TUJUAN PEMBELAJARAN
    # =========================================================

    st.header("🎯 Tujuan Pembelajaran")

    st.markdown(r"""
    Setelah mempelajari materi ini, siswa diharapkan mampu:

    - Menjelaskan konsep pemodelan matematika menggunakan fungsi.
    - Mengidentifikasi variabel dalam suatu permasalahan.
    - Menentukan hubungan antara variabel bebas dan variabel terikat.
    - Membentuk fungsi dari permasalahan kontekstual.
    - Menentukan domain dan range model.
    - Menginterpretasikan parameter dalam suatu model fungsi.
    - Membuat dan membaca grafik model fungsi.
    - Menggunakan model fungsi untuk melakukan prediksi.
    - Mengevaluasi keterbatasan suatu model matematika.
    """)

    # =========================================================
    # APERSEPSI
    # =========================================================

    st.header("💡 Apersepsi")

    st.markdown(r"""
    Dalam kehidupan sehari-hari, banyak besaran yang saling berhubungan.

    Misalnya:

    - biaya bergantung pada jumlah barang,
    - jarak bergantung pada waktu,
    - pendapatan bergantung pada jumlah penjualan,
    - tinggi benda bergantung pada waktu,
    - luas bergantung pada ukuran suatu objek.

    Hubungan tersebut dapat dinyatakan menggunakan **fungsi**.
    """)

    st.latex(r"y=f(x)")

    # =========================================================
    # 1. KONSEP PEMODELAN
    # =========================================================

    st.header("1. Konsep Pemodelan Matematika")

    st.markdown(r"""
    **Pemodelan matematika** adalah proses menerjemahkan suatu masalah
    nyata ke dalam bentuk matematika sehingga dapat dianalisis.

    Secara sederhana, prosesnya dapat digambarkan sebagai:

    **Masalah nyata → Identifikasi variabel → Model matematika →
    Analisis → Interpretasi**
    """)

    st.info(r"""
    Model matematika bukanlah kenyataan itu sendiri. Model merupakan
    penyederhanaan dari suatu situasi nyata.
    """)

    # =========================================================
    # 2. VARIABEL
    # =========================================================

    st.header("2. Variabel dalam Model")

    st.markdown(r"""
    Dalam pemodelan fungsi biasanya terdapat:

    - **Variabel bebas ($x$)** → nilai yang dapat dipilih atau menjadi input.
    - **Variabel terikat ($y$)** → nilai yang bergantung pada variabel bebas.
    """)

    st.latex(r"y=f(x)")

    st.markdown(r"""
    Contoh:

    Jika biaya pembelian bergantung pada jumlah barang, maka:

    - $x$ = jumlah barang
    - $y$ = total biaya
    """)

    # =========================================================
    # 3. CONTOH MODEL LINEAR
    # =========================================================

    st.header("3. Model Fungsi Linear")

    st.markdown(r"""
    Sebuah toko menjual produk dengan harga Rp15.000 per unit dan biaya
    tetap Rp50.000.

    Jika $x$ adalah jumlah produk, maka total biaya dapat dimodelkan:
    """)

    st.latex(r"C(x)=15000x+50000")

    st.markdown(r"""
    Dalam model tersebut:

    - $15.000$ adalah biaya per unit.
    - $50.000$ adalah biaya tetap.
    - $x$ adalah jumlah unit.
    - $C(x)$ adalah total biaya.
    """)

    # =========================================================
    # 4. EKSPLORASI MODEL LINEAR
    # =========================================================

    st.header("4. Eksplorasi Model Biaya")

    harga_unit = st.number_input(
        "Harga per unit (Rp)",
        min_value=0.0,
        value=15000.0,
        step=1000.0,
        key="model_harga_unit"
    )

    biaya_tetap = st.number_input(
        "Biaya tetap (Rp)",
        min_value=0.0,
        value=50000.0,
        step=5000.0,
        key="model_biaya_tetap"
    )

    jumlah_unit = st.number_input(
        "Jumlah unit",
        min_value=0,
        value=10,
        step=1,
        key="model_jumlah_unit"
    )

    total_biaya = harga_unit * jumlah_unit + biaya_tetap

    st.info(f"Total biaya = Rp{total_biaya:,.0f}")

    # =========================================================
    # 5. GRAFIK MODEL LINEAR
    # =========================================================

    st.header("5. Grafik Model Linear")

    x_linear = np.arange(0, 101)
    y_linear = harga_unit * x_linear + biaya_tetap

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(x_linear, y_linear, "b-")
    ax.axhline(0, color="gray", linewidth=0.6)
    ax.axvline(0, color="gray", linewidth=0.6)
    ax.grid(True, linestyle=":", alpha=0.6)
    ax.set_xlabel("Jumlah unit (x)")
    ax.set_ylabel("Total biaya C(x)")
    ax.set_title(rf"$C(x) = {harga_unit:.0f}x + {biaya_tetap:.0f}$")

    fig.tight_layout()
    st.pyplot(fig)

    # =========================================================
    # 6. DOMAIN DAN RANGE
    # =========================================================

    st.header("6. Domain dan Range Model")

    st.markdown(r"""
    Dalam pemodelan nyata, domain tidak selalu berupa semua bilangan real.

    Misalnya jumlah barang tidak mungkin bernilai negatif atau pecahan.
    """)

    st.latex(r"x\in\{0,1,2,3,\ldots\}")

    st.markdown(r"""
    Oleh karena itu, domain harus disesuaikan dengan konteks permasalahan.
    """)

    # =========================================================
    # 7. MODEL KUADRAT
    # =========================================================

    st.header("7. Model Fungsi Kuadrat")

    st.markdown(r"""
    Fungsi kuadrat dapat digunakan untuk memodelkan berbagai fenomena,
    misalnya lintasan benda atau hubungan luas dengan ukuran tertentu.
    """)

    st.latex(r"f(x)=ax^2+bx+c")

    st.markdown("Contoh model tinggi benda:")

    st.latex(r"h(t)=-5t^2+20t+2")

    st.markdown(r"""
    Karena koefisien $t^2$ bernilai negatif, grafik membuka ke bawah.
    """)

    # =========================================================
    # 8. EKSPLORASI MODEL KUADRAT
    # =========================================================

    st.header("8. Eksplorasi Model Kuadrat")

    qa = st.number_input("Koefisien a", value=-5.0, key="model_qa")
    qb = st.number_input("Koefisien b", value=20.0, key="model_qb")
    qc = st.number_input("Konstanta c", value=2.0, key="model_qc")

    x_quad = np.linspace(-5, 10, 400)
    y_quad = qa * x_quad**2 + qb * x_quad + qc

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(x_quad, y_quad, "g-")
    ax.axhline(0, color="gray", linewidth=0.6)
    ax.axvline(0, color="gray", linewidth=0.6)
    ax.grid(True, linestyle=":", alpha=0.6)
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.set_title(rf"$f(x) = {qa:.2f}x^2 + {qb:.2f}x + {qc:.2f}$")

    fig.tight_layout()
    st.pyplot(fig)

    if qa != 0:
        x_vertex = -qb / (2 * qa)
        y_vertex = qa * x_vertex**2 + qb * x_vertex + qc
        st.info(f"Titik puncak: ({x_vertex:.4f}, {y_vertex:.4f})")

    # =========================================================
    # 9. MODEL EKSPONENSIAL
    # =========================================================

    st.header("9. Model Fungsi Eksponensial")

    st.markdown(r"""
    Fungsi eksponensial dapat digunakan untuk memodelkan pertumbuhan
    atau peluruhan.
    """)

    st.latex(r"f(x)=ab^x")

    st.markdown(r"""
    Jika $b>1$, model menunjukkan pertumbuhan.

    Jika $0<b<1$, model menunjukkan peluruhan.
    """)

    # =========================================================
    # 10. EKSPLORASI EKSPONENSIAL
    # =========================================================

    st.header("10. Eksplorasi Pertumbuhan Eksponensial")

    nilai_awal = st.number_input(
        "Nilai awal a",
        min_value=0.01,
        value=100.0,
        key="model_exp_a"
    )

    faktor = st.number_input(
        "Faktor pertumbuhan b",
        min_value=0.01,
        value=1.10,
        step=0.01,
        key="model_exp_b"
    )

    x_exp = np.arange(0, 21)
    y_exp = nilai_awal * faktor**x_exp

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(x_exp, y_exp, "r-o")
    ax.grid(True, linestyle=":", alpha=0.6)
    ax.set_xlabel("Periode (x)")
    ax.set_ylabel("Nilai f(x)")
    ax.set_title(rf"$f(x) = {nilai_awal:.2f} \cdot {faktor:.2f}^x$")
    st.pyplot(fig)

    st.info(f"Nilai pada periode ke-20 = {y_exp[-1]:.2f}")

    # =========================================================
    # 11. MODEL LOGARITMA
    # =========================================================

    st.header("11. Model Fungsi Logaritma")

    st.markdown(r"""
    Fungsi logaritma merupakan kebalikan dari fungsi eksponensial.
    """)

    st.latex(r"y=\log_b x")

    st.markdown(r"""
    Model logaritma dapat digunakan ketika perubahan suatu variabel
    berlangsung cepat pada awalnya kemudian semakin melambat.
    """)

    # =========================================================
    # 12. MODEL PERIODIK
    # =========================================================

    st.header("12. Model Periodik")

    st.markdown(r"""
    Fenomena yang berulang secara periodik dapat dimodelkan menggunakan
    fungsi sinus atau cosinus.
    """)

    st.latex(r"y=A\sin(Bx+C)+D")

    st.markdown(r"""
    Contoh fenomena periodik:

    - gelombang,
    - pasang surut,
    - getaran,
    - perubahan suhu,
    - gerak periodik.
    """)

    # =========================================================
    # 13. EKSPLORASI MODEL PERIODIK
    # =========================================================

    st.header("13. Eksplorasi Model Periodik")

    amp_model = st.slider(
        "Amplitudo A", 0.1, 10.0, 2.0, step=0.1, key="model_periodik_amp"
    )

    freq_model = st.slider(
        "Frekuensi B", 0.1, 5.0, 1.0, step=0.1, key="model_periodik_freq"
    )

    offset_model = st.slider(
        "Pergeseran vertikal D", -5.0, 5.0, 0.0,
        step=0.5, key="model_periodik_offset"
    )

    x_periodik = np.linspace(0, 2 * np.pi, 400)
    y_periodik = amp_model * np.sin(freq_model * x_periodik) + offset_model

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(x_periodik, y_periodik, "m-")
    ax.axhline(0, color="gray", linewidth=0.6)
    ax.axvline(0, color="gray", linewidth=0.6)
    ax.grid(True, linestyle=":", alpha=0.6)
    ax.set_xlabel("x (radian)")
    ax.set_ylabel("f(x)")
    ax.set_title(
        rf"$f(x) = {amp_model:.1f}\sin({freq_model:.1f}x) + {offset_model:.1f}$"
    )
    st.pyplot(fig)

    # =========================================================
    # 14. PEMODELAN DARI DATA
    # =========================================================

    st.header("14. Pemodelan Berdasarkan Data")

    st.markdown(r"""
    Model fungsi juga dapat dibangun berdasarkan data hasil pengamatan.

    Langkah sederhana:

    1. Mengumpulkan data.
    2. Menentukan variabel.
    3. Membuat grafik data.
    4. Mengidentifikasi pola.
    5. Memilih bentuk fungsi.
    6. Menentukan parameter model.
    7. Mengevaluasi kesesuaian model.
    """)

    # =========================================================
    # 15. DATA INTERAKTIF
    # =========================================================

    st.header("15. Eksplorasi Data")

    data_model = pd.DataFrame({
        "x": [1, 2, 3, 4, 5],
        "y": [3, 5, 7, 9, 11]
    })

    data_edit = st.data_editor(
        data_model,
        num_rows="dynamic",
        use_container_width=True,
        key="editor_model_fungsi"
    )

    if len(data_edit) >= 2:

        x_data = pd.to_numeric(data_edit["x"], errors="coerce")
        y_data = pd.to_numeric(data_edit["y"], errors="coerce")

        mask = x_data.notna() & y_data.notna()
        x_clean = x_data[mask]
        y_clean = y_data[mask]

        if len(x_clean) >= 2:

            koef_linear = np.polyfit(x_clean, y_clean, 1)
            y_pred = koef_linear[0] * x_clean + koef_linear[1]

            fig, ax = plt.subplots(figsize=(8, 4))
            ax.scatter(x_clean, y_clean, color="blue", label="Data")
            ax.plot(x_clean, y_pred, "r-", label="Model linear")
            ax.grid(True, linestyle=":", alpha=0.6)
            ax.set_xlabel("x")
            ax.set_ylabel("y")
            ax.set_title("Data vs Model Linear")
            ax.legend()
            st.pyplot(fig)

            st.info(
                f"Model linear: "
                f"y = {koef_linear[0]:.4f}x + {koef_linear[1]:.4f}"
            )

    # =========================================================
    # 16. RESIDUAL
    # =========================================================

    st.header("16. Evaluasi Model")

    st.markdown(r"""
    Salah satu cara mengevaluasi model adalah melihat selisih antara
    nilai aktual dan nilai prediksi.

    Selisih tersebut disebut **residual**.
    """)

    st.latex(r"e=y-\hat{y}")

    st.markdown(r"""
    Semakin kecil residual secara umum, semakin dekat prediksi model
    terhadap data pengamatan.
    """)

    # =========================================================
    # 17. PREDIKSI
    # =========================================================

    st.header("17. Prediksi Menggunakan Model")

    slope_pred = st.number_input(
        "Koefisien x", value=2.0, key="pred_slope"
    )

    intercept_pred = st.number_input(
        "Konstanta", value=1.0, key="pred_intercept"
    )

    x_pred = st.number_input(
        "Nilai x untuk prediksi", value=10.0, key="pred_x"
    )

    hasil_prediksi = slope_pred * x_pred + intercept_pred

    st.info(f"Prediksi y = {hasil_prediksi:.4f}")

    # =========================================================
    # 18. VALIDASI MODEL
    # =========================================================

    st.header("18. Validasi Model")

    st.markdown(r"""
    Model matematika perlu dievaluasi sebelum digunakan untuk membuat
    kesimpulan.

    Beberapa pertanyaan penting:

    - Apakah model sesuai dengan data?
    - Apakah asumsi model masuk akal?
    - Apakah domain model sesuai dengan kondisi nyata?
    - Apakah model masih akurat ketika digunakan untuk prediksi?
    - Apakah terdapat faktor lain yang tidak dimasukkan?
    """)

    st.warning(r"""
    Model yang baik pada suatu kondisi belum tentu akurat jika digunakan
    di luar kondisi tempat model tersebut dibangun.
    """)

    # =========================================================
    # 19. OPTIMASI SEDERHANA
    # =========================================================

    st.header("19. Optimasi Sederhana")

    st.markdown(r"""
    Model fungsi juga dapat digunakan untuk mencari nilai maksimum atau
    minimum suatu besaran.

    Misalnya keuntungan dimodelkan:
    """)

    st.latex(r"K(x)=-x^2+20x-50")

    st.markdown(r"""
    Karena grafik berbentuk parabola yang membuka ke bawah, nilai maksimum
    berada pada titik puncak.
    """)

    a_opt, b_opt, c_opt = -1, 20, -50
    x_opt = -b_opt / (2 * a_opt)
    k_opt = a_opt * x_opt**2 + b_opt * x_opt + c_opt

    st.info(
        f"Nilai maksimum terjadi saat x = {x_opt:.0f}, "
        f"dengan K(x) = {k_opt:.0f}."
    )

    # =========================================================
    # 20. STUDI KASUS PENDAPATAN
    # =========================================================

    st.header("20. Studi Kasus: Pendapatan")

    st.markdown(r"""
    Sebuah usaha menjual produk dengan harga Rp20.000 per unit.

    Jika $x$ adalah jumlah produk yang terjual, maka pendapatan dapat
    dimodelkan sebagai:
    """)

    st.latex(r"R(x)=20000x")

    jumlah_penjualan = st.slider(
        "Jumlah produk terjual", 0, 1000, 100, key="model_penjualan"
    )

    pendapatan = 20000 * jumlah_penjualan

    st.metric("Pendapatan", f"Rp{pendapatan:,.0f}")

    # =========================================================
    # 21. KASUS TEKNOLOGI
    # =========================================================

    st.header("21. Studi Kasus: Teknologi")

    st.markdown(r"""
    Misalkan jumlah pengguna suatu aplikasi bertambah mengikuti model
    eksponensial:
    """)

    st.latex(r"N(t)=N_0(1+r)^t")

    st.markdown(r"""
    dengan:

    - $N_0$ = jumlah pengguna awal.
    - $r$ = laju pertumbuhan.
    - $t$ = waktu.
    - $N(t)$ = jumlah pengguna pada waktu $t$.
    """)

    # =========================================================
    # 22. LATIHAN
    # =========================================================

    st.header("📝 Latihan")

    st.markdown(r"""
    **Soal 1**

    Sebuah produk memiliki harga Rp25.000 per unit dan biaya tetap
    Rp100.000. Bentuklah fungsi biaya $C(x)$.
    """)

    st.markdown(r"""
    **Soal 2**

    Diberikan fungsi $f(x)=2x^2-3x+5$. Tentukan $f(4)$.
    """)

    st.markdown(r"""
    **Soal 3**

    Sebuah populasi dimodelkan dengan $P(t)=1000(1,05)^t$.
    Tentukan populasi setelah 5 periode.
    """)

    st.markdown(r"""
    **Soal 4**

    Jelaskan mengapa domain model matematika harus disesuaikan dengan
    kondisi nyata.
    """)

    st.markdown(r"""
    **Soal 5**

    Jelaskan mengapa model matematika tidak selalu memberikan gambaran
    sempurna mengenai kondisi nyata.
    """)

    # =========================================================
    # 23. KUIS
    # =========================================================

    st.header("🎯 Kuis")

    jawaban_model = st.radio(
        "Jika biaya tetap Rp50.000 dan biaya setiap produk Rp10.000, "
        "fungsi total biaya yang benar adalah:",
        [
            "C(x)=50.000x+10.000",
            "C(x)=10.000x+50.000",
            "C(x)=60.000x",
            "C(x)=50.000x"
        ],
        key="quiz_pemodelan_fungsi"
    )

    if st.button("Periksa Jawaban", key="cek_quiz_pemodelan"):
        if jawaban_model == "C(x)=10.000x+50.000":
            st.success(
                "✅ Benar. Biaya variabel = 10.000x dan biaya tetap = 50.000."
            )
        else:
            st.error(
                "❌ Belum tepat. Perhatikan perbedaan biaya tetap "
                "dan biaya per unit."
            )

    # =========================================================
    # 24. REFLEKSI
    # =========================================================

    st.header("💭 Refleksi")

    st.markdown(r"""
    Setelah mempelajari pemodelan fungsi, coba jelaskan:

    1. Apa yang dimaksud dengan model matematika?
    2. Bagaimana menentukan variabel bebas dan variabel terikat?
    3. Mengapa domain harus disesuaikan dengan konteks?
    4. Apa perbedaan model linear, kuadrat, dan eksponensial?
    5. Bagaimana model fungsi dapat digunakan untuk prediksi?
    6. Mengapa model matematika perlu divalidasi?
    """)

    # =========================================================
    # 25. RANGKUMAN
    # =========================================================

    st.header("📌 Rangkuman")

    st.markdown(r"""
    **Pemodelan fungsi** merupakan proses menerjemahkan permasalahan nyata
    ke dalam bentuk fungsi matematika.

    Konsep utama:

    - Variabel bebas merupakan input model.
    - Variabel terikat merupakan output model.
    - Model linear digunakan untuk hubungan linear.
    - Model kuadrat dapat digunakan untuk hubungan berbentuk parabola.
    - Model eksponensial dapat digunakan untuk pertumbuhan atau peluruhan.
    - Fungsi sinus dan cosinus dapat digunakan untuk fenomena periodik.
    - Domain dan range harus sesuai dengan konteks nyata.
    - Model dapat digunakan untuk prediksi dan optimasi.
    - Model perlu divalidasi terhadap data dan kondisi nyata.
    """)

    st.success("🎉 Materi Pemodelan Fungsi selesai dipelajari.")



def trigonometri():

    st.markdown(
        '<div class="content-title">📕 Trigonometri</div>',
        unsafe_allow_html=True
    )

    # =========================================================
    # TUJUAN PEMBELAJARAN
    # =========================================================

    st.header("🎯 Tujuan Pembelajaran")

    st.markdown(r"""
    Setelah mempelajari materi ini, siswa diharapkan mampu:

    - Menjelaskan hubungan sudut dan perbandingan trigonometri.
    - Menggunakan nilai sinus, cosinus, dan tangen.
    - Menggunakan identitas dasar trigonometri.
    - Menentukan nilai trigonometri pada berbagai kuadran.
    - Menyelesaikan persamaan trigonometri sederhana.
    - Menggunakan aturan sinus dan aturan cosinus.
    - Menentukan luas segitiga menggunakan konsep trigonometri.
    - Menganalisis grafik fungsi sinus, cosinus, dan tangen.
    - Menentukan amplitudo, periode, dan pergeseran grafik trigonometri.
    - Menerapkan trigonometri dalam masalah kontekstual.
    """)

    # =========================================================
    # APERSEPSI
    # =========================================================

    st.header("💡 Apersepsi")

    st.markdown(r"""
    Trigonometri mempelajari hubungan antara sudut dan panjang sisi.

    Konsep ini tidak hanya digunakan pada segitiga, tetapi juga dalam
    gelombang, astronomi, teknik, navigasi, robotika, fisika, dan
    pemodelan matematika.
    """)

    st.latex(r"\sin\theta=\frac{\text{sisi depan}}{\text{sisi miring}}")

    # =========================================================
    # 1. PERBANDINGAN TRIGONOMETRI
    # =========================================================

    st.header("1. Perbandingan Trigonometri")

    st.markdown(r"""
    Pada segitiga siku-siku, tiga perbandingan trigonometri utama adalah
    sinus, cosinus, dan tangen.
    """)

    st.latex(r"\sin\theta=\frac{\text{depan}}{\text{miring}}")
    st.latex(r"\cos\theta=\frac{\text{samping}}{\text{miring}}")
    st.latex(r"\tan\theta=\frac{\text{depan}}{\text{samping}}")

    st.markdown("Hubungan ketiganya:")

    st.latex(r"\tan\theta=\frac{\sin\theta}{\cos\theta}")

    # =========================================================
    # 2. UNIT CIRCLE
    # =========================================================

    st.header("2. Lingkaran Satuan")

    st.markdown(r"""
    Lingkaran satuan adalah lingkaran yang berpusat di titik asal
    dengan jari-jari 1.
    """)

    st.latex(r"x^2+y^2=1")

    st.markdown(r"""
    Untuk sudut $\theta$, koordinat titik pada lingkaran satuan dapat
    dinyatakan sebagai:
    """)

    st.latex(r"P(\cos\theta,\sin\theta)")

    st.markdown(r"""
    Dengan demikian:

    - koordinat $x$ berkaitan dengan $\cos\theta$,
    - koordinat $y$ berkaitan dengan $\sin\theta$.
    """)

    st.markdown("#### 🔎 Eksplorasi Lingkaran Satuan")

    angle_unit = st.slider(
        "Sudut θ (derajat)",
        min_value=0,
        max_value=360,
        value=45,
        key="trig_unit_angle"
    )

    angle_rad = math.radians(angle_unit)
    sin_val = math.sin(angle_rad)
    cos_val = math.cos(angle_rad)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("sin θ", f"{sin_val:.4f}")

    with col2:
        st.metric("cos θ", f"{cos_val:.4f}")

    with col3:
        st.metric(
            "tan θ",
            "tidak terdefinisi" if abs(cos_val) < 1e-10
            else f"{math.tan(angle_rad):.4f}"
        )

    # =========================================================
    # 3. NILAI SUDUT ISTIMEWA
    # =========================================================

    st.header("3. Nilai Sudut Istimewa")

    data_sudut = pd.DataFrame({
        "Sudut": ["0°", "30°", "45°", "60°", "90°"],
        "sin": ["0", "1/2", "√2/2", "√3/2", "1"],
        "cos": ["1", "√3/2", "√2/2", "1/2", "0"],
        "tan": ["0", "√3/3", "1", "√3", "Tidak terdefinisi"]
    })

    st.dataframe(
        data_sudut,
        use_container_width=True,
        hide_index=True
    )

    # =========================================================
    # 4. KUADRAN
    # =========================================================

    st.header("4. Tanda Trigonometri pada Kuadran")

    st.markdown(r"""
    Tanda nilai trigonometri bergantung pada kuadran tempat sudut berada.
    """)

    st.markdown("#### Kuadran I")
    st.markdown("- sin positif")
    st.markdown("- cos positif")
    st.markdown("- tan positif")

    st.markdown("#### Kuadran II")
    st.markdown("- sin positif")
    st.markdown("- cos negatif")
    st.markdown("- tan negatif")

    st.markdown("#### Kuadran III")
    st.markdown("- sin negatif")
    st.markdown("- cos negatif")
    st.markdown("- tan positif")

    st.markdown("#### Kuadran IV")
    st.markdown("- sin negatif")
    st.markdown("- cos positif")
    st.markdown("- tan negatif")

    # =========================================================
    # 5. IDENTITAS PYTHAGORAS
    # =========================================================

    st.header("5. Identitas Trigonometri")

    st.markdown("Identitas dasar yang sangat penting adalah:")

    st.latex(r"\sin^2\theta+\cos^2\theta=1")

    st.markdown("Dari identitas tersebut diperoleh:")

    st.latex(r"1+\tan^2\theta=\sec^2\theta")
    st.latex(r"1+\cot^2\theta=\csc^2\theta")

    st.markdown(r"""
    Identitas digunakan untuk menyederhanakan bentuk trigonometri dan
    membuktikan hubungan matematis.
    """)

    # =========================================================
    # 6. EKSPLORASI IDENTITAS
    # =========================================================

    st.header("6. Eksplorasi Identitas Pythagoras")

    sudut_identitas = st.slider(
        "Pilih sudut",
        0.0,
        360.0,
        30.0,
        step=1.0,
        key="trig_identity_angle"
    )

    rad_identitas = math.radians(sudut_identitas)
    nilai_sin = math.sin(rad_identitas)
    nilai_cos = math.cos(rad_identitas)
    hasil_identitas = nilai_sin**2 + nilai_cos**2

    st.metric("sin²θ + cos²θ", f"{hasil_identitas:.6f}")

    st.info("Nilainya selalu mendekati 1 karena sin²θ + cos²θ = 1.")

    # =========================================================
    # 7. RUMUS JUMLAH DAN SELISIH SUDUT
    # =========================================================

    st.header("7. Rumus Jumlah dan Selisih Sudut")

    st.markdown("#### Untuk Sinus")

    st.latex(r"\sin(A+B)=\sin A\cos B+\cos A\sin B")
    st.latex(r"\sin(A-B)=\sin A\cos B-\cos A\sin B")

    st.markdown("#### Untuk Cosinus")

    st.latex(r"\cos(A+B)=\cos A\cos B-\sin A\sin B")
    st.latex(r"\cos(A-B)=\cos A\cos B+\sin A\sin B")

    st.markdown("#### Untuk Tangen")

    st.latex(r"\tan(A+B)=\frac{\tan A+\tan B}{1-\tan A\tan B}")

    # =========================================================
    # 8. SUDUT GANDA
    # =========================================================

    st.header("8. Rumus Sudut Ganda")

    st.latex(r"\sin2\theta=2\sin\theta\cos\theta")
    st.latex(r"\cos2\theta=\cos^2\theta-\sin^2\theta")
    st.latex(r"\cos2\theta=2\cos^2\theta-1")
    st.latex(r"\cos2\theta=1-2\sin^2\theta")
    st.latex(r"\tan2\theta=\frac{2\tan\theta}{1-\tan^2\theta}")

    # =========================================================
    # 9. PERSAMAAN TRIGONOMETRI
    # =========================================================

    st.header("9. Persamaan Trigonometri")

    st.markdown(r"""
    Persamaan trigonometri adalah persamaan yang memuat fungsi
    trigonometri.
    """)

    st.markdown("Contoh:")

    st.latex(r"\sin x=\frac{1}{2}")

    st.markdown(r"""
    Untuk $0^\circ\leq x\leq360^\circ$, penyelesaiannya adalah:
    """)

    st.latex(r"x=30^\circ\text{ atau }150^\circ")

    st.markdown("Contoh lainnya:")

    st.latex(r"\cos x=0")
    st.latex(r"x=90^\circ\text{ atau }270^\circ")

    # =========================================================
    # 10. KALKULATOR NILAI TRIGONOMETRI
    # =========================================================

    st.header("10. Kalkulator Nilai Trigonometri")

    sudut_kalk = st.number_input(
        "Masukkan sudut (derajat)",
        value=30.0,
        key="trig_kalk_sudut"
    )

    rad_kalk = math.radians(sudut_kalk)
    nilai_s = math.sin(rad_kalk)
    nilai_c = math.cos(rad_kalk)

    if abs(nilai_c) < 1e-10:
        nilai_t = None
    else:
        nilai_t = math.tan(rad_kalk)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("sin", f"{nilai_s:.6f}")

    with col2:
        st.metric("cos", f"{nilai_c:.6f}")

    with col3:
        if nilai_t is None:
            st.metric("tan", "Tidak terdefinisi")
        else:
            st.metric("tan", f"{nilai_t:.6f}")

    # =========================================================
    # 11. ATURAN SINUS
    # =========================================================

    st.header("11. Aturan Sinus")

    st.markdown(r"""
    Aturan sinus digunakan pada segitiga sembarang.
    """)

    st.latex(r"\frac{a}{\sin A}=\frac{b}{\sin B}=\frac{c}{\sin C}")

    st.markdown(r"""
    Aturan sinus berguna ketika diketahui kombinasi sisi dan sudut tertentu
    pada sebuah segitiga.
    """)

    # =========================================================
    # 12. ATURAN COSINUS
    # =========================================================

    st.header("12. Aturan Cosinus")

    st.markdown(r"""
    Aturan cosinus merupakan generalisasi Teorema Pythagoras untuk
    segitiga sembarang.
    """)

    st.latex(r"c^2=a^2+b^2-2ab\cos C")

    st.markdown(r"""
    Jika $C=90^\circ$, maka $\cos C=0$, sehingga:
    """)

    st.latex(r"c^2=a^2+b^2")

    st.markdown("Inilah Teorema Pythagoras.")

    # =========================================================
    # 13. KALKULATOR ATURAN COSINUS
    # =========================================================

    st.header("13. Kalkulator Aturan Cosinus")

    col1, col2, col3 = st.columns(3)

    with col1:
        sisi_a = st.number_input(
            "Sisi a", min_value=0.01, value=5.0, key="cos_a"
        )

    with col2:
        sisi_b = st.number_input(
            "Sisi b", min_value=0.01, value=6.0, key="cos_b"
        )

    with col3:
        sudut_C = st.number_input(
            "Sudut C (derajat)",
            min_value=0.0,
            max_value=180.0,
            value=60.0,
            key="cos_C"
        )

    c_squared = (
        sisi_a**2
        + sisi_b**2
        - 2 * sisi_a * sisi_b * math.cos(math.radians(sudut_C))
    )

    sisi_c = math.sqrt(max(c_squared, 0))

    st.info(f"Sisi c = {sisi_c:.4f}")

    # =========================================================
    # 14. LUAS SEGITIGA
    # =========================================================

    st.header("14. Luas Segitiga dengan Trigonometri")

    st.markdown(r"""
    Jika diketahui dua sisi dan sudut apitnya, luas segitiga dapat
    dihitung menggunakan:
    """)

    st.latex(r"L=\frac{1}{2}ab\sin C")

    st.markdown("Contoh:")

    st.latex(r"a=6,\quad b=8,\quad C=30^\circ")
    st.latex(r"L=\frac{1}{2}(6)(8)\sin30^\circ=12")

    # =========================================================
    # 15. KALKULATOR LUAS
    # =========================================================

    st.header("15. Kalkulator Luas Segitiga")

    luas_a = st.number_input(
        "Sisi a", min_value=0.01, value=6.0, key="luas_a"
    )

    luas_b = st.number_input(
        "Sisi b", min_value=0.01, value=8.0, key="luas_b"
    )

    luas_sudut = st.number_input(
        "Sudut apit (derajat)",
        min_value=0.0,
        max_value=180.0,
        value=30.0,
        key="luas_sudut"
    )

    luas = 0.5 * luas_a * luas_b * math.sin(math.radians(luas_sudut))

    st.info(f"Luas segitiga = {luas:.4f} satuan²")

    # =========================================================
    # 16. GRAFIK FUNGSI SINUS
    # =========================================================

    st.header("16. Grafik Fungsi Trigonometri")

    st.markdown("Fungsi sinus dasar adalah:")

    st.latex(r"y=\sin x")

    x_grafik = np.linspace(0, 2 * np.pi, 400)

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(x_grafik, np.sin(x_grafik), "b-")
    ax.axhline(0, color="gray", linewidth=0.6)
    ax.axvline(0, color="gray", linewidth=0.6)
    ax.grid(True, linestyle=":", alpha=0.6)
    ax.set_xlabel("x (radian)")
    ax.set_ylabel("sin x")
    ax.set_title("y = sin x")
    st.pyplot(fig)

    # =========================================================
    # 17. FUNGSI SINUS UMUM
    # =========================================================

    st.header("17. Bentuk Umum Fungsi Sinus")

    st.latex(r"y=a\sin(bx+c)+d")

    st.markdown(r"""
    Parameter tersebut memengaruhi bentuk grafik:

    - $|a|$ menentukan amplitudo.
    - $b$ menentukan periode.
    - $c$ menentukan pergeseran horizontal.
    - $d$ menentukan pergeseran vertikal.
    """)

    st.latex(r"\text{Amplitudo}=|a|")
    st.latex(r"\text{Periode}=\frac{2\pi}{|b|}")

    # =========================================================
    # 18. EKSPLORASI GRAFIK
    # =========================================================

    st.header("18. Eksplorasi Grafik Sinus")

    col1, col2 = st.columns(2)

    with col1:
        amp = st.slider(
            "Amplitudo a", -5.0, 5.0, 1.0, step=0.5, key="trig_amp"
        )

        freq = st.slider(
            "Frekuensi b", 0.5, 5.0, 1.0, step=0.5, key="trig_freq"
        )

    with col2:
        fase = st.slider(
            "Pergeseran fase c", -math.pi, math.pi, 0.0,
            step=0.1, key="trig_fase"
        )

        vertikal = st.slider(
            "Pergeseran vertikal d", -5.0, 5.0, 0.0,
            step=0.5, key="trig_vertikal"
        )

    y_grafik = amp * np.sin(freq * x_grafik + fase) + vertikal

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(x_grafik, y_grafik, "m-")
    ax.axhline(0, color="gray", linewidth=0.6)
    ax.axvline(0, color="gray", linewidth=0.6)
    ax.grid(True, linestyle=":", alpha=0.6)
    ax.set_xlabel("x (radian)")
    ax.set_ylabel("y")
    ax.set_title(rf"$y = {amp:.1f}\sin({freq:.1f}x + {fase:.1f}) + {vertikal:.1f}$")
    st.pyplot(fig)

    periode = 2 * math.pi / abs(freq) if freq != 0 else float("inf")

    st.info(
        f"Amplitudo = {abs(amp):.2f} | "
        f"Periode = {periode:.4f} rad"
    )

    # =========================================================
    # 19. FUNGSI COSINUS
    # =========================================================

    st.header("19. Fungsi Cosinus")

    st.latex(r"y=\cos x")

    st.markdown(r"""
    Grafik cosinus memiliki bentuk gelombang yang serupa dengan sinus,
    tetapi memiliki titik awal yang berbeda.
    """)

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(x_grafik, np.cos(x_grafik), "r-")
    ax.axhline(0, color="gray", linewidth=0.6)
    ax.axvline(0, color="gray", linewidth=0.6)
    ax.grid(True, linestyle=":", alpha=0.6)
    ax.set_xlabel("x (radian)")
    ax.set_ylabel("cos x")
    ax.set_title("y = cos x")
    st.pyplot(fig)

    # =========================================================
    # 20. FUNGSI TANGEN
    # =========================================================

    st.header("20. Fungsi Tangen")

    st.latex(r"y=\tan x")

    st.markdown(r"""
    Fungsi tangen mempunyai periode $\pi$ dan memiliki asimtot vertikal
    pada $x=\frac{\pi}{2}+k\pi$ untuk setiap bilangan bulat $k$.
    """)

    x_tan = np.linspace(-2 * np.pi, 2 * np.pi, 2000)
    y_tan = np.tan(x_tan)
    y_tan[np.abs(y_tan) > 10] = np.nan

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(x_tan, y_tan, "g-")
    ax.axhline(0, color="gray", linewidth=0.6)
    ax.axvline(0, color="gray", linewidth=0.6)
    ax.set_ylim(-10, 10)
    ax.grid(True, linestyle=":", alpha=0.6)
    ax.set_xlabel("x (radian)")
    ax.set_ylabel("tan x")
    ax.set_title("y = tan x")
    st.pyplot(fig)

    # =========================================================
    # 21. HUBUNGAN SINUS, COSINUS, TANGEN
    # =========================================================

    st.header("21. Hubungan Sinus, Cosinus, dan Tangen")

    st.latex(r"\tan\theta=\frac{\sin\theta}{\cos\theta}")
    st.latex(r"\sin^2\theta+\cos^2\theta=1")

    st.markdown(r"""
    Dua hubungan tersebut merupakan dasar penting dalam manipulasi
    aljabar trigonometri.
    """)

    # =========================================================
    # 22. PENERAPAN
    # =========================================================

    st.header("🌍 Penerapan Trigonometri")

    st.markdown(r"""
    Trigonometri digunakan dalam:

    - Pengukuran tinggi bangunan.
    - Navigasi.
    - Astronomi.
    - Teknik sipil.
    - Robotika.
    - Gelombang dan getaran.
    - Grafika komputer.
    - Pemodelan periodik.
    - Sistem GPS.
    """)

    # =========================================================
    # 23. STUDI KASUS
    # =========================================================

    st.header("📐 Studi Kasus: Mengukur Tinggi Bangunan")

    st.markdown(r"""
    Seorang siswa berdiri sejauh 20 meter dari sebuah gedung.

    Sudut elevasi ke puncak gedung adalah $35^\circ$.
    Jika tinggi mata siswa diabaikan, tinggi gedung dapat dihitung dengan:
    """)

    st.latex(r"\tan35^\circ=\frac{h}{20}")
    st.latex(r"h=20\tan35^\circ")

    tinggi_gedung = 20 * math.tan(math.radians(35))

    st.info(f"Perkiraan tinggi gedung = {tinggi_gedung:.2f} meter.")

    # =========================================================
    # 24. LATIHAN
    # =========================================================

    st.header("📝 Latihan")

    st.markdown(r"""
    **Soal 1**

    Tentukan nilai $\sin30^\circ$, $\cos60^\circ$, dan $\tan45^\circ$.
    """)

    st.markdown(r"""
    **Soal 2**

    Jika $\sin\theta=\frac{3}{5}$ dan $\theta$ berada pada kuadran I,
    tentukan $\cos\theta$.
    """)

    st.markdown(r"""
    **Soal 3**

    Tentukan penyelesaian $\sin x=\frac{1}{2}$ untuk
    $0^\circ\leq x\leq360^\circ$.
    """)

    st.markdown(r"""
    **Soal 4**

    Dua sisi segitiga masing-masing 6 cm dan 8 cm dengan sudut apit
    $30^\circ$. Tentukan luas segitiga.
    """)

    st.markdown(r"""
    **Soal 5**

    Tentukan sisi ketiga segitiga jika $a=5$, $b=6$, dan $C=60^\circ$.
    """)

    # =========================================================
    # 25. KUIS
    # =========================================================

    st.header("🎯 Kuis")

    jawaban_trig = st.radio(
        "Nilai sin 30° adalah:",
        ["0", "1/2", "√2/2", "√3/2"],
        key="quiz_trigonometri"
    )

    if st.button("Periksa Jawaban", key="cek_quiz_trigonometri"):
        if jawaban_trig == "1/2":
            st.success("✅ Benar. sin 30° = 1/2.")
        else:
            st.error("❌ Belum tepat. Ingat tabel sudut istimewa.")

    # =========================================================
    # 26. REFLEKSI
    # =========================================================

    st.header("💭 Refleksi")

    st.markdown(r"""
    Setelah mempelajari trigonometri, coba jelaskan:

    1. Apa hubungan sinus, cosinus, dan tangen?
    2. Mengapa lingkaran satuan penting dalam trigonometri?
    3. Bagaimana tanda fungsi trigonometri ditentukan berdasarkan kuadran?
    4. Apa perbedaan aturan sinus dan aturan cosinus?
    5. Bagaimana menentukan amplitudo dan periode fungsi sinus?
    6. Bagaimana trigonometri digunakan dalam pengukuran tinggi?
    """)

    # =========================================================
    # 27. RANGKUMAN
    # =========================================================

    st.header("📌 Rangkuman")

    st.markdown(r"""
    **Trigonometri** mempelajari hubungan antara sudut dan panjang sisi.

    Konsep utama:

    - Sinus, cosinus, dan tangen merupakan perbandingan trigonometri utama.
    - Lingkaran satuan membantu memahami nilai fungsi trigonometri.
    - Identitas $\sin^2\theta+\cos^2\theta=1$ merupakan identitas dasar.
    - Rumus jumlah dan selisih sudut digunakan untuk mengembangkan bentuk
      trigonometri.
    - Persamaan trigonometri dapat memiliki lebih dari satu penyelesaian
      dalam suatu interval.
    - Aturan sinus dan cosinus digunakan pada segitiga sembarang.
    - Fungsi sinus dan cosinus memiliki pola periodik.
    - Amplitudo dan periode menentukan karakteristik grafik.
    - Trigonometri digunakan dalam teknik, sains, navigasi, robotika,
      grafika komputer, dan berbagai bidang lainnya.
    """)

    st.success("🎉 Materi Trigonometri selesai dipelajari.")
    

def transformasi_geometri():
    st.markdown(
        '<div class="content-title">📕 Transformasi Geometri</div>',
        unsafe_allow_html=True
    )

    # =========================================================
    # TUJUAN PEMBELAJARAN
    # =========================================================

    st.header("🎯 Tujuan Pembelajaran")

    st.markdown(r"""
    Setelah mempelajari materi ini, siswa diharapkan mampu:

    - Menjelaskan konsep transformasi geometri.
    - Menentukan hasil translasi suatu titik atau bangun.
    - Menentukan hasil refleksi terhadap berbagai garis.
    - Menentukan hasil rotasi terhadap pusat tertentu.
    - Menentukan hasil dilatasi suatu titik atau bangun.
    - Menggunakan matriks untuk merepresentasikan transformasi.
    - Menentukan hasil komposisi transformasi.
    - Menganalisis hubungan antara transformasi dan koordinat.
    - Menerapkan transformasi geometri dalam masalah kontekstual.
    """)

    # =========================================================
    # APERSEPSI
    # =========================================================

    st.header("💡 Apersepsi")

    st.markdown(r"""
    Pernahkah kamu melihat gambar yang digeser, dicerminkan, diputar,
    atau diperbesar?

    Perubahan posisi, orientasi, maupun ukuran suatu objek tersebut dapat
    dipelajari menggunakan **transformasi geometri**.

    Dalam sistem koordinat, transformasi digunakan untuk menentukan posisi
    baru suatu titik atau bangun.
    """)

    st.latex(r"P(x,y)\to P'(x',y')")   # FIX: \rightarrow → \to (lebih aman)

    # =========================================================
    # 1. KONSEP DASAR
    # =========================================================

    st.header("1️⃣ Konsep Dasar Transformasi")

    st.markdown(r"""
    Transformasi geometri adalah pemetaan setiap titik pada suatu bidang
    ke titik lain sehingga diperoleh objek hasil transformasi.

    Titik sebelum transformasi disebut **titik asal**, sedangkan titik
    setelah transformasi disebut **bayangan**.
    """)

    st.latex(r"P(x,y)\to P'(x',y')")

    st.markdown(r"""
    Empat transformasi dasar yang dipelajari adalah:

    - **Translasi** → pergeseran.
    - **Refleksi** → pencerminan.
    - **Rotasi** → perputaran.
    - **Dilatasi** → perubahan ukuran.
    """)

    # =========================================================
    # 2. TRANSLASI
    # =========================================================

    st.header("2️⃣ Translasi")

    st.markdown(r"""
    Translasi adalah transformasi yang memindahkan setiap titik dengan
    jarak dan arah yang sama.
    """)

    st.latex(r"T=\begin{pmatrix}a\\b\end{pmatrix}")

    st.markdown(r"Jika titik $P(x,y)$ ditranslasikan oleh $T(a,b)$, maka:")

    st.latex(r"P'(x',y')=(x+a,\;y+b)")   # FIX: \; untuk spasi setelah koma

    st.markdown("Contoh:")

    st.latex(r"P(2,3)\to P'(6,2)\quad\text{oleh }T(4,-1)")  # FIX: hindari \xrightarrow

    # =========================================================
    # 3. EKSPLORASI TRANSLASI
    # =========================================================

    st.header("🔎 Eksplorasi Translasi")

    col1, col2 = st.columns(2)

    with col1:
        tx = st.number_input("Koordinat x titik P", value=2.0, key="geo_tx")
        ty = st.number_input("Koordinat y titik P", value=3.0, key="geo_ty")

    with col2:
        a_trans = st.number_input("Pergeseran horizontal (a)", value=4.0, key="geo_a_trans")
        b_trans = st.number_input("Pergeseran vertikal (b)", value=-1.0, key="geo_b_trans")

    tx_baru = tx + a_trans
    ty_baru = ty + b_trans

    st.info(f"P({tx:g}, {ty:g}) → P'({tx_baru:g}, {ty_baru:g})")  # FIX: success → info

    # =========================================================
    # 4. REFLEKSI
    # =========================================================

    st.header("3️⃣ Refleksi")

    st.markdown(r"""
    Refleksi atau pencerminan menghasilkan bayangan yang memiliki jarak
    sama terhadap garis cermin.
    """)

    st.markdown("Refleksi terhadap sumbu-X")
    st.latex(r"(x,y)\to(x,-y)")

    st.markdown("Refleksi terhadap sumbu-Y")
    st.latex(r"(x,y)\to(-x,y)")

    st.markdown("Refleksi terhadap titik asal O")
    st.latex(r"(x,y)\to(-x,-y)")

    st.markdown("Refleksi terhadap garis y = x")
    st.latex(r"(x,y)\to(y,x)")

    st.markdown("Refleksi terhadap garis y = -x")
    st.latex(r"(x,y)\to(-y,-x)")

    # =========================================================
    # 5. REFLEKSI TERHADAP GARIS VERTIKAL / HORIZONTAL
    # =========================================================

    st.markdown("Refleksi terhadap garis x = a")
    st.latex(r"(x,y)\to(2a-x,\;y)")
    st.markdown("Di sini $a$ adalah konstanta yang menyatakan posisi garis cermin, bukan variabel titik.")  # FIX: klarifikasi

    st.markdown("Refleksi terhadap garis y = b")
    st.latex(r"(x,y)\to(x,\;2b-y)")

    # =========================================================
    # 6. EKSPLORASI REFLEKSI
    # =========================================================

    st.header("🔎 Eksplorasi Refleksi")

    rx = st.number_input("Koordinat x", value=3.0, key="geo_rx")
    ry = st.number_input("Koordinat y", value=2.0, key="geo_ry")

    refleksi = st.selectbox(
        "Pilih jenis refleksi",
        ["Sumbu-X", "Sumbu-Y", "Titik Asal O", "Garis y = x", "Garis y = -x"],
        key="geo_refleksi"
    )

    if refleksi == "Sumbu-X":
        xr, yr = rx, -ry
    elif refleksi == "Sumbu-Y":
        xr, yr = -rx, ry
    elif refleksi == "Titik Asal O":
        xr, yr = -rx, -ry
    elif refleksi == "Garis y = x":
        xr, yr = ry, rx
    else:
        xr, yr = -ry, -rx

    st.info(f"P({rx:g}, {ry:g}) → P'({xr:g}, {yr:g})")

    # =========================================================
    # 7. ROTASI
    # =========================================================

    st.header("4️⃣ Rotasi")

    st.markdown(r"""
    Rotasi adalah transformasi yang memutar titik atau bangun terhadap
    suatu pusat dengan besar sudut tertentu.

    Arah rotasi **berlawanan arah jarum jam (CCW)** kecuali disebutkan lain.
    """)  # FIX: klarifikasi arah

    st.markdown(r"#### Rotasi berpusat di titik asal $O(0,0)$:")

    st.markdown("##### Rotasi 90° berlawanan arah jarum jam (CCW)")
    st.latex(r"(x,y)\to(-y,\;x)")

    st.markdown("##### Rotasi 90° searah jarum jam (CW)")
    st.latex(r"(x,y)\to(y,\;-x)")

    st.markdown("##### Rotasi 180°")
    st.latex(r"(x,y)\to(-x,\;-y)")

    st.markdown("##### Rotasi 270° berlawanan arah jarum jam (CCW)")
    st.latex(r"(x,y)\to(y,\;-x)")
    st.markdown("Perhatikan: rotasi 270° CCW sama dengan rotasi 90° CW.")  # FIX: klarifikasi

    # =========================================================
    # 8. MATRIKS ROTASI
    # =========================================================

    st.header("5️⃣ Matriks Rotasi")

    st.markdown("Rotasi dapat direpresentasikan menggunakan matriks.")

    st.markdown("##### Rotasi 90° CCW")
    st.latex(r"R_{90}=\begin{pmatrix}0&-1\\1&0\end{pmatrix}")

    st.markdown("##### Rotasi 180°")
    st.latex(r"R_{180}=\begin{pmatrix}-1&0\\0&-1\end{pmatrix}")

    st.markdown("##### Rotasi 270° CCW")
    st.latex(r"R_{270}=\begin{pmatrix}0&1\\-1&0\end{pmatrix}")

    # =========================================================
    # 9. ROTASI DENGAN SUDUT UMUM
    # =========================================================

    st.header("6️⃣ Rotasi dengan Sudut Umum")

    st.markdown(r"Untuk rotasi sebesar sudut $\theta$ terhadap titik asal:")

    st.latex(r"R_\theta=\begin{pmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{pmatrix}")

    st.markdown("Sehingga:")

    st.latex(r"\begin{pmatrix}x'\\y'\end{pmatrix}=R_\theta\begin{pmatrix}x\\y\end{pmatrix}")

    # =========================================================
    # 10. EKSPLORASI ROTASI
    # =========================================================

    st.header("🔎 Eksplorasi Rotasi")

    rot_x = st.number_input("x titik P", value=2.0, key="geo_rot_x")
    rot_y = st.number_input("y titik P", value=3.0, key="geo_rot_y")

    sudut = st.selectbox(
        "Sudut rotasi (berlawanan arah jarum jam / CCW)",  # FIX: klarifikasi arah
        [90, 180, 270],
        key="geo_sudut_rotasi"
    )

    if sudut == 90:
        x_rot, y_rot = -rot_y, rot_x
    elif sudut == 180:
        x_rot, y_rot = -rot_x, -rot_y
    else:  # 270 CCW
        x_rot, y_rot = rot_y, -rot_x

    st.info(f"P({rot_x:g}, {rot_y:g}) → P'({x_rot:g}, {y_rot:g})")

    # =========================================================
    # 11. DILATASI
    # =========================================================

    st.header("7️⃣ Dilatasi")

    st.markdown(r"""
    Dilatasi adalah transformasi yang mengubah ukuran suatu objek
    berdasarkan faktor skala tertentu.
    """)

    st.markdown(r"Jika pusat dilatasi adalah $O(0,0)$ dan faktor skala $k$, maka:")

    st.latex(r"(x,y)\to(kx,\;ky)")

    st.markdown(r"""
    Interpretasi faktor skala:

    - $k>1$ → diperbesar.
    - $0<k<1$ → diperkecil.
    - $k=1$ → tetap.
    - $k<0$ → bayangan berada pada arah berlawanan dari pusat.
    """)

    st.markdown("Contoh:")
    st.latex(r"P(2,3)\to P'(4,6)\quad\text{untuk }k=2")

    # =========================================================
    # 12. DILATASI DENGAN PUSAT LAIN
    # =========================================================

    st.header("8️⃣ Dilatasi dengan Pusat (a, b)")  # FIX: LaTeX di header tidak dirender

    st.markdown(r"Jika pusat dilatasi adalah $C(a,b)$ dan faktor skala $k$, maka:")

    st.latex(r"x'=a+k(x-a)")
    st.latex(r"y'=b+k(y-b)")

    # =========================================================
    # 13. EKSPLORASI DILATASI
    # =========================================================

    st.header("🔎 Eksplorasi Dilatasi")

    dx = st.number_input("Koordinat x titik P", value=2.0, key="geo_dx")
    dy = st.number_input("Koordinat y titik P", value=3.0, key="geo_dy")
    faktor = st.number_input("Faktor skala k", value=2.0, key="geo_faktor")

    dx_baru = faktor * dx
    dy_baru = faktor * dy

    st.info(f"P({dx:g}, {dy:g}) → P'({dx_baru:g}, {dy_baru:g})")

    # =========================================================
    # 14. KOMPOSISI TRANSFORMASI
    # =========================================================

    st.header("9️⃣ Komposisi Transformasi")

    st.markdown(r"""
    Dua atau lebih transformasi dapat dilakukan secara berurutan.
    Transformasi gabungan tersebut disebut **komposisi transformasi**.
    """)

    st.markdown(r"Misalnya titik $P$ terlebih dahulu ditranslasikan kemudian direfleksikan.")

    st.latex(r"P\;\overset{T}{\longrightarrow}\;P'\;\overset{R}{\longrightarrow}\;P''")  # FIX: ganti \xrightarrow

    st.markdown(r"""
    Urutan transformasi penting karena pada umumnya hasilnya dapat berbeda
    jika urutannya ditukar.
    """)

    st.latex(r"R\circ T\neq T\circ R")

    # =========================================================
    # 15. EKSPLORASI KOMPOSISI
    # =========================================================

    st.header("🔬 Eksplorasi Komposisi Transformasi")

    cx = st.number_input("x titik awal", value=2.0, key="geo_comp_x")
    cy = st.number_input("y titik awal", value=1.0, key="geo_comp_y")
    ct = st.number_input("Translasi horizontal", value=3.0, key="geo_comp_tx")
    cv = st.number_input("Translasi vertikal", value=2.0, key="geo_comp_ty")

    komposisi = st.selectbox(
        "Transformasi kedua",
        [
            "Refleksi sumbu-X",
            "Refleksi sumbu-Y",
            "Rotasi 90° CCW",   # FIX: tambah CCW
            "Dilatasi k = 2"
        ],
        key="geo_komposisi"
    )

    x1, y1 = cx + ct, cy + cv

    if komposisi == "Refleksi sumbu-X":
        x2, y2 = x1, -y1
    elif komposisi == "Refleksi sumbu-Y":
        x2, y2 = -x1, y1
    elif komposisi == "Rotasi 90° CCW":
        x2, y2 = -y1, x1
    else:
        x2, y2 = 2 * x1, 2 * y1

    st.info(f"P({cx:g}, {cy:g}) → P'({x1:g}, {y1:g}) → P''({x2:g}, {y2:g})")

    # =========================================================
    # 16. MATRIKS REFLEKSI   # FIX: typo "MATRKS" → "MATRIKS"
    # =========================================================

    st.header("🔢 Matriks Transformasi")

    st.markdown("Refleksi terhadap sumbu-X:")
    st.latex(r"M_x=\begin{pmatrix}1&0\\0&-1\end{pmatrix}")

    st.markdown("Refleksi terhadap sumbu-Y:")
    st.latex(r"M_y=\begin{pmatrix}-1&0\\0&1\end{pmatrix}")

    st.markdown(r"Dilatasi dengan faktor $k$:")
    st.latex(r"D=\begin{pmatrix}k&0\\0&k\end{pmatrix}")

    # =========================================================
    # 17. TRANSFORMASI PADA BANGUN
    # =========================================================

    st.header("🔺 Transformasi pada Bangun")

    st.markdown(r"""
    Transformasi tidak hanya dapat diterapkan pada satu titik.

    Jika sebuah bangun memiliki beberapa titik sudut, transformasi diterapkan
    pada setiap titik tersebut.
    """)

    st.markdown("Misalnya segitiga:")

    st.latex(r"A(1,1),\quad B(4,1),\quad C(2,4)")

    st.markdown("Jika direfleksikan terhadap sumbu-X:")

    st.latex(r"A'(1,-1),\quad B'(4,-1),\quad C'(2,-4)")

    # =========================================================
    # 18. VISUALISASI SEDERHANA   # FIX: ganti st.line_chart → matplotlib
    # =========================================================

    st.header("📈 Visualisasi Transformasi")

    titik_asal_x = [1, 4, 2, 1]
    titik_asal_y = [1, 1, 4, 1]
    titik_bayangan_x = [1, 4, 2, 1]
    titik_bayangan_y = [-1, -1, -4, -1]

    fig, ax = plt.subplots(figsize=(5, 5))
    ax.plot(titik_asal_x, titik_asal_y, "b-o", label="Segitiga asal")
    ax.plot(titik_bayangan_x, titik_bayangan_y, "r--o", label="Bayangan (sumbu-X)")

    ax.axhline(0, color="gray", linewidth=0.8)
    ax.axvline(0, color="gray", linewidth=0.8)
    ax.grid(True, linestyle=":", alpha=0.6)
    ax.set_aspect("equal", adjustable="box")
    ax.set_xlim(-1, 6)
    ax.set_ylim(-6, 6)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend(loc="upper right")
    ax.set_title("Refleksi segitiga terhadap sumbu-X")

    st.pyplot(fig)

    # =========================================================
    # 19. SIFAT-SIFAT TRANSFORMASI
    # =========================================================

    st.header("🔍 Sifat Transformasi")

    st.markdown(r"""
    Beberapa transformasi mempertahankan bentuk dan ukuran bangun.

    **Isometri** meliputi:

    - Translasi.
    - Refleksi.
    - Rotasi.

    Transformasi tersebut mempertahankan:

    - panjang sisi,
    - besar sudut,
    - bentuk bangun.

    Dilatasi mempertahankan bentuk dan besar sudut, tetapi dapat mengubah
    ukuran bangun.
    """)

    # =========================================================
    # 20. APLIKASI
    # =========================================================

    st.header("🌍 Penerapan Transformasi Geometri")

    st.markdown(r"""
    Transformasi geometri digunakan dalam berbagai bidang:

    - Grafika komputer.
    - Desain dan animasi.
    - Pengolahan citra.
    - Arsitektur.
    - Robotika.
    - Computer vision.
    - Sistem informasi geografis.
    - Pemodelan 3D.
    - Permainan digital.
    """)

    # =========================================================
    # 21. KASUS ROBOTIKA
    # =========================================================

    st.header("🤖 Studi Kasus: Robotika")

    st.markdown(r"""
    Dalam robotika, posisi suatu objek dapat dinyatakan menggunakan
    koordinat. Perubahan posisi atau orientasi objek dapat dimodelkan
    menggunakan transformasi geometri.

    Misalnya sebuah titik pada lengan robot:
    """)

    st.latex(r"P=\begin{pmatrix}2\\3\end{pmatrix}")

    st.markdown(r"Jika titik tersebut diputar $90^\circ$ berlawanan arah jarum jam:")

    st.latex(r"P'=R_{90}\,P")
    st.latex(r"P'=\begin{pmatrix}-3\\2\end{pmatrix}")

    st.info(r"""
    Konsep transformasi seperti ini menjadi dasar dalam pemodelan posisi
    objek pada robotika dan grafika komputer.
    """)

    # =========================================================
    # 22. LATIHAN
    # =========================================================

    st.header("📝 Latihan")

    st.markdown(r"""
    **Soal 1**

    Titik $P(3,4)$ ditranslasikan oleh $T(2,-1)$.
    Tentukan koordinat bayangannya.
    """)

    st.markdown(r"""
    **Soal 2**

    Titik $A(5,-2)$ direfleksikan terhadap sumbu-X.
    Tentukan koordinat bayangannya.
    """)

    st.markdown(r"""
    **Soal 3**

    Titik $B(2,3)$ diputar $90^\circ$ berlawanan arah jarum jam terhadap
    titik asal. Tentukan koordinat bayangannya.
    """)

    st.markdown(r"""
    **Soal 4**

    Titik $C(3,4)$ didilatasi terhadap titik asal dengan faktor skala $2$.
    Tentukan koordinat bayangannya.
    """)

    st.markdown(r"""
    **Soal 5**

    Titik $P(2,1)$ ditranslasikan oleh $T(3,2)$ kemudian direfleksikan
    terhadap sumbu-X. Tentukan koordinat akhirnya.
    """)

    # =========================================================
    # 23. KUIS
    # =========================================================

    st.header("🎯 Kuis")

    jawaban = st.radio(
        "Titik P(2,3) diputar 90° berlawanan arah jarum jam terhadap O. "
        "Koordinat bayangannya adalah:",
        [
            "(3, −2)",
            "(−3, 2)",
            "(−2, −3)",
            "(2, −3)"
        ],
        key="quiz_transformasi_geometri"
    )

    if st.button("Periksa Jawaban", key="cek_quiz_transformasi_geometri"):
        if jawaban == "(−3, 2)":
            st.success(
                "✅ Benar. Rotasi 90° berlawanan arah jarum jam mengikuti "
                "aturan (x,y) → (−y, x)."
            )
        else:
            st.error("❌ Belum tepat. Gunakan aturan (x,y) → (−y, x).")

    # =========================================================
    # 24. REFLEKSI
    # =========================================================

    st.header("💭 Refleksi")

    st.markdown(r"""
    Setelah mempelajari transformasi geometri, coba jelaskan:

    1. Apa perbedaan translasi dan refleksi?
    2. Bagaimana menentukan bayangan titik setelah rotasi?
    3. Apa fungsi faktor skala pada dilatasi?
    4. Mengapa urutan komposisi transformasi dapat memengaruhi hasil?
    5. Bagaimana matriks dapat digunakan untuk merepresentasikan transformasi?
    6. Di mana transformasi geometri digunakan dalam kehidupan nyata?
    """)

    # =========================================================
    # 25. RANGKUMAN
    # =========================================================

    st.header("📌 Rangkuman")

    st.markdown(r"""
    **Transformasi geometri** merupakan pemetaan titik atau bangun ke posisi
    baru pada bidang.

    Konsep utama:

    - Translasi merupakan pergeseran.
    - Refleksi merupakan pencerminan.
    - Rotasi merupakan perputaran.
    - Dilatasi merupakan perubahan ukuran.
    - Translasi, refleksi, dan rotasi mempertahankan panjang dan bentuk.
    - Dilatasi mempertahankan bentuk tetapi mengubah ukuran.
    - Transformasi dapat direpresentasikan menggunakan matriks.
    - Beberapa transformasi dapat dikombinasikan menjadi komposisi.
    - Transformasi geometri banyak digunakan dalam grafika komputer,
      robotika, pengolahan citra, dan pemodelan matematika.
    """)

    st.success("🎉 Materi Transformasi Geometri selesai dipelajari.")
    

def matriks():
    st.markdown('<div class="content-title">📕 Matriks</div>', unsafe_allow_html=True)

    # =========================================================
    # TUJUAN PEMBELAJARAN
    # =========================================================

    st.header("🎯 Tujuan Pembelajaran")

    st.markdown("""
    Setelah mempelajari materi ini, siswa diharapkan mampu:

    - Menjelaskan pengertian dan notasi matriks.
    - Menentukan ordo, elemen, baris, dan kolom matriks.
    - Menentukan kesamaan dua matriks.
    - Melakukan operasi penjumlahan dan pengurangan matriks.
    - Melakukan perkalian matriks dengan skalar.
    - Melakukan perkalian dua matriks.
    - Menentukan transpose matriks.
    - Menentukan determinan matriks.
    - Menentukan invers matriks.
    - Menggunakan matriks untuk menyelesaikan sistem persamaan linear.
    - Menerapkan matriks dalam masalah kontekstual.
    """)

    # =========================================================
    # APERSEPSI
    # =========================================================

    st.header("💡 Apersepsi")

    st.markdown("""
    Dalam kehidupan sehari-hari kita sering menemukan data yang tersusun
    dalam bentuk baris dan kolom, misalnya data nilai siswa, harga barang,
    jumlah produksi, dan data penjualan.

    Data tersebut dapat disajikan secara sistematis menggunakan **matriks**.
    """)

    st.latex(r"A=\begin{pmatrix}2&4&6\\1&3&5\\7&8&9\end{pmatrix}")

    st.markdown("""
    Matriks memungkinkan data tersebut diolah menggunakan operasi matematika.
    """)

    # =========================================================
    # 1. PENGERTIAN MATRIKS
    # =========================================================

    st.header("1️⃣ Pengertian Matriks")

    st.markdown("""
    **Matriks** adalah susunan bilangan atau elemen yang disusun dalam
    baris dan kolom serta ditulis dalam tanda kurung.
    """)

    st.latex(r"A=\begin{pmatrix}a_{11}&a_{12}\\a_{21}&a_{22}\end{pmatrix}")

    st.markdown("""
    Elemen $a_{ij}$ menunjukkan elemen pada:

    - baris ke-$i$
    - kolom ke-$j$
    """)

    # =========================================================
    # 2. ORDO MATRIKS
    # =========================================================

    st.header("2️⃣ Ordo Matriks")

    st.markdown(r"""
    Ordo matriks menunjukkan banyaknya baris dan kolom.

    Jika matriks memiliki $m$ baris dan $n$ kolom, maka ordonya adalah
    $m \times n$.
    """)

    st.latex(r"A=\begin{pmatrix}2&4&6\\1&3&5\end{pmatrix}")

    st.markdown(r"""
    Matriks tersebut mempunyai:

    - 2 baris
    - 3 kolom
    - Ordo $2\times3$
    """)

    # =========================================================
    # 3. EKSPLORASI ORDO
    # =========================================================

    st.header("🔎 Eksplorasi Ordo Matriks")

    baris = st.number_input(
        "Jumlah baris",
        min_value=1,
        max_value=6,
        value=2,
        step=1,
        key="mat_baris"
    )

    kolom = st.number_input(
        "Jumlah kolom",
        min_value=1,
        max_value=6,
        value=3,
        step=1,
        key="mat_kolom"
    )

    data = np.arange(1, baris * kolom + 1).reshape(baris, kolom)

    df_matriks = pd.DataFrame(
        data,
        index=[f"Baris {i+1}" for i in range(baris)],
        columns=[f"Kolom {j+1}" for j in range(kolom)]
    )

    st.dataframe(df_matriks, use_container_width=True)

    st.info(f"Ordo matriks adalah {baris} × {kolom}.")

    # =========================================================
    # 4. JENIS-JENIS MATRIKS
    # =========================================================

    st.header("3️⃣ Jenis-Jenis Matriks")

    st.markdown("""
    Beberapa jenis matriks yang penting:

    - **Matriks baris** → hanya memiliki satu baris.
    - **Matriks kolom** → hanya memiliki satu kolom.
    - **Matriks persegi** → jumlah baris sama dengan jumlah kolom.
    - **Matriks nol** → semua elemennya nol.
    - **Matriks diagonal** → elemen di luar diagonal utama bernilai nol.
    - **Matriks identitas** → diagonal utama bernilai 1 dan elemen lainnya 0.
    """)

    st.latex(r"I_3=\begin{pmatrix}1&0&0\\0&1&0\\0&0&1\end{pmatrix}")

    # =========================================================
    # 5. KESAMAAN MATRIKS
    # =========================================================

    st.header("4️⃣ Kesamaan Dua Matriks")

    st.markdown("""
    Dua matriks dikatakan sama jika:

    1. Mempunyai ordo yang sama.
    2. Setiap elemen yang bersesuaian mempunyai nilai yang sama.
    """)

    st.latex(r"A=B\iff a_{ij}=b_{ij}")

    # =========================================================
    # 6. PENJUMLAHAN DAN PENGURANGAN
    # =========================================================

    st.header("5️⃣ Penjumlahan dan Pengurangan Matriks")

    st.markdown("""
    Dua matriks hanya dapat dijumlahkan atau dikurangkan jika mempunyai
    ordo yang sama.
    """)

    st.latex(r"A=\begin{pmatrix}1&2\\3&4\end{pmatrix}")

    st.latex(r"B=\begin{pmatrix}5&6\\7&8\end{pmatrix}")

    st.markdown("Maka:")

    st.latex(r"A+B=\begin{pmatrix}6&8\\10&12\end{pmatrix}")

    st.latex(r"A-B=\begin{pmatrix}-4&-4\\-4&-4\end{pmatrix}")

    # =========================================================
    # 7. PERKALIAN SKALAR
    # =========================================================

    st.header("6️⃣ Perkalian Matriks dengan Skalar")

    st.markdown("""
    Setiap elemen matriks dikalikan dengan bilangan skalar tersebut.
    """)

    st.latex(r"3A=3\begin{pmatrix}1&2\\3&4\end{pmatrix}")

    st.latex(r"3A=\begin{pmatrix}3&6\\9&12\end{pmatrix}")

    # =========================================================
    # 8. PERKALIAN MATRIKS
    # =========================================================

    st.header("7️⃣ Perkalian Dua Matriks")

    st.markdown(r"""
    Matriks $A$ berordo $m\times n$ dapat dikalikan dengan matriks $B$
    berordo $n\times p$.

    Hasil perkalian akan mempunyai ordo $m\times p$.
    """)

    st.latex(r"A_{m\times n}B_{n\times p}=C_{m\times p}")

    st.markdown("Contoh:")

    st.latex(r"A=\begin{pmatrix}1&2\\3&4\end{pmatrix}")

    st.latex(r"B=\begin{pmatrix}5&6\\7&8\end{pmatrix}")

    st.latex(r"AB=\begin{pmatrix}19&22\\43&50\end{pmatrix}")

    # =========================================================
    # 9. SIFAT PERKALIAN
    # =========================================================

    st.header("8️⃣ Sifat Perkalian Matriks")

    st.markdown("""
    Berbeda dengan perkalian bilangan biasa, pada umumnya perkalian matriks
    tidak bersifat komutatif.
    """)

    st.latex(r"AB\neq BA")

    st.markdown("""
    Namun, perkalian matriks tetap memenuhi sifat asosiatif:
    """)

    st.latex(r"(AB)C=A(BC)")

    # =========================================================
    # 10. TRANSPOSE
    # =========================================================

    st.header("9️⃣ Transpose Matriks")

    st.markdown("""
    Transpose matriks diperoleh dengan menukar baris menjadi kolom dan
    kolom menjadi baris.
    """)

    st.latex(r"A=\begin{pmatrix}1&2&3\\4&5&6\end{pmatrix}")

    st.latex(r"A^T=\begin{pmatrix}1&4\\2&5\\3&6\end{pmatrix}")

    st.markdown("Sifat penting:")

    st.latex(r"(A^T)^T=A")

    # =========================================================
    # 11. DETERMINAN
    # =========================================================

    st.header("🔟 Determinan Matriks")

    st.markdown(r"""
    Untuk matriks persegi berordo $2\times2$:
    """)

    st.latex(r"A=\begin{pmatrix}a&b\\c&d\end{pmatrix}")

    st.latex(r"\det(A)=ad-bc")

    st.markdown("Contoh:")

    st.latex(r"A=\begin{pmatrix}3&2\\1&4\end{pmatrix}")

    st.latex(r"\det(A)=(3)(4)-(2)(1)=10")

    # =========================================================
    # 12. KALKULATOR DETERMINAN
    # =========================================================

    st.header("🧮 Kalkulator Determinan")

    col1, col2 = st.columns(2)

    with col1:
        a11 = st.number_input("a₁₁", value=3.0, key="det_a11")
        a21 = st.number_input("a₂₁", value=1.0, key="det_a21")

    with col2:
        a12 = st.number_input("a₁₂", value=2.0, key="det_a12")
        a22 = st.number_input("a₂₂", value=4.0, key="det_a22")

    det = a11 * a22 - a12 * a21

    st.latex(
        rf"\det(A)=({a11:g})({a22:g})-({a12:g})({a21:g})={det:g}"
    )

    if det == 0:
        st.warning("Determinan = 0. Matriks tidak mempunyai invers.")
    else:
        st.success("Determinan ≠ 0. Matriks mempunyai invers.")

    # =========================================================
    # 13. INVERS
    # =========================================================

    st.header("1️⃣1️⃣ Invers Matriks")

    st.markdown(r"""
    Jika:

    $$A=\begin{pmatrix}a&b\\c&d\end{pmatrix}$$

    dan $\det(A)\neq0$, maka:
    """)

    st.latex(r"A^{-1}=\frac{1}{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}")

    st.markdown("Contoh:")

    st.latex(r"A=\begin{pmatrix}2&1\\1&1\end{pmatrix}")

    st.latex(r"\det(A)=1")

    st.latex(r"A^{-1}=\begin{pmatrix}1&-1\\-1&2\end{pmatrix}")

    # =========================================================
    # 14. VERIFIKASI INVERS
    # =========================================================

    st.header("🔍 Verifikasi Invers")

    st.markdown("""
    Suatu matriks $A^{-1}$ merupakan invers dari $A$ jika hasil perkaliannya
    dengan $A$ menghasilkan matriks identitas.
    """)

    st.latex(r"AA^{-1}=A^{-1}A=I")

    # =========================================================
    # 15. SPL DENGAN MATRIKS
    # =========================================================

    st.header("1️⃣2️⃣ Sistem Persamaan Linear")

    st.markdown("""
    Sistem persamaan linear dapat ditulis dalam bentuk matriks:
    """)

    st.latex(r"AX=B")

    st.markdown("""
    Misalnya:
    """)

    st.latex(r"2x+y=5")

    st.latex(r"x+y=3")

    st.markdown("Dapat ditulis sebagai:")

    st.latex(r"\begin{pmatrix}2&1\\1&1\end{pmatrix}\begin{pmatrix}x\\y\end{pmatrix}=\begin{pmatrix}5\\3\end{pmatrix}")

    st.markdown("Jika $A$ mempunyai invers, maka:")

    st.latex(r"X=A^{-1}B")

    # =========================================================
    # 16. KALKULATOR SPL
    # =========================================================

    st.header("🧮 Kalkulator SPL 2 Variabel")

    col1, col2 = st.columns(2)

    with col1:
        p = st.number_input("Koefisien x persamaan 1", value=2.0, key="spl_p")
        q = st.number_input("Koefisien y persamaan 1", value=1.0, key="spl_q")
        r = st.number_input("Konstanta persamaan 1", value=5.0, key="spl_r")

    with col2:
        s = st.number_input("Koefisien x persamaan 2", value=1.0, key="spl_s")
        t = st.number_input("Koefisien y persamaan 2", value=1.0, key="spl_t")
        u = st.number_input("Konstanta persamaan 2", value=3.0, key="spl_u")

    det_spl = p * t - q * s

    if det_spl != 0:

        x_sol = (r * t - q * u) / det_spl
        y_sol = (p * u - r * s) / det_spl

        st.success(
            f"Solusi: x = {x_sol:.4f}, y = {y_sol:.4f}"
        )

    else:
        st.warning(
            "Determinan = 0. Sistem tidak mempunyai solusi tunggal."
        )

    # =========================================================
    # 17. MATRIKS DAN TRANSFORMASI GEOMETRI
    # =========================================================

    st.header("1️⃣3️⃣ Matriks dalam Transformasi Geometri")

    st.markdown("""
    Matriks dapat digunakan untuk merepresentasikan transformasi titik
    pada bidang koordinat.
    """)

    st.markdown("Misalnya rotasi $90^\\circ$ berlawanan arah jarum jam:")

    st.latex(r"R=\begin{pmatrix}0&-1\\1&0\end{pmatrix}")

    st.markdown("Jika titik $P(x,y)$ ditulis sebagai vektor:")

    st.latex(r"P=\begin{pmatrix}x\\y\end{pmatrix}")

    st.markdown("Maka hasil rotasi diperoleh dari:")

    st.latex(r"P'=RP")

    # =========================================================
    # 18. EKSPLORASI TRANSFORMASI
    # =========================================================

    st.header("🔬 Eksplorasi Transformasi Matriks")

    x_p = st.number_input(
        "Koordinat x",
        value=2.0,
        key="transform_x"
    )

    y_p = st.number_input(
        "Koordinat y",
        value=1.0,
        key="transform_y"
    )

    transformasi = st.selectbox(
        "Pilih transformasi",
        [
            "Identitas",
            "Rotasi 90° berlawanan arah jarum jam",
            "Refleksi terhadap sumbu-X",
            "Refleksi terhadap sumbu-Y"
        ],
        key="transformasi_matriks"
    )

    if transformasi == "Identitas":
        xp = x_p
        yp = y_p

    elif transformasi == "Rotasi 90° berlawanan arah jarum jam":
        xp = -y_p
        yp = x_p

    elif transformasi == "Refleksi terhadap sumbu-X":
        xp = x_p
        yp = -y_p

    else:
        xp = -x_p
        yp = y_p

    st.success(
        f"Hasil transformasi: P'({xp:g}, {yp:g})"
    )

    # =========================================================
    # 19. APLIKASI KONTEKSTUAL
    # =========================================================

    st.header("🌍 Penerapan Matriks")

    st.markdown("""
    Matriks digunakan dalam berbagai bidang, antara lain:

    - Sistem persamaan linear.
    - Grafika komputer.
    - Transformasi gambar.
    - Pengolahan citra.
    - Statistik.
    - Ekonomi.
    - Teknik.
    - Pemodelan matematika.
    - Machine learning dan artificial intelligence.
    """)

    # =========================================================
    # 20. KASUS KONTEKSTUAL
    # =========================================================

    st.header("📊 Studi Kasus")

    st.markdown("""
    Sebuah toko menjual dua jenis produk, yaitu Produk A dan Produk B.

    Penjualan pada dua hari dicatat dalam matriks:
    """)

    st.latex(r"Q=\begin{pmatrix}20&15\\30&25\end{pmatrix}")

    st.markdown("""
    Baris menunjukkan hari dan kolom menunjukkan jenis produk.

    Jika harga produk adalah:
    """)

    st.latex(r"H=\begin{pmatrix}10000\\15000\end{pmatrix}")

    st.markdown("Maka total pendapatan setiap hari dapat dihitung dengan perkalian matriks:")

    st.latex(r"QH")

    st.markdown("""
    Dengan demikian, matriks dapat digunakan untuk mengolah data penjualan
    secara sistematis.
    """)

    # =========================================================
    # 21. LATIHAN
    # =========================================================

    st.header("📝 Latihan")

    st.markdown(r"""
    **Soal 1**

    Tentukan ordo matriks:

    $$A=\begin{pmatrix}1&2&3\\4&5&6\\7&8&9\end{pmatrix}$$
    """)

    st.markdown(r"""
    **Soal 2**

    Tentukan hasil:

    $$\begin{pmatrix}1&2\\3&4\end{pmatrix}+\begin{pmatrix}5&6\\7&8\end{pmatrix}$$
    """)

    st.markdown(r"""
    **Soal 3**

    Tentukan determinan:

    $$A=\begin{pmatrix}4&2\\3&5\end{pmatrix}$$
    """)

    st.markdown(r"""
    **Soal 4**

    Tentukan invers:

    $$A=\begin{pmatrix}2&1\\1&1\end{pmatrix}$$
    """)

    st.markdown(r"""
    **Soal 5**

    Tentukan solusi sistem:

    $$2x+y=5$$

    $$x+y=3$$
    """)

    # =========================================================
    # 22. KUIS
    # =========================================================

    st.header("🎯 Kuis")

    soal_matriks = st.radio(
        "Jika A = [[2,1],[1,1]], maka determinan A adalah:",
        [
            "0",
            "1",
            "2",
            "3"
        ],
        key="quiz_matriks"
    )

    if st.button(
        "Periksa Jawaban",
        key="cek_quiz_matriks"
    ):

        if soal_matriks == "1":
            st.success(
                "✅ Benar. det(A) = (2)(1) − (1)(1) = 1."
            )
        else:
            st.error(
                "❌ Belum tepat. Gunakan rumus det(A) = ad − bc."
            )

    # =========================================================
    # 23. REFLEKSI
    # =========================================================

    st.header("💭 Refleksi")

    st.markdown(r"""
    Setelah mempelajari matriks, coba jelaskan:

    1. Apa yang dimaksud dengan ordo matriks?
    2. Kapan dua matriks dapat dijumlahkan?
    3. Bagaimana menentukan hasil perkalian dua matriks?
    4. Apa fungsi transpose matriks?
    5. Bagaimana menentukan determinan matriks $2\times2$?
    6. Kapan sebuah matriks mempunyai invers?
    7. Bagaimana matriks digunakan untuk menyelesaikan SPL?
    8. Bagaimana matriks digunakan dalam transformasi geometri?
    """)

    # =========================================================
    # 24. RANGKUMAN
    # =========================================================

    st.header("📌 Rangkuman")

    st.markdown("""
    **Matriks** merupakan susunan elemen dalam baris dan kolom.

    Konsep penting:

    - Ordo matriks menunjukkan jumlah baris dan kolom.
    - Matriks dapat dijumlahkan jika memiliki ordo yang sama.
    - Perkalian matriks memiliki syarat kesesuaian dimensi.
    - Transpose menukar baris menjadi kolom.
    - Determinan digunakan untuk mengetahui sifat matriks persegi.
    - Matriks memiliki invers jika determinannya tidak sama dengan nol.
    - Matriks dapat digunakan untuk menyelesaikan sistem persamaan linear.
    - Matriks dapat digunakan untuk merepresentasikan transformasi geometri.
    - Matriks banyak digunakan dalam matematika, statistik, ekonomi, teknik,
      grafika komputer, dan machine learning.
    """)

    st.success("🎉 Materi Matriks selesai dipelajari.")




def polinomial():

    st.markdown('<div class="content-title">📕 Polinomial</div>', unsafe_allow_html=True)

    # =========================================================
    # TUJUAN PEMBELAJARAN
    # =========================================================

    st.header("🎯 Tujuan Pembelajaran")

    st.markdown("""
    Setelah mempelajari materi ini, mahasiswa/siswa diharapkan mampu:

    - Menjelaskan pengertian dan bentuk umum polinomial.
    - Menentukan derajat, koefisien, dan konstanta polinomial.
    - Melakukan operasi penjumlahan, pengurangan, dan perkalian polinomial.
    - Melakukan pembagian polinomial.
    - Menentukan nilai suatu polinomial.
    - Menggunakan Teorema Sisa dan Teorema Faktor.
    - Menentukan faktor dan akar polinomial.
    - Menentukan hubungan antara akar dan koefisien polinomial.
    - Menyelesaikan masalah kontekstual menggunakan polinomial.
    """)

    # =========================================================
    # APERSEPSI
    # =========================================================

    st.header("💡 Apersepsi")

    st.markdown("""
    Perhatikan fungsi:

    $$f(x)=2x^3-3x^2+4x-5$$

    Bentuk tersebut merupakan salah satu contoh polinomial.

    Polinomial banyak digunakan untuk memodelkan hubungan antara suatu
    variabel dengan variabel lainnya, termasuk dalam pemodelan matematika,
    ekonomi, fisika, teknik, dan ilmu komputer.
    """)

    # =========================================================
    # 1. PENGERTIAN
    # =========================================================

    st.header("1️⃣ Pengertian Polinomial")

    st.markdown("""
    **Polinomial** atau suku banyak adalah bentuk aljabar yang terdiri atas
    beberapa suku dengan pangkat variabel berupa bilangan cacah.

    Bentuk umum polinomial berderajat $n$ adalah:
    """)

    st.latex(r"P(x)=a_nx^n+a_{n-1}x^{n-1}+\cdots+a_2x^2+a_1x+a_0")

    st.markdown(dedent(r"""
    dengan:

    - $a_n, a_{n-1}, \ldots, a_1, a_0$ merupakan koefisien.
    - $a_n \neq 0$.
    - $n$ merupakan derajat polinomial.
    - $a_0$ merupakan konstanta.
    """))

    # =========================================================
    # 2. CONTOH MENENTUKAN KOMPONEN
    # =========================================================

    st.header("2️⃣ Derajat, Koefisien, dan Konstanta")

    st.markdown("Perhatikan polinomial berikut:")

    st.latex(r"P(x)=4x^5-3x^3+7x^2-2x+6")

    st.markdown("""
    Dari polinomial tersebut:

    - Derajat polinomial = $5$
    - Koefisien $x^5$ = $4$
    - Koefisien $x^3$ = $-3$
    - Koefisien $x^2$ = $7$
    - Koefisien $x$ = $-2$
    - Konstanta = $6$
    """)

    # =========================================================
    # 3. NILAI POLINOMIAL
    # =========================================================

    st.header("3️⃣ Nilai Polinomial")

    st.markdown("Untuk menentukan nilai polinomial, substitusikan nilai $x$ ke dalam polinomial.")

    st.latex(r"P(x)=2x^3-3x^2+x+5")

    st.markdown("Misalnya $x=2$:")

    st.latex(r"P(2)=2(2)^3-3(2)^2+2+5")

    st.latex(r"P(2)=16-12+2+5=11")

    # =========================================================
    # 4. OPERASI POLINOMIAL
    # =========================================================

    st.header("4️⃣ Operasi Polinomial")

    st.subheader("➕ Penjumlahan")

    st.markdown("""
    Penjumlahan dilakukan dengan menggabungkan suku-suku yang memiliki
    pangkat variabel sama.
    """)

    st.latex(r"(3x^2+2x+1)+(2x^2-5x+4)=5x^2-3x+5")

    st.subheader("➖ Pengurangan")

    st.latex(r"(4x^2+3x-2)-(x^2-2x+5)=3x^2+5x-7")

    st.subheader("✖️ Perkalian")

    st.latex(r"(x+2)(x+3)=x^2+5x+6")

    # =========================================================
    # 5. EKSPOLORASI OPERASI
    # =========================================================

    st.header("🔎 Eksplorasi Operasi Polinomial")

    col1, col2 = st.columns(2)

    with col1:
        a = st.number_input("Koefisien x² polinomial pertama", value=1.0)
        b = st.number_input("Koefisien x polinomial pertama", value=2.0)
        c = st.number_input("Konstanta polinomial pertama", value=1.0)

    with col2:
        d = st.number_input("Koefisien x² polinomial kedua", value=2.0)
        e = st.number_input("Koefisien x polinomial kedua", value=3.0)
        f = st.number_input("Konstanta polinomial kedua", value=2.0)

    operasi = st.selectbox(
        "Pilih operasi",
        ["Penjumlahan", "Pengurangan"]
    )

    if operasi == "Penjumlahan":
        hasil = f"{a+d:.2f}x² + {b+e:.2f}x + {c+f:.2f}"
    else:
        hasil = f"{a-d:.2f}x² + {b-e:.2f}x + {c-f:.2f}"

    st.success(f"Hasil: {hasil}")

    # =========================================================
    # 6. PEMBAGIAN POLINOMIAL
    # =========================================================

    st.header("5️⃣ Pembagian Polinomial")

    st.markdown("""
    Pembagian polinomial dapat dilakukan menggunakan pembagian bersusun
    maupun metode Horner/sintetik untuk pembagi berbentuk $(x-a)$.
    """)

    st.markdown("Contoh:")

    st.latex(r"\frac{x^3-6x^2+11x-6}{x-1}")

    st.markdown("Hasil pembagiannya adalah:")

    st.latex(r"x^2-5x+6")

    st.markdown("dengan sisa $0$.")

    # =========================================================
    # 7. TEOREMA SISA
    # =========================================================

    st.header("6️⃣ Teorema Sisa")

    st.markdown("""
    Jika polinomial $P(x)$ dibagi oleh $(x-a)$, maka sisanya adalah $P(a)$.
    """)

    st.latex(r"P(x)=(x-a)Q(x)+P(a)")

    st.markdown("Contoh:")

    st.latex(r"P(x)=x^3+2x^2-5x+3")

    st.markdown("Jika dibagi dengan $(x-2)$, maka sisanya:")

    st.latex(r"P(2)=2^3+2(2)^2-5(2)+3=9")

    st.info("Jadi, sisa pembagian adalah 9.")

    # =========================================================
    # 8. TEOREMA FAKTOR
    # =========================================================

    st.header("7️⃣ Teorema Faktor")

    st.markdown("""
    Jika $P(a)=0$, maka $(x-a)$ merupakan faktor dari $P(x)$.

    Sebaliknya, jika $(x-a)$ merupakan faktor dari $P(x)$, maka $P(a)=0$.
    """)

    st.latex(r"P(a)=0\iff(x-a)\text{ adalah faktor dari }P(x)")

    st.markdown("Contoh:")

    st.latex(r"P(x)=x^3-6x^2+11x-6")

    st.markdown("""
    Untuk $x=1$:
    """)

    st.latex(r"P(1)=1-6+11-6=0")

    st.success("Jadi, (x − 1) merupakan faktor dari P(x).")

    # =========================================================
    # 9. AKAR POLINOMIAL
    # =========================================================

    st.header("8️⃣ Akar-Akar Polinomial")

    st.markdown("""
    Akar polinomial adalah nilai $x$ yang menyebabkan nilai polinomial sama
    dengan nol.
    """)

    st.latex(r"P(x)=0")

    st.markdown("Contoh:")

    st.latex(r"x^3-6x^2+11x-6=0")

    st.markdown("Polinomial tersebut dapat difaktorkan menjadi:")

    st.latex(r"(x-1)(x-2)(x-3)=0")

    st.markdown("""
    Maka akar-akarnya adalah:

    - $x=1$
    - $x=2$
    - $x=3$
    """)

    # =========================================================
    # 10. EKSPLORASI AKAR POLINOMIAL
    # =========================================================

    st.header("🔬 Eksplorasi Akar Polinomial")

    st.markdown("""
    Masukkan koefisien polinomial kubik:

    $$P(x)=ax^3+bx^2+cx+d$$
    """)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        aa = st.number_input("a", value=1.0, key="poly_a")

    with col2:
        bb = st.number_input("b", value=-6.0, key="poly_b")

    with col3:
        cc = st.number_input("c", value=11.0, key="poly_c")

    with col4:
        dd = st.number_input("d", value=-6.0, key="poly_d")

    koef = [aa, bb, cc, dd]

    akar = np.roots(koef)

    df_akar = pd.DataFrame({
        "Akar": akar
    })

    st.dataframe(df_akar, use_container_width=True)

    # =========================================================
    # 11. VISUALISASI GRAFIK
    # =========================================================

    st.header("📈 Visualisasi Grafik Polinomial")

    x = np.linspace(-10, 10, 400)
    y = aa*x**3 + bb*x**2 + cc*x + dd

    df_grafik = pd.DataFrame({
        "x": x,
        "P(x)": y
    })

    st.line_chart(
        df_grafik.set_index("x")
    )

    st.markdown("""
    Titik ketika grafik memotong atau menyentuh sumbu-$x$ menunjukkan
    akar-akar real polinomial.
    """)

    # =========================================================
    # 12. HUBUNGAN AKAR DAN KOEFISIEN
    # =========================================================

    st.header("9️⃣ Hubungan Akar dan Koefisien")

    st.markdown("""
    Untuk polinomial kuadrat:
    """)

    st.latex(r"ax^2+bx+c=0")

    st.markdown("Jika akar-akarnya adalah $x_1$ dan $x_2$, maka:")

    st.latex(r"x_1+x_2=-\frac{b}{a}")

    st.latex(r"x_1x_2=\frac{c}{a}")

    st.markdown("""
    Untuk polinomial kubik:
    """)

    st.latex(r"ax^3+bx^2+cx+d=0")

    st.markdown("Jika akar-akarnya adalah $x_1,x_2,x_3$, maka:")

    st.latex(r"x_1+x_2+x_3=-\frac{b}{a}")

    st.latex(r"x_1x_2+x_1x_3+x_2x_3=\frac{c}{a}")

    st.latex(r"x_1x_2x_3=-\frac{d}{a}")

    # =========================================================
    # 13. POLINOMIAL DENGAN KOEFISIEN TERTENTU
    # =========================================================

    st.header("🔢 Menentukan Koefisien Polinomial")

    st.markdown("""
    Misalkan diketahui polinomial:

    $$P(x)=x^3+ax^2+bx+6$$

    dan diketahui salah satu akarnya adalah $x=1$.
    """)

    st.markdown("Karena $x=1$ merupakan akar, maka:")

    st.latex(r"P(1)=0")

    st.latex(r"1+a+b+6=0")

    st.markdown("""
    Sehingga diperoleh hubungan:

    $$a+b=-7$$

    Untuk menentukan $a$ dan $b$ secara unik diperlukan informasi tambahan.
    """)

    # =========================================================
    # 14. PEMODELAN POLINOMIAL
    # =========================================================

    st.header("🔧 Pemodelan dengan Polinomial")

    st.markdown("""
    Polinomial dapat digunakan untuk memodelkan hubungan antara dua
    variabel. Misalnya hubungan antara waktu dan jarak, ukuran dan biaya,
    atau posisi dan waktu.
    """)

    st.markdown("Contoh model:")

    st.latex(r"s(t)=2t^2+3t+5")

    st.markdown("""
    dengan:

    - $t$ = waktu
    - $s(t)$ = posisi

    Untuk $t=4$:
    """)

    st.latex(r"s(4)=2(4)^2+3(4)+5=49")

    # =========================================================
    # 15. KALKULATOR NILAI POLINOMIAL
    # =========================================================

    st.header("🧮 Kalkulator Nilai Polinomial")

    st.markdown("Gunakan bentuk polinomial kubik:")

    st.latex(r"P(x)=ax^3+bx^2+cx+d")

    nilai_x = st.number_input(
        "Masukkan nilai x",
        value=2.0,
        key="nilai_x_polynomial"
    )

    hasil_nilai = (
        aa * nilai_x**3
        + bb * nilai_x**2
        + cc * nilai_x
        + dd
    )

    st.success(
        f"P({nilai_x:g}) = {hasil_nilai:g}"
    )

    # =========================================================
    # 16. PEMBAGIAN SINTETIK / HORNER
    # =========================================================

    st.header("🧠 Metode Horner")

    st.markdown("""
    Metode Horner dapat digunakan untuk menghitung nilai polinomial secara
    lebih efisien dan juga membantu proses pembagian oleh bentuk $(x-a)$.
    """)

    st.markdown("Untuk:")

    st.latex(r"P(x)=2x^3-3x^2+4x-5")

    st.markdown("nilai $P(2)$ dapat dihitung dengan bentuk Horner:")

    st.latex(r"P(2)=((2(2)-3)(2)+4)(2)-5")

    st.latex(r"P(2)=7")

    # =========================================================
    # 17. KASUS KONTEKSTUAL
    # =========================================================

    st.header("🌍 Penerapan Polinomial")

    st.markdown("""
    Sebuah model matematika menyatakan tinggi suatu benda terhadap waktu
    dengan fungsi:
    """)

    st.latex(r"h(t)=-5t^2+20t+2")

    st.markdown("""
    Model tersebut dapat digunakan untuk menentukan:

    - tinggi awal benda,
    - tinggi benda pada waktu tertentu,
    - waktu ketika benda mencapai ketinggian tertentu,
    - dan waktu ketika benda mencapai tanah.
    """)

    st.markdown("Tinggi awal benda:")

    st.latex(r"h(0)=2")

    st.markdown("Jadi, benda berada pada ketinggian 2 satuan ketika $t=0$.")

    # =========================================================
    # 18. LATIHAN
    # =========================================================

    st.header("📝 Latihan")

    st.markdown("""
    **Soal 1**

    Tentukan derajat polinomial:

    $$P(x)=5x^4-3x^2+7x-8$$
    """)

    st.markdown("""
    **Soal 2**

    Tentukan nilai:

    $$P(2)$$

    untuk:

    $$P(x)=x^3-2x^2+3x+1$$
    """)

    st.markdown("""
    **Soal 3**

    Tentukan sisa pembagian:

    $$P(x)=x^3-4x^2+5x-2$$

    oleh $(x-2)$.
    """)

    st.markdown("""
    **Soal 4**

    Tentukan apakah $(x-1)$ merupakan faktor dari:

    $$P(x)=x^3-3x^2+3x-1$$
    """)

    st.markdown("""
    **Soal 5**

    Tentukan akar-akar:

    $$x^3-6x^2+11x-6=0$$
    """)

    # =========================================================
    # 19. KUIS
    # =========================================================

    st.header("🎯 Kuis")

    soal = st.radio(
        "Jika P(x)=x²−5x+6, maka akar-akarnya adalah:",
        [
            "1 dan 6",
            "2 dan 3",
            "-2 dan -3",
            "3 dan 6"
        ],
        key="quiz_polinomial_1"
    )

    if st.button("Periksa Jawaban", key="cek_quiz_polinomial"):

        if soal == "2 dan 3":
            st.success("✅ Benar. Karena x²−5x+6=(x−2)(x−3).")
        else:
            st.error("❌ Belum tepat. Faktorkan x²−5x+6.")

    # =========================================================
    # 20. REFLEKSI
    # =========================================================

    st.header("💭 Refleksi")

    st.markdown("""
    Setelah mempelajari polinomial, coba jelaskan:

    1. Apa yang dimaksud dengan derajat polinomial?
    2. Bagaimana menentukan nilai polinomial?
    3. Apa hubungan Teorema Sisa dengan nilai $P(a)$?
    4. Bagaimana Teorema Faktor digunakan untuk menentukan faktor?
    5. Bagaimana akar polinomial berhubungan dengan grafik?
    6. Bagaimana polinomial dapat digunakan dalam pemodelan matematika?
    """)

    # =========================================================
    # 21. RANGKUMAN
    # =========================================================

    st.header("📌 Rangkuman")

    st.markdown("""
    **Polinomial** adalah bentuk aljabar yang terdiri atas suku-suku dengan
    pangkat variabel berupa bilangan cacah.

    Konsep penting:

    - Derajat polinomial ditentukan oleh pangkat tertinggi.
    - Nilai polinomial diperoleh dengan substitusi nilai variabel.
    - Polinomial dapat dijumlahkan, dikurangkan, dan dikalikan.
    - Pembagian polinomial dapat dilakukan dengan pembagian bersusun atau
      metode Horner/sintetik.
    - Teorema Sisa menyatakan bahwa sisa pembagian $P(x)$ oleh $(x-a)$ adalah
      $P(a)$.
    - Jika $P(a)=0$, maka $(x-a)$ merupakan faktor polinomial.
    - Akar polinomial merupakan nilai $x$ yang menyebabkan $P(x)=0$.
    - Akar polinomial dapat divisualisasikan melalui grafik.
    - Hubungan akar dan koefisien dapat digunakan untuk menentukan informasi
      tentang suatu polinomial.
    - Polinomial dapat digunakan sebagai model matematika dalam berbagai
      permasalahan.
    """)

    st.success("🎉 Materi Polinomial selesai dipelajari.")



def tampilkan(materi):
    if materi == "Polinomial":
        polinomial()

    elif materi == "Matriks":
        matriks()
        #pass

    elif materi == "Transformasi Geometri":
        transformasi_geometri()
        #pass

    elif materi == "Trigonometri":
        trigonometri()
        #pass

    elif materi == "Pemodelan Fungsi":
        pemodelan_fungsi()
        #pass

    elif materi == "Vektor":
        #vektor()
        pass

    elif materi == "Irisan Kerucut": # (lingkaran & elips)":
        irisan_kerucut()
        #pass

    elif materi == "Distribusi peluang (binom & normal)":
        #distribusi_peluang()
        pass

    elif materi == "Limit Fungsi (Tambahan)":
        #limit_fungsi()
        pass

    elif materi == "Turunan & Penerapannya (Tambahan)":
        #turunan()
        pass

    elif materi == "Integral (Tambahan)":
        #integral()
        pass
