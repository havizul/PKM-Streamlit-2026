
def tampilkan(materi):

    if materi == "Barisan dan Deret":
        barisan_deret()

    elif materi == "Matematika Keuangan":
        # matematika_keuangan()
        pass

    elif materi == "Fungsi, Invers dan Komposisi Fungsi":
        # fungsi_invers_komposisi()
        pass
        
def barisan_deret():

    st.header("🔢 Barisan dan Deret")

    st.markdown("""
    ### Matematika Fase F — Kelas XI & XII

    Barisan dan deret merupakan konsep matematika yang mempelajari
    pola susunan bilangan serta jumlah suku-suku dalam suatu pola.

    Konsep ini banyak digunakan dalam perhitungan pertumbuhan,
    tabungan, investasi, cicilan, produksi, dan berbagai masalah
    kehidupan sehari-hari.
    """)

    # ========================================================
    # TUJUAN PEMBELAJARAN
    # ========================================================

    with st.expander("🎯 Tujuan Pembelajaran", expanded=True):

        st.markdown("""
        Setelah mempelajari materi ini, peserta didik diharapkan mampu:

        1. Menjelaskan pengertian barisan dan deret.
        2. Menentukan pola dan suku suatu barisan.
        3. Menentukan suku ke-n barisan aritmetika.
        4. Menentukan jumlah n suku pertama deret aritmetika.
        5. Menentukan suku ke-n barisan geometri.
        6. Menentukan jumlah n suku pertama deret geometri.
        7. Menentukan jumlah deret geometri tak hingga.
        8. Menentukan hubungan antarunsur dalam barisan dan deret.
        9. Menyelesaikan masalah kontekstual menggunakan barisan dan deret.
        10. Menganalisis pola pertumbuhan dan peluruhan menggunakan konsep deret.
        """)

    # ========================================================
    # 1. APERSEPSI
    # ========================================================

    st.subheader("1. Apersepsi")

    st.markdown("""
    Perhatikan pola bilangan berikut:
    """)

    st.latex(r"2,\ 4,\ 6,\ 8,\ 10,\ \ldots")

    st.markdown("""
    Setiap bilangan diperoleh dengan menambahkan 2 pada
    bilangan sebelumnya.

    Perhatikan pola lainnya:
    """)

    st.latex(r"3,\ 6,\ 12,\ 24,\ 48,\ \ldots")

    st.markdown("""
    Pada pola kedua, setiap bilangan diperoleh dengan mengalikan
    bilangan sebelumnya dengan 2.

    Kedua pola tersebut merupakan contoh barisan bilangan.
    """)

    # ========================================================
    # 2. BARISAN
    # ========================================================

    st.subheader("2. Pengertian Barisan")

    st.markdown("""
    Barisan adalah susunan bilangan yang memiliki aturan atau
    pola tertentu.

    Setiap bilangan dalam barisan disebut **suku**.
    """)

    st.markdown("Contoh:");

    st.latex(r"5,\ 8,\ 11,\ 14,\ 17,\ \ldots")

    st.markdown("""
    Suku pertama adalah 5, suku kedua adalah 8, dan seterusnya.
    """)

    st.latex(r"U_1=5")

    st.latex(r"U_2=8")

    st.latex(r"U_3=11")

    # ========================================================
    # 3. DERET
    # ========================================================

    st.subheader("3. Pengertian Deret")

    st.markdown("""
    Deret merupakan penjumlahan suku-suku suatu barisan.
    """)

    st.markdown("Misalnya barisan:");

    st.latex(r"2,\ 4,\ 6,\ 8,\ \ldots")

    st.markdown("Deretnya adalah:");

    st.latex(r"2+4+6+8+\ldots")

    st.info(
        "Barisan adalah susunan bilangan, sedangkan deret adalah penjumlahan suku-suku barisan."
    )

    # ========================================================
    # 4. NOTASI
    # ========================================================

    st.subheader("4. Notasi Barisan")

    st.markdown("""
    Suku ke-n biasanya ditulis dengan simbol Uₙ.
    """)

    st.latex(r"U_n")

    st.markdown("""
    Jumlah n suku pertama biasanya ditulis dengan simbol Sₙ.
    """)

    st.latex(r"S_n")

    # ========================================================
    # 5. BARISAN ARITMETIKA
    # ========================================================

    st.subheader("5. Barisan Aritmetika")

    st.markdown("""
    Barisan aritmetika adalah barisan yang memiliki selisih
    tetap antara dua suku yang berurutan.

    Selisih tetap tersebut disebut **beda** dan biasanya
    dilambangkan dengan d.
    """)

    st.markdown("Contoh:");

    st.latex(r"3,\ 7,\ 11,\ 15,\ 19,\ \ldots")

    st.latex(r"d=7-3=4")

    st.latex(r"d=11-7=4")

    st.latex(r"d=15-11=4")

    st.success("Karena bedanya tetap, barisan tersebut merupakan barisan aritmetika.")

    # ========================================================
    # 6. RUMUS SUKU KE-N ARITMETIKA
    # ========================================================

    st.subheader("6. Suku ke-n Barisan Aritmetika")

    st.markdown("""
    Rumus suku ke-n barisan aritmetika adalah:
    """)

    st.latex(r"U_n=a+(n-1)d")

    st.markdown("""
    Keterangan:

    - a = suku pertama;
    - d = beda;
    - n = nomor suku;
    - Uₙ = suku ke-n.
    """)

    # ========================================================
    # 7. CONTOH ARITMETIKA
    # ========================================================

    st.subheader("7. Contoh Menentukan Suku ke-n")

    st.markdown("""
    Diketahui barisan:
    """)

    st.latex(r"5,\ 8,\ 11,\ 14,\ldots")

    st.markdown("""
    Tentukan suku ke-20.
    """)

    st.latex(r"a=5")

    st.latex(r"d=3")

    st.latex(r"U_{20}=5+(20-1)(3)")

    st.latex(r"U_{20}=62")

    st.success("Suku ke-20 adalah 62.")

    # ========================================================
    # 8. MENENTUKAN BEDA
    # ========================================================

    st.subheader("8. Menentukan Beda")

    st.markdown("""
    Beda dapat diperoleh dengan mengurangkan suatu suku
    dengan suku sebelumnya.
    """)

    st.latex(r"d=U_n-U_{n-1}")

    st.markdown("Contoh:");

    st.latex(r"12,\ 17,\ 22,\ 27,\ldots")

    st.latex(r"d=17-12=5")

    st.success("Beda barisan adalah 5.")

    # ========================================================
    # 9. DERET ARITMETIKA
    # ========================================================

    st.subheader("9. Deret Aritmetika")

    st.markdown("""
    Deret aritmetika merupakan penjumlahan suku-suku
    dari suatu barisan aritmetika.
    """)

    st.latex(r"3+7+11+15+\ldots")

    st.markdown("""
    Jumlah n suku pertama deret aritmetika dapat dihitung
    menggunakan rumus:
    """)

    st.latex(r"S_n=\frac{n}{2}(2a+(n-1)d)")

    st.markdown("Bentuk lainnya:");

    st.latex(r"S_n=\frac{n}{2}(a+U_n)")

    # ========================================================
    # 10. CONTOH DERET ARITMETIKA
    # ========================================================

    st.subheader("10. Contoh Jumlah Deret Aritmetika")

    st.markdown("""
    Hitung jumlah 20 suku pertama dari:
    """)

    st.latex(r"5+8+11+14+\ldots")

    st.latex(r"a=5")

    st.latex(r"d=3")

    st.latex(r"n=20")

    st.latex(r"S_{20}=\frac{20}{2}(2(5)+(20-1)(3))")

    st.latex(r"S_{20}=10(67)")

    st.latex(r"S_{20}=670")

    st.success("Jumlah 20 suku pertama adalah 670.")

    # ========================================================
    # 11. BARISAN GEOMETRI
    # ========================================================

    st.subheader("11. Barisan Geometri")

    st.markdown("""
    Barisan geometri adalah barisan yang memiliki rasio
    tetap antara dua suku yang berurutan.

    Rasio biasanya dilambangkan dengan r.
    """)

    st.markdown("Contoh:");

    st.latex(r"2,\ 6,\ 18,\ 54,\ 162,\ldots")

    st.latex(r"r=\frac{6}{2}=3")

    st.latex(r"r=\frac{18}{6}=3")

    st.success("Karena rasionya tetap, barisan tersebut merupakan barisan geometri.")

    # ========================================================
    # 12. RUMUS SUKU KE-N GEOMETRI
    # ========================================================

    st.subheader("12. Suku ke-n Barisan Geometri")

    st.markdown("""
    Rumus suku ke-n barisan geometri adalah:
    """)

    st.latex(r"U_n=ar^{n-1}")

    st.markdown("""
    Keterangan:

    - a = suku pertama;
    - r = rasio;
    - n = nomor suku;
    - Uₙ = suku ke-n.
    """)

    # ========================================================
    # 13. CONTOH GEOMETRI
    # ========================================================

    st.subheader("13. Contoh Menentukan Suku ke-n Geometri")

    st.markdown("""
    Diketahui:
    """)

    st.latex(r"3,\ 6,\ 12,\ 24,\ldots")

    st.markdown("""
    Tentukan suku ke-8.
    """)

    st.latex(r"a=3")

    st.latex(r"r=2")

    st.latex(r"U_8=3(2)^{8-1}")

    st.latex(r"U_8=384")

    st.success("Suku ke-8 adalah 384.")

    # ========================================================
    # 14. MENENTUKAN RASIO
    # ========================================================

    st.subheader("14. Menentukan Rasio")

    st.markdown("""
    Rasio diperoleh dengan membagi suatu suku dengan
    suku sebelumnya.
    """)

    st.latex(r"r=\frac{U_n}{U_{n-1}}")

    st.markdown("Contoh:");

    st.latex(r"5,\ 15,\ 45,\ 135,\ldots")

    st.latex(r"r=\frac{15}{5}=3")

    st.success("Rasio barisan adalah 3.")

    # ========================================================
    # 15. DERET GEOMETRI
    # ========================================================

    st.subheader("15. Deret Geometri")

    st.markdown("""
    Deret geometri adalah penjumlahan suku-suku
    dari barisan geometri.
    """)

    st.latex(r"2+6+18+54+\ldots")

    st.markdown("""
    Jumlah n suku pertama deret geometri dapat dihitung
    menggunakan rumus:
    """)

    st.latex(r"S_n=a\frac{r^n-1}{r-1}")

    st.markdown("""
    Rumus tersebut digunakan ketika r ≠ 1.
    """)

    # ========================================================
    # 16. CONTOH DERET GEOMETRI
    # ========================================================

    st.subheader("16. Contoh Jumlah Deret Geometri")

    st.markdown("""
    Tentukan jumlah 6 suku pertama:
    """)

    st.latex(r"2+6+18+54+\ldots")

    st.latex(r"a=2")

    st.latex(r"r=3")

    st.latex(r"n=6")

    st.latex(r"S_6=2\frac{3^6-1}{3-1}")

    st.latex(r"S_6=728")

    st.success("Jumlah 6 suku pertama adalah 728.")

    # ========================================================
    # 17. DERET GEOMETRI TAK HINGGA
    # ========================================================

    st.subheader("17. Deret Geometri Tak Hingga")

    st.markdown("""
    Deret geometri tak hingga merupakan deret yang memiliki
    jumlah suku tidak terbatas.
    """)

    st.latex(r"a+ar+ar^2+ar^3+\ldots")

    st.markdown("""
    Deret tersebut memiliki jumlah hingga jika:
    """)

    st.latex(r"|r|<1")

    st.markdown("""
    Jumlah deret geometri tak hingga adalah:
    """)

    st.latex(r"S_\infty=\frac{a}{1-r}")

    # ========================================================
    # 18. CONTOH TAK HINGGA
    # ========================================================

    st.subheader("18. Contoh Deret Geometri Tak Hingga")

    st.markdown("""
    Tentukan jumlah:
    """)

    st.latex(r"8+4+2+1+\ldots")

    st.latex(r"a=8")

    st.latex(r"r=\frac{1}{2}")

    st.latex(r"S_\infty=\frac{8}{1-\frac{1}{2}}")

    st.latex(r"S_\infty=16")

    st.success("Jumlah deret geometri tak hingga adalah 16.")

    # ========================================================
    # 19. KAPAN DERET TIDAK KONVERGEN?
    # ========================================================

    st.subheader("19. Deret Tak Hingga yang Tidak Konvergen")

    st.markdown("""
    Jika nilai mutlak rasio memenuhi:
    """)

    st.latex(r"|r|\geq1")

    st.markdown("""
    maka deret geometri tak hingga tidak memiliki jumlah
    hingga atau tidak konvergen.
    """)

    st.markdown("Contoh:");

    st.latex(r"1+2+4+8+\ldots")

    st.latex(r"r=2")

    st.warning(
        "Karena |r| > 1, deret tersebut tidak memiliki jumlah hingga."
    )

    # ========================================================
    # 20. PERBANDINGAN ARITMETIKA DAN GEOMETRI
    # ========================================================

    st.subheader("20. Barisan Aritmetika vs Geometri")

    st.table({
        "Aspek": [
            "Ciri utama",
            "Konstanta",
            "Suku ke-n",
            "Contoh"
        ],
        "Aritmetika": [
            "Selisih tetap",
            "Beda d",
            "a + (n−1)d",
            "2, 5, 8, 11, ..."
        ],
        "Geometri": [
            "Rasio tetap",
            "Rasio r",
            "arⁿ⁻¹",
            "2, 6, 18, 54, ..."
        ]
    })

    # ========================================================
    # 21. SISIPAN ARITMETIKA
    # ========================================================

    st.subheader("21. Sisipan pada Barisan Aritmetika")

    st.markdown("""
    Menyisipkan bilangan aritmetika berarti menambahkan
    beberapa bilangan di antara dua bilangan sehingga
    membentuk barisan aritmetika.
    """)

    st.markdown("Contoh menyisipkan 3 bilangan antara 2 dan 18:");

    st.latex(r"2,\ \_,\ \_,\ \_,\ 18")

    st.markdown("""
    Jumlah interval adalah 4, sehingga:
    """)

    st.latex(r"d=\frac{18-2}{4}=4")

    st.latex(r"2,\ 6,\ 10,\ 14,\ 18")

    st.success("Bilangan yang disisipkan adalah 6, 10, dan 14.")

    # ========================================================
    # 22. SISIPAN GEOMETRI
    # ========================================================

    st.subheader("22. Sisipan pada Barisan Geometri")

    st.markdown("""
    Menyisipkan bilangan geometri berarti menambahkan
    bilangan di antara dua bilangan sehingga membentuk
    barisan dengan rasio tetap.
    """)

    st.markdown("Contoh:");

    st.latex(r"2,\ \_,\ \_,\ 54")

    st.markdown("""
    Karena terdapat tiga interval:
    """)

    st.latex(r"2r^3=54")

    st.latex(r"r^3=27")

    st.latex(r"r=3")

    st.latex(r"2,\ 6,\ 18,\ 54")

    # ========================================================
    # 23. HUBUNGAN SUKU
    # ========================================================

    st.subheader("23. Hubungan Antar Suku")

    st.markdown("""
    Pada barisan aritmetika, suku tengah dapat digunakan
    untuk melihat hubungan antara suku sebelum dan sesudahnya.
    """)

    st.latex(r"2U_n=U_{n-1}+U_{n+1}")

    st.markdown("""
    Pada barisan geometri:
    """)

    st.latex(r"U_n^2=U_{n-1}U_{n+1}")

    # ========================================================
    # 24. PERTUMBUHAN EKSPONENSIAL
    # ========================================================

    st.subheader("24. Barisan Geometri dalam Pertumbuhan")

    st.markdown("""
    Pertumbuhan yang memiliki faktor pengali tetap dapat
    dimodelkan menggunakan barisan geometri.
    """)

    st.markdown("""
    Misalnya jumlah bakteri mula-mula 100 dan setiap periode
    menjadi dua kali lipat.
    """)

    st.latex(r"U_n=100(2)^{n-1}")

    st.markdown("Jumlah bakteri pada periode ke-5:");

    st.latex(r"U_5=100(2)^4")

    st.latex(r"U_5=1600")

    st.success("Jumlah bakteri pada periode ke-5 adalah 1.600.")

    # ========================================================
    # 25. BUNGA MAJEMUK
    # ========================================================

    st.subheader("25. Penerapan pada Bunga Majemuk")

    st.markdown("""
    Pertumbuhan nilai investasi dengan bunga majemuk
    merupakan salah satu penerapan barisan geometri.
    """)

    st.latex(r"A=P(1+r)^n")

    st.markdown("""
    dengan:

    - A = nilai akhir;
    - P = modal awal;
    - r = tingkat pertumbuhan per periode;
    - n = jumlah periode.
    """)

    st.markdown("Contoh:");

    st.markdown("""
    Modal Rp2.000.000 mendapat pertumbuhan 5% per tahun.
    Tentukan nilai setelah 4 tahun.
    """)

    st.latex(r"A=2000000(1.05)^4")

    st.latex(r"A=2431012.5")

    st.success("Nilai setelah 4 tahun adalah Rp2.431.012,50.")

    # ========================================================
    # 26. CICILAN DAN TABUNGAN
    # ========================================================

    st.subheader("26. Penerapan dalam Tabungan")

    st.markdown("""
    Barisan dan deret dapat digunakan untuk menghitung
    akumulasi tabungan yang dilakukan secara berkala.

    Jika setiap periode seseorang menabung dengan jumlah
    yang sama, pola tersebut berkaitan dengan deret aritmetika.

    Jika jumlah tabungan bertambah berdasarkan faktor pengali
    tetap, pola tersebut dapat berkaitan dengan deret geometri.
    """)

    # ========================================================
    # 27. EKSPERIMEN BARISAN
    # ========================================================

    st.subheader("27. Eksplorasi Barisan Interaktif")

    jenis_barisan = st.selectbox(
        "Pilih jenis barisan",
        [
            "Aritmetika",
            "Geometri"
        ],
        key="jenis_barisan"
    )

    suku_awal = st.number_input(
        "Suku pertama",
        value=2.0,
        step=1.0,
        key="suku_awal_barisan"
    )

    parameter = st.number_input(
        "Beda / Rasio",
        value=3.0,
        step=1.0,
        key="parameter_barisan"
    )

    jumlah_suku = st.slider(
        "Jumlah suku",
        min_value=3,
        max_value=20,
        value=10,
        step=1,
        key="jumlah_suku_barisan"
    )

    if jenis_barisan == "Aritmetika":

        data_barisan = [
            suku_awal + i * parameter
            for i in range(jumlah_suku)
        ]

        st.latex(r"U_n=a+(n-1)d")

    else:

        data_barisan = [
            suku_awal * parameter ** i
            for i in range(jumlah_suku)
        ]

        st.latex(r"U_n=ar^{n-1}")

    df_barisan = pd.DataFrame({
        "Suku ke-n": range(1, jumlah_suku + 1),
        "Nilai": data_barisan
    })

    st.table(df_barisan)

    # ========================================================
    # 28. VISUALISASI BARISAN
    # ========================================================

    st.subheader("28. Grafik Barisan")

    df_grafik = pd.DataFrame({
        "n": range(1, jumlah_suku + 1),
        "U_n": data_barisan
    })

    st.line_chart(
        df_grafik,
        x="n",
        y="U_n"
    )

    # ========================================================
    # 29. KALKULATOR BARISAN
    # ========================================================

    st.subheader("29. Kalkulator Suku ke-n")

    kalkulator_jenis = st.selectbox(
        "Jenis barisan",
        [
            "Aritmetika",
            "Geometri"
        ],
        key="kalkulator_jenis_barisan"
    )

    a_kalkulator = st.number_input(
        "Nilai a",
        value=2.0,
        key="a_kalkulator"
    )

    parameter_kalkulator = st.number_input(
        "Nilai d atau r",
        value=3.0,
        key="parameter_kalkulator"
    )

    n_kalkulator = st.number_input(
        "Nilai n",
        min_value=1,
        value=10,
        step=1,
        key="n_kalkulator"
    )

    if kalkulator_jenis == "Aritmetika":

        hasil_un = a_kalkulator + (n_kalkulator - 1) * parameter_kalkulator

        st.latex(r"U_n=a+(n-1)d")

    else:

        hasil_un = a_kalkulator * parameter_kalkulator ** (n_kalkulator - 1)

        st.latex(r"U_n=ar^{n-1}")

    st.metric(
        "Suku ke-n",
        f"{hasil_un:.2f}"
    )

    # ========================================================
    # 30. KALKULATOR JUMLAH DERET
    # ========================================================

    st.subheader("30. Kalkulator Jumlah n Suku")

    deret_jenis = st.selectbox(
        "Jenis deret",
        [
            "Aritmetika",
            "Geometri"
        ],
        key="deret_jenis"
    )

    a_deret = st.number_input(
        "Suku pertama",
        value=2.0,
        key="a_deret"
    )

    parameter_deret = st.number_input(
        "Beda / Rasio",
        value=3.0,
        key="parameter_deret"
    )

    n_deret = st.number_input(
        "Jumlah suku",
        min_value=1,
        value=5,
        step=1,
        key="n_deret"
    )

    if deret_jenis == "Aritmetika":

        hasil_sn = (
            n_deret / 2
        ) * (
            2 * a_deret
            + (n_deret - 1) * parameter_deret
        )

        st.latex(r"S_n=\frac{n}{2}(2a+(n-1)d)")

    else:

        if parameter_deret == 1:

            hasil_sn = a_deret * n_deret

        else:

            hasil_sn = (
                a_deret
                * (
                    parameter_deret ** n_deret - 1
                )
                / (
                    parameter_deret - 1
                )
            )

        st.latex(r"S_n=a\frac{r^n-1}{r-1}")

    st.metric(
        "Jumlah n suku",
        f"{hasil_sn:.2f}"
    )

    # ========================================================
    # 31. LATIHAN
    # ========================================================

    st.subheader("31. Latihan")

    st.markdown("""
    **Soal 1**

    Tentukan suku ke-15 dari barisan:

    4, 7, 10, 13, ...
    """)

    st.markdown("""
    **Soal 2**

    Tentukan jumlah 20 suku pertama dari:

    3 + 7 + 11 + 15 + ...
    """)

    st.markdown("""
    **Soal 3**

    Tentukan suku ke-8 dari barisan:

    2, 6, 18, 54, ...
    """)

    st.markdown("""
    **Soal 4**

    Tentukan jumlah 6 suku pertama dari:

    5 + 10 + 20 + 40 + ...
    """)

    st.markdown("""
    **Soal 5**

    Tentukan jumlah deret tak hingga:

    12 + 6 + 3 + 1,5 + ...
    """)

    st.markdown("""
    **Soal 6**

    Tentukan apakah barisan berikut merupakan aritmetika,
    geometri, atau bukan keduanya:

    2, 6, 18, 54, ...
    """)

    st.markdown("""
    **Soal 7**

    Sebuah populasi bakteri mula-mula 500.
    Setiap periode jumlahnya menjadi tiga kali lipat.
    Tentukan jumlah bakteri pada periode ke-6.
    """)

    st.markdown("""
    **Soal 8**

    Seseorang menabung Rp100.000 pada bulan pertama.
    Setiap bulan jumlah tabungannya bertambah Rp25.000.
    Tentukan total tabungan selama 12 bulan.
    """)

    # ========================================================
    # 32. KUIS
    # ========================================================

    st.subheader("32. Kuis Interaktif")

    jawaban = st.radio(
        "Barisan 5, 8, 11, 14, ... merupakan barisan...",
        [
            "Geometri dengan r = 3",
            "Aritmetika dengan d = 3",
            "Aritmetika dengan d = 4",
            "Geometri dengan r = 4"
        ],
        key="kuis_barisan_1"
    )

    if st.button(
        "Periksa Jawaban",
        key="cek_barisan_1"
    ):

        if jawaban == "Aritmetika dengan d = 3":

            st.success(
                "✅ Benar! Selisih setiap suku adalah 3."
            )

        else:

            st.error(
                "❌ Belum tepat. Periksa selisih atau rasio antar suku."
            )

    # ========================================================
    # 33. RANGKUMAN
    # ========================================================

    with st.expander("📌 Rangkuman Materi", expanded=False):

        st.markdown("""
        ### Barisan

        Barisan adalah susunan bilangan yang memiliki pola tertentu.

        ### Deret

        Deret adalah penjumlahan suku-suku dalam suatu barisan.

        ### Barisan Aritmetika

        Memiliki beda yang tetap.

        """)

        st.latex(r"U_n=a+(n-1)d")

        st.latex(r"S_n=\frac{n}{2}(2a+(n-1)d)")

        st.markdown("""
        ### Barisan Geometri

        Memiliki rasio yang tetap.

        """)

        st.latex(r"U_n=ar^{n-1}")

        st.latex(r"S_n=a\frac{r^n-1}{r-1}")

        st.markdown("""
        ### Deret Geometri Tak Hingga

        Memiliki jumlah hingga jika:
        """)

        st.latex(r"|r|<1")

        st.latex(r"S_\infty=\frac{a}{1-r}")

        st.markdown("""
        ### Penerapan

        Barisan dan deret dapat digunakan untuk memodelkan
        pertumbuhan, tabungan, investasi, produksi, populasi,
        dan berbagai pola kuantitatif dalam kehidupan nyata.
        """)
