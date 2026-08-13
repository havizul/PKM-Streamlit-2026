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
    st.markdown(r"\n dengan $a \neq 0$.")

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

    st.markdown(r"Untuk setiap bilangan real \($a \neq 0$\), berlaku:")
    #st.markdown(r"dengan $a \neq 0$.")

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

    st.markdown(r"dengan \($a \neq 0$\).")

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
    st.latex(r"x^2=16")
    st.latex(r"4^2=16")    
    st.latex(r"4\times4=16")    
    st.latex(r"x=4")

    st.markdown("Contoh lain:")

    st.latex(r"27^{\frac{2}{3}}=\sqrt[3]{27^2}")
    st.latex(r"x^3=27^2")
    st.latex(r"x^3=729")
    st.latex(r"9^3=729")
    st.latex(r"9\times9\times9=729")
    st.latex(r"x=9")

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
    
    with st.container(border=True):
        st.markdown("**Soal 1**")
        st.markdown("Sederhanakan:")
        st.latex(r"2^5 \times 2^3")
    
    with st.container(border=True):
        st.markdown("**Soal 2**")
        st.markdown("Sederhanakan:")
        st.latex(r"\frac{3^7}{3^4}")
     
    with st.container(border=True):
        st.markdown("**Soal 3**")
        st.markdown("Tentukan nilai:")
        st.latex(r"5^{-2}")
        
        
    with st.container(border=True):
        st.markdown("**Soal4**")
        st.markdown("Tentukan nilai:")
        st.latex(r"81^{1/2}")

    with st.container(border=True):
        st.markdown("**Soal 5**")
        st.markdown("Sederhanakan:")
        st.latex(r"\sqrt{180}")

    with st.container(border=True):
        st.markdown("**Soal 6**")
        st.markdown("Sederhanakan:")
        st.latex(r"3\sqrt{5}+4\sqrt{5}")
        
    with st.container(border=True):
        st.markdown("**Soal 7**")
        st.markdown("Rasionalkan:")
        st.latex(r"\frac{1}{\sqrt{5}}")
        
    with st.container(border=True):
        st.markdown("**Soal 8**")
        st.markdown("Tuliskan 7.200.000 dalam notasi ilmiah.")

    
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



def persamaan_fungsi_eksponensial():

    st.header("📈 Persamaan dan Fungsi Eksponensial")

    st.markdown("""
    ### Matematika Kelas X — Fase E

    Fungsi eksponensial merupakan fungsi yang variabelnya
    berada pada pangkat. Konsep ini banyak digunakan untuk
    memodelkan pertumbuhan dan peluruhan dalam kehidupan nyata,
    seperti pertumbuhan penduduk, pertumbuhan bakteri, investasi,
    dan peluruhan zat.
    """)

    # ========================================================
    # TUJUAN PEMBELAJARAN
    # ========================================================

    with st.expander("🎯 Tujuan Pembelajaran", expanded=True):

        st.markdown("""
        Setelah mempelajari materi ini, peserta didik diharapkan mampu:

        1. Menjelaskan pengertian fungsi eksponensial.
        2. Menentukan karakteristik fungsi eksponensial.
        3. Menggambar dan membaca grafik fungsi eksponensial.
        4. Menentukan domain dan range fungsi eksponensial.
        5. Membedakan pertumbuhan dan peluruhan eksponensial.
        6. Menyelesaikan persamaan eksponensial sederhana.
        7. Menyelesaikan masalah kontekstual menggunakan model eksponensial.
        """)

    # ========================================================
    # 1. APERSEPSI
    # ========================================================

    st.subheader("1. Apersepsi")

    st.markdown("""
    Perhatikan pola bilangan berikut:

    1, 2, 4, 8, 16, 32, ...

    Setiap bilangan diperoleh dengan mengalikan bilangan
    sebelumnya dengan 2.

    Pola tersebut dapat dinyatakan dalam bentuk pangkat 2.
    """)

    st.latex(r"1=2^0")

    st.latex(r"2=2^1")

    st.latex(r"4=2^2")

    st.latex(r"8=2^3")

    st.latex(r"16=2^4")

    st.info(
        "Pola pertumbuhan dengan faktor pengali tetap merupakan "
        "salah satu contoh dasar perilaku eksponensial."
    )

    # ========================================================
    # 2. PENGERTIAN FUNGSI EKSPONENSIAL
    # ========================================================

    st.subheader("2. Pengertian Fungsi Eksponensial")

    st.markdown("""
    Fungsi eksponensial adalah fungsi yang variabelnya
    berada pada bagian pangkat.
    """)

    st.latex(r"f(x)=a^x")

    st.markdown("""
    dengan syarat:

    - \(a>0\)
    - \(a\neq1\)
    """)

    st.markdown("""
    Keterangan:

    - \(a\) disebut basis.
    - \(x\) merupakan variabel atau eksponen.
    - \(f(x)\) merupakan nilai fungsi.
    """)

    st.markdown("Contoh fungsi eksponensial:")

    st.latex(r"f(x)=2^x")

    st.latex(r"f(x)=3^x")

    st.latex(r"f(x)=\left(\frac{1}{2}\right)^x")

    st.latex(r"f(x)=5^x")

    # ========================================================
    # 3. BUKAN FUNGSI EKSPONENSIAL
    # ========================================================

    st.subheader("3. Contoh yang Bukan Fungsi Eksponensial")

    st.markdown("""
    Tidak semua fungsi yang memiliki bentuk pangkat
    merupakan fungsi eksponensial.

    Pada fungsi eksponensial, **variabel berada pada pangkat**.
    """)

    st.markdown("Contoh fungsi eksponensial:")

    st.latex(r"f(x)=2^x")

    st.markdown("Contoh yang bukan fungsi eksponensial:")

    st.latex(r"f(x)=x^2")

    st.latex(r"f(x)=x^3+2")

    st.info(
        "Pada x², variabel x merupakan basis, sedangkan pada 2ˣ, "
        "variabel x merupakan eksponen."
    )

    # ========================================================
    # 4. NILAI FUNGSI
    # ========================================================

    st.subheader("4. Menentukan Nilai Fungsi Eksponensial")

    st.markdown("""
    Untuk menentukan nilai fungsi, substitusikan nilai x
    ke dalam fungsi.
    """)

    st.markdown("Contoh:")

    st.latex(r"f(x)=2^x")

    st.markdown("Jika \(x=3\):")

    st.latex(r"f(3)=2^3")

    st.latex(r"f(3)=8")

    st.markdown("Jika \(x=-2\):")

    st.latex(r"f(-2)=2^{-2}")

    st.latex(r"f(-2)=\frac{1}{4}")

    # ========================================================
    # 5. TABEL NILAI
    # ========================================================

    st.subheader("5. Tabel Nilai Fungsi")

    st.markdown("""
    Perhatikan fungsi \(f(x)=2^x\).
    """)

    st.table({
        "x": [-3, -2, -1, 0, 1, 2, 3],
        "f(x) = 2ˣ": [
            "1/8",
            "1/4",
            "1/2",
            "1",
            "2",
            "4",
            "8"
        ]
    })

    st.markdown("""
    Dari tabel tersebut terlihat bahwa ketika x bertambah,
    nilai fungsi juga bertambah.
    """)

    # ========================================================
    # 6. KARAKTERISTIK GRAFIK
    # ========================================================

    st.subheader("6. Karakteristik Grafik Fungsi Eksponensial")

    st.markdown("""
    Fungsi \(f(x)=a^x\) mempunyai beberapa karakteristik penting:

    - Grafik selalu melalui titik \((0,1)\).
    - Nilai fungsi selalu positif.
    - Grafik tidak pernah memotong sumbu-X.
    - Domain berupa seluruh bilangan real.
    - Range berupa bilangan real positif.
    """)

    st.latex(r"f(0)=a^0=1")

    st.latex(r"D_f=\mathbb{R}")

    st.latex(r"R_f=(0,\infty)")

    # ========================================================
    # 7. PERTUMBUHAN EKSPONENSIAL
    # ========================================================

    st.subheader("7. Pertumbuhan Eksponensial")

    st.markdown("""
    Jika basis lebih besar dari 1, yaitu \(a>1\),
    maka fungsi eksponensial bersifat meningkat.
    """)

    st.latex(r"f(x)=a^x,\quad a>1")

    st.markdown("Contoh:")

    st.latex(r"f(x)=2^x")

    st.latex(r"f(x)=3^x")

    st.latex(r"f(x)=5^x")

    st.success(
        "Basis a > 1 → fungsi mengalami pertumbuhan eksponensial."
    )

    # ========================================================
    # 8. PELURUHAN EKSPONENSIAL
    # ========================================================

    st.subheader("8. Peluruhan Eksponensial")

    st.markdown("""
    Jika \(0<a<1\), maka fungsi eksponensial bersifat menurun.
    Kondisi ini disebut peluruhan eksponensial.
    """)

    st.latex(r"f(x)=a^x,\quad0<a<1")

    st.markdown("Contoh:")

    st.latex(r"f(x)=\left(\frac{1}{2}\right)^x")

    st.latex(r"f(x)=\left(\frac{1}{3}\right)^x")

    st.success(
        "0 < a < 1 → fungsi mengalami peluruhan eksponensial."
    )

    # ========================================================
    # 9. PERBANDINGAN
    # ========================================================

    st.subheader("9. Pertumbuhan dan Peluruhan")

    st.table({
        "Kondisi Basis": [
            "a > 1",
            "0 < a < 1"
        ],
        "Perilaku": [
            "Meningkat",
            "Menurun"
        ],
        "Contoh": [
            "2ˣ",
            "(1/2)ˣ"
        ]
    })

    # ========================================================
    # 10. ASIMTOT
    # ========================================================

    st.subheader("10. Asimtot Horizontal")

    st.markdown("""
    Grafik fungsi eksponensial dasar \(f(x)=a^x\)
    mempunyai asimtot horizontal pada sumbu-X.
    """)

    st.latex(r"y=0")

    st.markdown("""
    Artinya, grafik semakin mendekati sumbu-X tetapi
    tidak pernah menyentuhnya.
    """)

    # ========================================================
    # 11. TRANSFORMASI DASAR
    # ========================================================

    st.subheader("11. Bentuk Umum Fungsi Eksponensial")

    st.latex(r"f(x)=A\cdot a^{x-h}+k")

    st.markdown("""
    Parameter pada fungsi tersebut dapat memengaruhi bentuk
    dan posisi grafik.

    - A memengaruhi peregangan atau pencerminan.
    - h memengaruhi pergeseran horizontal.
    - k memengaruhi pergeseran vertikal.
    """)

    # ========================================================
    # 12. PERSAMAAN EKSPONENSIAL
    # ========================================================

    st.subheader("12. Persamaan Eksponensial")

    st.markdown("""
    Persamaan eksponensial adalah persamaan yang variabelnya
    terdapat pada pangkat.
    """)

    st.latex(r"a^{f(x)}=a^{g(x)}")

    st.markdown("""
    Jika kedua ruas memiliki basis yang sama dan basis tersebut
    memenuhi \(a>0\) serta \(a\neq1\), maka eksponennya dapat
    disamakan.
    """)

    st.latex(r"f(x)=g(x)")

    # ========================================================
    # 13. CONTOH PERSAMAAN BASIS SAMA
    # ========================================================

    st.subheader("13. Persamaan dengan Basis Sama")

    st.markdown("Contoh:")

    st.latex(r"2^{x+3}=2^7")

    st.latex(r"x+3=7")

    st.latex(r"x=4")

    st.success("Jadi, penyelesaiannya adalah x = 4.")

    # ========================================================
    # 14. CONTOH LAIN
    # ========================================================

    st.markdown("Contoh:")

    st.latex(r"3^{2x-1}=3^5")

    st.latex(r"2x-1=5")

    st.latex(r"2x=6")

    st.latex(r"x=3")

    # ========================================================
    # 15. MENYAMAKAN BASIS
    # ========================================================

    st.subheader("15. Menyamakan Basis")

    st.markdown("""
    Jika basis kedua ruas berbeda, tetapi masih dapat dinyatakan
    menggunakan basis yang sama, ubahlah terlebih dahulu.
    """)

    st.markdown("Contoh:")

    st.latex(r"4^x=2^6")

    st.markdown("""
    Karena \(4=2^2\), maka:
    """)

    st.latex(r"(2^2)^x=2^6")

    st.latex(r"2^{2x}=2^6")

    st.latex(r"2x=6")

    st.latex(r"x=3")

    # ========================================================
    # 16. CONTOH 2
    # ========================================================

    st.markdown("Contoh:")

    st.latex(r"8^{x-1}=2^9")

    st.markdown("""
    Karena \(8=2^3\), maka:
    """)

    st.latex(r"(2^3)^{x-1}=2^9")

    st.latex(r"2^{3x-3}=2^9")

    st.latex(r"3x-3=9")

    st.latex(r"x=4")

    # ========================================================
    # 17. PERSAMAAN EKSPONENSIAL DENGAN SUBSTITUSI
    # ========================================================

    st.subheader("17. Persamaan Eksponensial dengan Substitusi")

    st.markdown("""
    Beberapa persamaan eksponensial dapat diselesaikan
    dengan melakukan substitusi.
    """)

    st.markdown("Contoh:")

    st.latex(r"4^x-5(2^x)+4=0")

    st.markdown("""
    Karena \(4^x=(2^x)^2\), misalkan:
    """)

    st.latex(r"t=2^x")

    st.markdown("Maka persamaannya menjadi:")

    st.latex(r"t^2-5t+4=0")

    st.latex(r"(t-1)(t-4)=0")

    st.latex(r"t=1\quad\text{atau}\quad t=4")

    st.markdown("Kembalikan ke \(2^x\):")

    st.latex(r"2^x=1")

    st.latex(r"x=0")

    st.latex(r"2^x=4")

    st.latex(r"x=2")

    st.success("Jadi, penyelesaiannya adalah x = 0 atau x = 2.")

    # ========================================================
    # 18. PERSAMAAN EKSPONENSIAL DALAM KEHIDUPAN
    # ========================================================

    st.subheader("18. Model Pertumbuhan Eksponensial")

    st.markdown("""
    Pertumbuhan eksponensial terjadi ketika suatu besaran
    bertambah dengan faktor pengali yang tetap dalam setiap
    periode waktu.
    """)

    st.latex(r"N(t)=N_0a^t")

    st.markdown("""
    Keterangan:

    - \(N(t)\) = jumlah pada waktu t
    - \(N_0\) = jumlah awal
    - \(a\) = faktor pertumbuhan
    - \(t\) = waktu
    """)

    # ========================================================
    # 19. CONTOH PERTUMBUHAN
    # ========================================================

    st.subheader("19. Contoh Pertumbuhan Bakteri")

    st.markdown("""
    Sebuah koloni bakteri mula-mula berjumlah 500.
    Setiap satu jam jumlahnya menjadi dua kali lipat.

    Tentukan jumlah bakteri setelah 5 jam.
    """)

    st.latex(r"N(t)=500(2)^t")

    st.latex(r"N(5)=500(2)^5")

    st.latex(r"N(5)=500(32)")

    st.latex(r"N(5)=16000")

    st.success(
        "Jumlah bakteri setelah 5 jam adalah 16.000 bakteri."
    )

    # ========================================================
    # 20. MODEL PELURUHAN
    # ========================================================

    st.subheader("20. Model Peluruhan Eksponensial")

    st.markdown("""
    Peluruhan eksponensial terjadi ketika suatu besaran
    berkurang dengan faktor pengali yang tetap pada setiap periode.
    """)

    st.latex(r"N(t)=N_0a^t")

    st.markdown("""
    dengan \(0<a<1\).
    """)

    st.markdown("Contoh faktor peluruhan:")

    st.latex(r"a=\frac{1}{2}")

    st.latex(r"a=\frac{1}{3}")

    st.latex(r"a=0.8")

    # ========================================================
    # 21. CONTOH PELURUHAN
    # ========================================================

    st.subheader("21. Contoh Peluruhan")

    st.markdown("""
    Suatu zat memiliki massa awal 800 gram.
    Setiap periode massanya menjadi 75% dari massa sebelumnya.

    Tentukan massa setelah 4 periode.
    """)

    st.latex(r"N(t)=800(0.75)^t")

    st.latex(r"N(4)=800(0.75)^4")

    st.latex(r"N(4)=253.125")

    st.success(
        "Massa zat setelah 4 periode adalah 253,125 gram."
    )

    # ========================================================
    # 22. BUNGA MAJEMUK
    # ========================================================

    st.subheader("22. Penerapan pada Bunga Majemuk")

    st.markdown("""
    Pertumbuhan nilai uang dengan bunga majemuk merupakan
    salah satu penerapan fungsi eksponensial.
    """)

    st.latex(r"A=P(1+r)^n")

    st.markdown("""
    Keterangan:

    - \(A\) = nilai akhir
    - \(P\) = modal awal
    - \(r\) = tingkat bunga per periode
    - \(n\) = banyak periode
    """)

    st.markdown("Contoh:")

    st.markdown("""
    Modal Rp1.000.000 mendapat bunga 10% per tahun.
    Berapa nilai setelah 3 tahun?
    """)

    st.latex(r"A=1000000(1+0.10)^3")

    st.latex(r"A=1000000(1.1)^3")

    st.latex(r"A=1331000")

    st.success(
        "Nilai investasi setelah 3 tahun adalah Rp1.331.000."
    )

    # ========================================================
    # 23. GRAFIK INTERAKTIF
    # ========================================================

    st.subheader("23. Eksplorasi Grafik")

    basis = st.slider(
        "Pilih nilai basis a",
        min_value=0.2,
        max_value=5.0,
        value=2.0,
        step=0.1
    )

    x_values = list(range(-5, 6))

    y_values = []

    for x in x_values:
        y_values.append(basis ** x)

    chart_data = {
        "x": x_values,
        "f(x)": y_values
    }

    st.line_chart(
        chart_data,
        x="x",
        y="f(x)"
    )

    if basis > 1:

        st.success(
            f"a = {basis} > 1 → grafik menunjukkan pertumbuhan eksponensial."
        )

    elif basis < 1:

        st.warning(
            f"0 < a = {basis} < 1 → grafik menunjukkan peluruhan eksponensial."
        )

    # ========================================================
    # 24. LATIHAN
    # ========================================================

    st.subheader("24. Latihan")

    st.markdown("""
    **Soal 1**

    Tentukan nilai \(f(3)\) jika \(f(x)=2^x\).
    """)

    st.markdown("""
    **Soal 2**

    Tentukan penyelesaian \(2^{x+2}=2^6\).
    """)

    st.markdown("""
    **Soal 3**

    Tentukan penyelesaian \(3^{2x-1}=3^7\).
    """)

    st.markdown("""
    **Soal 4**

    Tentukan penyelesaian \(4^x=2^8\).
    """)

    st.markdown("""
    **Soal 5**

    Tentukan penyelesaian \(9^x=3^6\).
    """)

    st.markdown("""
    **Soal 6**

    Sebuah populasi mula-mula 2.000 orang dan bertambah
    menjadi dua kali lipat setiap periode. Tentukan populasi
    setelah 6 periode.
    """)

    st.markdown("""
    **Soal 7**

    Suatu zat mula-mula memiliki massa 1.000 gram.
    Setiap periode massanya menjadi 80% dari sebelumnya.
    Tentukan massa setelah 3 periode.
    """)

    # ========================================================
    # 25. KUIS
    # ========================================================

    st.subheader("25. Kuis Interaktif")

    jawaban = st.radio(
        "Berapakah nilai x dari 2ˣ = 32?",
        [
            "x = 3",
            "x = 4",
            "x = 5",
            "x = 6"
        ],
        key="kuis_eksponen_1"
    )

    if st.button(
        "Periksa Jawaban",
        key="cek_eksponen_1"
    ):

        if jawaban == "x = 5":

            st.success(
                "✅ Benar! Karena 32 = 2⁵, maka x = 5."
            )

        else:

            st.error(
                "❌ Belum tepat. Ubah 32 menjadi bentuk pangkat dengan basis 2."
            )

    # ========================================================
    # 26. RANGKUMAN
    # ========================================================

    with st.expander("📌 Rangkuman Materi", expanded=False):

        st.markdown("""
        ### Konsep penting

        **1. Fungsi eksponensial**

        Variabel berada pada pangkat.

        **2. Bentuk umum**

        \(f(x)=a^x\)

        dengan \(a>0\) dan \(a\neq1\).

        **3. Pertumbuhan**

        Jika \(a>1\), fungsi meningkat.

        **4. Peluruhan**

        Jika \(0<a<1\), fungsi menurun.

        **5. Persamaan eksponensial**

        Jika basis sama, eksponen dapat disamakan.

        **6. Grafik**

        Grafik melalui titik \((0,1)\), mempunyai range positif,
        dan mempunyai asimtot horizontal \(y=0\).

        **7. Penerapan**

        Fungsi eksponensial dapat digunakan untuk memodelkan
        pertumbuhan penduduk, bakteri, investasi, dan peluruhan.
        """)
