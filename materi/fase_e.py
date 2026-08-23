import streamlit as st
import numpy as np
import plotly.graph_objects as go

def tampilkan(materi):

    if materi == "Bilangan Berpangkat":
        bilangan_berpangkat()

    elif materi == "Persamaan dan Fungsi Eksponensial":
        # materi berikutnya
        #pass
        persamaan_fungsi_eksponensial()

    elif materi == "SPtLDV":
        # materi berikutnya
        #pass
        sptldv()
        
    elif materi == "Persamaan dan Fungsi Kuadrat":
        persamaan_fungsi_kuadrat()

    elif materi == "Trigonometri I":
        trigonometri_1()
        
    elif materi == "Statistika":
        statistika()
        
    # dan seterusnya

def statistika():

    st.header("📊 Statistika")

    st.markdown("""
    ### Matematika Kelas X — Fase E

    Statistika merupakan cabang matematika yang mempelajari
    cara mengumpulkan, menyajikan, mengolah, menganalisis,
    dan menginterpretasikan data.

    Statistika digunakan dalam pendidikan, ekonomi, kesehatan,
    penelitian, bisnis, pemerintahan, teknologi, dan berbagai
    bidang kehidupan.
    """)

    # ========================================================
    # TUJUAN PEMBELAJARAN
    # ========================================================

    with st.expander("🎯 Tujuan Pembelajaran", expanded=True):

        st.markdown("""
        Setelah mempelajari materi ini, peserta didik diharapkan mampu:

        1. Menjelaskan pengertian statistika dan data.
        2. Membedakan populasi dan sampel.
        3. Mengidentifikasi jenis-jenis data.
        4. Menyajikan data dalam tabel dan diagram.
        5. Menentukan ukuran pemusatan data.
        6. Menentukan mean, median, dan modus.
        7. Menentukan kuartil dan jangkauan.
        8. Menentukan varians dan simpangan baku.
        9. Membaca dan menginterpretasikan histogram.
        10. Membaca dan menginterpretasikan boxplot.
        11. Membandingkan dua kelompok data.
        12. Menyelesaikan masalah statistika dalam kehidupan nyata.
        """)

    # ========================================================
    # 1. PENGERTIAN STATISTIKA
    # ========================================================

    st.subheader("1. Pengertian Statistika")

    st.markdown("""
    **Statistika** adalah ilmu yang mempelajari proses
    pengumpulan, pengolahan, penyajian, analisis, dan
    interpretasi data.

    Sedangkan **statistik** dapat merujuk pada nilai atau
    ukuran yang diperoleh dari pengolahan data.
    """)

    st.info(
        "Contoh statistik: rata-rata nilai siswa, median pendapatan, "
        "persentase kelulusan, dan simpangan baku."
    )

    # ========================================================
    # 2. DATA
    # ========================================================

    st.subheader("2. Pengertian Data")

    st.markdown("""
    **Data** adalah sekumpulan informasi atau fakta yang
    diperoleh melalui pengamatan, pengukuran, pencatatan,
    atau sumber lainnya.
    """)

    st.markdown("""
    Contoh data:

    - nilai ujian siswa;
    - tinggi badan;
    - berat badan;
    - jumlah anggota keluarga;
    - usia;
    - pendapatan;
    - jumlah kendaraan;
    - hasil survei.
    """)

    # ========================================================
    # 3. POPULASI
    # ========================================================

    st.subheader("3. Populasi")

    st.markdown("""
    **Populasi** adalah seluruh objek atau individu yang menjadi
    sasaran penelitian atau pengamatan.
    """)

    st.markdown("""
    Contoh:

    Jika penelitian ingin mengetahui rata-rata nilai matematika
    seluruh siswa kelas X di sebuah sekolah, maka seluruh siswa
    kelas X tersebut merupakan populasi.
    """)

    # ========================================================
    # 4. SAMPEL
    # ========================================================

    st.subheader("4. Sampel")

    st.markdown("""
    **Sampel** adalah sebagian anggota populasi yang dipilih
    untuk mewakili populasi.
    """)

    st.markdown("""
    Contoh:

    Dari 500 siswa kelas X, peneliti memilih 100 siswa untuk
    dianalisis. Sebanyak 100 siswa tersebut merupakan sampel.
    """)

    st.warning(
        "Sampel yang baik harus dapat memberikan gambaran yang representatif terhadap populasi."
    )

    # ========================================================
    # 5. JENIS DATA
    # ========================================================

    st.subheader("5. Jenis Data")

    st.markdown("""
    Data dapat dibedakan berdasarkan sifat dan bentuknya.
    """)

    st.markdown("""
    ### Data Kualitatif

    Data yang berupa kategori atau sifat.

    Contoh:

    - jenis kelamin;
    - warna;
    - jenis pekerjaan;
    - status kelulusan.

    ### Data Kuantitatif

    Data yang berupa angka dan dapat diukur.

    Contoh:

    - tinggi badan;
    - berat badan;
    - nilai ujian;
    - jumlah siswa.
    """)

    # ========================================================
    # 6. DATA DISKRIT DAN KONTINU
    # ========================================================

    st.subheader("6. Data Diskrit dan Kontinu")

    st.markdown("""
    Data kuantitatif dapat dibedakan menjadi data diskrit
    dan data kontinu.
    """)

    st.markdown("""
    **Data diskrit** adalah data yang biasanya berupa hasil
    pencacahan dan memiliki nilai yang terpisah.

    Contoh:

    Jumlah siswa = 35 orang.

    **Data kontinu** adalah data yang diperoleh melalui
    pengukuran dan dapat memiliki nilai dalam suatu interval.

    Contoh:

    Tinggi badan = 165,5 cm.
    """)

    # ========================================================
    # 7. PENYAJIAN DATA
    # ========================================================

    st.subheader("7. Penyajian Data")

    st.markdown("""
    Data dapat disajikan dalam berbagai bentuk agar lebih mudah
    dibaca dan dianalisis.
    """)

    st.markdown("""
    Bentuk penyajian data antara lain:

    - tabel;
    - diagram batang;
    - diagram garis;
    - diagram lingkaran;
    - histogram;
    - poligon frekuensi;
    - boxplot.
    """)

    # ========================================================
    # 8. TABEL DATA
    # ========================================================

    st.subheader("8. Penyajian Data dalam Tabel")

    data_nilai = {
        "Siswa": [
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H"
        ],
        "Nilai": [
            70,
            75,
            80,
            80,
            85,
            90,
            90,
            95
        ]
    }

    st.dataframe(
        data_nilai,
        use_container_width=True
    )

    # ========================================================
    # 9. FREKUENSI
    # ========================================================

    st.subheader("9. Frekuensi")

    st.markdown("""
    **Frekuensi** adalah banyaknya kemunculan suatu nilai
    atau kelompok nilai dalam suatu data.
    """)

    data_frekuensi = {
        "Nilai": [70, 75, 80, 85, 90, 95],
        "Frekuensi": [1, 1, 2, 1, 2, 1]
    }

    st.table(data_frekuensi)

    # ========================================================
    # 10. DIAGRAM BATANG
    # ========================================================

    st.subheader("10. Diagram Batang")

    import pandas as pd

    df_batang = pd.DataFrame({
        "Nilai": [70, 75, 80, 85, 90, 95],
        "Frekuensi": [1, 1, 2, 1, 2, 1]
    })

    st.bar_chart(
        df_batang,
        x="Nilai",
        y="Frekuensi"
    )

    # ========================================================
    # 11. MEAN
    # ========================================================

    st.subheader("11. Mean atau Rata-Rata")

    st.markdown("""
    Mean atau rata-rata adalah jumlah seluruh nilai data
    dibagi dengan banyaknya data.
    """)

    st.latex(r"\bar{x}=\frac{\sum x_i}{n}")

    st.markdown("""
    dengan:

    - x̄ = rata-rata;
    - Σxᵢ = jumlah seluruh data;
    - n = banyak data.
    """)

    # ========================================================
    # 12. CONTOH MEAN
    # ========================================================

    st.subheader("12. Contoh Menghitung Mean")

    st.markdown("""
    Diketahui data:
    """)

    st.latex(r"60,\ 70,\ 80,\ 90,\ 100")

    st.markdown("Jumlah data:");

    st.latex(r"\sum x_i=400")

    st.markdown("Banyak data:");

    st.latex(r"n=5")

    st.markdown("Maka:");

    st.latex(r"\bar{x}=\frac{400}{5}=80")

    st.success("Rata-rata data adalah 80.")

    # ========================================================
    # 13. MEAN DENGAN FREKUENSI
    # ========================================================

    st.subheader("13. Mean Data Berfrekuensi")

    st.markdown("""
    Untuk data yang memiliki frekuensi, mean dapat dihitung dengan:
    """)

    st.latex(r"\bar{x}=\frac{\sum f_ix_i}{\sum f_i}")

    st.markdown("""
    dengan:

    - fᵢ = frekuensi;
    - xᵢ = nilai data.
    """)

    # ========================================================
    # 14. MEDIAN
    # ========================================================

    st.subheader("14. Median")

    st.markdown("""
    Median adalah nilai tengah setelah data diurutkan dari
    nilai terkecil hingga terbesar.
    """)

    st.markdown("""
    Jika jumlah data ganjil:
    """)

    st.latex(r"Me=x_{\frac{n+1}{2}}")

    st.markdown("""
    Jika jumlah data genap:
    """)

    st.latex(r"Me=\frac{x_{\frac{n}{2}}+x_{\frac{n}{2}+1}}{2}")

    # ========================================================
    # 15. CONTOH MEDIAN GANJIL
    # ========================================================

    st.subheader("15. Contoh Median Data Ganjil")

    st.markdown("""
    Data:
    """)

    st.latex(r"60,\ 65,\ 70,\ 75,\ 80,\ 85,\ 90")

    st.markdown("""
    Banyak data adalah 7.
    """)

    st.latex(r"Me=x_{\frac{7+1}{2}}=x_4")

    st.success("Median = 75.")

    # ========================================================
    # 16. CONTOH MEDIAN GENAP
    # ========================================================

    st.subheader("16. Contoh Median Data Genap")

    st.markdown("""
    Data:
    """)

    st.latex(r"60,\ 65,\ 70,\ 75,\ 80,\ 85")

    st.markdown("""
    Banyak data adalah 6.
    """)

    st.latex(r"Me=\frac{x_3+x_4}{2}")

    st.latex(r"Me=\frac{70+75}{2}=72.5")

    st.success("Median = 72,5.")

    # ========================================================
    # 17. MODUS
    # ========================================================

    st.subheader("17. Modus")

    st.markdown("""
    Modus adalah nilai yang paling sering muncul dalam suatu data.
    """)

    st.markdown("Contoh:");

    st.latex(r"70,\ 75,\ 80,\ 80,\ 80,\ 85,\ 90")

    st.success("Modus = 80.")

    st.markdown("""
    Suatu data dapat memiliki:

    - satu modus;
    - dua modus;
    - lebih dari dua modus;
    - atau tidak memiliki modus.
    """)

    # ========================================================
    # 18. UKURAN PEMUSATAN
    # ========================================================

    st.subheader("18. Perbandingan Mean, Median, dan Modus")

    st.table({
        "Ukuran": [
            "Mean",
            "Median",
            "Modus"
        ],
        "Pengertian": [
            "Rata-rata seluruh data",
            "Nilai tengah data",
            "Nilai yang paling sering muncul"
        ]
    })

    st.info(
        "Mean, median, dan modus digunakan untuk menggambarkan pusat atau kecenderungan suatu kumpulan data."
    )

    # ========================================================
    # 19. KUARTIL
    # ========================================================

    st.subheader("19. Kuartil")

    st.markdown("""
    Kuartil membagi data yang telah diurutkan menjadi
    empat bagian yang memiliki jumlah data relatif sama.
    """)

    st.markdown("""
    Terdapat tiga kuartil:

    - Q₁ = kuartil bawah;
    - Q₂ = median;
    - Q₃ = kuartil atas.
    """)

    st.latex(r"Q_2=Me")

    # ========================================================
    # 20. INTERPRETASI KUARTIL
    # ========================================================

    st.subheader("20. Interpretasi Kuartil")

    st.markdown("""
    Q₁ menunjukkan nilai yang membatasi sekitar 25% data terbawah.

    Q₂ merupakan median dan membatasi sekitar 50% data.

    Q₃ menunjukkan nilai yang membatasi sekitar 75% data.
    """)

    # ========================================================
    # 21. JANGKAUAN
    # ========================================================

    st.subheader("21. Jangkauan")

    st.markdown("""
    Jangkauan atau range merupakan selisih antara nilai
    maksimum dan minimum.
    """)

    st.latex(r"R=x_{\max}-x_{\min}")

    st.markdown("Contoh:");

    st.latex(r"60,\ 65,\ 70,\ 75,\ 80,\ 90")

    st.latex(r"R=90-60=30")

    st.success("Jangkauan data adalah 30.")

    # ========================================================
    # 22. JANGKAUAN INTERKUARTIL
    # ========================================================

    st.subheader("22. Jangkauan Interkuartil")

    st.markdown("""
    Jangkauan interkuartil atau IQR merupakan selisih antara
    kuartil ketiga dan kuartil pertama.
    """)

    st.latex(r"IQR=Q_3-Q_1")

    st.info(
        "IQR menggambarkan penyebaran 50% data yang berada di bagian tengah."
    )

    # ========================================================
    # 23. VARIANS
    # ========================================================

    st.subheader("23. Varians")

    st.markdown("""
    Varians mengukur seberapa jauh data menyebar dari rata-ratanya.
    """)

    st.markdown("Untuk populasi:");

    st.latex(r"\sigma^2=\frac{\sum(x_i-\mu)^2}{N}")

    st.markdown("""
    dengan:

    - σ² = varians populasi;
    - μ = mean populasi;
    - N = jumlah anggota populasi.
    """)

    # ========================================================
    # 24. SIMPANGAN BAKU
    # ========================================================

    st.subheader("24. Simpangan Baku")

    st.markdown("""
    Simpangan baku merupakan akar kuadrat dari varians.
    """)

    st.latex(r"\sigma=\sqrt{\sigma^2}")

    st.markdown("""
    Semakin besar simpangan baku, semakin besar penyebaran
    data terhadap rata-ratanya.
    """)

    # ========================================================
    # 25. CONTOH SIMPANGAN BAKU
    # ========================================================

    st.subheader("25. Interpretasi Simpangan Baku")

    st.markdown("""
    Misalkan dua kelompok memiliki rata-rata yang sama,
    tetapi simpangan bakunya berbeda.
    """)

    st.table({
        "Kelompok": ["A", "B"],
        "Mean": [75, 75],
        "Simpangan Baku": [3, 12]
    })

    st.markdown("""
    Kelompok A memiliki data yang lebih terkonsentrasi
    di sekitar rata-rata.

    Kelompok B memiliki data yang lebih menyebar.
    """)

    # ========================================================
    # 26. KALKULATOR STATISTIKA
    # ========================================================

    st.subheader("26. Kalkulator Statistika")

    input_data = st.text_input(
        "Masukkan data dipisahkan dengan koma",
        value="60, 70, 70, 80, 80, 80, 90",
        key="input_statistika"
    )

    try:

        data = [
            float(x.strip())
            for x in input_data.split(",")
            if x.strip()
        ]

        if len(data) > 0:

            import statistics

            mean_data = statistics.mean(data)
            median_data = statistics.median(data)

            modus_data = statistics.multimode(data)

            minimum = min(data)
            maksimum = max(data)

            range_data = maksimum - minimum

            st.markdown("### Hasil Analisis")

            col1, col2, col3 = st.columns(3)

            with col1:

                st.metric(
                    "Mean",
                    f"{mean_data:.2f}"
                )

            with col2:

                st.metric(
                    "Median",
                    f"{median_data:.2f}"
                )

            with col3:

                st.metric(
                    "Jangkauan",
                    f"{range_data:.2f}"
                )

            st.write(
                "Modus:",
                ", ".join(
                    f"{x:g}" for x in modus_data
                )
            )

            # =================================================
            # GRAFIK
            # =================================================

            df_data = pd.DataFrame({
                "Data": data
            })

            st.markdown("### Distribusi Data")

            st.bar_chart(
                df_data
            )

    except ValueError:

        st.error(
            "Masukkan data numerik yang dipisahkan dengan koma."
        )

    # ========================================================
    # 27. HISTOGRAM
    # ========================================================

    st.subheader("27. Histogram")

    st.markdown("""
    Histogram digunakan untuk menggambarkan distribusi
    data kuantitatif berdasarkan interval kelas.
    """)

    data_histogram = [
        55, 60, 62, 65, 66, 68, 70, 71, 72, 72,
        73, 74, 75, 75, 76, 78, 80, 81, 82, 85,
        86, 88, 90, 92, 95
    ]

    df_histogram = pd.DataFrame({
        "Nilai": data_histogram
    })

    st.bar_chart(
        df_histogram
    )

    st.markdown("""
    Histogram membantu melihat bentuk distribusi data,
    termasuk apakah data cenderung terkonsentrasi,
    menyebar, menceng, atau memiliki lebih dari satu puncak.
    """)

    # ========================================================
    # 28. BOXPLOT
    # ========================================================

    st.subheader("28. Boxplot")

    st.markdown("""
    Boxplot merupakan diagram yang digunakan untuk
    menggambarkan distribusi data berdasarkan:

    - minimum;
    - Q₁;
    - median;
    - Q₃;
    - maksimum.
    """)

    st.markdown("""
    Lima nilai tersebut dikenal sebagai **five-number summary**.
    """)

    # ========================================================
    # 29. FIVE NUMBER SUMMARY
    # ========================================================

    st.subheader("29. Five-Number Summary")

    st.markdown("""
    Lima ukuran penting dalam boxplot adalah:
    """)

    st.table({
        "Ukuran": [
            "Minimum",
            "Q₁",
            "Median",
            "Q₃",
            "Maksimum"
        ],
        "Keterangan": [
            "Nilai terkecil",
            "Kuartil pertama",
            "Nilai tengah",
            "Kuartil ketiga",
            "Nilai terbesar"
        ]
    })

    # ========================================================
    # 30. OUTLIER
    # ========================================================

    st.subheader("30. Pencilan atau Outlier")

    st.markdown("""
    Outlier adalah data yang memiliki posisi sangat jauh
    dibandingkan sebagian besar data lainnya.
    """)

    st.markdown("""
    Salah satu aturan umum untuk mengidentifikasi outlier
    menggunakan IQR adalah:
    """)

    st.latex(r"x<Q_1-1.5(IQR)")

    st.latex(r"x>Q_3+1.5(IQR)")

    st.info(
        "Outlier perlu diperiksa karena dapat menunjukkan kesalahan pengukuran, kondisi khusus, atau karakteristik data yang memang berbeda."
    )

    # ========================================================
    # 31. DISTRIBUSI DATA
    # ========================================================

    st.subheader("31. Distribusi Data")

    st.markdown("""
    Distribusi data menunjukkan bagaimana nilai-nilai data
    tersebar dalam suatu kelompok.
    """)

    st.markdown("""
    Beberapa pola distribusi yang dapat ditemukan:

    - distribusi relatif simetris;
    - menceng ke kanan;
    - menceng ke kiri;
    - memiliki pencilan;
    - memiliki lebih dari satu puncak.
    """)

    # ========================================================
    # 32. INTERPRETASI DATA
    # ========================================================

    st.subheader("32. Interpretasi Data")

    st.markdown("""
    Dalam statistika, kita tidak cukup hanya menghitung
    nilai statistik. Hasil tersebut harus diinterpretasikan.
    """)

    st.markdown("""
    Contoh:

    Rata-rata nilai kelas adalah 78 dengan simpangan baku 4.

    Artinya, nilai siswa secara umum berada di sekitar
    rata-rata 78 dan penyebarannya relatif kecil.
    """)

    # ========================================================
    # 33. PERBANDINGAN DUA KELOMPOK
    # ========================================================

    st.subheader("33. Membandingkan Dua Kelompok Data")

    data_kelompok = pd.DataFrame({
        "Kelompok": [
            "A",
            "A",
            "A",
            "A",
            "A",
            "B",
            "B",
            "B",
            "B",
            "B"
        ],
        "Nilai": [
            70,
            72,
            75,
            77,
            76,
            60,
            70,
            80,
            90,
            100
        ]
    })

    st.dataframe(
        data_kelompok,
        use_container_width=True
    )

    st.markdown("""
    Kedua kelompok dapat memiliki rata-rata yang sama,
    tetapi tingkat penyebaran datanya berbeda.

    Oleh karena itu, analisis data sebaiknya tidak hanya
    memperhatikan ukuran pemusatan, tetapi juga ukuran penyebaran.
    """)

    # ========================================================
    # 34. DATA INTERAKTIF
    # ========================================================

    st.subheader("34. Eksplorasi Data Interaktif")

    nilai_slider = st.slider(
        "Tambahkan sebuah nilai ke dataset",
        min_value=0,
        max_value=1000,
        value=75,
        step=1,
        key="slider_statistika"
    )
    
    data_awal = [
        60,
        65,
        70,
        70,
        75,
        80,
        80,
        85,
        90
    ]
    
    data_baru = data_awal + [nilai_slider]
    
    mean_baru = statistics.mean(data_baru)
    median_baru = statistics.median(data_baru)
    
    # Tabel data
    df_data = pd.DataFrame({
        "No": range(1, len(data_baru) + 1),
        "Nilai": data_baru
    })
    
    st.markdown("### Data")
    
    st.dataframe(
        df_data,
        use_container_width=True,
        hide_index=True
    )
    
    # Ukuran statistik
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric(
            "Mean",
            f"{mean_baru:.2f}"
        )
    
    with col2:
        st.metric(
            "Median",
            f"{median_baru:.2f}"
        )
    
    st.markdown("""
    Perhatikan bagaimana penambahan satu nilai dapat
    memengaruhi mean dan median.
    """)

    # ========================================================
    # 35. LATIHAN
    # ========================================================

    st.subheader("35. Latihan")

    st.markdown("""
    **Soal 1**

    Tentukan mean dari data:

    60, 70, 80, 90, 100
    """)

    st.markdown("""
    **Soal 2**

    Tentukan median dari data:

    55, 60, 70, 75, 80, 85, 90
    """)

    st.markdown("""
    **Soal 3**

    Tentukan modus dari data:

    70, 75, 80, 80, 85, 90, 80
    """)

    st.markdown("""
    **Soal 4**

    Tentukan jangkauan data:

    45, 50, 60, 70, 80, 95
    """)

    st.markdown("""
    **Soal 5**

    Jelaskan perbedaan antara populasi dan sampel.
    """)

    st.markdown("""
    **Soal 6**

    Jelaskan perbedaan data diskrit dan data kontinu
    serta berikan masing-masing satu contoh.
    """)

    st.markdown("""
    **Soal 7**

    Apa yang dimaksud dengan outlier?
    """)

    st.markdown("""
    **Soal 8**

    Mengapa dalam analisis data kita perlu memperhatikan
    ukuran pemusatan dan ukuran penyebaran?
    """)

    # ========================================================
    # 36. KUIS
    # ========================================================

    st.subheader("36. Kuis Interaktif")

    jawaban = st.radio(
        "Mean dari data 60, 70, 80, 90, dan 100 adalah...",
        [
            "70",
            "75",
            "80",
            "85"
        ],
        key="kuis_statistika_1"
    )

    if st.button(
        "Periksa Jawaban",
        key="cek_statistika_1"
    ):

        if jawaban == "80":

            st.success(
                "✅ Benar! Jumlah data = 400 dan banyak data = 5, sehingga mean = 80."
            )

        else:

            st.error(
                "❌ Belum tepat. Gunakan rumus mean = jumlah seluruh data / banyak data."
            )

    # ========================================================
    # 37. RANGKUMAN
    # ========================================================

    with st.expander("📌 Rangkuman Materi", expanded=False):

        st.markdown("""
        ### Statistika

        Statistika merupakan ilmu yang mempelajari
        pengumpulan, penyajian, pengolahan, analisis,
        dan interpretasi data.

        ### Ukuran Pemusatan

        Mean:

        $bar{x}=\frac{\sum x_i}{n}$

        Median adalah nilai tengah data yang telah diurutkan.

        Modus adalah nilai yang paling sering muncul.

        ### Ukuran Penyebaran

        Jangkauan:

        \(R=x_{\max}-x_{\min}\)

        Jangkauan interkuartil:

        \(IQR=Q_3-Q_1\)

        Varians mengukur rata-rata kuadrat penyimpangan
        data terhadap mean.

        Simpangan baku merupakan akar dari varians.

        ### Penyajian Data

        Data dapat disajikan menggunakan:

        - tabel;
        - diagram batang;
        - diagram garis;
        - diagram lingkaran;
        - histogram;
        - boxplot.

        ### Hal Penting

        Analisis statistika tidak hanya menghitung angka,
        tetapi juga memahami makna angka tersebut dan
        menggunakannya untuk mengambil kesimpulan.
        """)

def trigonometri_1():

    st.header("📐 Trigonometri I")

    st.markdown("""
    ### Matematika Kelas X — Fase E

    Trigonometri merupakan cabang matematika yang mempelajari
    hubungan antara sudut dan panjang sisi pada segitiga.

    Trigonometri banyak digunakan dalam pengukuran tinggi,
    jarak, kemiringan, navigasi, astronomi, teknik, arsitektur,
    dan berbagai permasalahan kehidupan nyata.
    """)

    # ========================================================
    # TUJUAN PEMBELAJARAN
    # ========================================================

    with st.expander("🎯 Tujuan Pembelajaran", expanded=True):

        st.markdown("""
        Setelah mempelajari materi ini, peserta didik diharapkan mampu:

        1. Menjelaskan pengertian sudut.
        2. Mengubah ukuran sudut derajat dan radian.
        3. Mengidentifikasi sisi-sisi pada segitiga siku-siku.
        4. Menjelaskan perbandingan trigonometri.
        5. Menentukan nilai sinus, cosinus, dan tangen.
        6. Menentukan nilai trigonometri sudut istimewa.
        7. Menggunakan teorema Pythagoras dalam permasalahan trigonometri.
        8. Menentukan panjang sisi segitiga menggunakan perbandingan trigonometri.
        9. Menentukan besar sudut menggunakan invers trigonometri.
        10. Menggunakan identitas trigonometri dasar.
        11. Menyelesaikan masalah kontekstual menggunakan trigonometri.
        """)

    # ========================================================
    # 1. PENGERTIAN TRIGONOMETRI
    # ========================================================

    st.subheader("1. Pengertian Trigonometri")

    st.markdown("""
    Kata trigonometri berasal dari bahasa Yunani yang berkaitan
    dengan pengukuran segitiga.

    Secara sederhana, trigonometri mempelajari hubungan antara
    besar sudut dan panjang sisi pada segitiga.
    """)

    st.info(
        "Konsep dasar Trigonometri I pada materi ini menggunakan segitiga siku-siku."
    )

    # ========================================================
    # 2. SUDUT
    # ========================================================

    st.subheader("2. Sudut")

    st.markdown("""
    Sudut terbentuk dari dua sinar garis yang memiliki titik pangkal
    yang sama.

    Satuan sudut yang umum digunakan adalah derajat dan radian.
    """)

    st.markdown("### Satuan Derajat")

    st.markdown("""
    Satu putaran penuh memiliki besar:
    """)

    st.latex(r"360^\circ")

    st.markdown("""
    Sudut siku-siku:
    """)

    st.latex(r"90^\circ")

    st.markdown("""
    Sudut lurus:
    """)

    st.latex(r"180^\circ")

    # ========================================================
    # 3. RADIAN
    # ========================================================

    st.subheader("3. Ukuran Sudut dalam Radian")

    st.markdown("""
    Selain derajat, sudut dapat dinyatakan dalam radian.

    Hubungan antara derajat dan radian adalah:
    """)

    st.latex(r"180^\circ=\pi\text{ radian}")

    st.markdown("Sehingga:");

    st.latex(r"360^\circ=2\pi\text{ radian}")

    st.latex(r"90^\circ=\frac{\pi}{2}\text{ radian}")

    st.latex(r"60^\circ=\frac{\pi}{3}\text{ radian}")

    st.latex(r"45^\circ=\frac{\pi}{4}\text{ radian}")

    st.latex(r"30^\circ=\frac{\pi}{6}\text{ radian}")

    # ========================================================
    # 4. SEGITIGA SIKU-SIKU
    # ========================================================

    st.subheader("4. Segitiga Siku-Siku")

    st.markdown("""
    Segitiga siku-siku adalah segitiga yang memiliki satu sudut
    sebesar 90°.

    Pada segitiga siku-siku terdapat tiga sisi penting:

    - sisi miring atau hipotenusa;
    - sisi depan terhadap sudut yang diamati;
    - sisi samping terhadap sudut yang diamati.
    """)

    st.markdown("""
    Penamaan sisi depan dan sisi samping bergantung pada sudut
    yang sedang diamati.
    """)

    # ========================================================
    # 5. PYTHAGORAS
    # ========================================================

    st.subheader("5. Teorema Pythagoras")

    st.markdown("""
    Pada segitiga siku-siku, hubungan ketiga sisi dinyatakan
    dengan teorema Pythagoras.
    """)

    st.latex(r"a^2+b^2=c^2")

    st.markdown("""
    dengan c merupakan sisi miring atau hipotenusa.
    """)

    st.markdown("Contoh segitiga dengan sisi 3, 4, dan 5:");

    st.latex(r"3^2+4^2=5^2")

    st.latex(r"9+16=25")

    st.success("Segitiga dengan sisi 3, 4, dan 5 merupakan segitiga siku-siku.")

    # ========================================================
    # 6. SINUS
    # ========================================================

    st.subheader("6. Perbandingan Trigonometri: Sinus")

    st.markdown("""
    Sinus suatu sudut pada segitiga siku-siku merupakan perbandingan
    antara sisi depan sudut dan sisi miring.
    """)

    st.latex(r"\sin(\theta)=\frac{\text{sisi depan}}{\text{sisi miring}}")

    st.markdown("""
    Cara mudah mengingatnya adalah **SOH**:

    **S**ine = **O**pposite / **H**ypotenuse.
    """)

    # Visualisasi segitiga
    
    # ========================================================
    # 7. COSINUS
    # ========================================================

    st.subheader("7. Perbandingan Trigonometri: Cosinus")

    st.markdown("""
    Cosinus suatu sudut pada segitiga siku-siku merupakan
    perbandingan antara sisi samping dan sisi miring.
    """)

    st.latex(r"\cos(\theta)=\frac{\text{sisi samping}}{\text{sisi miring}}")

    st.markdown("""
    Cara mudah mengingatnya adalah **CAH**:

    **C**osine = **A**djacent / **H**ypotenuse.
    """)

    # Visualisasi cosinus menggunakan rasio 4/5
    
    # ========================================================
    # 8. TANGEN
    # ========================================================

    st.subheader("8. Perbandingan Trigonometri: Tangen")

    st.markdown("""
    Tangen suatu sudut pada segitiga siku-siku merupakan
    perbandingan antara sisi depan dan sisi samping.
    """)

    st.latex(r"\tan(\theta)=\frac{\text{sisi depan}}{\text{sisi samping}}")

    st.markdown("""
    Cara mudah mengingatnya adalah **TOA**:

    **T**angent = **O**pposite / **A**djacent.
    """)

    # ========================================================
    # 9. SOH CAH TOA
    # ========================================================

    st.subheader("9. SOH — CAH — TOA")

    st.markdown("""
    Ketiga perbandingan trigonometri dasar dapat diringkas sebagai:
    """)

    st.markdown("""
    **SOH**

    Sinus = sisi depan / sisi miring

    **CAH**

    Cosinus = sisi samping / sisi miring

    **TOA**

    Tangen = sisi depan / sisi samping
    """)

    # ========================================================
    # 10. CONTOH SEGITIGA 3-4-5
    # ========================================================

    st.subheader("10. Contoh Perbandingan Trigonometri")

    st.markdown("""
    Diketahui segitiga siku-siku memiliki sisi depan = 3,
    sisi samping = 4, dan sisi miring = 5.
    """)

    st.markdown("Maka:");

    st.latex(r"\sin(\theta)=\frac{3}{5}")

    st.latex(r"\cos(\theta)=\frac{4}{5}")

    st.latex(r"\tan(\theta)=\frac{3}{4}")

    st.success(
        "Perhatikan bahwa sisi depan dan sisi samping ditentukan berdasarkan sudut θ."
    )

    # ========================================================
    # 11. HUBUNGAN SIN COS TAN
    # ========================================================

    st.subheader("11. Hubungan Sinus, Cosinus, dan Tangen")

    st.markdown("""
    Tangen dapat dinyatakan menggunakan sinus dan cosinus:
    """)

    st.latex(r"\tan(\theta)=\frac{\sin(\theta)}{\cos(\theta)}")

    # Visualisasi hubungan tangen


    # ========================================================
    # 12. IDENTITAS PYTHAGORAS
    # ========================================================

    st.subheader("12. Identitas Trigonometri Dasar")

    st.markdown("""
    Salah satu identitas trigonometri paling penting adalah:
    """)

    st.latex(r"\sin^2(\theta)+\cos^2(\theta)=1")

    st.markdown("""
    Identitas ini berasal dari teorema Pythagoras pada
    lingkaran satuan.
    """)


    # ========================================================
    # 13. SUDUT ISTIMEWA
    # ========================================================

    st.subheader("13. Nilai Trigonometri Sudut Istimewa")

    st.markdown("""
    Beberapa sudut memiliki nilai sinus, cosinus, dan tangen
    yang dapat ditentukan secara eksak.
    """)

    data_sudut = {
        "Sudut": [
            "0°",
            "30°",
            "45°",
            "60°",
            "90°"
        ],
        "Sinus": [
            "0",
            "1/2",
            "√2/2",
            "√3/2",
            "1"
        ],
        "Cosinus": [
            "1",
            "√3/2",
            "√2/2",
            "1/2",
            "0"
        ],
        "Tangen": [
            "0",
            "√3/3",
            "1",
            "√3",
            "Tidak terdefinisi"
        ]
    }

    st.table(data_sudut)


    
    # ========================================================
    # 14. POLA NILAI SUDUT ISTIMEWA
    # ========================================================

    st.subheader("14. Pola Nilai Sinus Sudut Istimewa")

    st.markdown("""
    Nilai sinus sudut 0°, 30°, 45°, 60°, dan 90° dapat
    diingat menggunakan pola:
    """)

    st.latex(r"\sin(\theta)=\frac{\sqrt{n}}{2}")

    st.markdown("""
    dengan n berturut-turut 0, 1, 2, 3, dan 4.
    """)

    st.markdown("Sehingga:");

    st.latex(r"\sin(0^\circ)=\frac{\sqrt{0}}{2}")

    st.latex(r"\sin(30^\circ)=\frac{\sqrt{1}}{2}")

    st.latex(r"\sin(45^\circ)=\frac{\sqrt{2}}{2}")

    st.latex(r"\sin(60^\circ)=\frac{\sqrt{3}}{2}")

    st.latex(r"\sin(90^\circ)=\frac{\sqrt{4}}{2}")

    # ========================================================
    # 15. KUADRAN
    # ========================================================

    st.subheader("15. Kuadran pada Bidang Koordinat")

    st.markdown("""
    Dalam pembahasan trigonometri yang lebih luas, bidang koordinat
    dibagi menjadi empat kuadran.
    """)

    st.markdown("""
    **Kuadran I**

    Sinus, cosinus, dan tangen bernilai positif.

    **Kuadran II**

    Sinus positif, sedangkan cosinus dan tangen negatif.

    **Kuadran III**

    Tangen positif, sedangkan sinus dan cosinus negatif.

    **Kuadran IV**

    Cosinus positif, sedangkan sinus dan tangen negatif.
    """)

    # ========================================================
    # 16. NILAI NEGATIF
    # ========================================================

    st.subheader("16. Nilai Trigonometri Positif dan Negatif")

    st.markdown("""
    Tanda positif atau negatif nilai trigonometri bergantung
    pada posisi sudut pada kuadran.
    """)

    st.table({
        "Kuadran": ["I", "II", "III", "IV"],
        "sin": ["+", "+", "−", "−"],
        "cos": ["+", "−", "−", "+"],
        "tan": ["+", "−", "+", "−"]
    })

    # ========================================================
    # 17. MENENTUKAN SISI
    # ========================================================

    st.subheader("17. Menentukan Panjang Sisi")

    st.markdown("""
    Misalkan diketahui:
    """)

    st.latex(r"\sin(30^\circ)=\frac{x}{10}")

    st.markdown("""
    Karena nilai sinus 30° adalah 1/2:
    """)

    st.latex(r"\frac{1}{2}=\frac{x}{10}")

    st.latex(r"x=5")

    st.success("Panjang sisi depan adalah 5 satuan.")

    # ========================================================
    # 18. CONTOH COSINUS
    # ========================================================

    st.subheader("18. Contoh Menggunakan Cosinus")

    st.markdown("""
    Diketahui sisi miring sebuah segitiga adalah 12 cm
    dan sudutnya 60°.

    Tentukan panjang sisi samping.
    """)

    st.latex(r"\cos(60^\circ)=\frac{x}{12}")

    st.latex(r"\frac{1}{2}=\frac{x}{12}")

    st.latex(r"x=6")

    st.success("Panjang sisi samping adalah 6 cm.")

    # ========================================================
    # 19. CONTOH TANGEN
    # ========================================================

    st.subheader("19. Contoh Menggunakan Tangen")

    st.markdown("""
    Sebuah segitiga siku-siku memiliki sisi samping 8 cm
    dan sudut 45°.

    Tentukan panjang sisi depan.
    """)

    st.latex(r"\tan(45^\circ)=\frac{x}{8}")

    st.latex(r"1=\frac{x}{8}")

    st.latex(r"x=8")

    st.success("Panjang sisi depan adalah 8 cm.")

    # ========================================================
    # 20. INVERS TRIGONOMETRI
    # ========================================================

    st.subheader("20. Menentukan Besar Sudut")

    st.markdown("""
    Jika nilai perbandingan trigonometri diketahui,
    besar sudut dapat dicari menggunakan fungsi invers.
    """)

    st.markdown("Untuk sinus:");

    st.latex(r"\theta=\sin^{-1}(x)")

    st.markdown("Untuk cosinus:");

    st.latex(r"\theta=\cos^{-1}(x)")

    st.markdown("Untuk tangen:");

    st.latex(r"\theta=\tan^{-1}(x)")

    st.markdown("Contoh:");

    st.latex(r"\sin(\theta)=\frac{1}{2}")

    st.latex(r"\theta=\sin^{-1}\left(\frac{1}{2}\right)")

    st.latex(r"\theta=30^\circ")

    # ========================================================
    # 21. KALKULATOR TRIGONOMETRI
    # ========================================================

    st.subheader("21. Kalkulator Trigonometri")

    sudut = st.number_input(
        "Masukkan sudut dalam derajat",
        min_value=0.00,
        max_value=720.00,
        value=30.00,
        step=0.01,
        key="sudut_trigonometri"
    )

    import math

    radian = math.radians(sudut)

    nilai_sin = math.sin(radian)
    nilai_cos = math.cos(radian)

    if abs(math.cos(radian)) < 1e-10:
        nilai_tan = None
    else:
        nilai_tan = math.tan(radian)

    st.metric(
        "sin(θ)",
        f"{nilai_sin:.6f}"
    )

    st.metric(
        "cos(θ)",
        f"{nilai_cos:.6f}"
    )

    if nilai_tan is not None:

        st.metric(
            "tan(θ)",
            f"{nilai_tan:.6f}"
        )

    else:

        st.metric(
            "tan(θ)",
            "Tidak terdefinisi"
        )

    # ========================================================
    # 22. MASALAH KONTEKSTUAL
    # ========================================================

    st.subheader("22. Penerapan Trigonometri")

    st.markdown("""
    Trigonometri dapat digunakan untuk menentukan tinggi
    atau jarak yang sulit diukur secara langsung.
    """)

    st.markdown("""
    Contohnya:

    - menentukan tinggi gedung;
    - menentukan tinggi pohon;
    - menentukan jarak kapal;
    - menentukan kemiringan jalan;
    - menentukan panjang tangga;
    - menentukan sudut elevasi;
    - menentukan sudut depresi.
    """)

    # ========================================================
    # 23. CONTOH TINGGI POHON
    # ========================================================

    st.subheader("23. Contoh Menentukan Tinggi Pohon")

    st.markdown("""
    Seseorang berdiri sejauh 20 meter dari sebuah pohon.
    Sudut elevasi ke puncak pohon adalah 30°.

    Abaikan tinggi mata pengamat.
    """)

    st.markdown("Gunakan tangen:");

    st.latex(r"\tan(30^\circ)=\frac{h}{20}")

    st.latex(r"\frac{\sqrt{3}}{3}=\frac{h}{20}")

    st.latex(r"h=\frac{20\sqrt{3}}{3}")

    st.success(
        "Tinggi pohon dapat diperkirakan sekitar 11,55 meter."
    )

    # ========================================================
    # 24. SUDUT ELEVASI
    # ========================================================

    st.subheader("24. Sudut Elevasi")

    st.markdown("""
    Sudut elevasi adalah sudut yang terbentuk antara garis
    horizontal dengan garis pandang menuju objek yang berada
    lebih tinggi.
    """)

    st.markdown("""
    Misalnya seseorang melihat puncak gedung dari permukaan tanah.
    Sudut antara garis horizontal dan garis pandang ke puncak
    gedung disebut sudut elevasi.
    """)

    # ========================================================
    # 25. SUDUT DEPRESI
    # ========================================================

    st.subheader("25. Sudut Depresi")

    st.markdown("""
    Sudut depresi adalah sudut yang terbentuk antara garis
    horizontal dengan garis pandang menuju objek yang berada
    lebih rendah.
    """)

    st.info(
        "Sudut elevasi digunakan ketika objek berada di atas pengamat, "
        "sedangkan sudut depresi digunakan ketika objek berada di bawah pengamat."
    )

    # ========================================================
    # 26. EKSPLORASI SUDUT
    # ========================================================

    st.subheader("26. Eksplorasi Nilai Trigonometri")

    sudut_eksplorasi = st.slider(
        "Pilih sudut",
        min_value=0,
        max_value=90,
        value=30,
        step=1,
        key="eksplorasi_sudut_trig"
    )

    rad = math.radians(sudut_eksplorasi)

    sin_val = math.sin(rad)
    cos_val = math.cos(rad)

    if abs(math.cos(rad)) < 1e-10:
        tan_text = "Tidak terdefinisi"
    else:
        tan_text = f"{math.tan(rad):.4f}"

    st.markdown(
        f"Untuk sudut **{sudut_eksplorasi}°**:"
    )

    st.latex(
        f"\\sin({sudut_eksplorasi}^\\circ)={sin_val:.4f}"
    )

    st.latex(
        f"\\cos({sudut_eksplorasi}^\\circ)={cos_val:.4f}"
    )

    st.latex(
        f"\\tan({sudut_eksplorasi}^\\circ)={tan_text}"
    )

    # ========================================================
    # 27. LATIHAN
    # ========================================================

    st.subheader("27. Latihan")

    st.markdown("""
    **Soal 1**

    Tentukan nilai:

    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$sin(30°)$
    """)

    st.markdown("""
    **Soal 2**

    Tentukan nilai:

    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$cos(60°)$
    """)

    st.markdown("""
    **Soal 3**

    Tentukan nilai:

    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$tan(45°)$
    """)

    st.markdown("""
    **Soal 4**

    Sebuah segitiga siku-siku memiliki sisi depan 6 cm
    dan sisi miring 10 cm. Tentukan nilai sinus sudutnya.
    """)

    st.markdown("""
    **Soal 5**

    Sebuah segitiga siku-siku memiliki sisi samping 8 cm
    dan sisi miring 10 cm. Tentukan nilai cosinus sudutnya.
    """)

    st.markdown("""
    **Soal 6**

    Sebuah tangga panjangnya 10 m disandarkan pada dinding
    dengan sudut 60° terhadap tanah. Tentukan tinggi yang
    dicapai tangga pada dinding.
    """)

    st.markdown("""
    **Soal 7**

    Dari jarak 30 meter, seseorang melihat puncak sebuah
    gedung dengan sudut elevasi 45°. Tentukan tinggi gedung
    jika tinggi mata diabaikan.
    """)

    # ========================================================
    # 28. KUIS
    # ========================================================

    st.subheader("28. Kuis Interaktif")

    jawaban = st.radio(
        "Jika sisi depan = 3 dan sisi miring = 5, maka sin(θ) adalah...",
        [
            "3/4",
            "4/5",
            "3/5",
            "5/3"
        ],
        key="kuis_trigonometri_1"
    )

    if st.button(
        "Periksa Jawaban",
        key="cek_trigonometri_1"
    ):

        if jawaban == "3/5":

            st.success(
                "✅ Benar! Sinus = sisi depan / sisi miring = 3/5."
            )

        else:

            st.error(
                "❌ Belum tepat. Ingat SOH: Sinus = Opposite / Hypotenuse."
            )

    # ========================================================
    # 29. RANGKUMAN
    # ========================================================

    with st.expander("📌 Rangkuman Materi", expanded=False):

        st.markdown("""
        ### Konsep Utama Trigonometri I

        **1. Sudut**

        Sudut dapat dinyatakan dalam derajat maupun radian.

        **2. Teorema Pythagoras**

        Hubungan sisi segitiga siku-siku:

        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$a^2+b^2=c^2$

        **3. Sinus**

        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sin(θ) = sisi depan / sisi miring

        **4. Cosinus**

        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cos(θ) = sisi samping / sisi miring

        **5. Tangen**

        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tan(θ) = sisi depan / sisi samping

        **6. Hubungan Sinus dan Cosinus**

        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tan(θ) = sin(θ) / cos(θ)

        **7. Identitas Pythagoras**

        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sin²(θ) + cos²(θ) = 1

        **8. Sudut Istimewa**

        Sudut yang penting untuk dikuasai:

        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0°, 30°, 45°, 60°, dan 90°.

        **9. Aplikasi**

        Trigonometri dapat digunakan untuk menentukan
        tinggi, jarak, panjang, dan sudut dalam berbagai
        permasalahan kehidupan nyata.
        """)
        
        
def persamaan_fungsi_kuadrat():

    st.header("📈 Persamaan dan Fungsi Kuadrat")

    st.markdown("""
    ### Matematika Kelas X — Fase E

    Persamaan dan fungsi kuadrat merupakan konsep penting dalam
    matematika yang berkaitan dengan polinomial berderajat dua.
    Konsep ini dapat digunakan untuk menyelesaikan berbagai
    masalah matematika dan masalah kontekstual.
    """)

    # ========================================================
    # TUJUAN PEMBELAJARAN
    # ========================================================

    with st.expander("🎯 Tujuan Pembelajaran", expanded=True):

        st.markdown("""
        Setelah mempelajari materi ini, peserta didik diharapkan mampu:

        1. Menjelaskan pengertian persamaan kuadrat.
        2. Menentukan bentuk umum persamaan kuadrat.
        3. Menentukan akar-akar persamaan kuadrat.
        4. Menyelesaikan persamaan kuadrat dengan faktorisasi.
        5. Menyelesaikan persamaan kuadrat dengan melengkapkan kuadrat sempurna.
        6. Menggunakan rumus kuadrat atau rumus ABC.
        7. Menentukan diskriminan dan jenis akar.
        8. Menentukan hubungan antara akar dan koefisien.
        9. Menjelaskan pengertian fungsi kuadrat.
        10. Menggambar dan menganalisis grafik fungsi kuadrat.
        11. Menentukan titik puncak dan sumbu simetri.
        12. Menerapkan fungsi kuadrat dalam masalah kontekstual.
        """)

    # ========================================================
    # 1. APERSEPSI
    # ========================================================

    st.subheader("1. Apersepsi")

    st.markdown("""
    Perhatikan persamaan berikut:
    """)

    st.latex(r"x^2-5x+6=0")

    st.markdown("""
    Persamaan tersebut merupakan persamaan kuadrat karena
    pangkat tertinggi dari variabel x adalah 2.

    Persamaan kuadrat banyak ditemukan dalam permasalahan
    yang melibatkan luas, lintasan benda, keuntungan, dan
    berbagai hubungan nonlinear.
    """)

    # ========================================================
    # 2. PENGERTIAN PERSAMAAN KUADRAT
    # ========================================================

    st.subheader("2. Pengertian Persamaan Kuadrat")

    st.markdown("""
    Persamaan kuadrat adalah persamaan polinomial yang
    memiliki derajat dua.
    """)

    st.markdown("Bentuk umumnya adalah:")

    st.latex(r"ax^2+bx+c=0")

    st.markdown("""
    dengan:

    - a, b, dan c merupakan bilangan real;
    - a ≠ 0;
    - x merupakan variabel.
    """)

    # ========================================================
    # 3. CONTOH PERSAMAAN KUADRAT
    # ========================================================

    st.subheader("3. Contoh Persamaan Kuadrat")

    st.markdown("Contoh:");

    st.latex(r"x^2-5x+6=0")

    st.latex(r"2x^2+3x-5=0")

    st.latex(r"4x^2-16=0")

    st.latex(r"-3x^2+7x+2=0")

    st.markdown("""
    Semua persamaan tersebut merupakan persamaan kuadrat
    karena memiliki pangkat tertinggi dua.
    """)

    # ========================================================
    # 4. BUKAN PERSAMAAN KUADRAT
    # ========================================================

    st.subheader("4. Contoh yang Bukan Persamaan Kuadrat")

    st.latex(r"2x+5=0")

    st.latex(r"x^3-2x+1=0")

    st.latex(r"\frac{1}{x}+2=0")

    st.info(
        "Persamaan linear memiliki derajat satu, sedangkan "
        "persamaan kubik memiliki derajat tiga."
    )

    # ========================================================
    # 5. KOEFISIEN
    # ========================================================

    st.subheader("5. Koefisien Persamaan Kuadrat")

    st.markdown("""
    Pada persamaan:
    """)

    st.latex(r"3x^2-7x+4=0")

    st.markdown("""
    diperoleh:

    - a = 3
    - b = −7
    - c = 4
    """)

    # ========================================================
    # 6. MENYELESAIKAN PERSAMAAN KUADRAT
    # ========================================================

    st.subheader("6. Penyelesaian Persamaan Kuadrat")

    st.markdown("""
    Akar atau penyelesaian persamaan kuadrat adalah nilai x
    yang membuat persamaan bernilai benar.

    Beberapa metode yang dapat digunakan adalah:

    1. Faktorisasi.
    2. Melengkapkan kuadrat sempurna.
    3. Rumus kuadrat atau rumus ABC.
    """)

    # ========================================================
    # 7. FAKTORISASI
    # ========================================================

    st.subheader("7. Metode Faktorisasi")

    st.markdown("""
    Perhatikan persamaan:
    """)

    st.latex(r"x^2-5x+6=0")

    st.markdown("""
    Kita mencari dua bilangan yang hasil kalinya 6
    dan jumlahnya −5.
    """)

    st.latex(r"-2\times-3=6")

    st.latex(r"-2+(-3)=-5")

    st.markdown("Maka:");

    st.latex(r"(x-2)(x-3)=0")

    st.markdown("""
    Berdasarkan sifat perkalian nol:
    """)

    st.latex(r"x-2=0")

    st.latex(r"x-3=0")

    st.latex(r"x=2\quad\text{atau}\quad x=3")

    st.success("Akar-akarnya adalah x = 2 dan x = 3.")

    # ========================================================
    # 8. FAKTORISASI DENGAN KOEFISIEN A TIDAK SAMA 1
    # ========================================================

    st.subheader("8. Faktorisasi dengan a ≠ 1")

    st.markdown("""
    Contoh:
    """)

    st.latex(r"2x^2+7x+3=0")

    st.markdown("""
    Faktorkan:
    """)

    st.latex(r"(2x+1)(x+3)=0")

    st.markdown("Maka:");

    st.latex(r"2x+1=0")

    st.latex(r"x=-\frac{1}{2}")

    st.latex(r"x+3=0")

    st.latex(r"x=-3")

    st.success("Akar-akarnya adalah x = −1/2 dan x = −3.")

    # ========================================================
    # 9. MELENGKAPKAN KUADRAT SEMPURNA
    # ========================================================

    st.subheader("9. Metode Melengkapkan Kuadrat Sempurna")

    st.markdown("""
    Metode ini mengubah persamaan kuadrat menjadi bentuk
    kuadrat sempurna.
    """)

    st.markdown("Contoh:");

    st.latex(r"x^2+6x+5=0")

    st.markdown("Pindahkan konstanta:");

    st.latex(r"x^2+6x=-5")

    st.markdown("""
    Tambahkan kuadrat dari setengah koefisien x.
    """)

    st.latex(r"\left(\frac{6}{2}\right)^2=9")

    st.markdown("Maka:");

    st.latex(r"x^2+6x+9=4")

    st.latex(r"(x+3)^2=4")

    st.latex(r"x+3=\pm2")

    st.latex(r"x=-1\quad\text{atau}\quad x=-5")

    # ========================================================
    # 10. RUMUS ABC
    # ========================================================

    st.subheader("10. Rumus Kuadrat atau Rumus ABC")

    st.markdown("""
    Untuk persamaan:
    """)

    st.latex(r"ax^2+bx+c=0")

    st.markdown("""
    akar-akarnya dapat ditentukan menggunakan rumus:
    """)

    st.latex(r"x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}")

    st.markdown("""
    Rumus ini dapat digunakan untuk semua persamaan kuadrat
    dengan a ≠ 0.
    """)

    # ========================================================
    # 11. CONTOH RUMUS ABC
    # ========================================================

    st.subheader("11. Contoh Menggunakan Rumus ABC")

    st.markdown("""
    Tentukan akar-akar:
    """)

    st.latex(r"2x^2-5x-3=0")

    st.markdown("""
    Diperoleh:
    """)

    st.latex(r"a=2,\quad b=-5,\quad c=-3")

    st.markdown("Substitusi:");

    st.latex(r"x=\frac{-(-5)\pm\sqrt{(-5)^2-4(2)(-3)}}{2(2)}")

    st.latex(r"x=\frac{5\pm\sqrt{49}}{4}")

    st.latex(r"x=\frac{5\pm7}{4}")

    st.markdown("Sehingga:");

    st.latex(r"x=3")

    st.latex(r"x=-\frac{1}{2}")

    # ========================================================
    # 12. DISKRIMINAN
    # ========================================================

    st.subheader("12. Diskriminan")

    st.markdown("""
    Diskriminan adalah bagian dari rumus ABC yang menentukan
    jenis akar persamaan kuadrat.
    """)

    st.latex(r"D=b^2-4ac")

    st.markdown("""
    Nilai diskriminan menentukan banyak dan jenis akar.
    """)

    st.table({
        "Nilai D": [
            "D > 0",
            "D = 0",
            "D < 0"
        ],
        "Jenis Akar": [
            "Dua akar real berbeda",
            "Satu akar real kembar",
            "Tidak memiliki akar real"
        ]
    })

    # ========================================================
    # 13. CONTOH DISKRIMINAN
    # ========================================================

    st.subheader("13. Contoh Menentukan Jenis Akar")

    st.markdown("""
    Tentukan jenis akar:
    """)

    st.latex(r"x^2-4x+4=0")

    st.latex(r"D=(-4)^2-4(1)(4)")

    st.latex(r"D=0")

    st.success(
        "Karena D = 0, persamaan memiliki satu akar real kembar."
    )

    # ========================================================
    # 14. HUBUNGAN AKAR DAN KOEFISIEN
    # ========================================================

    st.subheader("14. Hubungan Akar dan Koefisien")

    st.markdown("""
    Misalkan akar-akar persamaan:
    """)

    st.latex(r"ax^2+bx+c=0")

    st.markdown("""
    adalah x₁ dan x₂.
    """)

    st.markdown("Jumlah akar:");

    st.latex(r"x_1+x_2=-\frac{b}{a}")

    st.markdown("Hasil kali akar:");

    st.latex(r"x_1x_2=\frac{c}{a}")

    # ========================================================
    # 15. CONTOH HUBUNGAN AKAR
    # ========================================================

    st.subheader("15. Contoh Hubungan Akar dan Koefisien")

    st.markdown("""
    Diketahui:
    """)

    st.latex(r"2x^2-7x+3=0")

    st.markdown("Jumlah akar:");

    st.latex(r"x_1+x_2=\frac{7}{2}")

    st.markdown("Hasil kali akar:");

    st.latex(r"x_1x_2=\frac{3}{2}")

    # ========================================================
    # 16. FUNGSI KUADRAT
    # ========================================================

    st.subheader("16. Pengertian Fungsi Kuadrat")

    st.markdown("""
    Fungsi kuadrat adalah fungsi polinomial yang memiliki
    pangkat tertinggi dua.
    """)

    st.latex(r"f(x)=ax^2+bx+c")

    st.markdown("""
    dengan a ≠ 0.
    """)

    st.markdown("Contoh:");

    st.latex(r"f(x)=x^2-4x+3")

    st.latex(r"f(x)=2x^2+3x-5")

    # ========================================================
    # 17. HUBUNGAN PERSAMAAN DAN FUNGSI KUADRAT
    # ========================================================

    st.subheader("17. Hubungan Persamaan dan Fungsi Kuadrat")

    st.markdown("""
    Persamaan kuadrat dapat diperoleh dengan membuat
    nilai fungsi kuadrat sama dengan nol.
    """)

    st.latex(r"f(x)=ax^2+bx+c")

    st.latex(r"f(x)=0")

    st.latex(r"ax^2+bx+c=0")

    st.info(
        "Akar persamaan kuadrat merupakan nilai x ketika "
        "grafik fungsi kuadrat memotong atau menyentuh sumbu-X."
    )

    # ========================================================
    # 18. GRAFIK FUNGSI KUADRAT
    # ========================================================

    st.subheader("18. Grafik Fungsi Kuadrat")

    st.markdown("""
    Grafik fungsi kuadrat berbentuk parabola.

    Bentuk dasar:
    """)

    st.latex(r"f(x)=x^2")

    st.markdown("""
    Jika a > 0, parabola terbuka ke atas.

    Jika a < 0, parabola terbuka ke bawah.
    """)

    st.markdown("Contoh grafik fungsi kuadrat:")

    st.latex(r"f(x)=x^2-4x+3")

    # ========================================================
    # GRAFIK INTERAKTIF
    # ========================================================

    st.subheader("19. Eksplorasi Grafik Parabola")

    a = st.slider(
        "Koefisien a",
        min_value=-5.0,
        max_value=5.0,
        value=1.0,
        step=0.5,
        key="kuadrat_a"
    )

    b = st.slider(
        "Koefisien b",
        min_value=-10.0,
        max_value=10.0,
        value=0.0,
        step=1.0,
        key="kuadrat_b"
    )

    c = st.slider(
        "Konstanta c",
        min_value=-10.0,
        max_value=10.0,
        value=0.0,
        step=1.0,
        key="kuadrat_c"
    )

    if a != 0:

        st.latex(
            f"f(x)={a}x^2+{b}x+{c}"
        )

        st.markdown("""
        Ubah nilai a, b, dan c untuk melihat perubahan
        bentuk grafik fungsi kuadrat.
        """)

        import numpy as np
        import pandas as pd

        x = np.linspace(-10, 10, 200)
        y = a * x**2 + b * x + c

        data = pd.DataFrame({
            "x": x,
            "f(x)": y
        })

        st.line_chart(
            data,
            x="x",
            y="f(x)"
        )

        if a > 0:

            st.success(
                "Karena a > 0, parabola terbuka ke atas."
            )

        else:

            st.warning(
                "Karena a < 0, parabola terbuka ke bawah."
            )

    else:

        st.warning(
            "Nilai a tidak boleh 0 karena akan menghasilkan fungsi linear."
        )

    # ========================================================
    # 20. SUMBU SIMETRI
    # ========================================================

    st.subheader("20. Sumbu Simetri")

    st.markdown("""
    Sumbu simetri parabola merupakan garis vertikal yang
    membagi parabola menjadi dua bagian yang simetris.
    """)

    st.latex(r"x=-\frac{b}{2a}")

    st.markdown("Contoh:");

    st.latex(r"f(x)=x^2-6x+5")

    st.latex(r"x=-\frac{-6}{2(1)}")

    st.latex(r"x=3")

    st.success("Sumbu simetrinya adalah x = 3.")

    # ========================================================
    # 21. TITIK PUNCAK
    # ========================================================

    st.subheader("21. Titik Puncak")

    st.markdown("""
    Titik puncak merupakan titik maksimum atau minimum
    pada grafik fungsi kuadrat.
    """)

    st.markdown("Koordinat x titik puncak:");

    st.latex(r"x_p=-\frac{b}{2a}")

    st.markdown("Koordinat y diperoleh dengan:");

    st.latex(r"y_p=f(x_p)")

    st.markdown("Sehingga titik puncaknya adalah:");

    st.latex(r"(x_p,y_p)")

    # ========================================================
    # 22. CONTOH TITIK PUNCAK
    # ========================================================

    st.subheader("22. Contoh Menentukan Titik Puncak")

    st.markdown("""
    Diketahui:
    """)

    st.latex(r"f(x)=x^2-6x+5")

    st.markdown("Sumbu simetri:");

    st.latex(r"x_p=3")

    st.markdown("Nilai y:");

    st.latex(r"y_p=3^2-6(3)+5")

    st.latex(r"y_p=-4")

    st.success(
        "Titik puncaknya adalah (3, −4)."
    )

    # ========================================================
    # 23. NILAI MAKSIMUM DAN MINIMUM
    # ========================================================

    st.subheader("23. Nilai Maksimum dan Minimum")

    st.markdown("""
    Jika a > 0, parabola terbuka ke atas sehingga
    titik puncak merupakan nilai minimum.

    Jika a < 0, parabola terbuka ke bawah sehingga
    titik puncak merupakan nilai maksimum.
    """)

    st.table({
        "Kondisi": [
            "a > 0",
            "a < 0"
        ],
        "Parabola": [
            "Terbuka ke atas",
            "Terbuka ke bawah"
        ],
        "Titik Puncak": [
            "Minimum",
            "Maksimum"
        ]
    })

    # ========================================================
    # 24. TITIK POTONG SUMBU Y
    # ========================================================

    st.subheader("24. Titik Potong dengan Sumbu-Y")

    st.markdown("""
    Untuk menentukan titik potong dengan sumbu-Y,
    gunakan x = 0.
    """)

    st.latex(r"f(0)=c")

    st.markdown("""
    Jadi titik potong dengan sumbu-Y adalah:
    """)

    st.latex(r"(0,c)")

    st.markdown("Contoh:");

    st.latex(r"f(x)=x^2-4x+3")

    st.latex(r"f(0)=3")

    st.success("Titik potong sumbu-Y adalah (0, 3).")

    # ========================================================
    # 25. TITIK POTONG SUMBU X
    # ========================================================

    st.subheader("25. Titik Potong dengan Sumbu-X")

    st.markdown("""
    Untuk menentukan titik potong dengan sumbu-X,
    kita mencari nilai x ketika y = 0.
    """)

    st.latex(r"f(x)=0")

    st.markdown("Contoh:");

    st.latex(r"x^2-4x+3=0")

    st.latex(r"(x-1)(x-3)=0")

    st.latex(r"x=1\quad\text{atau}\quad x=3")

    st.success(
        "Grafik memotong sumbu-X di titik (1, 0) dan (3, 0)."
    )

    # ========================================================
    # 26. BENTUK VERTEX
    # ========================================================

    st.subheader("26. Bentuk Puncak atau Vertex Form")

    st.markdown("""
    Fungsi kuadrat dapat ditulis dalam bentuk:
    """)

    st.latex(r"f(x)=a(x-h)^2+k")

    st.markdown("""
    Bentuk tersebut memudahkan kita menentukan titik puncak.
    """)

    st.latex(r"(h,k)")

    st.markdown("Contoh:");

    st.latex(r"f(x)=2(x-3)^2-4")

    st.success(
        "Titik puncaknya adalah (3, −4)."
    )

    # ========================================================
    # 27. TRANSFORMASI GRAFIK
    # ========================================================

    st.subheader("27. Transformasi Grafik Fungsi Kuadrat")

    st.markdown("""
    Bentuk:
    """)

    st.latex(r"f(x)=a(x-h)^2+k")

    st.markdown("""
    memberikan informasi:

    - h menggeser grafik secara horizontal;
    - k menggeser grafik secara vertikal;
    - a menentukan arah buka dan tingkat kelengkungan.
    """)

    # ========================================================
    # 28. PENERAPAN
    # ========================================================

    st.subheader("28. Penerapan Fungsi Kuadrat")

    st.markdown("""
    Fungsi kuadrat dapat digunakan untuk memodelkan:

    - lintasan benda;
    - tinggi maksimum;
    - luas maksimum;
    - keuntungan maksimum;
    - jarak dan waktu;
    - desain arsitektur;
    - bentuk parabola pada teknologi.
    """)

    # ========================================================
    # 29. CONTOH LINTASAN
    # ========================================================

    st.subheader("29. Contoh Masalah Kontekstual")

    st.markdown("""
    Ketinggian sebuah bola yang dilempar ke udara dimodelkan oleh:
    """)

    st.latex(r"h(t)=-5t^2+20t+1")

    st.markdown("""
    dengan h dalam meter dan t dalam detik.

    Tentukan waktu ketika bola mencapai ketinggian maksimum.
    """)

    st.markdown("Gunakan rumus sumbu simetri:");

    st.latex(r"t=-\frac{b}{2a}")

    st.latex(r"t=-\frac{20}{2(-5)}")

    st.latex(r"t=2")

    st.success(
        "Bola mencapai ketinggian maksimum setelah 2 detik."
    )

    st.markdown("Tinggi maksimumnya:");

    st.latex(r"h(2)=-5(2)^2+20(2)+1")

    st.latex(r"h(2)=21")

    st.success(
        "Tinggi maksimum bola adalah 21 meter."
    )

    # ========================================================
    # 30. CONTOH LUAS
    # ========================================================

    st.subheader("30. Contoh Masalah Luas Maksimum")

    st.markdown("""
    Sebuah persegi panjang memiliki panjang x dan lebar
    yang bergantung pada x.

    Misalkan luasnya dimodelkan oleh:
    """)

    st.latex(r"L(x)=-x^2+10x")

    st.markdown("""
    Karena koefisien x² negatif, grafik membuka ke bawah.
    Dengan demikian, titik puncaknya merupakan nilai maksimum.
    """)

    st.latex(r"x=-\frac{10}{2(-1)}")

    st.latex(r"x=5")

    st.latex(r"L(5)=-5^2+10(5)")

    st.latex(r"L(5)=25")

    st.success(
        "Nilai maksimum luas adalah 25 satuan luas."
    )

    # ========================================================
    # 31. LATIHAN
    # ========================================================

    st.subheader("31. Latihan")

    st.markdown("""
    **Soal 1**

    Tentukan akar-akar persamaan:
    """)
    st.latex(r"x^2-7x+12=0")

    st.markdown("""
    **Soal 2**

    Tentukan akar-akar:
    """)
    st.latex(r"2x^2-5x-3=0")

    st.markdown("""
    **Soal 3**

    Tentukan diskriminan:
    """)
    st.latex(r"x^2+4x+5=0")


    st.markdown("""
    **Soal 4**

    Tentukan jumlah dan hasil kali akar:
    """)
    st.latex(r"3x^2-8x+2=0")

    st.markdown("""
    **Soal 5**

    Tentukan sumbu simetri:
    """)
    st.latex(r"f(x)=x^2-8x+10")
    
    st.markdown("""
    **Soal 6**

    Tentukan titik puncak:
    """)
    st.latex(r"f(x)=x^2-6x+5")

    st.markdown("""
    **Soal 7**

    Tentukan titik potong dengan sumbu-Y:
    """)
    st.latex(r"f(x)=2x^2-3x+5")

    st.markdown("""
    **Soal 8**

    Tentukan nilai maksimum fungsi:
    """)
    st.latex(r"f(x)=-x^2+6x+2")

    # ========================================================
    # 32. KUIS
    # ========================================================

    st.subheader("32. Kuis Interaktif")

    jawaban = st.radio(
        "Akar-akar dari x² − 5x + 6 = 0 adalah...",
        [
            "x = 1 dan x = 6",
            "x = 2 dan x = 3",
            "x = −2 dan x = −3",
            "x = 3 dan x = 4"
        ],
        key="kuis_kuadrat_1"
    )

    if st.button(
        "Periksa Jawaban",
        key="cek_kuadrat_1"
    ):

        if jawaban == "x = 2 dan x = 3":

            st.success(
                "✅ Benar! x² − 5x + 6 = (x − 2)(x − 3)."
            )

        else:

            st.error(
                "❌ Belum tepat. Coba faktorkan x² − 5x + 6."
            )

    # ========================================================
    # 33. RANGKUMAN
    # ========================================================

    with st.expander("📌 Rangkuman Materi", expanded=False):

        st.markdown("""
        ### Persamaan Kuadrat

        Bentuk umum:
        """)
        #st.latex(r"ax^2+bx+c=0")
        st.markdown(r"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$ax^2+bx+c=0$")
        
        st.markdown(r"""
        dengan a ≠ 0.

        Persamaan kuadrat dapat diselesaikan dengan:

        - faktorisasi;
        - melengkapkan kuadrat sempurna;
        - rumus ABC.

        ### Diskriminan

        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$D=b^2-4ac$

        - D > 0 → dua akar real berbeda.
        - D = 0 → satu akar real kembar.
        - D < 0 → tidak memiliki akar real.

        ### Fungsi Kuadrat

        Bentuk umum:

        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$f(x)=ax^2+bx+c$

        Grafik fungsi kuadrat berbentuk parabola.

        Jika a > 0 → parabola terbuka ke atas.

        Jika a < 0 → parabola terbuka ke bawah.

        ### Sumbu Simetri 
        """)
        st.markdown(r"""
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$x=-\frac{b}{2a}$
        """)
        
        st.markdown("""

        ### Titik Puncak

        Titik puncak dapat diperoleh dari:

        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$(x_p,f(x_p))$

        Fungsi kuadrat banyak digunakan dalam masalah
        maksimum, minimum, lintasan, dan pemodelan.
        """)



def sptldv():

    st.header("📊 Sistem Pertidaksamaan Linear Dua Variabel (SPtLDV)")

    st.markdown("""
    ### Matematika Kelas X — Fase E

    Sistem Pertidaksamaan Linear Dua Variabel atau SPtLDV merupakan
    sistem yang terdiri atas dua atau lebih pertidaksamaan linear
    yang melibatkan dua variabel.

    Konsep SPtLDV banyak digunakan untuk menentukan daerah yang
    memenuhi beberapa batasan secara bersamaan, misalnya dalam
    perencanaan produksi, alokasi sumber daya, dan masalah optimasi.
    """)

    # ========================================================
    # TUJUAN PEMBELAJARAN
    # ========================================================

    with st.expander("🎯 Tujuan Pembelajaran", expanded=True):

        st.markdown("""
        Setelah mempelajari materi ini, peserta didik diharapkan mampu:

        1. Menjelaskan pengertian pertidaksamaan linear dua variabel.
        2. Menentukan bentuk umum pertidaksamaan linear dua variabel.
        3. Menggambar grafik garis batas.
        4. Menentukan daerah penyelesaian pertidaksamaan.
        5. Menggunakan titik uji untuk menentukan daerah penyelesaian.
        6. Menentukan daerah penyelesaian sistem pertidaksamaan.
        7. Menyelesaikan masalah kontekstual menggunakan SPtLDV.
        """)

    # ========================================================
    # 1. APERSEPSI
    # ========================================================

    st.subheader("1. Apersepsi")

    st.markdown("""
    Dalam kehidupan sehari-hari sering terdapat kondisi yang
    menggunakan kata-kata seperti:

    - paling sedikit;
    - paling banyak;
    - tidak lebih dari;
    - tidak kurang dari;
    - maksimum;
    - minimum.

    Kondisi tersebut dapat dinyatakan menggunakan pertidaksamaan.
    """)

    st.markdown("""
    Misalnya, seorang siswa memiliki uang Rp50.000 dan ingin membeli
    buku seharga x rupiah serta alat tulis seharga y rupiah.

    Jumlah uang yang digunakan tidak boleh melebihi Rp50.000.
    """)

    st.latex(r"x+y\leq50000")

    st.info(
        "Pertidaksamaan digunakan untuk menyatakan kondisi yang "
        "memiliki batas atau rentang nilai tertentu."
    )

    # ========================================================
    # 2. PENGERTIAN
    # ========================================================

    st.subheader("2. Pengertian Pertidaksamaan Linear Dua Variabel")

    st.markdown("""
    Pertidaksamaan linear dua variabel adalah pertidaksamaan
    yang memuat dua variabel dengan pangkat tertinggi masing-masing
    variabel adalah satu.
    """)

    st.markdown("Bentuk umumnya adalah:")

    st.latex(r"ax+by<c")

    st.markdown("atau bentuk lainnya:")

    st.latex(r"ax+by\leq c")

    st.latex(r"ax+by>c")

    st.latex(r"ax+by\geq c")

    st.markdown("""
    dengan a dan b tidak keduanya sama dengan nol.
    """)

    # ========================================================
    # 3. CONTOH
    # ========================================================

    st.subheader("3. Contoh Pertidaksamaan Linear Dua Variabel")

    st.markdown("Beberapa contoh:");

    st.latex(r"2x+3y\leq12")

    st.latex(r"x-y>4")

    st.latex(r"3x+2y\geq6")

    st.latex(r"4x+y<20")

    st.markdown("""
    Semua bentuk tersebut merupakan pertidaksamaan linear
    dua variabel karena variabel x dan y berpangkat satu.
    """)

    # ========================================================
    # 4. BUKAN PERTIDAKSAMAAN LINEAR
    # ========================================================

    st.subheader("4. Contoh yang Bukan Pertidaksamaan Linear")

    st.markdown("""
    Beberapa bentuk berikut bukan pertidaksamaan linear
    dua variabel:
    """)

    st.latex(r"x^2+y\leq10")

    st.latex(r"xy>5")

    st.latex(r"x+y^2<8")

    st.info(
        "Jika terdapat perkalian antarvariabel atau pangkat variabel "
        "lebih dari satu, maka bentuk tersebut bukan pertidaksamaan linear."
    )

    # ========================================================
    # 5. HUBUNGAN DENGAN PERSAMAAN GARIS
    # ========================================================

    st.subheader("5. Garis Batas")

    st.markdown("""
    Untuk menggambar grafik pertidaksamaan linear,
    tanda pertidaksamaan sementara diubah menjadi tanda sama dengan.

    Misalnya:
    """)

    st.latex(r"2x+y\leq6")

    st.markdown("Garis batasnya adalah:")

    st.latex(r"2x+y=6")

    st.markdown("""
    Garis tersebut digunakan untuk membatasi daerah yang memenuhi
    pertidaksamaan.
    """)

    # ========================================================
    # 6. MENENTUKAN TITIK POTONG
    # ========================================================

    st.subheader("6. Menentukan Titik Potong Garis")

    st.markdown("""
    Untuk menggambar garis, salah satu cara yang mudah adalah
    menentukan titik potong dengan sumbu-X dan sumbu-Y.
    """)

    st.markdown("Misalkan:")

    st.latex(r"2x+y=6")

    st.markdown("### Titik potong sumbu-X")

    st.markdown("""
    Untuk sumbu-X, nilai y = 0.
    """)

    st.latex(r"2x+0=6")

    st.latex(r"x=3")

    st.markdown("Titiknya adalah:")

    st.latex(r"(3,0)")

    st.markdown("### Titik potong sumbu-Y")

    st.markdown("""
    Untuk sumbu-Y, nilai x = 0.
    """)

    st.latex(r"2(0)+y=6")

    st.latex(r"y=6")

    st.markdown("Titiknya adalah:")

    st.latex(r"(0,6)")

    # ========================================================
    # 7. GARIS SOLID DAN PUTUS-PUTUS
    # ========================================================

    st.subheader("7. Garis Batas pada Grafik")

    st.markdown("""
    Jenis garis batas ditentukan oleh tanda pertidaksamaan.
    """)

    st.table({
        "Tanda": [
            "<",
            ">",
            "≤",
            "≥"
        ],
        "Garis Batas": [
            "Putus-putus",
            "Putus-putus",
            "Penuh",
            "Penuh"
        ]
    })

    st.info(
        "Tanda ≤ atau ≥ berarti garis batas termasuk daerah penyelesaian."
    )

    # ========================================================
    # 8. MENENTUKAN DAERAH PENYELESAIAN
    # ========================================================

    st.subheader("8. Menentukan Daerah Penyelesaian")

    st.markdown("""
    Setelah menggambar garis batas, kita perlu menentukan
    sisi bidang yang memenuhi pertidaksamaan.

    Salah satu cara yang paling mudah adalah menggunakan
    titik uji.
    """)

    # ========================================================
    # 9. TITIK UJI
    # ========================================================

    st.subheader("9. Metode Titik Uji")

    st.markdown("""
    Misalkan diberikan:
    """)

    st.latex(r"2x+y\leq6")

    st.markdown("""
    Pilih titik yang tidak berada pada garis batas.
    Salah satu pilihan yang mudah adalah titik O(0,0).
    """)

    st.latex(r"2(0)+0\leq6")

    st.latex(r"0\leq6")

    st.success(
        "Pernyataan benar, sehingga titik (0,0) termasuk daerah penyelesaian."
    )

    # ========================================================
    # 10. CONTOH TITIK UJI LAIN
    # ========================================================

    st.markdown("""
    Misalkan:
    """)

    st.latex(r"x+y>4")

    st.markdown("""
    Gunakan titik (0,0) sebagai titik uji.
    """)

    st.latex(r"0+0>4")

    st.markdown("""
    Pernyataan tersebut salah.

    Jadi titik (0,0) bukan bagian dari daerah penyelesaian.
    """)

    # ========================================================
    # 11. SISTEM PERTIDAKSAMAAN
    # ========================================================

    st.subheader("11. Sistem Pertidaksamaan Linear Dua Variabel")

    st.markdown("""
    Sistem pertidaksamaan linear dua variabel terdiri atas
    dua atau lebih pertidaksamaan yang harus dipenuhi secara
    bersamaan.
    """)

    st.markdown("Contoh:")

    st.latex(r"x+y\leq6")

    st.latex(r"x\geq0")

    st.latex(r"y\geq0")

    st.markdown("""
    Daerah penyelesaian adalah daerah yang memenuhi
    seluruh pertidaksamaan tersebut.
    """)

    # ========================================================
    # 12. LANGKAH PENYELESAIAN
    # ========================================================

    st.subheader("12. Langkah-Langkah Menyelesaikan SPtLDV")

    st.markdown("""
    **Langkah 1**

    Ubah masing-masing pertidaksamaan menjadi persamaan
    untuk mendapatkan garis batas.

    **Langkah 2**

    Tentukan minimal dua titik pada masing-masing garis.

    **Langkah 3**

    Gambar garis batas pada bidang koordinat.

    **Langkah 4**

    Tentukan daerah penyelesaian masing-masing pertidaksamaan
    menggunakan titik uji.

    **Langkah 5**

    Tentukan irisan seluruh daerah penyelesaian.

    **Langkah 6**

    Arsirlah daerah yang memenuhi seluruh pertidaksamaan.
    """)

    # ========================================================
    # 13. CONTOH SPtLDV
    # ========================================================

    st.subheader("13. Contoh SPtLDV")

    st.markdown("""
    Tentukan daerah penyelesaian dari:
    """)

    st.latex(r"x+y\leq6")

    st.latex(r"x\geq0")

    st.latex(r"y\geq0")

    st.markdown("### Langkah 1 — Garis batas")

    st.latex(r"x+y=6")

    st.markdown("Titik potong dengan sumbu-X:")

    st.latex(r"(6,0)")

    st.markdown("Titik potong dengan sumbu-Y:")

    st.latex(r"(0,6)")

    st.markdown("""
    Karena x ≥ 0 dan y ≥ 0, daerah penyelesaian berada
    pada kuadran I.

    Daerah penyelesaian merupakan daerah segitiga yang
    dibatasi oleh sumbu-X, sumbu-Y, dan garis x + y = 6.
    """)

    # ========================================================
    # 14. CONTOH DENGAN DUA BATAS
    # ========================================================

    st.subheader("14. Contoh dengan Dua Pertidaksamaan")

    st.markdown("""
    Tentukan daerah penyelesaian:
    """)

    st.latex(r"x+y\leq8")

    st.latex(r"x+2y\leq10")

    st.latex(r"x\geq0")

    st.latex(r"y\geq0")

    st.markdown("""
    Penyelesaian diperoleh dengan menggambar seluruh garis batas
    kemudian mencari daerah yang memenuhi semua pertidaksamaan.
    """)

    # ========================================================
    # 15. DAERAH PENYELESAIAN DENGAN INTERAKTIF
    # ========================================================

    st.subheader("15. Eksplorasi Grafik SPtLDV")

    st.markdown("""
    Gunakan slider berikut untuk mengubah konstanta pada
    pertidaksamaan:
    """)

    batas = st.slider(
        "Nilai batas c pada x + y ≤ c",
        min_value=2,
        max_value=20,
        value=6,
        step=1
    )

    st.latex(r"x+y\leq c")

    st.markdown(f"""
    Pada eksplorasi ini digunakan nilai c = **{batas}**.

    Garis batasnya adalah:
    """)

    st.latex(f"x+y={batas}")

    # ------------------------------------------------------------
    # VISUALISASI GRAFIK SPtLDV
    # ------------------------------------------------------------
    
    x = np.linspace(0, batas, 200)
    y = batas - x
    
    fig = go.Figure()
    
    # Daerah penyelesaian
    fig.add_trace(
        go.Scatter(
            x=np.concatenate([x, [0]]),
            y=np.concatenate([y, [0]]),
            fill="toself",
            mode="none",
            name="Daerah penyelesaian"
        )
    )
    
    # Garis batas x + y = c
    fig.add_trace(
        go.Scatter(
            x=x,
            y=y,
            mode="lines",
            name=f"x + y = {batas}"
        )
    )
    
    # Titik potong sumbu
    fig.add_trace(
        go.Scatter(
            x=[0, batas],
            y=[batas, 0],
            mode="markers",
            name="Titik potong",
            text=[
                f"(0, {batas})",
                f"({batas}, 0)"
            ],
            textposition="top center"
        )
    )
    
    fig.update_layout(
        xaxis_title="x",
        yaxis_title="y",
        xaxis=dict(
            range=[0, batas + 1],
            zeroline=True
        ),
        yaxis=dict(
            range=[0, batas + 1],
            zeroline=True
        ),
        height=500,
        showlegend=True
    )
    
    st.plotly_chart(
        fig,
        use_container_width=True
    )


    st.info(
        "Semakin besar nilai c, semakin luas daerah yang memenuhi "
        "pertidaksamaan x + y ≤ c pada kuadran pertama."
    )

    # ========================================================
    # 16. PENERAPAN
    # ========================================================

    st.subheader("16. Penerapan SPtLDV")

    st.markdown("""
    SPtLDV dapat digunakan untuk memodelkan berbagai masalah
    dalam kehidupan sehari-hari, seperti:

    - perencanaan produksi;
    - pembelian barang;
    - penggunaan bahan baku;
    - alokasi waktu;
    - penggunaan anggaran;
    - kapasitas kendaraan;
    - perencanaan makanan;
    - masalah optimasi sederhana.
    """)

    # ========================================================
    # 17. CONTOH KONTEKSTUAL
    # ========================================================

    st.subheader("17. Contoh Masalah Kontekstual")

    st.markdown("""
    Sebuah toko menjual buku dan alat tulis.

    Misalkan:

    - x = banyak buku;
    - y = banyak alat tulis.

    Kapasitas penyimpanan toko paling banyak 50 barang.
    """)

    st.latex(r"x+y\leq50")

    st.markdown("""
    Jika jumlah buku dan alat tulis tidak boleh negatif:
    """)

    st.latex(r"x\geq0")

    st.latex(r"y\geq0")

    st.markdown("""
    Ketiga pertidaksamaan tersebut membentuk model SPtLDV
    untuk masalah tersebut.
    """)

    # ========================================================
    # 18. CONTOH PRODUKSI
    # ========================================================

    st.subheader("18. Contoh Perencanaan Produksi")

    st.markdown("""
    Sebuah usaha memproduksi meja dan kursi.

    Misalkan:

    - x = jumlah meja;
    - y = jumlah kursi.

    Setiap meja membutuhkan 4 unit bahan.
    Setiap kursi membutuhkan 2 unit bahan.
    Persediaan bahan hanya 40 unit.
    """)

    st.latex(r"4x+2y\leq40")

    st.markdown("""
    Jika kapasitas produksi paling banyak 15 barang:
    """)

    st.latex(r"x+y\leq15")

    st.markdown("""
    Karena jumlah produk tidak mungkin negatif:
    """)

    st.latex(r"x\geq0")

    st.latex(r"y\geq0")

    st.markdown("""
    Sistem tersebut merupakan model SPtLDV.
    """)

    # ========================================================
    # 19. HUBUNGAN DENGAN PROGRAM LINEAR
    # ========================================================

    st.subheader("19. SPtLDV dan Program Linear")

    st.markdown("""
    SPtLDV sering digunakan sebagai dasar dalam program linear.

    Dalam program linear, kita biasanya memiliki:

    **1. Variabel keputusan**

    Variabel yang nilainya ingin ditentukan.

    **2. Kendala**

    Pertidaksamaan yang membatasi variabel.

    **3. Fungsi tujuan**

    Fungsi yang akan dimaksimumkan atau diminimumkan.
    """)

    st.markdown("Contoh fungsi tujuan:")

    st.latex(r"Z=5000x+3000y")

    st.markdown("""
    Fungsi tersebut dapat digunakan untuk menentukan keuntungan
    maksimum apabila x dan y menyatakan jumlah produk.
    """)

    # ========================================================
    # 20. LATIHAN
    # ========================================================

    st.subheader("20. Latihan")

    st.markdown("""
    **Soal 1**

    Tentukan apakah bentuk berikut merupakan pertidaksamaan
    linear dua variabel:
    """)
    st.latex(r"2x+3y \leq 12")

                
    st.markdown("""
    **Soal 2**

    Tentukan titik potong sumbu-X dan sumbu-Y dari:
    """)
    st.latex(r"2x+y=8")

    st.markdown("""
    **Soal 3**

    Tentukan apakah titik (2,1) memenuhi:   
    """)
    st.latex(r"x+y \leq 4")

    st.markdown("""
    **Soal 4**

    Tentukan daerah penyelesaian:
    """)
    st.latex(r"x+y \leq 6,\quad x \geq 0,\quad \text{dan}\quad y \geq 0")

    st.markdown("""
    **Soal 5**

    Tentukan apakah titik (3,2) memenuhi sistem:
    """)
    st.latex("x+y \leq 5")
    st.latex(r"x \geq 0")
    st.latex(r"y \geq 0")

    st.markdown("""
    **Soal 6**

    Sebuah toko memiliki kapasitas penyimpanan paling banyak
    100 barang. Jika x menyatakan jumlah buku dan y menyatakan
    jumlah alat tulis, tuliskan model pertidaksamaannya.
    """)

    # ========================================================
    # 21. KUIS INTERAKTIF
    # ========================================================

    st.subheader("21. Kuis Interaktif")

    jawaban = st.radio(
        "Manakah yang merupakan pertidaksamaan linear dua variabel?",
        [
            "x² + y ≤ 10",
            "2x + 3y ≤ 12",
            "xy ≥ 5",
            "x + y² > 4"
        ],
        key="kuis_sptldv_1"
    )

    if st.button(
        "Periksa Jawaban",
        key="cek_sptldv_1"
    ):

        if jawaban == "2x + 3y ≤ 12":

            st.success(
                "✅ Benar! Variabel x dan y berpangkat satu."
            )

        else:

            st.error(
                "❌ Belum tepat. Perhatikan pangkat variabel x dan y."
            )

    # ========================================================
    # 22. RANGKUMAN
    # ========================================================

    with st.expander("📌 Rangkuman Materi", expanded=False):

        st.markdown("""
        ### Konsep penting SPtLDV

        **1. Pertidaksamaan linear dua variabel**

        Memuat dua variabel dengan pangkat tertinggi satu.

        **2. Garis batas**

        Diperoleh dengan mengganti tanda pertidaksamaan
        menjadi tanda sama dengan.

        **3. Titik uji**

        Digunakan untuk menentukan sisi bidang yang memenuhi
        pertidaksamaan.

        **4. Garis penuh**

        Digunakan untuk tanda ≤ atau ≥.

        **5. Garis putus-putus**

        Digunakan untuk tanda < atau >.

        **6. Sistem pertidaksamaan**

        Daerah penyelesaian merupakan irisan dari seluruh
        daerah yang memenuhi masing-masing pertidaksamaan.

        **7. Penerapan**

        SPtLDV dapat digunakan untuk memodelkan kendala
        dalam masalah kehidupan nyata dan menjadi dasar
        dalam program linear.
        """)



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

    st.markdown("dengan:")
    st.latex(r"1\leq a < 10")

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

#=======================================================================================================================================
#=======================================================================================================================================

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

    st.markdown("dengan syarat:")
    st.latex(r"a > 0")
    st.latex(r"a \neq 1")

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
    st.markdown(r"Perhatikan fungsi: $f(x)=2^x$.")



    st.markdown(
    """
    <table style="width:100%; text-align:center; vertical-align:middle;">
        <tr>
            <th>x</th>
            <th>f(x) = 2ˣ</th>
        </tr>
        <tr><td>-3</td><td>1/8</td></tr>
        <tr><td>-2</td><td>1/4</td></tr>
        <tr><td>-1</td><td>1/2</td></tr>
        <tr><td>0</td><td>1</td></tr>
        <tr><td>1</td><td>2</td></tr>
        <tr><td>2</td><td>4</td></tr>
        <tr><td>3</td><td>8</td></tr>
    </table>
    """,
    unsafe_allow_html=True
    )


    st.markdown("""
    Dari tabel tersebut terlihat bahwa ketika x bertambah,
    nilai fungsi juga bertambah.
    """)

    # ========================================================
    # 6. KARAKTERISTIK GRAFIK
    # ========================================================

    st.subheader("6. Karakteristik Grafik Fungsi Eksponensial")

    st.markdown(r"""
        Fungsi $f(x)=a^x$ mempunyai beberapa karakteristik penting:
        
        - Grafik selalu melalui titik $(0,1)$.
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
    Jika basis lebih besar dari 1, yaitu \(a > 1\),
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
    Jika \(0 < a < 1\), maka fungsi eksponensial bersifat menurun.
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

    st.markdown(r"""
    Jika kedua ruas memiliki basis yang sama dan basis tersebut
    memenuhi $a>0$ serta $a\neq1$, maka eksponennya dapat
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
    Karena $(4=2^2)$, maka:
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
    Karena $(8=2^3)$, maka:
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
    Karena $(4^x=(2^x)^2)$, misalkan:
    """)

    st.latex(r"t=2^x")

    st.markdown("Maka persamaannya menjadi:")

    st.latex(r"t^2-5t+4=0")

    st.latex(r"(t-1)(t-4)=0")

    st.latex(r"t=1\quad\text{atau}\quad t=4")

    st.markdown("Kembalikan ke $(2^x)$:")

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

    st.latex(r"N(t)=N_0 a^t")

    st.markdown("""
    Keterangan:

    - $N(t)$ = jumlah pada waktu t
    - $N_0$ = jumlah awal
    - $a$ = faktor pertumbuhan
    - $t$ = waktu
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

    with st.container(border=True):
        st.markdown("**Soal 1**")
        st.markdown(r"Tentukan nilai $f(3)$ jika $f(x)=2^x$.")


    with st.container(border=True):
        st.markdown("**Soal 2**")
        st.markdown(r"Tentukan penyelesaian $2^{x+2}=2^6$.")
    
    
    with st.container(border=True):
        st.markdown("**Soal 3**")
        st.markdown(r"Tentukan penyelesaian $3^{2x-1}=3^7$.")
    
    
    with st.container(border=True):
        st.markdown("**Soal 4**")
        st.markdown(r"Tentukan penyelesaian $4^x=2^8$.")
    
    
    with st.container(border=True):
        st.markdown("**Soal 5**")
        st.markdown(r"Tentukan penyelesaian $9^x=3^6$.")
    
    
    with st.container(border=True):
        st.markdown("**Soal 6**")
        st.markdown(
            """
            Sebuah populasi mula-mula 2.000 orang dan bertambah
            menjadi dua kali lipat setiap periode. Tentukan populasi
            setelah 6 periode.
            """
        )
    
    
    with st.container(border=True):
        st.markdown("**Soal 7**")
        st.markdown(
            """
            Suatu zat mula-mula memiliki massa 1.000 gram.
            Setiap periode massanya menjadi 80% dari sebelumnya.
            Tentukan massa setelah 3 periode.
            """
        )

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

        st.markdown(r"""
                
        **1. Fungsi eksponensial**
        
        Variabel berada pada pangkat.
        
        **2. Bentuk umum**
        
        $f(x)=a^x$
        
        dengan $a>0$ dan $a\neq1$.
        
        **3. Pertumbuhan**
        
        Jika $a>1$, fungsi meningkat.
        
        **4. Peluruhan**
        
        Jika $0<a<1$, fungsi menurun.
        
        **5. Persamaan eksponensial**
        
        Jika basis sama, eksponen dapat disamakan.
        
        **6. Grafik**
        
        Grafik melalui titik $(0,1)$, mempunyai range positif,
        dan mempunyai asimtot horizontal $y=0$.
        
        **7. Penerapan**
        
        Fungsi eksponensial dapat digunakan untuk memodelkan
        pertumbuhan penduduk, bakteri, investasi, dan peluruhan.
        """)
