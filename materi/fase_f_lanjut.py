import streamlit as st
import pandas as pd
import numpy as np
import math

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

    st.markdown(r"""
    dengan:
    
    - $a_n, a_{n-1}, \ldots, a_1, a_0$ merupakan koefisien.
    - $a_n \neq 0$.
    - $n$ merupakan derajat polinomial.
    - $a_0$ merupakan konstanta.
    """)

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
        #matriks()
        pass

    elif materi == "Transformasi geometri":
        #transformasi_geometri()
        pass

    elif materi == "Trigonometri":
        #trigonometri()
        pass

    elif materi == "Pemodelan fungsi":
        #pemodelan_fungsi()
        pass

    elif materi == "Vektor":
        #vektor()
        pass

    elif materi == "Irisan kerucut (lingkaran & elips)":
        #irisan_kerucut()
        pass

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
