import streamlit as st
import pandas as pd
import math

def tampilkan(materi):

    if materi == "Barisan dan Deret":
        barisan_deret()

    elif materi == "Matematika Keuangan":
        matematika_keuangan()
        #pass

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




# ============================================================
# MATEMATIKA KEUANGAN
# ============================================================

def matematika_keuangan():

    st.header("💰 Matematika Keuangan")

    st.markdown("""
    Matematika keuangan merupakan penerapan konsep matematika
    untuk menyelesaikan berbagai permasalahan yang berkaitan
    dengan uang, tabungan, bunga, pinjaman, investasi,
    angsuran, dan pertumbuhan nilai uang.
    """)

    # ========================================================
    # TUJUAN PEMBELAJARAN
    # ========================================================

    st.subheader("🎯 Tujuan Pembelajaran")

    st.markdown("""
    Setelah mempelajari materi ini, peserta didik diharapkan mampu:

    1. Menjelaskan konsep bunga tunggal dan bunga majemuk.
    2. Menghitung nilai akhir suatu tabungan atau investasi.
    3. Menghitung besar bunga yang diperoleh.
    4. Menyelesaikan permasalahan diskonto.
    5. Menghitung pertumbuhan nilai uang.
    6. Menghitung cicilan dan angsuran sederhana.
    7. Menganalisis permasalahan keuangan dalam kehidupan sehari-hari.
    """)

    st.divider()

    # ========================================================
    # 1. APERSEPSI
    # ========================================================

    st.subheader("1. Apersepsi")

    st.markdown("""
    Pernahkah kamu menabung di bank?

    Misalnya kamu memiliki uang sebesar Rp5.000.000 dan menyimpannya
    selama beberapa tahun. Apakah jumlah uang tersebut akan tetap sama?

    Jika bank memberikan bunga, maka uang yang kamu simpan dapat
    bertambah dari waktu ke waktu.

    Sebaliknya, ketika seseorang meminjam uang, biasanya terdapat
    tambahan pembayaran yang disebut bunga.
    """)

    st.info("""
    💡 **Pertanyaan pemantik**

    Jika Rp10.000.000 ditabung dengan bunga 5% per tahun,
    berapa jumlah uang setelah 1 tahun?
    """)

    # ========================================================
    # 2. KONSEP DASAR
    # ========================================================

    st.subheader("2. Konsep Dasar Matematika Keuangan")

    st.markdown("""
    Beberapa istilah penting dalam matematika keuangan adalah:

    **Modal awal (P)**  
    Jumlah uang yang dimiliki atau ditanamkan pada awal periode.

    **Bunga (I)**  
    Tambahan uang yang diperoleh dari tabungan/investasi atau
    tambahan pembayaran pada pinjaman.

    **Nilai akhir (A)**  
    Jumlah uang setelah modal ditambah bunga.

    **Suku bunga (r)**  
    Persentase bunga dalam suatu periode.

    **Waktu (t)**  
    Lama uang disimpan, diinvestasikan, atau dipinjam.
    """)

    st.latex(r"A=P+I")

    # ========================================================
    # 3. PERSENTASE
    # ========================================================

    st.subheader("3. Persentase")

    st.markdown("""
    Persentase menunjukkan suatu bagian dari keseluruhan dalam
    bentuk per seratus.
    """)

    st.latex(r"p\%= \frac{p}{100}")

    st.markdown("""
    Contoh:

    Bunga 8% berarti setiap Rp100 uang pokok menghasilkan bunga
    sebesar Rp8 dalam satu periode.
    """)

    st.latex(r"8\%=\frac{8}{100}=0,08")

    st.markdown("""
    Jika modal awal Rp2.000.000 dan bunga 8%, maka bunga untuk
    satu periode adalah:
    """)

    st.latex(r"I=0,08(2.000.000)=160.000")

    st.success("Bunga yang diperoleh adalah **Rp160.000**.")

    # ========================================================
    # 4. BUNGA TUNGGAL
    # ========================================================

    st.subheader("4. Bunga Tunggal")

    st.markdown("""
    **Bunga tunggal** adalah bunga yang setiap periodenya dihitung
    berdasarkan modal awal yang tetap.

    Artinya, bunga yang diperoleh tidak ditambahkan ke modal
    untuk menghitung bunga pada periode berikutnya.
    """)

    st.latex(r"I=P\cdot r\cdot t")

    st.markdown("""
    Keterangan:

    - \(P\) = modal awal
    - \(r\) = tingkat bunga per periode
    - \(t\) = banyak periode
    - \(I\) = bunga
    """)

    st.markdown("### Nilai Akhir Bunga Tunggal")

    st.latex(r"A=P(1+rt)")

    st.markdown("""
    **Contoh**

    Modal Rp5.000.000 ditabung dengan bunga tunggal 6% per tahun
    selama 3 tahun.

    """)

    st.latex(r"I=5.000.000(0,06)(3)")

    st.latex(r"I=900.000")

    st.latex(r"A=5.000.000+900.000")

    st.latex(r"A=5.900.000")

    st.success("Nilai akhir tabungan adalah **Rp5.900.000**.")

    # ========================================================
    # 5. BUNGA MAJEMUK
    # ========================================================

    st.subheader("5. Bunga Majemuk")

    st.markdown("""
    **Bunga majemuk** adalah bunga yang pada setiap periode
    ditambahkan ke modal sehingga pada periode berikutnya
    bunga dihitung berdasarkan modal yang sudah bertambah.
    """)

    st.latex(r"A=P(1+r)^t")

    st.markdown("""
    Keterangan:

    - \(P\) = modal awal
    - \(r\) = tingkat bunga per periode
    - \(t\) = jumlah periode
    - \(A\) = nilai akhir
    """)

    st.markdown("""
    **Contoh**

    Uang Rp10.000.000 diinvestasikan dengan bunga majemuk
    5% per tahun selama 3 tahun.
    """)

    st.latex(r"A=10.000.000(1+0,05)^3")

    st.latex(r"A=10.000.000(1,05)^3")

    st.latex(r"A=11.576.250")

    st.success("Nilai investasi setelah 3 tahun adalah **Rp11.576.250**.")

    # ========================================================
    # 6. PERBANDINGAN BUNGA
    # ========================================================

    st.subheader("6. Perbandingan Bunga Tunggal dan Majemuk")

    st.markdown("""
    Perbedaan utama:

    | Bunga Tunggal | Bunga Majemuk |
    |---|---|
    | Bunga dihitung dari modal awal | Bunga dihitung dari saldo yang berkembang |
    | Bunga setiap periode tetap | Bunga setiap periode dapat berubah |
    | Pertumbuhan linear | Pertumbuhan eksponensial |
    | Rumus \(A=P(1+rt)\) | Rumus \(A=P(1+r)^t\) |
    """)

    st.info("""
    📌 Dalam bunga majemuk, bunga pada periode sebelumnya
    ikut menghasilkan bunga pada periode berikutnya.
    """)

    # ========================================================
    # 7. BUNGA MAJEMUK PERIODE BERBEDA
    # ========================================================

    st.subheader("7. Bunga Majemuk dengan Beberapa Periode per Tahun")

    st.markdown("""
    Jika bunga diberikan beberapa kali dalam satu tahun,
    maka tingkat bunga dan jumlah periode harus disesuaikan.
    """)

    st.latex(r"A=P\left(1+\frac{r}{m}\right)^{mt}")

    st.markdown("""
    Keterangan:

    - \(m\) = banyak periode pembungaan dalam satu tahun
    - \(r\) = tingkat bunga tahunan
    - \(t\) = lama investasi dalam tahun
    """)

    st.markdown("""
    Contoh:

    Modal Rp10.000.000 mendapat bunga nominal 12% per tahun
    yang dibayarkan setiap bulan selama 2 tahun.
    """)

    st.latex(r"A=10.000.000\left(1+\frac{0,12}{12}\right)^{12(2)}")

    st.latex(r"A=10.000.000(1,01)^{24}")

    st.latex(r"A\approx12.697.346")

    # ========================================================
    # 8. PERTUMBUHAN NILAI
    # ========================================================

    st.subheader("8. Pertumbuhan Nilai Uang")

    st.markdown("""
    Model pertumbuhan eksponensial dapat digunakan untuk
    menggambarkan perkembangan investasi atau tabungan.
    """)

    st.latex(r"A_t=A_0(1+r)^t")

    st.markdown("""
    Model tersebut memiliki bentuk yang sama dengan barisan geometri.

    Artinya, matematika keuangan berkaitan erat dengan materi
    **barisan dan deret**.
    """)

    # ========================================================
    # 9. INFLASI
    # ========================================================

    st.subheader("9. Inflasi dan Nilai Uang")

    st.markdown("""
    Inflasi menyebabkan daya beli uang menurun dari waktu ke waktu.

    Jika tingkat inflasi sebesar \(r\) per tahun, maka secara
    sederhana nilai riil uang dapat dimodelkan dengan:
    """)

    st.latex(r"V_t=\frac{V_0}{(1+r)^t}")

    st.markdown("""
    Contoh:

    Uang Rp10.000.000 dengan inflasi 5% per tahun selama 3 tahun
    memiliki daya beli setara dengan:
    """)

    st.latex(r"V_t=\frac{10.000.000}{(1,05)^3}")

    st.latex(r"V_t\approx8.638.376")

    st.info("""
    Nilai tersebut merupakan pendekatan matematis terhadap
    daya beli berdasarkan model inflasi konstan.
    """)

    # ========================================================
    # 10. DISKONTO
    # ========================================================

    st.subheader("10. Diskonto")

    st.markdown("""
    Diskonto merupakan potongan atau pengurangan dari nilai nominal
    suatu pembayaran.

    Jika nilai nominal adalah \(N\) dan tingkat diskonto \(d\),
    maka besar diskonto:
    """)

    st.latex(r"D=N\cdot d\cdot t")

    st.markdown("Nilai tunai dapat dihitung dengan:")

    st.latex(r"V=N-D")

    st.markdown("""
    **Contoh**

    Sebuah surat memiliki nilai nominal Rp10.000.000 dengan
    diskonto 6% selama 1 tahun.
    """)

    st.latex(r"D=10.000.000(0,06)(1)")

    st.latex(r"D=600.000")

    st.latex(r"V=10.000.000-600.000")

    st.latex(r"V=9.400.000")

    st.success("Nilai tunainya adalah **Rp9.400.000**.")

    # ========================================================
    # 11. PINJAMAN
    # ========================================================

    st.subheader("11. Pinjaman")

    st.markdown("""
    Dalam kehidupan sehari-hari seseorang dapat meminjam uang
    untuk memenuhi kebutuhan tertentu.

    Jumlah pembayaran pinjaman bergantung pada:

    - jumlah pinjaman,
    - tingkat bunga,
    - jangka waktu,
    - sistem pembayaran,
    - dan frekuensi pembayaran.
    """)

    # ========================================================
    # 12. BUNGA PINJAMAN SEDERHANA
    # ========================================================

    st.subheader("12. Pinjaman dengan Bunga Tunggal")

    st.markdown("""
    Jika pinjaman menggunakan bunga tunggal, total bunga dapat
    dihitung dengan:
    """)

    st.latex(r"I=P\cdot r\cdot t")

    st.markdown("""
    Total pembayaran:
    """)

    st.latex(r"A=P+I")

    st.markdown("""
    Contoh:

    Seseorang meminjam Rp12.000.000 dengan bunga tunggal
    10% per tahun selama 2 tahun.
    """)

    st.latex(r"I=12.000.000(0,10)(2)")

    st.latex(r"I=2.400.000")

    st.latex(r"A=12.000.000+2.400.000")

    st.latex(r"A=14.400.000")

    st.success("Total pembayaran adalah **Rp14.400.000**.")

    # ========================================================
    # 13. ANGSURAN SEDERHANA
    # ========================================================

    st.subheader("13. Angsuran Sederhana")

    st.markdown("""
    Jika total pembayaran dibagi rata dalam sejumlah periode,
    maka besar angsuran sederhana dapat dihitung dengan:
    """)

    st.latex(r"C=\frac{A}{n}")

    st.markdown("""
    dengan:

    - \(C\) = cicilan per periode
    - \(A\) = total pembayaran
    - \(n\) = jumlah periode pembayaran
    """)

    st.markdown("""
    Contoh:

    Total pembayaran Rp14.400.000 dilakukan dalam 24 bulan.
    """)

    st.latex(r"C=\frac{14.400.000}{24}")

    st.latex(r"C=600.000")

    st.success("Angsuran sederhana adalah **Rp600.000 per bulan**.")

    # ========================================================
    # 14. ANUITAS
    # ========================================================

    st.subheader("14. Anuitas")

    st.markdown("""
    Dalam sistem anuitas, pembayaran dilakukan secara berkala
    dengan jumlah pembayaran yang sama.

    Nilai sekarang anuitas biasa dapat dihitung dengan:
    """)

    st.latex(r"PV=C\frac{1-(1+r)^{-n}}{r}")

    st.markdown("""
    Jika ingin mencari besar pembayaran periodik:
    """)

    st.latex(r"C=PV\frac{r(1+r)^n}{(1+r)^n-1}")

    st.markdown("""
    Keterangan:

    - \(PV\) = nilai pinjaman saat ini
    - \(C\) = pembayaran setiap periode
    - \(r\) = bunga per periode
    - \(n\) = jumlah pembayaran
    """)

    st.markdown("""
    **Contoh**

    Pinjaman Rp12.000.000 dengan bunga 1% per bulan
    akan dibayar selama 12 bulan.
    """)

    st.latex(r"C=12.000.000\frac{0,01(1,01)^{12}}{(1,01)^{12}-1}")

    st.latex(r"C\approx1.066.185")

    st.info("Angsuran per bulan sekitar **Rp1.066.185**.")

    # ========================================================
    # 15. NILAI SEKARANG
    # ========================================================

    st.subheader("15. Nilai Sekarang dan Nilai Masa Depan")

    st.markdown("""
    Dalam matematika keuangan, nilai uang dapat dilihat berdasarkan
    waktu.

    Nilai masa depan:
    """)

    st.latex(r"FV=PV(1+r)^n")

    st.markdown("""
    Nilai sekarang:
    """)

    st.latex(r"PV=\frac{FV}{(1+r)^n}")

    st.markdown("""
    Konsep ini penting dalam investasi, tabungan, pinjaman,
    dan perencanaan keuangan.
    """)

    # ========================================================
    # 16. INVESTASI
    # ========================================================

    st.subheader("16. Matematika Keuangan dalam Investasi")

    st.markdown("""
    Matematika keuangan dapat digunakan untuk menghitung
    perkembangan modal investasi.

    Misalnya modal awal sebesar Rp20.000.000 tumbuh rata-rata
    8% per tahun selama 5 tahun.
    """)

    st.latex(r"FV=20.000.000(1,08)^5")

    st.latex(r"FV\approx29.386.564")

    st.success("Nilai teoritis setelah 5 tahun sekitar **Rp29.386.564**.")

    st.warning("""
    ⚠️ Model matematika tersebut mengasumsikan tingkat pertumbuhan
    tetap. Dalam investasi nyata, tingkat keuntungan dapat berubah
    dan tidak selalu tetap setiap tahun.
    """)

    # ========================================================
    # 17. INTERAKTIF BUNGA TUNGGAL
    # ========================================================

    st.subheader("17. 🧮 Kalkulator Bunga Tunggal")

    col1, col2 = st.columns(2)

    with col1:

        modal_tunggal = st.number_input(
            "Modal awal (Rp)",
            min_value=0.0,
            value=10000000.0,
            step=500000.0,
            key="modal_tunggal"
        )

        bunga_tunggal = st.number_input(
            "Bunga per tahun (%)",
            min_value=0.0,
            value=5.0,
            step=0.5,
            key="bunga_tunggal"
        )

    with col2:

        waktu_tunggal = st.number_input(
            "Waktu (tahun)",
            min_value=1,
            value=5,
            step=1,
            key="waktu_tunggal"
        )

        r_tunggal = bunga_tunggal / 100

        bunga_hasil = modal_tunggal * r_tunggal * waktu_tunggal

        nilai_akhir_tunggal = modal_tunggal + bunga_hasil

    st.markdown("### Hasil")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Total Bunga",
            f"Rp{bunga_hasil:,.0f}"
        )

    with col2:
        st.metric(
            "Nilai Akhir",
            f"Rp{nilai_akhir_tunggal:,.0f}"
        )

    # ========================================================
    # 18. INTERAKTIF BUNGA MAJEMUK
    # ========================================================

    st.subheader("18. 📈 Kalkulator Bunga Majemuk")

    col1, col2 = st.columns(2)

    with col1:

        modal_majemuk = st.number_input(
            "Modal awal (Rp)",
            min_value=0.0,
            value=10000000.0,
            step=500000.0,
            key="modal_majemuk"
        )

        bunga_majemuk = st.number_input(
            "Bunga per tahun (%)",
            min_value=0.0,
            value=5.0,
            step=0.5,
            key="bunga_majemuk"
        )

    with col2:

        waktu_majemuk = st.number_input(
            "Waktu (tahun)",
            min_value=1,
            value=5,
            step=1,
            key="waktu_majemuk"
        )

        r_majemuk = bunga_majemuk / 100

        nilai_akhir_majemuk = (
            modal_majemuk *
            (1 + r_majemuk) ** waktu_majemuk
        )

        bunga_majemuk_hasil = (
            nilai_akhir_majemuk -
            modal_majemuk
        )

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Total Bunga",
            f"Rp{bunga_majemuk_hasil:,.0f}"
        )

    with col2:
        st.metric(
            "Nilai Akhir",
            f"Rp{nilai_akhir_majemuk:,.0f}"
        )

    # ========================================================
    # 19. PERBANDINGAN INTERAKTIF
    # ========================================================

    st.subheader("19. 📊 Perbandingan Bunga Tunggal dan Majemuk")

    modal_perbandingan = st.number_input(
        "Modal awal untuk perbandingan (Rp)",
        min_value=100000.0,
        value=10000000.0,
        step=500000.0,
        key="modal_perbandingan"
    )

    bunga_perbandingan = st.number_input(
        "Tingkat bunga per tahun (%)",
        min_value=0.0,
        value=8.0,
        step=0.5,
        key="bunga_perbandingan"
    )

    tahun_perbandingan = st.slider(
        "Jumlah tahun",
        min_value=1,
        max_value=20,
        value=10,
        key="tahun_perbandingan"
    )

    r_perbandingan = bunga_perbandingan / 100

    data_perbandingan = []

    for tahun in range(1, tahun_perbandingan + 1):

        bunga_tunggal_tahun = (
            modal_perbandingan *
            (1 + r_perbandingan * tahun)
        )

        bunga_majemuk_tahun = (
            modal_perbandingan *
            (1 + r_perbandingan) ** tahun
        )

        data_perbandingan.append({
            "Tahun": tahun,
            "Bunga Tunggal": bunga_tunggal_tahun,
            "Bunga Majemuk": bunga_majemuk_tahun
        })

    df_perbandingan = pd.DataFrame(data_perbandingan)

    st.table(
        df_perbandingan.style.format({
            "Bunga Tunggal": "Rp{:,.0f}",
            "Bunga Majemuk": "Rp{:,.0f}"
        })
    )

    st.line_chart(
        df_perbandingan.set_index("Tahun")
    )

    # ========================================================
    # 20. KALKULATOR ANUITAS
    # ========================================================

    st.subheader("20. 🏦 Kalkulator Angsuran Anuitas")

    col1, col2 = st.columns(2)

    with col1:

        pinjaman = st.number_input(
            "Jumlah pinjaman (Rp)",
            min_value=100000.0,
            value=10000000.0,
            step=500000.0,
            key="pinjaman_anuitas"
        )

        bunga_bulanan = st.number_input(
            "Bunga per bulan (%)",
            min_value=0.01,
            value=1.0,
            step=0.1,
            key="bunga_bulanan_anuitas"
        )

    with col2:

        jumlah_bulan = st.number_input(
            "Jumlah bulan",
            min_value=1,
            value=12,
            step=1,
            key="jumlah_bulan_anuitas"
        )

    r_bulanan = bunga_bulanan / 100

    if r_bulanan > 0:

        angsuran = (
            pinjaman *
            (
                r_bulanan *
                (1 + r_bulanan) ** jumlah_bulan
            ) /
            (
                (1 + r_bulanan) ** jumlah_bulan - 1
            )
        )

    else:

        angsuran = pinjaman / jumlah_bulan

    total_pembayaran = angsuran * jumlah_bulan

    total_bunga = total_pembayaran - pinjaman

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Angsuran / Bulan",
            f"Rp{angsuran:,.0f}"
        )

    with col2:
        st.metric(
            "Total Pembayaran",
            f"Rp{total_pembayaran:,.0f}"
        )

    with col3:
        st.metric(
            "Total Bunga",
            f"Rp{total_bunga:,.0f}"
        )

    # ========================================================
    # 21. TABEL AMORTISASI SEDERHANA
    # ========================================================

    st.subheader("21. 📋 Tabel Angsuran")

    saldo = pinjaman
    data_angsuran = []

    for periode in range(1, jumlah_bulan + 1):

        bunga_periode = saldo * r_bulanan

        pokok_periode = angsuran - bunga_periode

        saldo_akhir = saldo - pokok_periode

        if saldo_akhir < 0:
            saldo_akhir = 0

        data_angsuran.append({
            "Periode": periode,
            "Angsuran": angsuran,
            "Bunga": bunga_periode,
            "Pokok": pokok_periode,
            "Sisa Pinjaman": saldo_akhir
        })

        saldo = saldo_akhir

    df_angsuran = pd.DataFrame(data_angsuran)

    st.table(
        df_angsuran.style.format({
            "Angsuran": "Rp{:,.0f}",
            "Bunga": "Rp{:,.0f}",
            "Pokok": "Rp{:,.0f}",
            "Sisa Pinjaman": "Rp{:,.0f}"
        })
    )

    # ========================================================
    # 22. STUDI KASUS
    # ========================================================

    st.subheader("22. 🧩 Studi Kasus")

    st.markdown("""
    **Kasus 1 — Tabungan**

    Andi menabung Rp8.000.000 dengan bunga tunggal 6% per tahun
    selama 4 tahun.

    Tentukan:

    1. Besar bunga.
    2. Nilai akhir tabungan.
    """)

    st.latex(r"I=8.000.000(0,06)(4)")

    st.latex(r"I=1.920.000")

    st.latex(r"A=8.000.000+1.920.000")

    st.latex(r"A=9.920.000")

    st.markdown("""
    Jadi bunga yang diperoleh adalah **Rp1.920.000** dan nilai
    akhir tabungan adalah **Rp9.920.000**.
    """)

    # ========================================================
    # 23. STUDI KASUS BUNGA MAJEMUK
    # ========================================================

    st.subheader("23. Studi Kasus Bunga Majemuk")

    st.markdown("""
    Siti memiliki modal Rp15.000.000 dan menginvestasikannya
    dengan pertumbuhan 7% per tahun selama 5 tahun.
    """)

    st.latex(r"A=15.000.000(1,07)^5")

    st.latex(r"A\approx21.038.283")

    st.success("Nilai akhir sekitar **Rp21.038.283**.")

    # ========================================================
    # 24. SOAL LATIHAN
    # ========================================================

    st.subheader("24. ✏️ Latihan")

    st.markdown("""
    **Soal 1**

    Modal Rp4.000.000 disimpan dengan bunga tunggal 5% per tahun
    selama 3 tahun. Tentukan nilai akhirnya.

    **Soal 2**

    Modal Rp10.000.000 diinvestasikan dengan bunga majemuk 6%
    per tahun selama 4 tahun. Tentukan nilai akhirnya.

    **Soal 3**

    Pinjaman Rp20.000.000 dikenakan bunga tunggal 8% per tahun
    selama 2 tahun. Tentukan total pembayaran.

    **Soal 4**

    Pinjaman Rp12.000.000 memiliki bunga 1% per bulan dan
    dibayar selama 12 bulan dengan sistem anuitas.
    Tentukan perkiraan angsuran per bulan.

    **Soal 5**

    Jelaskan mengapa bunga majemuk dapat menghasilkan pertumbuhan
    yang lebih besar dibandingkan bunga tunggal dalam jangka panjang.
    """)

    # ========================================================
    # 25. KUIS
    # ========================================================

    st.subheader("25. 📝 Kuis")

    q1 = st.radio(
        "1. Rumus bunga tunggal adalah ...",
        [
            "I = P + r + t",
            "I = P × r × t",
            "I = P(1+r)^t",
            "I = P/r/t"
        ],
        key="kuis_keuangan_1"
    )

    if q1:
        if q1 == "I = P × r × t":
            st.success("✅ Benar!")
        else:
            st.error("❌ Jawaban belum tepat.")

    q2 = st.radio(
        "2. Rumus nilai akhir bunga majemuk adalah ...",
        [
            "A = P + r + t",
            "A = P(1+r)^t",
            "A = P × r × t",
            "A = P/r"
        ],
        key="kuis_keuangan_2"
    )

    if q2:
        if q2 == "A = P(1+r)^t":
            st.success("✅ Benar!")
        else:
            st.error("❌ Jawaban belum tepat.")

    q3 = st.radio(
        "3. Jika modal Rp10.000.000 dan bunga 10% per tahun, "
        "maka bunga satu tahun adalah ...",
        [
            "Rp100.000",
            "Rp500.000",
            "Rp1.000.000",
            "Rp10.000.000"
        ],
        key="kuis_keuangan_3"
    )

    if q3:
        if q3 == "Rp1.000.000":
            st.success("✅ Benar!")
        else:
            st.error("❌ Jawaban belum tepat.")

    q4 = st.radio(
        "4. Bunga majemuk berbeda dari bunga tunggal karena ...",
        [
            "Tidak menggunakan modal",
            "Bunga sebelumnya ikut menjadi bagian modal",
            "Tidak menggunakan persentase",
            "Selalu menghasilkan kerugian"
        ],
        key="kuis_keuangan_4"
    )

    if q4:
        if q4 == "Bunga sebelumnya ikut menjadi bagian modal":
            st.success("✅ Benar!")
        else:
            st.error("❌ Jawaban belum tepat.")

    # ========================================================
    # 26. REFLEKSI
    # ========================================================

    st.subheader("26. 💭 Refleksi")

    st.markdown("""
    Setelah mempelajari matematika keuangan, coba pikirkan:

    - Mengapa seseorang perlu memahami bunga sebelum meminjam uang?
    - Apa perbedaan pertumbuhan linear dan eksponensial dalam keuangan?
    - Bagaimana inflasi memengaruhi daya beli?
    - Mengapa waktu menjadi faktor penting dalam investasi?
    - Bagaimana matematika membantu mengambil keputusan keuangan?
    """)

    # ========================================================
    # 27. RANGKUMAN
    # ========================================================

    st.subheader("27. 📚 Rangkuman")

    st.markdown("""
    ### Matematika Keuangan

    Matematika keuangan digunakan untuk memodelkan berbagai
    permasalahan yang berkaitan dengan uang dan waktu.

    ### Bunga Tunggal

    Bunga selalu dihitung berdasarkan modal awal.

    """)

    st.latex(r"I=P\cdot r\cdot t")

    st.latex(r"A=P(1+rt)")

    st.markdown("""
    ### Bunga Majemuk

    Bunga pada periode sebelumnya ditambahkan ke modal.
    """)

    st.latex(r"A=P(1+r)^t")

    st.markdown("""
    ### Bunga Majemuk Berkala
    """)

    st.latex(r"A=P\left(1+\frac{r}{m}\right)^{mt}")

    st.markdown("""
    ### Nilai Sekarang
    """)

    st.latex(r"PV=\frac{FV}{(1+r)^n}")

    st.markdown("""
    ### Nilai Masa Depan
    """)

    st.latex(r"FV=PV(1+r)^n")

    st.markdown("""
    ### Anuitas
    """)

    st.latex(r"C=PV\frac{r(1+r)^n}{(1+r)^n-1}")

    st.success("""
    🎯 **Inti pembelajaran**

    Matematika keuangan menunjukkan bahwa nilai uang tidak hanya
    ditentukan oleh jumlahnya, tetapi juga oleh **waktu, tingkat
    pertumbuhan, bunga, dan sistem pembayaran**.
    """)
