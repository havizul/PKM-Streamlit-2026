import streamlit as st
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

from textwrap import dedent


def integral():
    st.markdown(
        '<div class="content-title">📕 Integral dan Penerapannya</div>',
        unsafe_allow_html=True
    )

    # =========================================================
    # TUJUAN PEMBELAJARAN
    # =========================================================

    st.header("🎯 Tujuan Pembelajaran")
    st.markdown(r"""
    Setelah mempelajari materi ini, siswa diharapkan mampu:

    - Menjelaskan konsep integral sebagai antiturunan.
    - Menentukan integral tak tentu fungsi aljabar.
    - Menggunakan aturan dasar integral.
    - Menentukan integral fungsi polinomial.
    - Menentukan integral fungsi eksponensial dan trigonometri sederhana.
    - Menentukan integral tentu.
    - Memahami hubungan integral dan turunan.
    - Menggunakan Teorema Dasar Kalkulus.
    - Menentukan luas daerah menggunakan integral.
    - Menggunakan integral untuk menentukan volume benda putar.
    - Menerapkan integral dalam masalah kontekstual.
    """)

    # =========================================================
    # APERSEPSI
    # =========================================================

    st.header("💡 Apersepsi")
    st.markdown(r"""
    Kita telah mempelajari turunan sebagai alat untuk menentukan **laju
    perubahan**.

    Sekarang kita membalik proses tersebut.

    Jika diketahui laju perubahan suatu besaran, bagaimana kita dapat
    memperoleh fungsi asalnya?

    Proses tersebut berkaitan dengan **integral**.
    """)

    # =========================================================
    # 1. PENGERTIAN INTEGRAL
    # =========================================================

    st.header("1. Pengertian Integral")
    st.markdown(r"""
    Integral dapat dipahami sebagai proses mencari antiturunan suatu
    fungsi.
    """)

    st.latex(r"\int f(x)\,dx=F(x)+C")

    st.markdown(r"""
    Jika $F'(x)=f(x)$, maka $F(x)$ disebut antiturunan dari $f(x)$.

    Konstanta $C$ diperlukan karena turunan dari konstanta adalah nol.
    """)

    # =========================================================
    # 2. HUBUNGAN INTEGRAL DAN TURUNAN
    # =========================================================

    st.header("2. Hubungan Integral dan Turunan")
    st.markdown("Integral dan turunan memiliki hubungan yang sangat erat.")

    st.latex(r"\frac{d}{dx}\left(\int f(x)\,dx\right)=f(x)")

    st.markdown(r"Sebaliknya, jika $F'(x)=f(x)$ maka:")

    st.latex(r"\int f(x)\,dx=F(x)+C")

    st.info(r"""
    **Inti konsep:**

    Turunan → mencari laju perubahan.

    Integral → mengembalikan fungsi dari laju perubahan tersebut.
    """)

    # =========================================================
    # 3. ATURAN PANGKAT
    # =========================================================

    st.header("3. Aturan Pangkat")
    st.markdown(r"Untuk $n\neq-1$, aturan dasar integral pangkat adalah:")

    st.latex(r"\int x^n\,dx=\frac{x^{n+1}}{n+1}+C")

    st.markdown("Contoh:")
    st.latex(r"\int x^3\,dx=\frac{x^4}{4}+C")

    # =========================================================
    # 4. INTEGRAL KONSTANTA
    # =========================================================

    st.header("4. Integral Konstanta")

    st.latex(r"\int c\,dx=cx+C")

    st.markdown("Contoh:")
    st.latex(r"\int 5\,dx=5x+C")

    # =========================================================
    # 5. INTEGRAL PENJUMLAHAN DAN PENGURANGAN
    # =========================================================

    st.header("5. Integral Penjumlahan dan Pengurangan")

    st.latex(r"\int[f(x)+g(x)]\,dx=\int f(x)\,dx+\int g(x)\,dx")
    st.latex(r"\int[f(x)-g(x)]\,dx=\int f(x)\,dx-\int g(x)\,dx")

    st.markdown("Contoh:")
    st.latex(r"\int(3x^2+4x-5)\,dx")
    st.latex(r"x^3+2x^2-5x+C")

    # =========================================================
    # 6. INTEGRAL DENGAN KONSTANTA PENGALI
    # =========================================================

    st.header("6. Integral dengan Konstanta Pengali")

    st.latex(r"\int c\,f(x)\,dx=c\int f(x)\,dx")

    st.markdown("Contoh:")
    st.latex(r"\int 6x^2\,dx=2x^3+C")

    # =========================================================
    # 7. INTEGRAL FUNGSI POLINOMIAL
    # =========================================================

    st.header("7. Integral Fungsi Polinomial")
    st.markdown(r"""
    Setiap suku pada polinomial dapat diintegralkan secara terpisah.
    """)

    st.latex(r"\int(4x^3-6x^2+2x-7)\,dx")
    st.latex(r"x^4-2x^3+x^2-7x+C")

    # =========================================================
    # 8. KALKULATOR INTEGRAL POLINOMIAL
    # =========================================================

    st.header("8. Kalkulator Integral Polinomial")

    col1, col2 = st.columns(2)

    with col1:
        koef_i3 = st.number_input(
            "Koefisien x³", value=2.0, key="integral_x3"
        )
        koef_i2 = st.number_input(
            "Koefisien x²", value=3.0, key="integral_x2"
        )

    with col2:
        koef_i = st.number_input(
            "Koefisien x", value=4.0, key="integral_x"
        )
        konstanta_i = st.number_input(
            "Konstanta", value=5.0, key="integral_const"
        )

    def format_polinomial(c3, c2, c1, c0):
        """Format polinomial dengan tanda yang rapi."""
        parts = []
        if c3 != 0:
            parts.append(f"{c3:g}x^3")
        if c2 != 0:
            sign = "+" if (c2 > 0 and parts) else ""
            parts.append(f"{sign}{c2:g}x^2")
        if c1 != 0:
            sign = "+" if (c1 > 0 and parts) else ""
            parts.append(f"{sign}{c1:g}x")
        if c0 != 0:
            sign = "+" if (c0 > 0 and parts) else ""
            parts.append(f"{sign}{c0:g}")
        return "".join(parts) if parts else "0"

    st.markdown("Fungsi yang dimasukkan:")
    st.latex(
        rf"f(x)={format_polinomial(koef_i3, koef_i2, koef_i, konstanta_i)}"
    )

    st.markdown("Integral tak tentunya:")
    st.latex(
        rf"\int f(x)\,dx = "
        rf"{koef_i3/4:g}x^4 + {koef_i2/3:g}x^3 + "
        rf"{koef_i/2:g}x^2 + {konstanta_i:g}x + C"
    )

    # =========================================================
    # 9. INTEGRAL TENTU
    # =========================================================

    st.header("9. Integral Tentu")
    st.markdown("Integral tentu memiliki batas bawah dan batas atas.")

    st.latex(r"\int_a^b f(x)\,dx")

    st.markdown(r"""
    Berbeda dengan integral tak tentu, integral tentu menghasilkan suatu
    nilai tertentu.
    """)

    # =========================================================
    # 10. TEOREMA DASAR KALKULUS
    # =========================================================

    st.header("10. Teorema Dasar Kalkulus")
    st.markdown(r"Jika $F(x)$ merupakan antiturunan dari $f(x)$, maka:")

    st.latex(r"\int_a^b f(x)\,dx=F(b)-F(a)")

    st.markdown("Contoh:")
    st.latex(r"\int_0^2 x^2\,dx")
    st.latex(r"\left[\frac{x^3}{3}\right]_0^2")
    st.latex(r"\frac{8}{3}")

    st.info("Jadi, nilai integral tentu adalah $8/3$.")

    # =========================================================
    # 11. VISUALISASI INTEGRAL TENTU
    # =========================================================

    st.header("11. Visualisasi Integral Tentu")
    st.markdown(r"""
    Integral tentu dapat diinterpretasikan sebagai **luas bertanda**
    di bawah kurva.
    """)

    x_vis = np.linspace(-0.5, 2.5, 400)
    y_vis = x_vis**2

    x_fill = np.linspace(0, 2, 200)
    y_fill = x_fill**2

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(x_vis, y_vis, "b-", label=r"$f(x)=x^2$")
    ax.fill_between(x_fill, y_fill, color="skyblue", alpha=0.5,
                    label=r"$\int_0^2 x^2\,dx = 8/3$")
    ax.axhline(0, color="gray", linewidth=0.6)
    ax.axvline(0, color="gray", linewidth=0.6)
    ax.grid(True, linestyle=":", alpha=0.6)
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.set_title(r"Luas di bawah $f(x)=x^2$ pada $[0,2]$")
    ax.legend()
    fig.tight_layout()
    st.pyplot(fig, use_container_width=True)

    # =========================================================
    # 12. SIFAT-SIFAT INTEGRAL TENTU
    # =========================================================

    st.header("12. Sifat-Sifat Integral Tentu")

    st.latex(r"\int_a^a f(x)\,dx=0")
    st.latex(r"\int_a^b f(x)\,dx=-\int_b^a f(x)\,dx")
    st.latex(
        r"\int_a^b[f(x)+g(x)]\,dx=\int_a^b f(x)\,dx+\int_a^b g(x)\,dx"
    )

    # =========================================================
    # 13. INTEGRAL FUNGSI EKSPONENSIAL
    # =========================================================

    st.header("13. Integral Fungsi Eksponensial")

    st.latex(r"\int e^x\,dx=e^x+C")

    st.markdown("Contoh:")
    st.latex(r"\int 3e^x\,dx=3e^x+C")

    st.markdown(r"Untuk bentuk $e^{u(x)}$:")

    st.latex(r"\int e^{u(x)}\,u'(x)\,dx=e^{u(x)}+C")

    # =========================================================
    # 14. INTEGRAL FUNGSI TRIGONOMETRI
    # =========================================================

    st.header("14. Integral Fungsi Trigonometri")

    st.latex(r"\int\cos x\,dx=\sin x+C")
    st.latex(r"\int\sin x\,dx=-\cos x+C")

    st.markdown("Contoh:")
    st.latex(r"\int(3\cos x-2\sin x)\,dx")
    st.latex(r"3\sin x+2\cos x+C")

    # =========================================================
    # 15. INTEGRAL SUBSTITUSI
    # =========================================================

    st.header("15. Integral Substitusi")
    st.markdown(r"""
    Metode substitusi digunakan ketika terdapat fungsi komposisi tertentu
    yang sesuai dengan turunan bagian dalamnya.
    """)

    st.markdown("Contoh:")
    st.latex(r"\int 2x(x^2+1)^3\,dx")

    st.markdown("Misalkan:")
    st.latex(r"u=x^2+1")
    st.latex(r"du=2x\,dx")

    st.markdown("Maka:")
    st.latex(r"\int u^3\,du")
    st.latex(r"\frac{u^4}{4}+C")

    st.markdown(r"Kembalikan ke variabel $x$:")
    st.latex(r"\frac{(x^2+1)^4}{4}+C")

    # =========================================================
    # 16. INTEGRAL PARSIAL
    # =========================================================

    st.header("16. Integral Parsial")
    st.markdown(r"""
    Integral parsial dapat digunakan untuk mengintegralkan hasil perkalian
    dua fungsi.
    """)

    st.latex(r"\int u\,dv=uv-\int v\,du")

    st.markdown("Contoh:")
    st.latex(r"\int x e^x\,dx")

    st.markdown("Ambil:")
    st.latex(r"u=x,\quad dv=e^x\,dx")
    st.latex(r"du=dx,\quad v=e^x")

    st.latex(r"\int x e^x\,dx=x e^x-\int e^x\,dx")
    st.latex(r"\int x e^x\,dx=x e^x-e^x+C")

    # =========================================================
    # 17. LUAS DAERAH DI BAWAH KURVA
    # =========================================================

    st.header("17. Luas Daerah di Bawah Kurva")
    st.markdown(r"""
    Jika fungsi bernilai tidak negatif pada interval $[a,b]$, luas daerah
    di bawah kurva dapat dihitung menggunakan:
    """)

    st.latex(r"A=\int_a^b f(x)\,dx")

    st.markdown("Contoh:")
    st.latex(r"f(x)=x")
    st.latex(r"A=\int_0^4 x\,dx")
    st.latex(r"A=8")

    st.info("Luas daerah di bawah garis $y=x$ dari $x=0$ sampai $x=4$ adalah $8$ satuan luas.")

    # =========================================================
    # 18. KALKULATOR LUAS
    # =========================================================

    st.header("18. Kalkulator Luas")

    batas_bawah_integral = st.number_input(
        "Batas bawah a", value=0.0, key="integral_lower"
    )
    batas_atas_integral = st.number_input(
        "Batas atas b", value=4.0, key="integral_upper"
    )

    if batas_bawah_integral < batas_atas_integral:
        luas_linear = (
            batas_atas_integral**2 / 2
            - batas_bawah_integral**2 / 2
        )

        st.latex(r"\int_a^b x\,dx=\frac{b^2-a^2}{2}")

        st.info(f"Nilai integral = {luas_linear:.4f}")
    else:
        st.warning("Batas atas harus lebih besar daripada batas bawah.")

    # =========================================================
    # 19. LUAS ANTARA DUA KURVA
    # =========================================================

    st.header("19. Luas Antara Dua Kurva")
    st.markdown(r"""
    Jika terdapat dua fungsi $f(x)$ dan $g(x)$ dengan $f(x)\geq g(x)$,
    luas daerah di antara kedua kurva adalah:
    """)

    st.latex(r"A=\int_a^b[f(x)-g(x)]\,dx")

    st.markdown("Contoh:")
    st.latex(r"f(x)=x+2")
    st.latex(r"g(x)=x")
    st.latex(r"A=\int_0^3[(x+2)-x]\,dx")
    st.latex(r"A=6")

    # =========================================================
    # 20. VOLUME BENDA PUTAR
    # =========================================================

    st.header("20. Volume Benda Putar")
    st.markdown(r"""
    Integral juga dapat digunakan untuk menentukan volume benda yang
    diperoleh dari pemutaran suatu daerah terhadap sumbu.

    **Metode cakram:**
    """)

    st.latex(r"V=\pi\int_a^b[f(x)]^2\,dx")

    st.markdown(r"""
    Rumus tersebut digunakan jika daerah diputar terhadap sumbu-$x$ dan
    fungsi berada di atas sumbu tersebut.
    """)

    st.markdown(r"""
    **Contoh:** Daerah di bawah kurva $y=x$ dari $x=0$ sampai $x=2$
    diputar terhadap sumbu-$x$.
    """)

    st.latex(r"V=\pi\int_0^2 x^2\,dx")
    st.latex(r"V=\frac{8\pi}{3}")

    st.info(r"Volume benda putar adalah $8\pi/3$ satuan volume.")

    # =========================================================
    # 21. HUBUNGAN INTEGRAL DENGAN LUAS
    # =========================================================

    st.header("21. Hubungan Integral dengan Luas")
    st.markdown(r"""
    Integral tentu tidak selalu menghasilkan luas geometris positif.
    Integral menghasilkan **luas bertanda**.

    Daerah di atas sumbu-$x$ memberikan kontribusi positif, sedangkan
    daerah di bawah sumbu-$x$ memberikan kontribusi negatif.
    """)

    st.latex(r"\int_a^b f(x)\,dx")

    # =========================================================
    # 22. INTEGRAL NUMERIK
    # =========================================================

    st.header("22. Integral Numerik")
    st.markdown(r"""
    Tidak semua integral mudah diselesaikan secara analitik.

    Salah satu pendekatan numerik adalah menggunakan metode trapesium.
    """)

    st.latex(
        r"\int_a^b f(x)\,dx \approx "
        r"\sum_{i=1}^{n} \frac{f(x_{i-1})+f(x_i)}{2}\,\Delta x"
    )

    jumlah_subinterval = st.slider(
        "Jumlah subinterval",
        min_value=2,
        max_value=100,
        value=10,
        key="integral_trapezoid_n"
    )

    a_num = st.number_input(
        "Batas bawah numerik", value=0.0, key="integral_num_a"
    )
    b_num = st.number_input(
        "Batas atas numerik", value=2.0, key="integral_num_b"
    )

    if a_num < b_num:
        x_num = np.linspace(a_num, b_num, jumlah_subinterval + 1)
        y_num = x_num**2

        try:
            nilai_trapesium = np.trapezoid(y_num, x_num)
        except AttributeError:
            nilai_trapesium = np.trapz(y_num, x_num)

        st.info(
            f"Pendekatan integral ∫x² dx = {nilai_trapesium:.6f} "
            f"(nilai eksak = {b_num**3/3 - a_num**3/3:.6f})"
        )
    else:
        st.warning("Batas atas harus lebih besar daripada batas bawah.")

    # =========================================================
    # 23. TEOREMA DASAR KALKULUS (BAGIAN 2)
    # =========================================================

    st.header("23. Teorema Dasar Kalkulus (Bagian 2)")
    st.markdown(r"""
    Teorema Dasar Kalkulus menghubungkan integral dan turunan.

    Jika:
    """)

    st.latex(r"F(x)=\int_a^x f(t)\,dt")

    st.markdown("maka:")

    st.latex(r"F'(x)=f(x)")

    st.info(r"""
    Konsep ini menunjukkan bahwa diferensiasi dan integrasi merupakan
    proses yang saling berkaitan.
    """)

    # =========================================================
    # 24. PENERAPAN INTEGRAL DALAM KEHIDUPAN
    # =========================================================

    st.header("24. Penerapan Integral dalam Kehidupan")
    st.markdown(r"""
    Integral dapat digunakan dalam berbagai bidang, antara lain:

    - menghitung jarak dari kecepatan,
    - menghitung perpindahan,
    - menghitung luas,
    - menghitung volume,
    - menghitung akumulasi,
    - analisis ekonomi,
    - fisika,
    - teknik,
    - pemodelan matematika.
    """)

    # =========================================================
    # 25. STUDI KASUS: JARAK DARI KECEPATAN
    # =========================================================

    st.header("🌍 Studi Kasus: Jarak dari Kecepatan")
    st.markdown("Misalkan kecepatan suatu benda adalah:")

    st.latex(r"v(t)=2t+3")

    st.markdown(r"Jarak yang ditempuh dari $t=0$ sampai $t=5$:")

    st.latex(r"s=\int_0^5(2t+3)\,dt")
    st.latex(r"s=[t^2+3t]_0^5")
    st.latex(r"s=40")

    st.info("Jarak yang ditempuh adalah $40$ satuan panjang.")

    # =========================================================
    # 26. VISUALISASI FUNGSI DAN LUAS
    # =========================================================

    st.header("26. Visualisasi Fungsi dan Luas")

    x_area = np.linspace(0, 4, 300)
    y_area = x_area  # f(x) = x

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(x_area, y_area, "b-", label=r"$f(x)=x$")
    ax.fill_between(x_area, y_area, color="skyblue", alpha=0.5,
                    label=r"$\int_0^4 x\,dx = 8$")
    ax.axhline(0, color="gray", linewidth=0.6)
    ax.axvline(0, color="gray", linewidth=0.6)
    ax.grid(True, linestyle=":", alpha=0.6)
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.set_title(r"Luas di bawah $f(x)=x$ pada $[0,4]$")
    ax.legend()
    fig.tight_layout()
    st.pyplot(fig, use_container_width=True)

    st.markdown(r"""
    Grafik tersebut menunjukkan fungsi $f(x)=x$. Integral pada interval
    tertentu memberikan luas bertanda di bawah grafik.
    """)

    # =========================================================
    # 27. PERBANDINGAN TURUNAN DAN INTEGRAL
    # =========================================================

    st.header("27. Perbandingan Turunan dan Integral")

    df_perbandingan_integral = pd.DataFrame({
        "Konsep": [
            "Turunan",
            "Integral tak tentu",
            "Integral tentu"
        ],
        "Makna": [
            "Laju perubahan",
            "Antiturunan",
            "Akumulasi atau luas bertanda"
        ],
        "Contoh penerapan": [
            "Kecepatan dan percepatan",
            "Mencari fungsi asal",
            "Luas dan volume"
        ]
    })

    st.dataframe(
        df_perbandingan_integral,
        use_container_width=True,
        hide_index=True
    )

    # =========================================================
    # 28. LATIHAN
    # =========================================================

    st.header("📝 Latihan")

    st.markdown(r"""
    **Soal 1** — Tentukan:
    """)
    st.latex(r"\int(3x^2+4x-5)\,dx")

    st.markdown(r"""
    **Soal 2** — Tentukan:
    """)
    st.latex(r"\int_0^2 x^2\,dx")

    st.markdown(r"""
    **Soal 3** — Tentukan:
    """)
    st.latex(r"\int 2x(x^2+1)^3\,dx")

    st.markdown(r"""
    **Soal 4** — Tentukan:
    """)
    st.latex(r"\int x e^x\,dx")

    st.markdown(r"""
    **Soal 5** — Tentukan luas daerah di bawah $y=x$ pada interval
    $[0,4]$.
    """)

    st.markdown(r"""
    **Soal 6** — Tentukan volume benda putar daerah di bawah $y=x$ dari
    $x=0$ sampai $x=2$ terhadap sumbu-$x$.
    """)

    st.markdown(r"""
    **Soal 7** — Jika kecepatan benda dinyatakan $v(t)=3t^2$, tentukan
    jarak yang ditempuh dari $t=0$ sampai $t=2$.
    """)

    # =========================================================
    # 29. KUIS
    # =========================================================

    st.header("🎯 Kuis")

    jawaban_integral = st.radio(
        "Hasil dari ∫ 2x dx adalah:",
        ["x + C", "x² + C", "2x² + C", "2x + C"],
        key="quiz_integral"
    )

    if st.button("Periksa Jawaban", key="cek_quiz_integral"):
        if jawaban_integral == "x² + C":
            st.success("✅ Benar. ∫2x dx = x² + C.")
        else:
            st.error("❌ Belum tepat. Gunakan aturan ∫xⁿ dx = xⁿ⁺¹/(n+1) + C.")

    # =========================================================
    # 30. REFLEKSI
    # =========================================================

    st.header("💭 Refleksi")
    st.markdown(r"""
    Setelah mempelajari integral, coba jelaskan:

    1. Apa yang dimaksud dengan integral?
    2. Apa hubungan antara integral dan turunan?
    3. Mengapa integral tak tentu memiliki konstanta $C$?
    4. Apa perbedaan integral tak tentu dan integral tentu?
    5. Apa makna geometris integral tentu?
    6. Kapan metode substitusi digunakan?
    7. Kapan integral parsial digunakan?
    8. Bagaimana integral digunakan untuk menghitung luas?
    9. Bagaimana integral digunakan untuk menghitung volume?
    10. Bagaimana integral dapat digunakan untuk menentukan jarak dari
        fungsi kecepatan?
    """)

    # =========================================================
    # 31. RANGKUMAN
    # =========================================================

    st.header("📌 Rangkuman")
    st.markdown(r"""
    **Integral** merupakan konsep yang berkaitan dengan antiturunan dan
    akumulasi.

    Konsep penting:

    - Integral tak tentu menghasilkan keluarga antiturunan.
    - Konstanta $C$ diperlukan pada integral tak tentu.
    - Integral tentu menghasilkan nilai tertentu.
    - Teorema Dasar Kalkulus menghubungkan integral dan turunan.
    - Integral tentu dapat digunakan untuk menghitung luas bertanda.
    - Integral dapat digunakan untuk menghitung luas antara dua kurva.
    - Integral dapat digunakan untuk menghitung volume benda putar.
    - Substitusi digunakan untuk integral fungsi komposisi tertentu.
    - Integral parsial digunakan antara lain untuk hasil kali fungsi.
    - Integral dapat digunakan untuk menghitung jarak dari fungsi
      kecepatan.
    - Integral merupakan konsep penting dalam matematika, fisika,
      teknik, ekonomi, dan pemodelan.
    """)

    st.success("🎉 Materi Integral selesai dipelajari.")


def turunan():
    st.markdown(
        '<div class="content-title">📕 Turunan dan Penerapannya</div>',
        unsafe_allow_html=True
    )

    # =========================================================
    # TUJUAN PEMBELAJARAN
    # =========================================================

    st.header("🎯 Tujuan Pembelajaran")
    st.markdown(r"""
    Setelah mempelajari materi ini, siswa diharapkan mampu:

    - Menjelaskan konsep turunan sebagai laju perubahan sesaat.
    - Menentukan turunan menggunakan definisi turunan.
    - Menggunakan aturan dasar turunan.
    - Menentukan turunan fungsi aljabar.
    - Menentukan turunan fungsi trigonometri sederhana.
    - Menggunakan aturan rantai.
    - Menentukan persamaan garis singgung.
    - Menentukan titik stasioner.
    - Menentukan interval fungsi naik dan turun.
    - Menentukan nilai maksimum dan minimum.
    - Menggunakan turunan untuk menyelesaikan masalah kontekstual.
    """)

    # =========================================================
    # APERSEPSI
    # =========================================================

    st.header("💡 Apersepsi")
    st.markdown(r"""
    Dalam kehidupan sehari-hari kita sering mempelajari perubahan suatu
    besaran terhadap besaran lainnya.

    Contohnya:

    - perubahan posisi terhadap waktu,
    - perubahan jarak terhadap waktu,
    - pertumbuhan populasi,
    - perubahan biaya terhadap jumlah produksi,
    - perubahan keuntungan terhadap jumlah barang.

    Turunan digunakan untuk mempelajari **laju perubahan suatu fungsi**.
    """)

    # =========================================================
    # 1. PENGERTIAN TURUNAN
    # =========================================================

    st.header("1. Pengertian Turunan")
    st.markdown(r"""
    Turunan fungsi menggambarkan laju perubahan sesaat suatu fungsi
    terhadap variabelnya.
    """)

    st.latex(r"f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}")

    st.markdown(r"""
    Notasi turunan dapat ditulis sebagai:

    - $f'(x)$
    - $y'$
    - $\frac{dy}{dx}$
    """)

    # =========================================================
    # 2. INTERPRETASI GEOMETRIS
    # =========================================================

    st.header("2. Interpretasi Geometris")
    st.markdown(r"""
    Secara geometris, turunan pada suatu titik menyatakan **gradien garis
    singgung** terhadap grafik fungsi pada titik tersebut.
    """)

    st.latex(r"m=f'(a)")

    st.info(r"""
    Semakin besar nilai turunan positif, grafik semakin meningkat secara
    tajam. Jika turunan bernilai negatif, grafik sedang menurun.
    """)

    # =========================================================
    # 3. TURUNAN MENGGUNAKAN DEFINISI
    # =========================================================

    st.header("3. Turunan Menggunakan Definisi")
    st.markdown("Misalkan:")

    st.latex(r"f(x)=x^2")

    st.markdown("Berdasarkan definisi turunan:")

    st.latex(r"f'(x)=\lim_{h\to0}\frac{(x+h)^2-x^2}{h}")
    st.latex(r"f'(x)=\lim_{h\to0}(2x+h)")
    st.latex(r"f'(x)=2x")

    st.info("Jadi, turunan dari $f(x)=x^2$ adalah $f'(x)=2x$.")

    # =========================================================
    # 4. ATURAN KONSTANTA
    # =========================================================

    st.header("4. Aturan Konstanta")
    st.markdown("Turunan dari suatu konstanta adalah nol.")

    st.latex(r"\frac{d}{dx}(c)=0")

    st.markdown("Contoh:")
    st.latex(r"\frac{d}{dx}(7)=0")

    # =========================================================
    # 5. ATURAN PANGKAT
    # =========================================================

    st.header("5. Aturan Pangkat")
    st.markdown(r"Untuk fungsi berbentuk $x^n$, berlaku aturan:")

    st.latex(r"\frac{d}{dx}(x^n)=nx^{n-1}")

    st.markdown("Contoh:")
    st.latex(r"\frac{d}{dx}(x^5)=5x^4")

    # =========================================================
    # 6. TURUNAN PENJUMLAHAN DAN PENGURANGAN
    # =========================================================

    st.header("6. Turunan Penjumlahan dan Pengurangan")

    st.latex(r"(f(x)+g(x))'=f'(x)+g'(x)")
    st.latex(r"(f(x)-g(x))'=f'(x)-g'(x)")

    st.markdown("Contoh:")
    st.latex(r"f(x)=3x^4+2x^2-5x+7")
    st.latex(r"f'(x)=12x^3+4x-5")

    # =========================================================
    # 7. ATURAN PERKALIAN KONSTANTA
    # =========================================================

    st.header("7. Aturan Perkalian Konstanta")

    st.latex(r"(cf(x))'=cf'(x)")

    st.markdown("Contoh:")
    st.latex(r"\frac{d}{dx}(5x^3)=15x^2")

    # =========================================================
    # 8. TURUNAN HASIL KALI
    # =========================================================

    st.header("8. Turunan Hasil Kali")
    st.markdown("Jika dua fungsi dikalikan, gunakan aturan hasil kali.")

    st.latex(r"(fg)'=f'g+fg'")

    st.markdown("Contoh:")
    st.latex(r"y=x^2(x+1)")
    st.latex(r"y'=2x(x+1)+x^2")
    st.latex(r"y'=3x^2+2x")

    # =========================================================
    # 9. TURUNAN HASIL BAGI
    # =========================================================

    st.header("9. Turunan Hasil Bagi")
    st.markdown("Jika suatu fungsi berbentuk hasil bagi dua fungsi:")

    st.latex(r"\left(\frac{f}{g}\right)'=\frac{f'g-fg'}{g^2}")

    st.markdown("Contoh:")
    st.latex(r"y=\frac{x^2+1}{x}")
    st.latex(r"y'=\frac{2x(x)-(x^2+1)}{x^2}")
    st.latex(r"y'=\frac{x^2-1}{x^2}")

    # =========================================================
    # 10. ATURAN RANTAI
    # =========================================================

    st.header("10. Aturan Rantai")
    st.markdown("Aturan rantai digunakan untuk fungsi komposisi.")

    st.latex(r"\frac{d}{dx}f(g(x))=f'(g(x))\,g'(x)")

    st.markdown("Contoh:")
    st.latex(r"y=(2x+1)^5")
    st.latex(r"y'=5(2x+1)^4(2)")
    st.latex(r"y'=10(2x+1)^4")

    # =========================================================
    # 11. TURUNAN FUNGSI TRIGONOMETRI
    # =========================================================

    st.header("11. Turunan Fungsi Trigonometri")

    st.latex(r"\frac{d}{dx}(\sin x)=\cos x")
    st.latex(r"\frac{d}{dx}(\cos x)=-\sin x")
    st.latex(r"\frac{d}{dx}(\tan x)=\sec^2 x")

    st.markdown("Contoh:")
    st.latex(r"f(x)=3\sin x+2\cos x")
    st.latex(r"f'(x)=3\cos x-2\sin x")

    # =========================================================
    # 12. KALKULATOR TURUNAN POLINOMIAL
    # =========================================================

    st.header("12. Kalkulator Turunan Polinomial")

    col1, col2 = st.columns(2)

    with col1:
        koef_x3 = st.number_input(
            "Koefisien x³", value=2.0, key="deriv_x3"
        )
        koef_x2 = st.number_input(
            "Koefisien x²", value=3.0, key="deriv_x2"
        )

    with col2:
        koef_x = st.number_input(
            "Koefisien x", value=4.0, key="deriv_x"
        )
        konstanta = st.number_input(
            "Konstanta", value=5.0, key="deriv_const"
        )

    def format_polinomial(c3, c2, c1, c0):
        """Format polinomial dengan tanda yang rapi."""
        parts = []
        if c3 != 0:
            parts.append(f"{c3:g}x^3")
        if c2 != 0:
            sign = "+" if c2 > 0 and parts else ""
            parts.append(f"{sign}{c2:g}x^2")
        if c1 != 0:
            sign = "+" if c1 > 0 and parts else ""
            parts.append(f"{sign}{c1:g}x")
        if c0 != 0:
            sign = "+" if c0 > 0 and parts else ""
            parts.append(f"{sign}{c0:g}")
        return "".join(parts) if parts else "0"

    st.markdown("Fungsi yang dimasukkan:")
    st.latex(rf"f(x)={format_polinomial(koef_x3, koef_x2, koef_x, konstanta)}")

    st.markdown("Turunannya:")
    st.latex(rf"f'(x)={format_polinomial(0, 3*koef_x3, 2*koef_x2, koef_x)}")

    # =========================================================
    # 13. VISUALISASI FUNGSI DAN TURUNAN (pakai input user)
    # =========================================================

    st.header("13. Visualisasi Fungsi dan Turunan")

    x_deriv = np.linspace(-5, 5, 400)

    f_deriv = (
        koef_x3 * x_deriv**3
        + koef_x2 * x_deriv**2
        + koef_x * x_deriv
        + konstanta
    )

    fp_deriv = (
        3 * koef_x3 * x_deriv**2
        + 2 * koef_x2 * x_deriv
        + koef_x
    )

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(x_deriv, f_deriv, "b-", label="f(x)")
    ax.plot(x_deriv, fp_deriv, "r--", label="f'(x)")
    ax.axhline(0, color="gray", linewidth=0.6)
    ax.axvline(0, color="gray", linewidth=0.6)
    ax.grid(True, linestyle=":", alpha=0.6)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Grafik f(x) dan turunannya")
    ax.legend()
    fig.tight_layout()
    st.pyplot(fig, use_container_width=True)

    st.markdown(r"""
    Grafik $f'(x)$ dapat membantu melihat bagaimana fungsi $f(x)$
    mengalami perubahan.
    """)

    # =========================================================
    # 14. TURUNAN KEDUA
    # =========================================================

    st.header("14. Turunan Kedua")
    st.markdown("Turunan dapat diturunkan kembali untuk memperoleh turunan kedua.")

    st.latex(r"f''(x)=\frac{d}{dx}f'(x)")

    st.markdown("Contoh:")
    st.latex(r"f(x)=x^3")
    st.latex(r"f'(x)=3x^2")
    st.latex(r"f''(x)=6x")

    # =========================================================
    # 15. GARIS SINGGUNG
    # =========================================================

    st.header("15. Garis Singgung")
    st.markdown(r"""
    Persamaan garis singgung grafik fungsi $f(x)$ pada titik $x=a$ dapat
    ditentukan menggunakan gradien $f'(a)$.
    """)

    st.latex(r"y-f(a)=f'(a)(x-a)")

    st.markdown(r"Contoh untuk $f(x)=x^2$ pada $x=2$:")

    st.latex(r"f(2)=4")
    st.latex(r"f'(2)=4")
    st.latex(r"y-4=4(x-2)")
    st.latex(r"y=4x-4")

    # =========================================================
    # 16. KALKULATOR GARIS SINGGUNG
    # =========================================================

    st.header("16. Kalkulator Garis Singgung")

    titik_a = st.number_input("Titik x = a", value=2.0, key="tangent_a")

    nilai_fa = titik_a**2
    nilai_fpa = 2 * titik_a

    st.latex(r"f(x)=x^2 \quad\Rightarrow\quad f'(x)=2x")

    st.info(
        f"Pada x = {titik_a:g}, diperoleh f(a) = {nilai_fa:g} "
        f"dan f'(a) = {nilai_fpa:g}."
    )

    st.latex(rf"y-{nilai_fa:g}={nilai_fpa:g}(x-{titik_a:g})")

    # =========================================================
    # 17. TITIK STASIONER
    # =========================================================

    st.header("17. Titik Stasioner")
    st.markdown(r"""
    Titik stasioner adalah titik pada grafik fungsi ketika turunan pertama
    sama dengan nol.
    """)

    st.latex(r"f'(x)=0")

    st.markdown(r"""
    Titik stasioner dapat berupa:

    - maksimum lokal,
    - minimum lokal,
    - atau titik stasioner lainnya.
    """)

    # =========================================================
    # 18. MENENTUKAN TITIK STASIONER
    # =========================================================

    st.header("18. Menentukan Titik Stasioner")
    st.markdown("Misalkan:")

    st.latex(r"f(x)=x^2-4x+3")
    st.latex(r"f'(x)=2x-4")

    st.markdown("Syarat titik stasioner:")
    st.latex(r"2x-4=0")
    st.latex(r"x=2")

    st.markdown("Nilai fungsi:")
    st.latex(r"f(2)=-1")

    st.info("Titik stasioner adalah $(2,-1)$.")

    # =========================================================
    # 19. FUNGSI NAIK DAN TURUN
    # =========================================================

    st.header("19. Fungsi Naik dan Turun")
    st.markdown(r"""
    Turunan dapat digunakan untuk menentukan interval fungsi naik dan
    turun.

    Secara umum:

    - Jika $f'(x)>0$, fungsi meningkat.
    - Jika $f'(x)<0$, fungsi menurun.
    - Jika $f'(x)=0$, terdapat titik kritis atau titik stasioner.
    """)

    # =========================================================
    # 20. EKSPLORASI FUNGSI NAIK DAN TURUN
    # =========================================================

    st.header("20. Eksplorasi Fungsi Naik dan Turun")

    x_explore = st.number_input(
        "Nilai x untuk fungsi f(x)=x²−4x+3",
        value=2.0,
        key="monotonic_x"
    )

    turunan_explore = 2 * x_explore - 4

    if turunan_explore > 0:
        st.success("f'(x) > 0 → fungsi sedang meningkat.")
    elif turunan_explore < 0:
        st.warning("f'(x) < 0 → fungsi sedang menurun.")
    else:
        st.info("f'(x) = 0 → titik stasioner.")

    # =========================================================
    # 21. MAKSIMUM DAN MINIMUM
    # =========================================================

    st.header("21. Maksimum dan Minimum")
    st.markdown(r"""
    Turunan dapat digunakan untuk menentukan nilai maksimum dan minimum
    suatu fungsi.

    Langkah umum:

    1. Tentukan $f'(x)$.
    2. Tentukan titik kritis dengan $f'(x)=0$.
    3. Analisis perubahan tanda turunan.
    4. Tentukan apakah titik tersebut maksimum atau minimum.
    """)

    st.markdown("Contoh:")

    st.latex(r"f(x)=x^2-4x+3")
    st.latex(r"f'(x)=2x-4")
    st.latex(r"2x-4=0 \Rightarrow x=2")
    st.latex(r"f(2)=-1")

    st.info(r"""
    Karena grafik berbentuk parabola terbuka ke atas, titik $(2,-1)$
    merupakan titik minimum.
    """)

    # =========================================================
    # 22. OPTIMASI FUNGSI KUADRAT
    # =========================================================

    st.header("22. Optimasi Fungsi Kuadrat")

    col1, col2, col3 = st.columns(3)

    with col1:
        a_opt = st.number_input("Koefisien a", value=1.0, key="opt_a")

    with col2:
        b_opt = st.number_input("Koefisien b", value=-4.0, key="opt_b")

    with col3:
        c_opt = st.number_input("Koefisien c", value=3.0, key="opt_c")

    if a_opt != 0:
        x_opt = -b_opt / (2 * a_opt)
        y_opt = a_opt * x_opt**2 + b_opt * x_opt + c_opt

        st.latex(rf"f(x)={a_opt:g}x^2+{b_opt:g}x+{c_opt:g}")

        st.info(
            f"Titik ekstrem berada pada x = {x_opt:.4f}, "
            f"dengan nilai f(x) = {y_opt:.4f}."
        )

        if a_opt > 0:
            st.info("Karena a > 0, titik ekstrem merupakan minimum.")
        else:
            st.info("Karena a < 0, titik ekstrem merupakan maksimum.")

        # Visualisasi (pakai input user!)
        x_opt_vis = np.linspace(x_opt - 10, x_opt + 10, 300)
        y_opt_vis = a_opt * x_opt_vis**2 + b_opt * x_opt_vis + c_opt

        fig, ax = plt.subplots(figsize=(8, 4))
        ax.plot(x_opt_vis, y_opt_vis, "g-")
        ax.plot(x_opt, y_opt, "ro", markersize=8,
                label=f"Ekstrem ({x_opt:.2f}, {y_opt:.2f})")
        ax.axhline(0, color="gray", linewidth=0.6)
        ax.axvline(0, color="gray", linewidth=0.6)
        ax.grid(True, linestyle=":", alpha=0.6)
        ax.set_xlabel("x")
        ax.set_ylabel("f(x)")
        ax.set_title(rf"$f(x) = {a_opt:g}x^2 + {b_opt:g}x + {c_opt:g}$")
        ax.legend()
        fig.tight_layout()
        st.pyplot(fig, use_container_width=True)

    else:
        st.warning("Koefisien a tidak boleh 0 untuk fungsi kuadrat.")

    # =========================================================
    # 23. PENERAPAN: KECEPATAN
    # =========================================================

    st.header("23. Penerapan Turunan: Kecepatan")
    st.markdown(r"""
    Jika posisi benda dinyatakan sebagai fungsi waktu $s(t)$, maka
    kecepatan sesaat merupakan turunan posisi terhadap waktu.
    """)

    st.latex(r"v(t)=s'(t)")

    st.markdown("Sedangkan percepatan merupakan turunan kecepatan terhadap waktu.")

    st.latex(r"a(t)=v'(t)=s''(t)")

    # =========================================================
    # 24. STUDI KASUS GERAK BENDA
    # =========================================================

    st.header("🌍 Studi Kasus: Gerak Benda")

    st.markdown("Posisi sebuah benda dinyatakan:")

    st.latex(r"s(t)=t^3-6t^2+9t")

    st.markdown("Kecepatan benda:")
    st.latex(r"v(t)=3t^2-12t+9")

    st.markdown("Percepatan benda:")
    st.latex(r"a(t)=6t-12")

    waktu = st.number_input(
        "Waktu t", min_value=0.0, value=2.0, key="motion_time"
    )

    posisi = waktu**3 - 6 * waktu**2 + 9 * waktu
    kecepatan = 3 * waktu**2 - 12 * waktu + 9
    percepatan = 6 * waktu - 12

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Posisi", f"{posisi:.4f}")

    with col2:
        st.metric("Kecepatan", f"{kecepatan:.4f}")

    with col3:
        st.metric("Percepatan", f"{percepatan:.4f}")

    # =========================================================
    # 25. PENERAPAN: OPTIMASI
    # =========================================================

    st.header("25. Penerapan Turunan: Optimasi")
    st.markdown(r"""
    Turunan banyak digunakan dalam masalah optimasi, misalnya:

    - menentukan luas maksimum,
    - menentukan volume maksimum,
    - memaksimalkan keuntungan,
    - meminimalkan biaya,
    - menentukan ukuran optimal suatu objek.
    """)

    st.markdown(r"""
    **Contoh:** Sebuah persegi panjang memiliki keliling 20 cm.

    Jika panjangnya $x$, maka lebarnya $10-x$.

    Luasnya:
    """)

    st.latex(r"A(x)=x(10-x)=10x-x^2")

    st.markdown("Turunan luas:")
    st.latex(r"A'(x)=10-2x")

    st.markdown("Untuk luas maksimum:")
    st.latex(r"10-2x=0 \Rightarrow x=5")

    st.info("Ukuran optimal adalah 5 cm × 5 cm.")

    # Visualisasi luas
    x_opt_vis = np.linspace(0, 10, 300)
    area_opt_vis = x_opt_vis * (10 - x_opt_vis)

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(x_opt_vis, area_opt_vis, "b-")
    ax.plot(5, 25, "ro", markersize=8, label="Maksimum (5, 25)")
    ax.axhline(0, color="gray", linewidth=0.6)
    ax.grid(True, linestyle=":", alpha=0.6)
    ax.set_xlabel("Panjang x (cm)")
    ax.set_ylabel("Luas A(x) (cm²)")
    ax.set_title(r"$A(x) = x(10-x)$")
    ax.legend()
    fig.tight_layout()
    st.pyplot(fig, use_container_width=True)

    # =========================================================
    # 26. TURUNAN FUNGSI EKSPONENSIAL
    # =========================================================

    st.header("26. Turunan Fungsi Eksponensial")

    st.latex(r"\frac{d}{dx}(e^x)=e^x")

    st.markdown(r"Untuk fungsi $e^{u(x)}$, digunakan aturan rantai.")

    st.latex(r"\frac{d}{dx}e^{u(x)}=e^{u(x)}\,u'(x)")

    st.markdown("Contoh:")
    st.latex(r"f(x)=e^{2x}")
    st.latex(r"f'(x)=2e^{2x}")

    # =========================================================
    # 27. TURUNAN FUNGSI LOGARITMA
    # =========================================================

    st.header("27. Turunan Fungsi Logaritma")

    st.latex(r"\frac{d}{dx}\ln x=\frac{1}{x}")

    st.markdown("Contoh:")
    st.latex(r"f(x)=\ln(x^2+1)")
    st.latex(r"f'(x)=\frac{2x}{x^2+1}")

    # =========================================================
    # 28. HUBUNGAN TURUNAN DAN GRAFIK
    # =========================================================

    st.header("28. Hubungan Turunan dan Grafik")
    st.markdown(r"""
    Turunan memberikan informasi penting mengenai bentuk grafik:

    - $f'(x)>0$ → grafik naik.
    - $f'(x)<0$ → grafik turun.
    - $f'(x)=0$ → kandidat titik stasioner.
    - $f''(x)>0$ → grafik cekung ke atas.
    - $f''(x)<0$ → grafik cekung ke bawah.
    """)

    # =========================================================
    # 29. LATIHAN
    # =========================================================

    st.header("📝 Latihan")

    st.markdown(r"""
    **Soal 1** — Tentukan turunan:
    """)
    st.latex(r"f(x)=3x^4-2x^3+5x-7")

    st.markdown(r"""
    **Soal 2** — Tentukan turunan:
    """)
    st.latex(r"f(x)=(2x+1)^4")

    st.markdown(r"""
    **Soal 3** — Tentukan turunan:
    """)
    st.latex(r"f(x)=x^2\sin x")

    st.markdown(r"""
    **Soal 4** — Tentukan persamaan garis singgung fungsi $f(x)=x^2$
    pada $x=3$.
    """)

    st.markdown(r"""
    **Soal 5** — Tentukan titik stasioner fungsi:
    """)
    st.latex(r"f(x)=x^2-6x+5")

    st.markdown(r"""
    **Soal 6** — Tentukan interval fungsi naik dan turun untuk:
    """)
    st.latex(r"f(x)=x^2-4x+3")

    st.markdown(r"""
    **Soal 7** — Sebuah benda memiliki posisi:
    """)
    st.latex(r"s(t)=t^3-3t^2+2t")
    st.markdown("Tentukan kecepatan dan percepatannya.")

    # =========================================================
    # 30. KUIS
    # =========================================================

    st.header("🎯 Kuis")

    jawaban_turunan = st.radio(
        "Turunan dari f(x)=x³ adalah:",
        ["x²", "2x²", "3x²", "3x"],
        key="quiz_turunan"
    )

    if st.button("Periksa Jawaban", key="cek_quiz_turunan"):
        if jawaban_turunan == "3x²":
            st.success("✅ Benar. Berdasarkan aturan pangkat, d(x³)/dx = 3x².")
        else:
            st.error("❌ Belum tepat. Gunakan aturan d(xⁿ)/dx = n·xⁿ⁻¹.")

   # =========================================================
    # 31. REFLEKSI
    # =========================================================

    st.header("💭 Refleksi")

    st.markdown(r"""
    Setelah mempelajari turunan, coba jelaskan:

    1. Apa makna turunan secara matematis?
    2. Apa makna turunan secara geometris?
    3. Apa hubungan turunan dengan gradien garis singgung?
    4. Kapan aturan rantai digunakan?
    5. Bagaimana turunan digunakan untuk menentukan fungsi naik dan turun?
    6. Bagaimana menentukan titik maksimum dan minimum?
    7. Apa hubungan turunan pertama dan turunan kedua?
    8. Bagaimana turunan digunakan untuk menentukan kecepatan dan percepatan?
    9. Mengapa turunan penting dalam masalah optimasi?
    """)

    # =========================================================
    # 32. RANGKUMAN
    # =========================================================

    st.header("📌 Rangkuman")

    st.markdown(r"""
    **Turunan** merupakan konsep matematika yang digunakan untuk
    menggambarkan laju perubahan suatu fungsi.

    Konsep penting:

    - Turunan dapat didefinisikan menggunakan limit.
    - Turunan secara geometris menyatakan gradien garis singgung.
    - Aturan pangkat digunakan untuk fungsi berbentuk $x^n$.
    - Aturan hasil kali digunakan untuk perkalian dua fungsi.
    - Aturan hasil bagi digunakan untuk pembagian dua fungsi.
    - Aturan rantai digunakan untuk fungsi komposisi.
    - Turunan kedua digunakan untuk menganalisis kecekungan grafik.
    - $f'(x)>0$ menunjukkan fungsi meningkat.
    - $f'(x)<0$ menunjukkan fungsi menurun.
    - $f'(x)=0$ digunakan untuk mencari titik kritis.
    - Turunan dapat digunakan untuk menentukan maksimum dan minimum.
    - Turunan digunakan dalam kecepatan dan percepatan.
    - Turunan merupakan alat penting dalam optimasi dan pemodelan.
    """)

    st.success("🎉 Materi Turunan dan Penerapannya selesai dipelajari.")
    
def limit_fungsi():
    st.markdown(
        '<div class="content-title">📕 Limit Fungsi</div>',
        unsafe_allow_html=True
    )

    # =========================================================
    # TUJUAN PEMBELAJARAN
    # =========================================================

    st.header("🎯 Tujuan Pembelajaran")
    st.markdown(r"""
    Setelah mempelajari materi ini, siswa diharapkan mampu:

    - Menjelaskan konsep limit fungsi.
    - Menentukan limit fungsi dengan substitusi langsung.
    - Menggunakan sifat-sifat limit.
    - Menyelesaikan limit bentuk tak tentu.
    - Menggunakan pemfaktoran untuk menentukan limit.
    - Menggunakan metode rasionalisasi.
    - Menentukan limit kiri dan limit kanan.
    - Menentukan limit fungsi di tak hingga.
    - Menggunakan limit fungsi trigonometri sederhana.
    - Menjelaskan hubungan limit dengan kekontinuan fungsi.
    - Menerapkan konsep limit dalam masalah kontekstual.
    """)

    # =========================================================
    # APERSEPSI
    # =========================================================

    st.header("💡 Apersepsi")
    st.markdown(r"""
    Bayangkan sebuah benda bergerak semakin mendekati suatu posisi tertentu.

    Kita dapat bertanya:

    **"Nilai apa yang didekati oleh fungsi ketika $x$ semakin mendekati
    suatu nilai tertentu?"**

    Konsep matematika yang digunakan untuk menjawab pertanyaan tersebut
    adalah **limit fungsi**.
    """)

    # =========================================================
    # 1. PENGERTIAN LIMIT
    # =========================================================

    st.header("1. Pengertian Limit")
    st.markdown(r"""
    Limit menggambarkan nilai yang didekati oleh suatu fungsi ketika
    variabel bebas mendekati suatu nilai tertentu.
    """)

    st.latex(r"\lim_{x\to a}f(x)=L")

    st.markdown(r"""
    Artinya, ketika $x$ semakin mendekati $a$, nilai $f(x)$ semakin
    mendekati $L$.
    """)

    # =========================================================
    # 2. INTERPRETASI GRAFIK
    # =========================================================

    st.header("2. Interpretasi Grafik")
    st.markdown(r"""
    Secara geometris, limit dapat dipahami dengan melihat perilaku grafik
    fungsi ketika $x$ bergerak mendekati suatu titik.

    Nilai fungsi pada titik tersebut bahkan dapat berbeda atau tidak
    terdefinisi, tetapi limit masih dapat ada.
    """)

    st.info(r"""
    **Ide utama:**

    Limit memperhatikan nilai yang **didekati**, bukan hanya nilai fungsi
    tepat pada titik tersebut.
    """)

    # =========================================================
    # 3. LIMIT DENGAN SUBSTITUSI LANGSUNG
    # =========================================================

    st.header("3. Limit dengan Substitusi Langsung")
    st.markdown(r"""
    Untuk fungsi yang kontinu pada $x=a$, limit dapat ditentukan dengan
    substitusi langsung.
    """)

    st.latex(r"\lim_{x\to a}f(x)=f(a)")

    st.markdown(r"""
    **Contoh:**

    Tentukan:
    """)

    st.latex(r"\lim_{x\to2}(x^2+3x+1)")

    st.markdown(r"""
    Dengan substitusi $x=2$:
    """)

    st.latex(r"2^2+3(2)+1=11")

    st.info("Jadi, nilai limit adalah 11.")

    # =========================================================
    # 4. SIFAT-SIFAT LIMIT
    # =========================================================

    st.header("4. Sifat-Sifat Limit")
    st.markdown(r"""
    Jika $\lim_{x\to a}f(x)=L$ dan $\lim_{x\to a}g(x)=M$, maka:
    """)

    st.latex(r"\lim_{x\to a}[f(x)+g(x)]=L+M")
    st.latex(r"\lim_{x\to a}[f(x)-g(x)]=L-M")
    st.latex(r"\lim_{x\to a}[f(x)g(x)]=LM")
    st.latex(r"\lim_{x\to a}\frac{f(x)}{g(x)}=\frac{L}{M},\quad M\neq0")

    # =========================================================
    # 5. LIMIT FUNGSI POLINOMIAL
    # =========================================================

    st.header("5. Limit Fungsi Polinomial")
    st.markdown(r"""
    Fungsi polinomial kontinu untuk semua bilangan real. Oleh karena itu,
    limit dapat ditentukan dengan substitusi langsung.
    """)

    st.latex(r"\lim_{x\to3}(2x^3-x^2+4x-5)")

    hasil_polinomial = 2 * 3**3 - 3**2 + 4 * 3 - 5
    st.info(f"Hasil = {hasil_polinomial}")

    # =========================================================
    # 6. BENTUK TAK TENTU
    # =========================================================

    st.header("6. Bentuk Tak Tentu")
    st.markdown(r"""
    Dalam beberapa kasus, substitusi langsung menghasilkan bentuk seperti:

    - $\frac{0}{0}$
    - $\frac{\infty}{\infty}$

    Bentuk tersebut disebut **bentuk tak tentu** dan belum merupakan
    jawaban akhir.
    """)

    st.latex(r"\frac{0}{0}")

    st.warning(
        "Bentuk 0/0 tidak berarti limitnya nol. "
        "Fungsi perlu dianalisis lebih lanjut."
    )

    # =========================================================
    # 7. LIMIT DENGAN PEMFAKTORAN
    # =========================================================

    st.header("7. Limit dengan Pemfaktoran")
    st.markdown(r"""
    Salah satu cara mengatasi bentuk $\frac{0}{0}$ adalah melakukan
    pemfaktoran.
    """)

    st.markdown("Contoh:")
    st.latex(r"\lim_{x\to2}\frac{x^2-4}{x-2}")

    st.markdown("Faktorkan pembilang:")

    st.latex(r"x^2-4=(x-2)(x+2)")

    st.markdown("Sehingga:")

    st.latex(r"\frac{x^2-4}{x-2}=x+2,\quad x\neq2")
    st.latex(r"\lim_{x\to2}(x+2)=4")

    st.info("Jadi, nilai limit adalah 4.")

    # =========================================================
    # 8. KALKULATOR LIMIT DENGAN PEMFAKTORAN
    # =========================================================

    st.header("8. Kalkulator Limit dengan Pemfaktoran")

    nilai_a = st.number_input(
        "Nilai a", value=2.0, key="limit_factor_a"
    )

    st.markdown("Untuk bentuk:")

    st.latex(r"\frac{x^2-a^2}{x-a}")

    hasil_factor = 2 * nilai_a

    st.info(f"Jika $x \\to {nilai_a:g}$, maka limit = {hasil_factor:g}")

    # =========================================================
    # 9. LIMIT DENGAN RASIONALISASI
    # =========================================================

    st.header("9. Limit dengan Rasionalisasi")
    st.markdown(r"""
    Rasionalisasi digunakan terutama pada limit yang mengandung bentuk
    akar dan menghasilkan $\frac{0}{0}$.
    """)

    st.markdown("Contoh:")
    st.latex(r"\lim_{x\to0}\frac{\sqrt{x+1}-1}{x}")

    st.markdown("Kalikan dengan bentuk sekawannya:")

    st.latex(
        r"\frac{\sqrt{x+1}-1}{x}\cdot\frac{\sqrt{x+1}+1}{\sqrt{x+1}+1}"
    )

    st.markdown("Maka:")

    st.latex(r"\frac{1}{\sqrt{x+1}+1}")
    st.latex(r"\lim_{x\to0}\frac{1}{\sqrt{x+1}+1}=\frac{1}{2}")

    st.info("Jadi, nilai limit adalah 1/2.")

    # =========================================================
    # 10. LIMIT KIRI DAN LIMIT KANAN
    # =========================================================

    st.header("10. Limit Kiri dan Limit Kanan")
    st.markdown(r"""
    Limit kiri adalah nilai yang didekati fungsi ketika $x$ mendekati $a$
    dari sebelah kiri.

    Limit kanan adalah nilai yang didekati fungsi ketika $x$ mendekati $a$
    dari sebelah kanan.
    """)

    st.latex(r"\lim_{x\to a^-}f(x)")
    st.latex(r"\lim_{x\to a^+}f(x)")

    st.markdown("Limit dua sisi ada jika limit kiri dan limit kanan sama.")

    st.latex(
        r"\lim_{x\to a}f(x)=L\iff"
        r"\lim_{x\to a^-}f(x)=\lim_{x\to a^+}f(x)=L"
    )

    # =========================================================
    # 11. CONTOH LIMIT SATU SISI
    # =========================================================

    st.header("11. Contoh Limit Satu Sisi")
    st.markdown("Perhatikan fungsi:")

    st.latex(
        r"f(x)=\begin{cases}x+1,&x<2\\x+3,&x\geq2\end{cases}"
    )

    st.markdown("Limit kiri:")
    st.latex(r"\lim_{x\to2^-}f(x)=3")

    st.markdown("Limit kanan:")
    st.latex(r"\lim_{x\to2^+}f(x)=5")

    st.error(
        "Karena limit kiri ≠ limit kanan, maka limit dua sisi tidak ada."
    )

    # =========================================================
    # 12. LIMIT DI TAK HINGGA
    # =========================================================

    st.header("12. Limit di Tak Hingga")
    st.markdown(r"""
    Limit di tak hingga digunakan untuk mempelajari perilaku fungsi
    ketika $x$ semakin besar atau semakin kecil tanpa batas.
    """)

    st.latex(r"\lim_{x\to\infty}f(x)")
    st.latex(r"\lim_{x\to-\infty}f(x)")

    # =========================================================
    # 13. LIMIT FUNGSI RASIONAL DI TAK HINGGA
    # =========================================================

    st.header("13. Limit Fungsi Rasional di Tak Hingga")
    st.markdown(r"""
    Untuk fungsi rasional, perilaku limit di tak hingga dapat dianalisis
    berdasarkan pangkat tertinggi pada pembilang dan penyebut.
    """)

    st.markdown("Contoh:")
    st.latex(r"\lim_{x\to\infty}\frac{2x^2+3x+1}{x^2-4}")

    st.markdown(r"""
    Karena pangkat tertinggi pembilang dan penyebut sama, limit ditentukan
    oleh perbandingan koefisien pangkat tertinggi.
    """)

    st.latex(r"\lim_{x\to\infty}\frac{2x^2+3x+1}{x^2-4}=2")

    # =========================================================
    # 14. KASUS PANGKAT TERTINGGI
    # =========================================================

    st.header("14. Kasus Pangkat Tertinggi")
    st.markdown(r"""
    Untuk $\dfrac{P(x)}{Q(x)}$ berlaku secara umum:

    - Derajat pembilang < derajat penyebut → limit 0.
    - Derajat pembilang = derajat penyebut → perbandingan koefisien utama.
    - Derajat pembilang > derajat penyebut → dapat menuju tak hingga atau
      tidak hingga tergantung tanda dan bentuk fungsi.
    """)

    # =========================================================
    # 15. LIMIT FUNGSI TRIGONOMETRI
    # =========================================================

    st.header("15. Limit Fungsi Trigonometri")
    st.markdown("Salah satu limit dasar yang sangat penting adalah:")

    st.latex(r"\lim_{x\to0}\frac{\sin x}{x}=1")

    st.markdown("Limit dasar lainnya:")

    st.latex(r"\lim_{x\to0}\frac{1-\cos x}{x}=0")
    st.latex(r"\lim_{x\to0}\frac{\tan x}{x}=1")

    # =========================================================
    # 16. CONTOH LIMIT TRIGONOMETRI
    # =========================================================

    st.header("16. Contoh Limit Trigonometri")
    st.markdown("Tentukan:")
    st.latex(r"\lim_{x\to0}\frac{\sin(3x)}{x}")

    st.markdown("Kita dapat menuliskan:")

    st.latex(r"\frac{\sin(3x)}{x}=3\cdot\frac{\sin(3x)}{3x}")
    st.latex(r"\lim_{x\to0}\frac{\sin(3x)}{x}=3")

    st.info("Jadi, nilai limit adalah 3.")

    # =========================================================
    # 17. KALKULATOR LIMIT TRIGONOMETRI
    # =========================================================

    st.header("17. Kalkulator Limit Trigonometri")

    koefisien_trig = st.number_input(
        "Koefisien k pada sin(kx)/x", value=3.0, key="limit_trig_k"
    )

    st.latex(r"\lim_{x\to0}\frac{\sin(kx)}{x}=k")

    st.info(
        f"Hasil untuk k = {koefisien_trig:g} adalah {koefisien_trig:g}"
    )

    # =========================================================
    # 18. KEKONTINUAN FUNGSI
    # =========================================================

    st.header("18. Kekontinuan Fungsi")
    st.markdown(r"""
    Sebuah fungsi $f(x)$ dikatakan kontinu di $x=a$ jika memenuhi tiga
    syarat:

    1. $f(a)$ terdefinisi.
    2. $\lim_{x\to a}f(x)$ ada.
    3. $\lim_{x\to a}f(x)=f(a)$.
    """)

    st.latex(r"\lim_{x\to a}f(x)=f(a)")

    st.info(r"""
    **Intuisi:** grafik fungsi kontinu dapat digambarkan tanpa mengangkat
    pensil dari kertas pada interval yang diperhatikan.
    """)

    # =========================================================
    # 19. EKSPLORASI KEKONTINUAN
    # =========================================================

    st.header("19. Eksplorasi Kekontinuan")

    nilai_kontinu = st.number_input(
        "Nilai a untuk fungsi f(x)=x²+2x+1",
        value=2.0,
        key="continuity_a"
    )

    nilai_f = nilai_kontinu**2 + 2 * nilai_kontinu + 1

    st.latex(r"f(x)=x^2+2x+1")

    st.info(
        f"f({nilai_kontinu:g}) = {nilai_f:g}. "
        "Karena fungsi polinomial kontinu, limit pada titik tersebut "
        "sama dengan nilai f(a)."
    )

    # =========================================================
    # 20. VISUALISASI FUNGSI
    # =========================================================

    st.header("20. Visualisasi Fungsi")

    x_visual = np.linspace(-5, 5, 400)
    y_visual = x_visual**2 - 4

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(x_visual, y_visual, "b-")
    ax.axhline(0, color="gray", linewidth=0.6)
    ax.axvline(0, color="gray", linewidth=0.6)
    ax.grid(True, linestyle=":", alpha=0.6)
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.set_title(r"$f(x) = x^2 - 4$")
    fig.tight_layout()
    st.pyplot(fig, use_container_width=True)

    st.markdown(r"""
    Grafik tersebut dapat digunakan untuk mengamati perilaku fungsi ketika
    $x$ mendekati suatu nilai tertentu.
    """)

    # =========================================================
    # 21. EKSPLORASI LIMIT SECARA NUMERIK
    # =========================================================

    st.header("21. Eksplorasi Limit Secara Numerik")

    titik_limit = st.number_input(
        "Titik yang didekati a", value=2.0, key="numeric_limit_a"
    )

    jarak = st.number_input(
        "Jarak ε",
        min_value=0.0001,
        value=0.1,
        format="%.4f",
        key="numeric_limit_eps"
    )

    x_kiri = titik_limit - jarak
    x_kanan = titik_limit + jarak

    f_kiri = x_kiri**2 + 3 * x_kiri + 1
    f_kanan = x_kanan**2 + 3 * x_kanan + 1

    df_limit = pd.DataFrame({
        "Posisi": ["Dari kiri", "Titik", "Dari kanan"],
        "x": [x_kiri, titik_limit, x_kanan],
        "f(x)": [
            f_kiri,
            titik_limit**2 + 3 * titik_limit + 1,
            f_kanan
        ]
    })

    st.dataframe(
        df_limit,
        use_container_width=True,
        hide_index=True
    )

    st.info(
        "Semakin kecil jarak ε, nilai dari kiri dan kanan semakin mendekati "
        "nilai limit."
    )

    # =========================================================
    # 22. PENERAPAN LIMIT
    # =========================================================

    st.header("22. Penerapan Limit")
    st.markdown(r"""
    Konsep limit menjadi dasar bagi berbagai konsep matematika dan ilmu
    terapan, antara lain:

    - turunan,
    - integral,
    - kecepatan sesaat,
    - percepatan,
    - optimasi,
    - pemodelan matematika,
    - analisis perubahan.
    """)

    # =========================================================
    # 23. STUDI KASUS: KECEPATAN SESAAT
    # =========================================================

    st.header("🌍 Studi Kasus: Kecepatan Sesaat")
    st.markdown(r"""
    Misalkan posisi suatu benda dinyatakan oleh:
    """)

    st.latex(r"s(t)=t^2")

    st.markdown(r"""
    Kecepatan rata-rata pada interval dari $t$ ke $t+h$ adalah:
    """)

    st.latex(r"\frac{s(t+h)-s(t)}{h}")

    st.markdown(r"""
    Kecepatan sesaat diperoleh ketika $h$ mendekati nol.
    """)

    st.latex(r"v(t)=\lim_{h\to0}\frac{s(t+h)-s(t)}{h}")

    st.markdown(r"Untuk $s(t)=t^2$:")

    st.latex(r"v(t)=2t")

    st.info(r"""
    Limit menjadi dasar untuk memahami konsep turunan dan kecepatan
    sesaat.
    """)

    # =========================================================
    # 24. RINGKASAN METODE MENENTUKAN LIMIT
    # =========================================================

    st.header("23. Ringkasan Metode Menentukan Limit")

    df_metode_limit = pd.DataFrame({
        "Kondisi": [
            "Substitusi menghasilkan bilangan",
            "Bentuk 0/0 polinomial",
            "Bentuk 0/0 mengandung akar",
            "Fungsi potongan",
            "x menuju tak hingga",
            "Limit trigonometri"
        ],
        "Metode": [
            "Substitusi langsung",
            "Pemfaktoran",
            "Rasionalisasi",
            "Limit kiri dan kanan",
            "Bandingkan pangkat tertinggi",
            "Gunakan limit dasar trigonometri"
        ]
    })

    st.dataframe(
        df_metode_limit,
        use_container_width=True,
        hide_index=True
    )

    # =========================================================
    # 25. LATIHAN
    # =========================================================

    st.header("📝 Latihan")

    st.markdown(r"""
    **Soal 1** — Tentukan:
    """)
    st.latex(r"\lim_{x\to3}(x^2+2x+1)")

    st.markdown(r"""
    **Soal 2** — Tentukan:
    """)
    st.latex(r"\lim_{x\to2}\frac{x^2-4}{x-2}")

    st.markdown(r"""
    **Soal 3** — Tentukan:
    """)
    st.latex(r"\lim_{x\to0}\frac{\sqrt{x+1}-1}{x}")

    st.markdown(r"""
    **Soal 4** — Tentukan:
    """)
    st.latex(r"\lim_{x\to0}\frac{\sin(5x)}{x}")

    st.markdown(r"""
    **Soal 5** — Jelaskan perbedaan antara limit kiri dan limit kanan.
    """)

    st.markdown(r"""
    **Soal 6** — Jelaskan tiga syarat suatu fungsi kontinu di $x=a$.
    """)

    st.markdown(r"""
    **Soal 7** — Tentukan:
    """)
    st.latex(r"\lim_{x\to\infty}\frac{3x^2+2x-1}{x^2+5}")

    # =========================================================
    # 26. KUIS
    # =========================================================

    st.header("🎯 Kuis")

    jawaban_limit = st.radio(
        "Nilai dari lim(x→2) (x² − 4)/(x − 2) adalah:",
        ["0", "2", "4", "Tidak ada"],
        key="quiz_limit_fungsi"
    )

    if st.button("Periksa Jawaban", key="cek_quiz_limit"):
        if jawaban_limit == "4":
            st.success(
                "✅ Benar. Dengan pemfaktoran, (x²−4)/(x−2)=x+2 "
                "sehingga limitnya 4."
            )
        else:
            st.error(
                "❌ Belum tepat. Faktorkan x²−4 menjadi (x−2)(x+2)."
            )

    # =========================================================
    # 27. REFLEKSI
    # =========================================================

    st.header("💭 Refleksi")

    st.markdown(r"""
    Setelah mempelajari limit, coba jelaskan:

    1. Apa yang dimaksud dengan limit fungsi?
    2. Apa perbedaan nilai fungsi dan nilai limit?
    3. Kapan substitusi langsung dapat digunakan?
    4. Mengapa bentuk $0/0$ disebut bentuk tak tentu?
    5. Kapan metode pemfaktoran digunakan?
    6. Mengapa rasionalisasi dapat digunakan pada bentuk yang mengandung akar?
    7. Apa syarat agar limit dua sisi ada?
    8. Apa hubungan limit dengan kekontinuan?
    9. Mengapa limit menjadi dasar bagi konsep turunan?
    """)

    # =========================================================
    # 28. RANGKUMAN
    # =========================================================

    st.header("📌 Rangkuman")

    st.markdown(r"""
    **Limit** menggambarkan nilai yang didekati oleh suatu fungsi ketika
    variabel mendekati suatu nilai tertentu.

    Konsep penting:

    - Limit ditulis dengan notasi $\lim_{x\to a}f(x)$.
    - Substitusi langsung dapat digunakan jika fungsi kontinu pada titik
      tersebut.
    - Bentuk $0/0$ merupakan bentuk tak tentu.
    - Pemfaktoran dapat digunakan untuk menyelesaikan bentuk $0/0$.
    - Rasionalisasi dapat digunakan pada bentuk yang mengandung akar.
    - Limit dua sisi ada jika limit kiri dan kanan sama.
    - Limit di tak hingga digunakan untuk mempelajari perilaku fungsi
      ketika $x$ semakin besar atau kecil tanpa batas.
    - Terdapat beberapa limit dasar trigonometri.
    - Fungsi kontinu memenuhi $\lim_{x\to a}f(x)=f(a)$.
    - Konsep limit menjadi dasar untuk mempelajari turunan dan integral.
    """)

    st.success("🎉 Materi Limit Fungsi selesai dipelajari.")



def distribusi_peluang():
    st.markdown(
        '<div class="content-title">📕 Distribusi Peluang (Binomial dan Normal)</div>',
        unsafe_allow_html=True
    )

    # =========================================================
    # TUJUAN PEMBELAJARAN
    # =========================================================

    st.header("🎯 Tujuan Pembelajaran")

    st.markdown(r"""
    Setelah mempelajari materi ini, siswa diharapkan mampu:

    - Menjelaskan konsep variabel acak dan distribusi peluang.
    - Membedakan variabel acak diskrit dan kontinu.
    - Menentukan fungsi peluang suatu variabel acak diskrit.
    - Menentukan nilai harapan dan varians.
    - Menjelaskan karakteristik distribusi binomial.
    - Menghitung peluang menggunakan distribusi binomial.
    - Menjelaskan karakteristik distribusi normal.
    - Menggunakan distribusi normal standar.
    - Menghitung skor-Z.
    - Menentukan peluang berdasarkan distribusi normal.
    - Menggunakan distribusi binomial dan normal dalam masalah kontekstual.
    """)

    # =========================================================
    # APERSEPSI
    # =========================================================

    st.header("💡 Apersepsi")

    st.markdown(r"""
    Dalam kehidupan sehari-hari kita sering berhadapan dengan hasil yang
    tidak dapat dipastikan sebelumnya.

    Contohnya:

    - jumlah siswa yang lulus,
    - jumlah produk yang rusak,
    - hasil pelemparan koin,
    - tinggi badan seseorang,
    - waktu tunggu,
    - nilai ujian.

    Hasil-hasil tersebut dapat dimodelkan menggunakan **variabel acak**
    dan **distribusi peluang**.
    """)

    # =========================================================
    # 1. VARIABEL ACAK
    # =========================================================

    st.header("1. Variabel Acak")

    st.markdown(r"""
    Variabel acak adalah variabel yang nilainya ditentukan oleh hasil
    suatu percobaan acak.

    Variabel acak dapat dibedakan menjadi:

    - **Diskrit** → memiliki nilai yang dapat dihitung satu per satu.
    - **Kontinu** → dapat memiliki nilai pada suatu interval.
    """)

    st.markdown(r"""
    Contoh variabel acak diskrit:

    - jumlah anak,
    - jumlah produk rusak,
    - jumlah sisi angka pada koin.

    Contoh variabel acak kontinu:

    - tinggi badan,
    - berat badan,
    - waktu,
    - suhu.
    """)

    # =========================================================
    # 2. DISTRIBUSI PELUANG DISKRIT
    # =========================================================

    st.header("2. Distribusi Peluang Diskrit")

    st.markdown(r"""
    Distribusi peluang menunjukkan probabilitas dari setiap kemungkinan
    nilai suatu variabel acak.
    """)

    st.latex(r"P(X=x)=p(x)")

    st.markdown("Jumlah seluruh peluang harus sama dengan 1.")

    st.latex(r"\sum P(X=x)=1")

    # =========================================================
    # 3. CONTOH DISTRIBUSI
    # =========================================================

    st.header("3. Contoh Distribusi Peluang")

    df_peluang = pd.DataFrame({
        "X": [0, 1, 2, 3],
        "P(X)": [0.1, 0.2, 0.4, 0.3]
    })

    st.dataframe(
        df_peluang,
        use_container_width=True,
        hide_index=True
    )

    st.info(f"Jumlah peluang = {df_peluang['P(X)'].sum():.1f}")

    # =========================================================
    # 4. NILAI HARAPAN
    # =========================================================

    st.header("4. Nilai Harapan")

    st.markdown(r"""
    Nilai harapan atau expected value merupakan rata-rata teoretis dari
    suatu variabel acak.
    """)

    st.latex(r"E(X)=\sum x\,p(x)")

    st.markdown("Untuk distribusi di atas:")

    expected_value = (df_peluang["X"] * df_peluang["P(X)"]).sum()

    st.latex(rf"E(X)={expected_value:.2f}")

    # =========================================================
    # 5. VARIANS
    # =========================================================

    st.header("5. Varians dan Simpangan Baku")

    st.latex(r"\text{Var}(X)=E(X^2)-[E(X)]^2")

    variance = (
        (df_peluang["X"]**2 * df_peluang["P(X)"]).sum()
        - expected_value**2
    )

    std_dev = math.sqrt(variance)

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Varians", f"{variance:.4f}")

    with col2:
        st.metric("Simpangan baku", f"{std_dev:.4f}")

    # =========================================================
    # 6. DISTRIBUSI BINOMIAL
    # =========================================================

    st.header("6. Distribusi Binomial")

    st.markdown(r"""
    Distribusi binomial digunakan untuk menghitung banyaknya keberhasilan
    dalam sejumlah percobaan yang memenuhi kondisi tertentu.

    Percobaan binomial memiliki karakteristik:

    - jumlah percobaan tetap,
    - setiap percobaan memiliki dua kemungkinan hasil,
    - peluang keberhasilan tetap,
    - setiap percobaan saling independen.
    """)

    # =========================================================
    # 7. RUMUS BINOMIAL
    # =========================================================

    st.header("7. Rumus Distribusi Binomial")

    st.latex(r"P(X=k)=\binom{n}{k}p^k(1-p)^{n-k}")

    st.markdown(r"""
    dengan:

    - $n$ = jumlah percobaan.
    - $k$ = jumlah keberhasilan.
    - $p$ = peluang keberhasilan.
    - $1-p$ = peluang kegagalan.
    """)

    # =========================================================
    # 8. CONTOH BINOMIAL
    # =========================================================

    st.header("8. Contoh Distribusi Binomial")

    st.markdown(r"""
    Sebuah koin dilempar 5 kali.

    Misalkan peluang muncul sisi angka adalah $p=0{,}5$.

    Peluang tepat 3 kali muncul angka:
    """)

    st.latex(r"P(X=3)=\binom{5}{3}(0{,}5)^3(0{,}5)^2")

    hasil_binomial = math.comb(5, 3) * (0.5**3) * (0.5**2)

    st.info(f"P(X=3) = {hasil_binomial:.4f}")

    # =========================================================
    # 9. KALKULATOR BINOMIAL
    # =========================================================

    st.header("9. Kalkulator Binomial")

    n_binom = st.number_input(
        "Jumlah percobaan n",
        min_value=1, max_value=100, value=10, step=1,
        key="binom_n"
    )

    p_binom = st.number_input(
        "Peluang keberhasilan p",
        min_value=0.0, max_value=1.0, value=0.5, step=0.05,
        key="binom_p"
    )

    k_binom = st.number_input(
        "Jumlah keberhasilan k",
        min_value=0, max_value=100, value=5, step=1,
        key="binom_k"
    )

    if k_binom <= n_binom:

        peluang_binom = (
            math.comb(int(n_binom), int(k_binom))
            * p_binom**k_binom
            * (1 - p_binom)**(n_binom - k_binom)
        )

        st.info(f"P(X={int(k_binom)}) = {peluang_binom:.6f}")

    else:
        st.warning("Nilai k tidak boleh lebih besar daripada n.")

    # =========================================================
    # 10. DISTRIBUSI BINOMIAL INTERAKTIF
    # =========================================================

    st.header("10. Visualisasi Distribusi Binomial")

    x_binom = np.arange(0, int(n_binom) + 1)

    y_binom = np.array([
        math.comb(int(n_binom), int(k))
        * p_binom**k
        * (1 - p_binom)**(int(n_binom) - int(k))
        for k in x_binom
    ])

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar(x_binom, y_binom, color="steelblue", edgecolor="black")
    ax.grid(True, linestyle=":", alpha=0.6, axis="y")
    ax.set_xlabel("Jumlah keberhasilan (k)")
    ax.set_ylabel("P(X = k)")
    ax.set_title(rf"Distribusi Binomial: $n={int(n_binom)}$, $p={p_binom:.2f}$")
    fig.tight_layout()
    st.pyplot(fig, use_container_width=True)

    # =========================================================
    # 11. NILAI HARAPAN BINOMIAL
    # =========================================================

    st.header("11. Nilai Harapan Distribusi Binomial")

    st.latex(r"E(X)=np")

    mean_binom = n_binom * p_binom

    st.info(f"E(X) = {mean_binom:.4f}")

    # =========================================================
    # 12. VARIANS BINOMIAL
    # =========================================================

    st.header("12. Varians Distribusi Binomial")

    st.latex(r"\text{Var}(X)=np(1-p)")

    variance_binom = n_binom * p_binom * (1 - p_binom)

    st.info(f"Var(X) = {variance_binom:.4f}")

    # =========================================================
    # 13. CONTOH KONTEKSTUAL
    # =========================================================

    st.header("🌍 Studi Kasus Binomial")

    st.markdown(r"""
    Sebuah mesin menghasilkan produk dengan peluang produk cacat sebesar
    5%.

    Jika dipilih 20 produk secara independen, jumlah produk cacat dapat
    dimodelkan menggunakan distribusi binomial dengan:

    - $n=20$
    - $p=0{,}05$
    """)

    st.latex(r"X\sim \text{Binomial}(20,\;0{,}05)")

    peluang_nol = math.comb(20, 0) * (0.05**0) * (0.95**20)

    st.info(f"Peluang tidak ada produk cacat = {peluang_nol:.6f}")

    # =========================================================
    # 14. DISTRIBUSI NORMAL
    # =========================================================

    st.header("13. Distribusi Normal")

    st.markdown(r"""
    Distribusi normal adalah distribusi kontinu yang memiliki bentuk
    seperti lonceng dan simetris terhadap nilai rata-ratanya.
    """)

    st.latex(r"X\sim N(\mu,\sigma^2)")

    st.markdown(r"""
    dengan:

    - $\mu$ = rata-rata.
    - $\sigma$ = simpangan baku.
    """)

    # =========================================================
    # 15. KARAKTERISTIK NORMAL
    # =========================================================

    st.header("14. Karakteristik Distribusi Normal")

    st.markdown(r"""
    Karakteristik distribusi normal:

    - Bentuknya simetris.
    - Rata-rata, median, dan modus sama.
    - Luas seluruh daerah di bawah kurva adalah 1.
    - Kurva mendekati sumbu horizontal tetapi tidak memotongnya.
    - Bentuk kurva ditentukan oleh $\mu$ dan $\sigma$.
    """)

    # =========================================================
    # 16. FUNGSI DENSITAS
    # =========================================================

    st.header("15. Fungsi Kepadatan Normal")

    st.latex(
        r"f(x)=\frac{1}{\sigma\sqrt{2\pi}}\,e^{-\frac{(x-\mu)^2}{2\sigma^2}}"
    )

    st.markdown(r"""
    Fungsi tersebut menggambarkan kepadatan peluang dari distribusi normal.
    """)

    # =========================================================
    # 17. DISTRIBUSI NORMAL STANDAR
    # =========================================================

    st.header("16. Distribusi Normal Standar")

    st.markdown(r"""
    Distribusi normal standar memiliki:

    - rata-rata 0,
    - simpangan baku 1.
    """)

    st.latex(r"Z\sim N(0,1)")

    # =========================================================
    # 18. SKOR Z
    # =========================================================

    st.header("17. Skor-Z")

    st.markdown(r"""
    Nilai suatu data dapat distandardisasi menggunakan skor-Z:
    """)

    st.latex(r"Z=\frac{X-\mu}{\sigma}")

    st.markdown(r"""
    Skor-Z menunjukkan berapa banyak simpangan baku suatu nilai berada
    dari rata-rata.
    """)

    # =========================================================
    # 19. KALKULATOR Z-SCORE
    # =========================================================

    st.header("18. Kalkulator Skor-Z")

    nilai_x = st.number_input("Nilai X", value=75.0, key="normal_x")
    mean_normal = st.number_input("Rata-rata μ", value=70.0, key="normal_mean")
    sd_normal = st.number_input(
        "Simpangan baku σ", min_value=0.01, value=10.0, key="normal_sd"
    )

    z_score = (nilai_x - mean_normal) / sd_normal

    st.info(f"Z = {z_score:.4f}")

    # =========================================================
    # 20. VISUALISASI DISTRIBUSI NORMAL
    # =========================================================

    st.header("19. Visualisasi Distribusi Normal")

    x_normal = np.linspace(
        mean_normal - 4 * sd_normal,
        mean_normal + 4 * sd_normal,
        500
    )

    y_normal = (
        1 / (sd_normal * math.sqrt(2 * math.pi))
        * np.exp(-((x_normal - mean_normal)**2) / (2 * sd_normal**2))
    )

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(x_normal, y_normal, "b-")
    ax.axvline(mean_normal, color="red", linestyle="--", linewidth=1,
               label=f"μ = {mean_normal:g}")
    ax.axvline(nilai_x, color="green", linestyle=":", linewidth=1,
               label=f"X = {nilai_x:g}")
    ax.fill_between(x_normal, y_normal, where=(x_normal <= nilai_x),
                    color="green", alpha=0.2)
    ax.grid(True, linestyle=":", alpha=0.6)
    ax.set_xlabel("X")
    ax.set_ylabel("Kepadatan")
    ax.set_title(
        rf"$N(\mu={mean_normal:g},\;\sigma={sd_normal:g})$"
    )
    ax.legend(loc="upper right")
    fig.tight_layout()
    st.pyplot(fig, use_container_width=True)

    # =========================================================
    # 21. PROBABILITAS NORMAL
    # =========================================================

    st.header("20. Menghitung Peluang Distribusi Normal")

    st.markdown(r"""
    Peluang pada distribusi normal dapat dihitung menggunakan fungsi
    distribusi kumulatif atau CDF.
    """)

    def normal_cdf(x, mu, sigma):
        return 0.5 * (
            1 + math.erf((x - mu) / (sigma * math.sqrt(2)))
        )

    batas_normal = st.number_input(
        "Batas X", value=75.0, key="normal_batas"
    )

    peluang_kurang = normal_cdf(batas_normal, mean_normal, sd_normal)

    st.info(f"P(X ≤ {batas_normal:g}) = {peluang_kurang:.6f}")

    # =========================================================
    # 22. PELUANG INTERVAL NORMAL
    # =========================================================

    st.header("21. Peluang pada Interval")

    batas_bawah = st.number_input(
        "Batas bawah", value=60.0, key="normal_lower"
    )

    batas_atas = st.number_input(
        "Batas atas", value=80.0, key="normal_upper"
    )

    if batas_bawah < batas_atas:

        peluang_interval = (
            normal_cdf(batas_atas, mean_normal, sd_normal)
            - normal_cdf(batas_bawah, mean_normal, sd_normal)
        )

        st.info(
            f"P({batas_bawah:g} < X < {batas_atas:g}) = "
            f"{peluang_interval:.6f}"
        )

    else:
        st.warning("Batas bawah harus lebih kecil daripada batas atas.")

    # =========================================================
    # 23. ATURAN EMPIRIS
    # =========================================================

    st.header("22. Aturan Empiris")

    st.markdown(r"""
    Untuk distribusi normal, secara pendekatan:

    - Sekitar 68% data berada dalam interval $\mu\pm\sigma$.
    - Sekitar 95% data berada dalam interval $\mu\pm2\sigma$.
    - Sekitar 99,7% data berada dalam interval $\mu\pm3\sigma$.
    """)

    st.latex(r"\mu\pm\sigma\approx 68\%")
    st.latex(r"\mu\pm 2\sigma\approx 95\%")
    st.latex(r"\mu\pm 3\sigma\approx 99{,}7\%")

    # =========================================================
    # 24. HUBUNGAN BINOMIAL DAN NORMAL
    # =========================================================

    st.header("23. Pendekatan Binomial dengan Normal")

    st.markdown(r"""
    Untuk nilai $n$ yang cukup besar, distribusi binomial dapat didekati
    menggunakan distribusi normal dengan:
    """)

    st.latex(r"\mu=np")
    st.latex(r"\sigma=\sqrt{np(1-p)}")

    st.markdown(r"""
    Dalam pendekatan ini perlu diperhatikan **koreksi kontinuitas**.
    """)

    # =========================================================
    # 25. SIMULASI BINOMIAL
    # =========================================================

    st.header("24. Simulasi Percobaan Binomial")

    jumlah_simulasi = st.slider(
        "Jumlah simulasi",
        100, 10000, 1000, step=100,
        key="sim_binom_n"
    )

    rng = np.random.default_rng(seed=42)
    hasil_simulasi = rng.binomial(
        int(n_binom), p_binom, jumlah_simulasi
    )

    # Histogram frekuensi
    unique, counts = np.unique(hasil_simulasi, return_counts=True)
    freq = counts / counts.sum()

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar(unique, freq, color="coral", edgecolor="black")
    ax.grid(True, linestyle=":", alpha=0.6, axis="y")
    ax.set_xlabel("Jumlah keberhasilan (k)")
    ax.set_ylabel("Frekuensi relatif")
    ax.set_title(
        rf"Simulasi Binomial: $n={int(n_binom)}$, $p={p_binom:.2f}$, "
        rf"$N={jumlah_simulasi}$"
    )
    fig.tight_layout()
    st.pyplot(fig, use_container_width=True)

    st.info(
        "Semakin banyak simulasi, pola distribusi hasil akan semakin "
        "mendekati distribusi teoritis."
    )

    # =========================================================
    # 26. APLIKASI NORMAL
    # =========================================================

    st.header("🌍 Studi Kasus Distribusi Normal")

    st.markdown(r"""
    Nilai ujian suatu kelompok siswa diasumsikan berdistribusi normal
    dengan rata-rata 70 dan simpangan baku 10.

    Modelnya:
    """)

    st.latex(r"X\sim N(70,\;10^2)")

    z_80 = (80 - 70) / 10

    st.markdown("Untuk nilai 80:")

    st.latex(r"Z=\frac{80-70}{10}=1")

    st.info(
        f"Nilai 80 berada {z_80:.0f} simpangan baku di atas rata-rata."
    )

    # =========================================================
    # 27. PERBANDINGAN BINOMIAL DAN NORMAL
    # =========================================================

    st.header("25. Binomial vs Normal")

    df_perbandingan = pd.DataFrame({
        "Aspek": [
            "Jenis variabel",
            "Bentuk distribusi",
            "Parameter",
            "Contoh"
        ],
        "Binomial": [
            "Diskrit",
            "Peluang tiap nilai",
            "n dan p",
            "Jumlah produk cacat"
        ],
        "Normal": [
            "Kontinu",
            "Kurva kepadatan",
            "μ dan σ",
            "Tinggi badan"
        ]
    })

    st.dataframe(
        df_perbandingan,
        use_container_width=True,
        hide_index=True
    )

    # =========================================================
    # 28. LATIHAN
    # =========================================================

    st.header("📝 Latihan")

    st.markdown(r"""
    **Soal 1**

    Sebuah koin dilempar 10 kali. Tentukan peluang tepat 6 kali muncul
    sisi angka jika peluang muncul angka adalah 0,5.
    """)

    st.markdown(r"""
    **Soal 2**

    Sebuah mesin memiliki peluang menghasilkan produk cacat sebesar 0,02.
    Jika diperiksa 50 produk, tentukan nilai harapan jumlah produk cacat.
    """)

    st.markdown(r"""
    **Soal 3**

    Suatu variabel acak berdistribusi normal dengan $\mu=70$ dan
    $\sigma=10$. Tentukan skor-Z untuk nilai 85.
    """)

    st.markdown(r"""
    **Soal 4**

    Jelaskan perbedaan variabel acak diskrit dan kontinu.
    """)

    st.markdown(r"""
    **Soal 5**

    Jelaskan kapan distribusi binomial dapat digunakan.
    """)

    # =========================================================
    # 29. KUIS
    # =========================================================

    st.header("🎯 Kuis")

    jawaban_distribusi = st.radio(
        "Jika X ~ Binomial(n=10, p=0,5), nilai harapan E(X) adalah:",
        ["2", "5", "10", "20"],
        key="quiz_distribusi_peluang"
    )

    if st.button("Periksa Jawaban", key="cek_quiz_distribusi"):
        if jawaban_distribusi == "5":
            st.success("✅ Benar. E(X) = np = (10)(0,5) = 5.")
        else:
            st.error("❌ Belum tepat. Gunakan rumus E(X) = np.")

    # =========================================================
    # 30. REFLEKSI
    # =========================================================

    st.header("💭 Refleksi")

    st.markdown(r"""
    Setelah mempelajari distribusi peluang, coba jelaskan:

    1. Apa yang dimaksud dengan variabel acak?
    2. Apa perbedaan variabel acak diskrit dan kontinu?
    3. Apa karakteristik distribusi binomial?
    4. Bagaimana menentukan nilai harapan distribusi binomial?
    5. Apa karakteristik distribusi normal?
    6. Apa makna skor-Z?
    7. Kapan distribusi binomial dapat didekati dengan distribusi normal?
    """)

    # =========================================================
    # 31. RANGKUMAN
    # =========================================================

    st.header("📌 Rangkuman")

    st.markdown(r"""
    **Distribusi peluang** digunakan untuk menggambarkan kemungkinan nilai
    suatu variabel acak.

    Konsep penting:

    - Variabel acak dapat berupa diskrit atau kontinu.
    - Distribusi peluang menunjukkan probabilitas setiap kemungkinan hasil.
    - Nilai harapan menunjukkan rata-rata teoretis.
    - Varians dan simpangan baku menunjukkan penyebaran data.
    - Distribusi binomial digunakan untuk sejumlah percobaan dengan dua
      kemungkinan hasil.
    - Distribusi binomial mempunyai parameter $n$ dan $p$.
    - Distribusi normal merupakan distribusi kontinu berbentuk lonceng.
    - Distribusi normal mempunyai parameter $\mu$ dan $\sigma$.
    - Skor-Z digunakan untuk melakukan standardisasi.
    - Distribusi binomial dengan $n$ cukup besar dapat didekati dengan
      distribusi normal.
    """)

    st.success("🎉 Materi Distribusi Peluang selesai dipelajari.")
    

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

    elif materi == "Distribusi Peluang":
        distribusi_peluang()
        #pass

    elif materi == "Limit Fungsi":
        limit_fungsi()
        #pass

    elif materi == "Turunan dan Penerapannya":
        turunan()
        #pass

    elif materi == "Integral":
        integral()
        #pass
