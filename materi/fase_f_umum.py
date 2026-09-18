import streamlit as st
import pandas as pd
import math

def tampilkan(materi):
    if materi == "Barisan dan Deret":
        pass
        #barisan_deret()

    elif materi == "Matematika Keuangan":
        matematika_keuangan()

    elif materi == "Fungsi, Invers dan Komposisi Fungsi":
        #fungsi_invers_komposisi()
        pass

    elif materi == "Transformasi Fungsi":
        #transformasi_fungsi()
        pass

    elif materi == "Lingkaran":
        #lingkaran()
        pass

    elif materi == "Statistika Bivariat":
        #statistika_bivariat()
        pass

    elif materi == "Kaidah Pencacahan":
        #kaidah_pencacahan()
        pass

    elif materi == "Peluang":
        #peluang()
        pass



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
