import streamlit as st

def tampilkan(materi):

    if materi == "Bilangan Berpangkat":
        bilangan_berpangkat()

    elif materi == "Persamaan dan Fungsi Eksponensial":
        # materi berikutnya
        #pass
        st.markdown("""
            ### UNDER MAINTENANCE !!!
            """)

    # dan seterusnya

def bilangan_berpangkat():

    st.header("🔢 Bilangan Berpangkat")

    st.markdown("""
    ### Matematika Kelas X — Fase E

    Bilangan berpangkat merupakan salah satu konsep dasar dalam
    matematika yang digunakan untuk menyatakan perkalian berulang.
    Konsep ini menjadi dasar untuk mempelajari bentuk akar,
    fungsi eksponensial, persamaan eksponensial, dan berbagai
    penerapan matematika dalam kehidupan sehari-hari.
    """)

    # ========================================================
    # TUJUAN PEMBELAJARAN
    # ========================================================

    with st.expander("🎯 Tujuan Pembelajaran", expanded=True):

        st.markdown("""
        Setelah mempelajari materi ini, peserta didik diharapkan mampu:

        1. Menjelaskan makna bilangan berpangkat.
        2. Menggunakan sifat-sifat bilangan berpangkat.
        3. Menyelesaikan operasi bilangan berpangkat.
        4. Menggunakan pangkat nol, negatif, dan pecahan.
        5. Mengubah bentuk pangkat pecahan menjadi bentuk akar.
        6. Melakukan operasi pada bentuk akar.
        7. Merasionalkan penyebut bentuk akar.
        8. Menggunakan notasi ilmiah.
        9. Menerapkan konsep bilangan berpangkat dalam masalah kontekstual.
        """)

    # ========================================================
    # 1. APERSEPSI
    # ========================================================

    st.subheader("1. Apersepsi")

    st.markdown("""
    Perhatikan perkalian berikut:

    2 × 2 × 2 × 2 × 2

    Perkalian tersebut memiliki faktor yang sama, yaitu 2,
    dan muncul sebanyak 5 kali.

    Agar penulisannya lebih sederhana, perkalian tersebut
    dapat ditulis menggunakan bentuk pangkat.
    """)

    st.latex(r"2^5=2\times2\times2\times2\times2")

    st.latex(r"2^5=32")

    st.info(
        "Bentuk pangkat merupakan cara singkat untuk menyatakan "
        "perkalian berulang dengan faktor yang sama."
    )

    # ========================================================
    # 2. KONSEP DASAR
    # ========================================================

    st.subheader("2. Konsep Bilangan Berpangkat")

    st.markdown("""
    Secara umum, bilangan berpangkat dapat ditulis sebagai:
    """)

    st.latex(r"a^n")

    st.markdown("""
    dengan:

    - **a** disebut basis atau bilangan pokok.
    - **n** disebut eksponen atau pangkat.
    """)

    st.markdown("Untuk bilangan bulat positif \(n\):")

    st.latex(r"a^n=\underbrace{a\times a\times\cdots\times a}_{n\ faktor}")

    st.markdown("Contoh:")

    st.latex(r"3^4=3\times3\times3\times3")

    st.latex(r"3^4=81")

    # ========================================================
    # 3. SIFAT PERKALIAN
    # ========================================================

    st.subheader("3. Sifat Perkalian Bilangan Berpangkat")

    st.markdown("""
    Jika dua bilangan berpangkat mempunyai basis yang sama,
    maka ketika dikalikan, pangkatnya dapat dijumlahkan.
    """)

    st.latex(r"a^m\times a^n=a^{m+n}")

    st.markdown("Contoh:")

    st.latex(r"2^3\times2^4=2^{3+4}")

    st.latex(r"2^7=128")

    st.success(
        "Kunci: basis sama → pangkat dijumlahkan."
    )

    # ========================================================
    # 4. SIFAT PEMBAGIAN
    # ========================================================

    st.subheader("4. Sifat Pembagian Bilangan Berpangkat")

    st.latex(r"\frac{a^m}{a^n}=a^{m-n}")

    #st.markdown("dengan a ≠ 0.")
    #st.markdown("dengan \(a\neq0\).")
    #st.markdown(r"dengan \(a\neq0\).")
    st.markdown(r"dengan $a \neq 0$.")

    st.markdown("Contoh:")

    st.latex(r"\frac{5^7}{5^3}=5^{7-3}")

    st.latex(r"=5^4=625")

    st.success(
        "Kunci: basis sama → pangkat dikurangkan."
    )

    # ========================================================
    # 5. PANGKAT DARI PANGKAT
    # ========================================================

    st.subheader("5. Pangkat dari Suatu Pangkat")

    st.latex(r"(a^m)^n=a^{mn}")

    st.markdown("Contoh:")

    st.latex(r"(2^3)^4=2^{3\times4}")

    st.latex(r"=2^{12}")

    st.success(
        "Kunci: pangkat dipangkatkan → pangkat dikalikan."
    )

    # ========================================================
    # 6. PANGKAT PADA PERKALIAN
    # ========================================================

    st.subheader("6. Pangkat pada Perkalian")

    st.latex(r"(ab)^n=a^nb^n")

    st.markdown("Contoh:")

    st.latex(r"(2\times3)^4=2^4\times3^4")

    st.latex(r"=16\times81")

    st.latex(r"=1296")

    # ========================================================
    # 7. PANGKAT PADA PEMBAGIAN
    # ========================================================

    st.subheader("7. Pangkat pada Pembagian")

    st.latex(r"\left(\frac{a}{b}\right)^n=\frac{a^n}{b^n}")

    #st.markdown("dengan \(b\neq0\).")
    st.markdown(r"dengan $b \neq 0$.")

    st.markdown("Contoh:")

    st.latex(r"\left(\frac{2}{3}\right)^3=\frac{2^3}{3^3}")

    st.latex(r"=\frac{8}{27}")

    # ========================================================
    # 8. PANGKAT NOL
    # ========================================================

    st.subheader("8. Pangkat Nol")

    st.markdown(r"Untuk setiap bilangan real \(a = 0), berlaku:")

    st.latex(r"a^0=1")

    st.markdown("Contoh:")

    st.latex(r"7^0=1")

    st.latex(r"(-12)^0=1")

    st.latex(r"\left(\frac{3}{5}\right)^0=1")

    st.warning(
        "Catatan: bentuk 0⁰ tidak dibahas sebagai bilangan berpangkat "
        "dalam konteks ini."
    )

    # ========================================================
    # 9. PANGKAT NEGATIF
    # ========================================================

    st.subheader("9. Pangkat Negatif")

    st.latex(r"a^{-n}=\frac{1}{a^n}")

    st.markdown("dengan \($a \neq 0$\).")

    st.markdown("Contoh:")

    st.latex(r"2^{-3}=\frac{1}{2^3}")

    st.latex(r"=\frac{1}{8}")

    st.markdown("Contoh lainnya:")

    st.latex(r"\frac{1}{5^{-2}}=5^2")

    st.latex(r"=25")

    # ========================================================
    # 10. PANGKAT PECAHAN
    # ========================================================

    st.subheader("10. Pangkat Pecahan")

    st.markdown("""
    Pangkat pecahan berhubungan erat dengan bentuk akar.
    """)

    st.latex(r"a^{\frac{1}{n}}=\sqrt[n]{a}")

    st.latex(r"a^{\frac{m}{n}}=\sqrt[n]{a^m}")

    st.markdown("Contoh:")

    st.latex(r"16^{\frac{1}{2}}=\sqrt{16}")

    st.latex(r"=4")

    st.markdown("Contoh lain:")

    st.latex(r"27^{\frac{2}{3}}=\sqrt[3]{27^2}")

    st.latex(r"=9")

    # ========================================================
    # 11. HUBUNGAN PANGKAT DAN AKAR
    # ========================================================

    st.subheader("11. Hubungan Pangkat dan Bentuk Akar")

    st.latex(r"\sqrt[n]{a^m}=a^{\frac{m}{n}}")

    st.markdown("Contoh:")

    st.latex(r"\sqrt[3]{x^5}=x^{\frac{5}{3}}")

    st.latex(r"\sqrt{x^3}=x^{\frac{3}{2}}")

    # ========================================================
    # 12. BENTUK AKAR
    # ========================================================

    st.subheader("12. Bentuk Akar")

    st.markdown("""
    Bentuk akar adalah bentuk yang memuat tanda akar dan
    tidak dapat disederhanakan lagi menjadi bilangan rasional.
    """)

    st.markdown("Contoh bentuk akar:")

    st.latex(r"\sqrt{2}")

    st.latex(r"\sqrt{3}")

    st.latex(r"\sqrt{5}")

    st.markdown("Sedangkan:")

    st.latex(r"\sqrt{25}=5")

    st.markdown("""
    sehingga √25 bukan lagi bentuk akar sederhana karena
    dapat dinyatakan sebagai bilangan rasional.
    """)

    # ========================================================
    # 13. MENYEDERHANAKAN BENTUK AKAR
    # ========================================================

    st.subheader("13. Menyederhanakan Bentuk Akar")

    st.markdown("Contoh:")

    st.latex(r"\sqrt{72}")

    st.latex(r"=\sqrt{36\times2}")

    st.latex(r"=6\sqrt{2}")

    st.markdown("Contoh lain:")

    st.latex(r"\sqrt{200}")

    st.latex(r"=\sqrt{100\times2}")

    st.latex(r"=10\sqrt{2}")

    # ========================================================
    # 14. PERKALIAN BENTUK AKAR
    # ========================================================

    st.subheader("14. Perkalian Bentuk Akar")

    st.latex(r"\sqrt{a}\times\sqrt{b}=\sqrt{ab}")

    st.markdown("Contoh:")

    st.latex(r"\sqrt{3}\times\sqrt{12}=\sqrt{36}")

    st.latex(r"=6")

    # ========================================================
    # 15. PEMBAGIAN BENTUK AKAR
    # ========================================================

    st.subheader("15. Pembagian Bentuk Akar")

    st.latex(r"\frac{\sqrt{a}}{\sqrt{b}}=\sqrt{\frac{a}{b}}")

    st.markdown("Contoh:")

    st.latex(r"\frac{\sqrt{18}}{\sqrt{2}}=\sqrt{9}")

    st.latex(r"=3")

    # ========================================================
    # 16. PENJUMLAHAN DAN PENGURANGAN
    # ========================================================

    st.subheader("16. Penjumlahan dan Pengurangan Bentuk Akar")

    st.markdown("""
    Bentuk akar hanya dapat dijumlahkan atau dikurangkan
    secara langsung jika mempunyai bentuk akar sejenis.
    """)

    st.markdown("Contoh:")

    st.latex(r"3\sqrt{2}+5\sqrt{2}=8\sqrt{2}")

    st.latex(r"7\sqrt{3}-2\sqrt{3}=5\sqrt{3}")

    st.markdown("Contoh yang perlu disederhanakan terlebih dahulu:")

    st.latex(r"\sqrt{12}+\sqrt{27}")

    st.latex(r"=2\sqrt{3}+3\sqrt{3}")

    st.latex(r"=5\sqrt{3}")

    # ========================================================
    # 17. RASIONALISASI
    # ========================================================

    st.subheader("17. Merasionalkan Penyebut")

    st.markdown("""
    Rasionalisasi penyebut dilakukan untuk menghilangkan
    bentuk akar pada penyebut pecahan.
    """)

    st.markdown("Contoh:")

    st.latex(r"\frac{1}{\sqrt{2}}")

    st.latex(r"=\frac{1}{\sqrt{2}}\times\frac{\sqrt{2}}{\sqrt{2}}")

    st.latex(r"=\frac{\sqrt{2}}{2}")

    st.markdown("Untuk penyebut berbentuk jumlah atau selisih akar,digunakan bentuk sekawan.")

    st.markdown("Contoh:")

    st.latex(r"\frac{1}{2+\sqrt{3}}")

    st.latex(r"=\frac{1}{2+\sqrt{3}}\times\frac{2-\sqrt{3}}{2-\sqrt{3}}")

    st.latex(r"=2-\sqrt{3}")

    # ========================================================
    # 18. NOTASI ILMIAH
    # ========================================================

    st.subheader("18. Notasi Ilmiah")

    st.markdown("""
    Notasi ilmiah digunakan untuk menyatakan bilangan yang
    sangat besar atau sangat kecil secara lebih ringkas.
    """)

    st.latex(r"a\times10^n")

    st.markdown("""
    dengan:

    \[
    1\leq a<10
    \]
    """)

    st.markdown("Contoh bilangan besar:")

    st.latex(r"4500000=4.5\times10^6")

    st.markdown("Contoh bilangan kecil:")

    st.latex(r"0.0000032=3.2\times10^{-6}")

    # ========================================================
    # 19. PENERAPAN
    # ========================================================

    st.subheader("19. Penerapan Bilangan Berpangkat")

    st.markdown("""
    Konsep bilangan berpangkat digunakan dalam berbagai bidang,
    antara lain:

    - pertumbuhan penduduk;
    - pertumbuhan bakteri;
    - bunga majemuk;
    - investasi;
    - teknologi komputer;
    - ukuran data digital;
    - astronomi;
    - fisika;
    - kimia;
    - notasi ilmiah.
    """)

    # ========================================================
    # 20. CONTOH SOAL KONTEKSTUAL
    # ========================================================

    st.subheader("20. Contoh Soal Kontekstual")

    st.markdown("""
    Sebuah koloni bakteri mula-mula berjumlah 500 bakteri.
    Setiap satu jam jumlah bakteri menjadi dua kali lipat.

    Berapa jumlah bakteri setelah 5 jam?
    """)

    st.latex(r"N=500\times2^5")

    st.latex(r"N=500\times32")

    st.latex(r"N=16000")

    st.success(
        "Jadi, jumlah bakteri setelah 5 jam adalah 16.000 bakteri."
    )

    # ========================================================
    # 21. LATIHAN
    # ========================================================

    st.subheader("21. Latihan")

    st.markdown("""
    **Soal 1**

    Sederhanakan:

    \(2^5\times2^3\)
    """)

    st.markdown("""
    **Soal 2**

    Sederhanakan:

    \(\frac{3^7}{3^4}\)
    """)

    st.markdown("""
    **Soal 3**

    Tentukan nilai:

    \(5^{-2}\)
    """)

    st.markdown("""
    **Soal 4**

    Tentukan nilai:

    \(81^{1/2}\)
    """)

    st.markdown("""
    **Soal 5**

    Sederhanakan:

    \(\sqrt{180}\)
    """)

    st.markdown("""
    **Soal 6**

    Sederhanakan:

    \(3\sqrt{5}+4\sqrt{5}\)
    """)

    st.markdown("""
    **Soal 7**

    Rasionalkan:

    \(\frac{1}{\sqrt{5}}\)
    """)

    st.markdown("""
    **Soal 8**

    Tuliskan 7.200.000 dalam notasi ilmiah.
    """)

    # ========================================================
    # 22. KUIS INTERAKTIF
    # ========================================================

    st.subheader("22. Kuis Interaktif")

    soal = st.radio(
        "Berapakah nilai dari 2⁴ × 2³?",
        [
            "2⁷",
            "2¹²",
            "4⁷",
            "4¹²"
        ],
        key="kuis_pangkat_1"
    )

    if st.button("Periksa Jawaban", key="cek_pangkat_1"):

        if soal == "2⁷":
            st.success("✅ Benar! 2⁴ × 2³ = 2⁷.")
        else:
            st.error(
                "❌ Belum tepat. Gunakan sifat "
                "aᵐ × aⁿ = aᵐ⁺ⁿ."
            )

    # ========================================================
    # 23. RANGKUMAN
    # ========================================================

    with st.expander("📌 Rangkuman Materi", expanded=False):

        st.markdown("""
        **Konsep utama yang perlu dikuasai:**

        1. Perkalian dengan basis sama → pangkat dijumlahkan.
        2. Pembagian dengan basis sama → pangkat dikurangkan.
        3. Pangkat dari pangkat → pangkat dikalikan.
        4. Pangkat nol → bernilai 1 untuk basis tidak nol.
        5. Pangkat negatif → menjadi kebalikan.
        6. Pangkat pecahan → berkaitan dengan bentuk akar.
        7. Bentuk akar dapat disederhanakan menggunakan faktor kuadrat sempurna.
        8. Penjumlahan akar hanya berlaku langsung untuk bentuk akar sejenis.
        9. Penyebut yang mengandung akar dapat dirasionalkan.
        10. Notasi ilmiah menggunakan bentuk \(a\times10^n\).
        """)
