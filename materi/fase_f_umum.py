import streamlit as st
import pandas as pd
import math

def transformasi_fungsi():

    st.markdown("## 📐 Transformasi Fungsi")

    st.markdown("""
    Transformasi fungsi merupakan perubahan bentuk, posisi, atau ukuran grafik
    suatu fungsi tanpa harus menggambar ulang grafik dari awal.

    Transformasi fungsi sangat penting untuk memahami hubungan antara grafik
    fungsi dasar dengan grafik fungsi hasil transformasi.
    """)

    # =========================================================
    # 1. TUJUAN PEMBELAJARAN
    # =========================================================

    st.markdown("### 🎯 Tujuan Pembelajaran")

    st.info("""
    Setelah mempelajari materi ini, mahasiswa/peserta didik diharapkan mampu:

    1. Menjelaskan konsep transformasi fungsi.
    2. Mengidentifikasi translasi grafik fungsi.
    3. Menentukan refleksi grafik fungsi.
    4. Menjelaskan peregangan dan penyusutan grafik fungsi.
    5. Menentukan persamaan fungsi hasil transformasi.
    6. Menghubungkan bentuk aljabar dengan perubahan grafik.
    7. Menganalisis kombinasi beberapa transformasi fungsi.
    """)

    # =========================================================
    # 2. APERSEPSI
    # =========================================================

    st.markdown("### 💡 Apersepsi")

    st.markdown("""
    Perhatikan fungsi:

    """)
    st.latex(r"f(x)=x^2")

    st.markdown("""
    Grafik fungsi tersebut berbentuk parabola dengan titik puncak di:

    """)
    st.latex(r"(0,0)")

    st.markdown("""
    Bagaimana jika grafik tersebut digeser ke kanan 3 satuan?
    Bagaimana jika digeser ke atas 2 satuan?

    Kita tidak perlu menggambar ulang fungsi dari awal. Cukup melakukan
    transformasi terhadap persamaan fungsi.
    """)

    # =========================================================
    # 3. KONSEP DASAR
    # =========================================================

    st.markdown("### 📖 1. Konsep Dasar Transformasi Fungsi")

    st.markdown("""
    Transformasi fungsi adalah perubahan terhadap grafik fungsi yang dapat
    berupa:

    - **Translasi** → menggeser grafik.
    - **Refleksi** → mencerminkan grafik.
    - **Dilatasi vertikal** → meregangkan atau menyusutkan grafik secara vertikal.
    - **Dilatasi horizontal** → meregangkan atau menyusutkan grafik secara horizontal.
    - **Kombinasi transformasi** → menerapkan beberapa transformasi sekaligus.
    """)

    st.markdown("#### Bentuk umum")

    st.latex(r"y=a\,f(b(x-h))+k")

    st.markdown("""
    Pada bentuk tersebut:

    - \(h\) menentukan pergeseran horizontal.
    - \(k\) menentukan pergeseran vertikal.
    - \(a\) menentukan perubahan vertikal.
    - \(b\) menentukan perubahan horizontal.
    """)

    # =========================================================
    # 4. TRANSLASI VERTIKAL
    # =========================================================

    st.markdown("### 📍 2. Translasi Vertikal")

    st.markdown("""
    Jika grafik fungsi:

    """)

    st.latex(r"y=f(x)")

    st.markdown("""
    ditranslasikan ke atas sebesar \(k\) satuan, maka:
    """)

    st.latex(r"y=f(x)+k")

    st.markdown("""
    Sedangkan jika ditranslasikan ke bawah sebesar \(k\) satuan:
    """)

    st.latex(r"y=f(x)-k")

    st.markdown("#### Contoh")

    st.latex(r"f(x)=x^2")

    st.markdown("Jika grafik digeser 4 satuan ke atas:")

    st.latex(r"g(x)=x^2+4")

    st.markdown("""
    Titik puncak berubah dari \((0,0)\) menjadi \((0,4)\).
    """)

    # =========================================================
    # 5. TRANSLASI HORIZONTAL
    # =========================================================

    st.markdown("### 📍 3. Translasi Horizontal")

    st.markdown("""
    Jika grafik digeser ke kanan sebesar \(h\) satuan:
    """)

    st.latex(r"y=f(x-h)")

    st.markdown("""
    Jika grafik digeser ke kiri sebesar \(h\) satuan:
    """)

    st.latex(r"y=f(x+h)")

    st.warning("""
    ⚠️ Perhatikan tanda pada bagian dalam fungsi.

    Pergeseran ke kanan menggunakan \(x-h\), sedangkan pergeseran ke kiri
    menggunakan \(x+h\).
    """)

    st.markdown("#### Contoh")

    st.latex(r"f(x)=x^2")

    st.markdown("Geser 3 satuan ke kanan:")

    st.latex(r"g(x)=(x-3)^2")

    st.markdown("""
    Titik puncaknya berubah dari \((0,0)\) menjadi \((3,0)\).
    """)

    # =========================================================
    # 6. KOMBINASI TRANSLASI
    # =========================================================

    st.markdown("### 📍 4. Kombinasi Translasi")

    st.markdown("""
    Translasi horizontal dan vertikal dapat dilakukan secara bersamaan.
    """)

    st.latex(r"g(x)=f(x-h)+k")

    st.markdown("""
    Artinya grafik \(f(x)\):

    - bergeser \(h\) satuan ke kanan;
    - bergeser \(k\) satuan ke atas.
    """)

    st.markdown("#### Contoh")

    st.latex(r"f(x)=x^2")

    st.latex(r"g(x)=(x-2)^2+3")

    st.markdown("""
    Grafik bergeser 2 satuan ke kanan dan 3 satuan ke atas.

    Titik puncak:

    """)

    st.latex(r"(0,0)\rightarrow(2,3)")

    # =========================================================
    # 7. REFLEKSI TERHADAP SUMBU X
    # =========================================================

    st.markdown("### 🔄 5. Refleksi terhadap Sumbu-X")

    st.markdown("""
    Refleksi terhadap sumbu-X dilakukan dengan mengubah tanda nilai fungsi:
    """)

    st.latex(r"g(x)=-f(x)")

    st.markdown("#### Contoh")

    st.latex(r"f(x)=x^2")

    st.latex(r"g(x)=-x^2")

    st.markdown("""
    Parabola yang semula terbuka ke atas menjadi terbuka ke bawah.
    """)

    # =========================================================
    # 8. REFLEKSI TERHADAP SUMBU Y
    # =========================================================

    st.markdown("### 🔄 6. Refleksi terhadap Sumbu-Y")

    st.markdown("""
    Refleksi terhadap sumbu-Y dilakukan dengan mengganti \(x\) menjadi \(-x\):
    """)

    st.latex(r"g(x)=f(-x)")

    st.markdown("#### Contoh")

    st.latex(r"f(x)=x^3")

    st.latex(r"g(x)=(-x)^3=-x^3")

    st.markdown("""
    Grafik dicerminkan terhadap sumbu-Y.
    """)

    # =========================================================
    # 9. DILATASI VERTIKAL
    # =========================================================

    st.markdown("### 📏 7. Dilatasi Vertikal")

    st.markdown("""
    Dilatasi vertikal dilakukan dengan mengalikan fungsi dengan konstanta \(a\):
    """)

    st.latex(r"g(x)=a\,f(x)")

    st.markdown("""
    Jika:

    - \(a>1\) → grafik meregang secara vertikal.
    - \(0<a<1\) → grafik menyusut secara vertikal.
    - \(a<0\) → selain dilatasi, terjadi refleksi terhadap sumbu-X.
    """)

    st.markdown("#### Contoh")

    st.latex(r"f(x)=x^2")

    st.latex(r"g(x)=2x^2")

    st.markdown("""
    Grafik menjadi lebih sempit karena nilai \(y\) menjadi dua kali lebih besar.
    """)

    # =========================================================
    # 10. DILATASI HORIZONTAL
    # =========================================================

    st.markdown("### 📏 8. Dilatasi Horizontal")

    st.markdown("""
    Dilatasi horizontal dilakukan melalui perubahan pada input fungsi:
    """)

    st.latex(r"g(x)=f(bx)")

    st.markdown("""
    Untuk memahami efeknya:

    - \(b>1\) → grafik menyusut secara horizontal.
    - \(0<b<1\) → grafik meregang secara horizontal.
    """)

    st.markdown("#### Contoh")

    st.latex(r"f(x)=x^2")

    st.latex(r"g(x)=f(2x)=4x^2")

    st.markdown("""
    Grafik menjadi lebih sempit secara horizontal.
    """)

    # =========================================================
    # 11. RANGKUMAN TRANSFORMASI
    # =========================================================

    st.markdown("### 📋 9. Ringkasan Transformasi Fungsi")

    df_transformasi = pd.DataFrame({
        "Transformasi": [
            "Naik k satuan",
            "Turun k satuan",
            "Kanan h satuan",
            "Kiri h satuan",
            "Refleksi sumbu-X",
            "Refleksi sumbu-Y",
            "Dilatasi vertikal",
            "Dilatasi horizontal"
        ],
        "Bentuk": [
            "f(x) + k",
            "f(x) - k",
            "f(x - h)",
            "f(x + h)",
            "-f(x)",
            "f(-x)",
            "a f(x)",
            "f(bx)"
        ]
    })

    st.dataframe(
        df_transformasi,
        use_container_width=True,
        hide_index=True
    )

    # =========================================================
    # 12. EKSPERIMEN INTERAKTIF
    # =========================================================

    st.markdown("### 🧪 10. Eksplorasi Transformasi Fungsi")

    st.markdown("""
    Gunakan kontrol berikut untuk melihat bagaimana perubahan parameter
    memengaruhi grafik fungsi kuadrat.
    """)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        a = st.slider(
            "a — skala vertikal",
            -3.0,
            3.0,
            1.0,
            0.5
        )

    with col2:
        h = st.slider(
            "h — geser horizontal",
            -5.0,
            5.0,
            0.0,
            0.5
        )

    with col3:
        k = st.slider(
            "k — geser vertikal",
            -5.0,
            5.0,
            0.0,
            0.5
        )

    with col4:
        b = st.slider(
            "b — skala horizontal",
            -3.0,
            3.0,
            1.0,
            0.5
        )

    if b == 0:
        st.error("Nilai b tidak boleh 0.")
    else:

        x_values = [
            -5 + i * 0.1
            for i in range(101)
        ]

        y_values = []

        for x in x_values:
            y = a * ((b * (x - h)) ** 2) + k
            y_values.append(y)

        df_grafik = pd.DataFrame({
            "x": x_values,
            "y": y_values
        })

        st.line_chart(
            df_grafik,
            x="x",
            y="y",
            use_container_width=True
        )

        st.markdown("#### Persamaan fungsi hasil transformasi")

        st.latex(
            rf"g(x)={a}\left({b}(x-{h})\right)^2+{k}"
        )

    # =========================================================
    # 13. CONTOH ANALISIS
    # =========================================================

    st.markdown("### 🧠 11. Contoh Analisis Transformasi")

    st.markdown("""
    Diketahui:
    """)

    st.latex(r"f(x)=x^2")

    st.markdown("""
    Tentukan hasil transformasi jika grafik:

    1. digeser 3 satuan ke kanan;
    2. kemudian digeser 2 satuan ke atas;
    3. kemudian direfleksikan terhadap sumbu-X.
    """)

    st.markdown("**Langkah 1 — Geser 3 satuan ke kanan:**")

    st.latex(r"g(x)=(x-3)^2")

    st.markdown("**Langkah 2 — Geser 2 satuan ke atas:**")

    st.latex(r"h(x)=(x-3)^2+2")

    st.markdown("**Langkah 3 — Refleksi terhadap sumbu-X:**")

    st.latex(r"p(x)=-\left((x-3)^2+2\right)")

    st.markdown("""
    Jadi, fungsi akhirnya adalah:
    """)

    st.latex(r"p(x)=-(x-3)^2-2")

    # =========================================================
    # 14. URUTAN TRANSFORMASI
    # =========================================================

    st.markdown("### 🔀 12. Urutan Transformasi")

    st.warning("""
    ⚠️ Urutan transformasi dapat memengaruhi hasil akhir.

    Oleh karena itu, ketika terdapat beberapa transformasi sekaligus,
    lakukan transformasi secara bertahap sesuai urutan yang diberikan.
    """)

    st.markdown("Contoh:")

    st.latex(r"f(x)=x^2")

    st.markdown("""
    Geser ke kanan 2 satuan, kemudian refleksi terhadap sumbu-X.
    """)

    st.latex(r"g(x)=(x-2)^2")

    st.latex(r"h(x)=-(x-2)^2")

    st.markdown("""
    Hasil akhirnya:
    """)

    st.latex(r"h(x)=-(x-2)^2")

    # =========================================================
    # 15. TRANSFORMASI FUNGSI LINEAR
    # =========================================================

    st.markdown("### 📈 13. Transformasi Fungsi Linear")

    st.markdown("""
    Misalkan fungsi awal:
    """)

    st.latex(r"f(x)=2x+1")

    st.markdown("""
    Jika fungsi digeser 3 satuan ke kanan:
    """)

    st.latex(r"g(x)=f(x-3)")

    st.latex(r"g(x)=2(x-3)+1")

    st.latex(r"g(x)=2x-5")

    st.markdown("""
    Perhatikan bahwa kemiringan garis tetap sama, tetapi posisi garis berubah.
    """)

    # =========================================================
    # 16. TRANSFORMASI FUNGSI NILAI MUTLAK
    # =========================================================

    st.markdown("### 📐 14. Transformasi Fungsi Nilai Mutlak")

    st.markdown("""
    Fungsi dasar:
    """)

    st.latex(r"f(x)=|x|")

    st.markdown("""
    Jika digeser 2 satuan ke kanan dan 3 satuan ke bawah:
    """)

    st.latex(r"g(x)=|x-2|-3")

    st.markdown("""
    Titik puncak berubah dari:
    """)

    st.latex(r"(0,0)")

    st.markdown("menjadi:")

    st.latex(r"(2,-3)")

    # =========================================================
    # 17. TRANSFORMASI FUNGSI EKSPONENSIAL
    # =========================================================

    st.markdown("### 📊 15. Transformasi Fungsi Eksponensial")

    st.markdown("""
    Misalkan:
    """)

    st.latex(r"f(x)=2^x")

    st.markdown("""
    Jika digeser 2 satuan ke kanan dan 1 satuan ke atas:
    """)

    st.latex(r"g(x)=2^{x-2}+1")

    st.markdown("""
    Asimtot horizontal yang semula:
    """)

    st.latex(r"y=0")

    st.markdown("berubah menjadi:")

    st.latex(r"y=1")

    # =========================================================
    # 18. TRANSFORMASI FUNGSI KUADRAT
    # =========================================================

    st.markdown("### 🔺 16. Bentuk Puncak Fungsi Kuadrat")

    st.markdown("""
    Bentuk umum fungsi kuadrat:
    """)

    st.latex(r"f(x)=a(x-h)^2+k")

    st.markdown("""
    Bentuk ini sangat berguna untuk membaca transformasi grafik secara langsung.

    Titik puncaknya adalah:
    """)

    st.latex(r"(h,k)")

    st.markdown("""
    Parameter \(a\) menentukan arah dan tingkat keterbukaan parabola.
    """)

    # =========================================================
    # 19. MENENTUKAN TRANSFORMASI DARI DUA FUNGSI
    # =========================================================

    st.markdown("### 🔎 17. Menentukan Transformasi dari Dua Fungsi")

    st.markdown("""
    Diketahui:
    """)

    st.latex(r"f(x)=x^2")

    st.latex(r"g(x)=(x-4)^2+3")

    st.markdown("""
    Bandingkan kedua fungsi tersebut.
    """)

    st.markdown("""
    Dari bentuk \(g(x)\), terlihat bahwa:

    - \(x-4\) menunjukkan pergeseran 4 satuan ke kanan.
    - \(+3\) menunjukkan pergeseran 3 satuan ke atas.
    """)

    st.latex(r"(0,0)\rightarrow(4,3)")

    # =========================================================
    # 20. KALKULATOR TRANSFORMASI
    # =========================================================

    st.markdown("### 🧮 18. Kalkulator Transformasi Fungsi")

    st.markdown("""
    Masukkan koefisien dan translasi untuk fungsi kuadrat:
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        a_calc = st.number_input(
            "Koefisien a",
            value=1.0,
            step=0.5
        )

    with col2:
        h_calc = st.number_input(
            "Pergeseran horizontal h",
            value=0.0,
            step=1.0
        )

    with col3:
        k_calc = st.number_input(
            "Pergeseran vertikal k",
            value=0.0,
            step=1.0
        )

    st.markdown("#### Fungsi hasil transformasi")

    st.latex(
        rf"g(x)={a_calc}(x-{h_calc})^2+{k_calc}"
    )

    st.markdown("#### Titik puncak")

    st.latex(
        rf"({h_calc},{k_calc})"
    )

    # =========================================================
    # 21. LATIHAN
    # =========================================================

    st.markdown("### ✏️ 19. Latihan")

    st.markdown("""
    **Soal 1**

    Diketahui:
    """)

    st.latex(r"f(x)=x^2")

    st.markdown("""
    Tentukan persamaan fungsi jika grafik digeser 5 satuan ke kanan dan
    2 satuan ke atas.
    """)

    with st.expander("💡 Lihat pembahasan"):

        st.latex(r"g(x)=(x-5)^2+2")

        st.markdown("""
        Karena bergeser ke kanan 5 satuan digunakan \(x-5\), sedangkan
        bergeser ke atas 2 satuan ditambahkan \(+2\).
        """)

    st.markdown("""
    **Soal 2**

    Diketahui:
    """)

    st.latex(r"f(x)=|x|")

    st.markdown("""
    Tentukan fungsi hasil refleksi terhadap sumbu-X.
    """)

    with st.expander("💡 Lihat pembahasan"):

        st.latex(r"g(x)=-|x|")

    st.markdown("""
    **Soal 3**

    Diketahui:
    """)

    st.latex(r"f(x)=x^2")

    st.markdown("""
    Tentukan fungsi yang diperoleh jika grafik direfleksikan terhadap
    sumbu-X kemudian digeser 3 satuan ke kanan.
    """)

    with st.expander("💡 Lihat pembahasan"):

        st.latex(r"g(x)=-(x-3)^2")

    # =========================================================
    # 22. KUIS INTERAKTIF
    # =========================================================

    st.markdown("### 🎯 20. Kuis Interaktif")

    skor = 0

    q1 = st.radio(
        "1. Grafik \(f(x)\) digeser 4 satuan ke kanan. Bentuk barunya adalah:",
        [
            "f(x+4)",
            "f(x-4)",
            "f(x)+4",
            "f(x)-4"
        ],
        key="transformasi_q1"
    )

    if q1 == "f(x-4)":
        skor += 1

    q2 = st.radio(
        "2. Refleksi terhadap sumbu-X menghasilkan:",
        [
            "f(-x)",
            "-f(x)",
            "f(x)+1",
            "f(x-1)"
        ],
        key="transformasi_q2"
    )

    if q2 == "-f(x)":
        skor += 1

    q3 = st.radio(
        "3. Grafik f(x) digeser 2 satuan ke kiri dan 3 satuan ke bawah:",
        [
            "f(x-2)+3",
            "f(x+2)-3",
            "f(x-2)-3",
            "f(x+2)+3"
        ],
        key="transformasi_q3"
    )

    if q3 == "f(x+2)-3":
        skor += 1

    q4 = st.radio(
        "4. Titik puncak dari y=(x-3)^2+5 adalah:",
        [
            "(3,5)",
            "(-3,5)",
            "(3,-5)",
            "(-3,-5)"
        ],
        key="transformasi_q4"
    )

    if q4 == "(3,5)":
        skor += 1

    if st.button("📊 Periksa Nilai", key="cek_transformasi"):

        st.success(
            f"Skor Anda: {skor}/4"
        )

        if skor == 4:
            st.balloons()
            st.success(
                "🎉 Sangat baik! Anda telah memahami konsep dasar transformasi fungsi."
            )
        elif skor >= 2:
            st.info(
                "👍 Cukup baik. Pelajari kembali bagian yang masih kurang tepat."
            )
        else:
            st.warning(
                "📚 Silakan pelajari kembali konsep translasi, refleksi, dan dilatasi."
            )

    # =========================================================
    # 23. REFLEKSI PEMBELAJARAN
    # =========================================================

    st.markdown("### 📝 21. Refleksi Pembelajaran")

    st.markdown("""
    Setelah mempelajari transformasi fungsi, renungkan pertanyaan berikut:

    1. Apa perbedaan \(f(x-h)\) dan \(f(x)+h\)?
    2. Mengapa pergeseran ke kanan menggunakan \(x-h\)?
    3. Apa pengaruh tanda negatif di depan fungsi?
    4. Bagaimana cara mengetahui titik puncak dari bentuk
       \(a(x-h)^2+k\)?
    5. Bagaimana pengaruh nilai \(a\) terhadap grafik?
    6. Bagaimana beberapa transformasi dapat digabungkan?
    """)

    # =========================================================
    # 24. RANGKUMAN
    # =========================================================

    st.markdown("### 📚 22. Rangkuman")

    st.success("""
    **Konsep penting transformasi fungsi:**

    • Translasi vertikal:
      grafik naik atau turun.

    • Translasi horizontal:
      grafik bergeser ke kiri atau kanan.

    • Refleksi:
      grafik dicerminkan terhadap sumbu-X atau sumbu-Y.

    • Dilatasi:
      grafik diregangkan atau diperkecil.

    • Bentuk umum:
      a f(b(x-h)) + k

    • Untuk fungsi kuadrat:
      a(x-h)²+k

      memiliki titik puncak (h,k).

    Kunci utama dalam mempelajari transformasi fungsi adalah memahami
    hubungan antara perubahan bentuk aljabar dan perubahan grafik.
    """)

    st.markdown("---")

    st.info("""
    💡 **Inti konsep**

    Jangan hanya menghafalkan rumus transformasi. Amati bagaimana perubahan
    pada persamaan fungsi menyebabkan perubahan posisi, bentuk, dan ukuran
    grafik.
    """)


def fungsi_invers_komposisi():

    st.header("🔗 Fungsi, Invers dan Komposisi Fungsi")

    st.markdown("""
    ### Matematika Fase F — Kelas XI & XII

    Fungsi merupakan salah satu konsep penting dalam matematika yang
    digunakan untuk menyatakan hubungan antara dua himpunan atau
    antara suatu input dengan output tertentu.

    Pada materi ini kita akan mempelajari konsep fungsi, domain dan range,
    operasi fungsi, fungsi invers, serta komposisi fungsi dan penerapannya
    dalam berbagai permasalahan.
    """)

    st.divider()

    # ========================================================
    # TUJUAN PEMBELAJARAN
    # ========================================================

    with st.expander("🎯 Tujuan Pembelajaran", expanded=True):

        st.markdown("""
        Setelah mempelajari materi ini, peserta didik diharapkan mampu:

        1. Menjelaskan pengertian fungsi.
        2. Menentukan domain, kodomain, dan range suatu fungsi.
        3. Menentukan nilai fungsi.
        4. Menentukan bentuk fungsi dari suatu permasalahan.
        5. Melakukan operasi pada fungsi.
        6. Menentukan fungsi invers.
        7. Menentukan syarat suatu fungsi memiliki invers.
        8. Menentukan komposisi dua fungsi atau lebih.
        9. Menentukan invers dari fungsi komposisi.
        10. Menyelesaikan masalah kontekstual menggunakan fungsi,
            invers, dan komposisi fungsi.
        """)

    # ========================================================
    # 1. APERSEPSI
    # ========================================================

    st.subheader("1. Apersepsi")

    st.markdown("""
    Dalam kehidupan sehari-hari kita sering menemukan hubungan antara
    suatu input dengan output.

    Contohnya adalah harga barang dan jumlah barang yang dibeli.

    Jika harga satu buku Rp10.000, maka harga 2 buku adalah Rp20.000,
    harga 3 buku adalah Rp30.000, dan seterusnya.

    Hubungan tersebut dapat dinyatakan menggunakan suatu aturan
    matematika yang disebut **fungsi**.
    """)

    st.info("""
    💡 **Pertanyaan pemantik**

    Jika harga sebuah buku Rp12.000 dan seseorang membeli 5 buku,
    bagaimana cara menentukan total harga secara matematis?
    """)

    # ========================================================
    # 2. PENGERTIAN FUNGSI
    # ========================================================

    st.subheader("2. Pengertian Fungsi")

    st.markdown("""
    Fungsi adalah suatu aturan yang memasangkan setiap anggota
    suatu himpunan asal dengan tepat satu anggota pada himpunan tujuan.

    Himpunan asal disebut **domain**.

    Himpunan tujuan disebut **kodomain**.

    Anggota kodomain yang memiliki pasangan dari domain disebut **range**.
    """)

    st.latex(r"f:A\rightarrow B")

    st.markdown("""
    Artinya fungsi \(f\) memetakan himpunan \(A\) ke himpunan \(B\).
    """)

    st.latex(r"f(x)=y")

    st.markdown("""
    Dengan demikian, setiap nilai \(x\) pada domain mempunyai tepat
    satu nilai keluaran \(y\).
    """)

    # ========================================================
    # 3. DOMAIN, KODOMAIN DAN RANGE
    # ========================================================

    st.subheader("3. Domain, Kodomain, dan Range")

    st.markdown("""
    Misalkan terdapat fungsi:

    \(f:A\rightarrow B\)

    dengan:

    - A = domain
    - B = kodomain
    - Range = himpunan hasil pemetaan dari A
    """)

    st.latex(r"A=\{1,2,3\}")

    st.latex(r"B=\{2,4,6,8\}")

    st.markdown("""
    Misalkan fungsi diberikan oleh:
    """)

    st.latex(r"f(x)=2x")

    st.markdown("""
    Maka:
    """)

    st.latex(r"f(1)=2")

    st.latex(r"f(2)=4")

    st.latex(r"f(3)=6")

    st.success("Range fungsi tersebut adalah {2, 4, 6}.")

    # ========================================================
    # 4. NOTASI FUNGSI
    # ========================================================

    st.subheader("4. Notasi Fungsi")

    st.markdown("""
    Fungsi biasanya dituliskan dalam bentuk:
    """)

    st.latex(r"f(x)=ax+b")

    st.markdown("""
    Misalnya:
    """)

    st.latex(r"f(x)=2x+3")

    st.markdown("""
    Untuk menentukan nilai fungsi pada \(x=4\), substitusikan
    \(x=4\) ke dalam fungsi.
    """)

    st.latex(r"f(4)=2(4)+3")

    st.latex(r"f(4)=11")

    st.success("Jadi, nilai f(4) adalah 11.")

    # ========================================================
    # 5. MENENTUKAN NILAI FUNGSI
    # ========================================================

    st.subheader("5. Menentukan Nilai Fungsi")

    st.markdown("""
    Misalkan:
    """)

    st.latex(r"f(x)=3x-5")

    st.markdown("Tentukan nilai \(f(7)\).")

    st.latex(r"f(7)=3(7)-5")

    st.latex(r"f(7)=21-5")

    st.latex(r"f(7)=16")

    st.success("Nilai f(7) adalah 16.")

    # ========================================================
    # 6. DOMAIN FUNGSI
    # ========================================================

    st.subheader("6. Menentukan Domain Fungsi")

    st.markdown("""
    Domain adalah nilai-nilai \(x\) yang diperbolehkan dalam suatu fungsi.

    Untuk fungsi polinomial, domain biasanya seluruh bilangan real.

    Namun, untuk fungsi pecahan terdapat pembatasan karena penyebut
    tidak boleh sama dengan nol.
    """)

    st.latex(r"f(x)=\frac{1}{x-2}")

    st.markdown("""
    Penyebut tidak boleh nol, sehingga:
    """)

    st.latex(r"x-2\neq0")

    st.latex(r"x\neq2")

    st.success("Domain fungsi adalah semua bilangan real kecuali x = 2.")

    # ========================================================
    # 7. OPERASI FUNGSI
    # ========================================================

    st.subheader("7. Operasi pada Fungsi")

    st.markdown("""
    Jika diketahui dua fungsi \(f(x)\) dan \(g(x)\), kita dapat
    melakukan operasi penjumlahan, pengurangan, perkalian,
    dan pembagian fungsi.
    """)

    st.latex(r"(f+g)(x)=f(x)+g(x)")

    st.latex(r"(f-g)(x)=f(x)-g(x)")

    st.latex(r"(fg)(x)=f(x)g(x)")

    st.latex(r"\left(\frac{f}{g}\right)(x)=\frac{f(x)}{g(x)}")

    # ========================================================
    # 8. CONTOH OPERASI FUNGSI
    # ========================================================

    st.subheader("8. Contoh Operasi Fungsi")

    st.markdown("""
    Diketahui:
    """)

    st.latex(r"f(x)=2x+3")

    st.latex(r"g(x)=x-1")

    st.markdown("Maka penjumlahan kedua fungsi adalah:")

    st.latex(r"(f+g)(x)=(2x+3)+(x-1)")

    st.latex(r"(f+g)(x)=3x+2")

    st.markdown("Perkalian kedua fungsi:")

    st.latex(r"(fg)(x)=(2x+3)(x-1)")

    st.latex(r"(fg)(x)=2x^2+x-3")

    # ========================================================
    # 9. FUNGSI LINEAR
    # ========================================================

    st.subheader("9. Fungsi Linear")

    st.markdown("""
    Fungsi linear merupakan fungsi yang dapat dituliskan dalam bentuk:
    """)

    st.latex(r"f(x)=ax+b")

    st.markdown("""
    dengan \(a\) dan \(b\) merupakan konstanta.

    Grafik fungsi linear berbentuk garis lurus.
    """)

    st.latex(r"f(x)=2x+1")

    st.markdown("""
    Pada fungsi tersebut:

    - gradien = 2
    - titik potong sumbu-y = 1
    """)

    # ========================================================
    # 10. GRAFIK FUNGSI INTERAKTIF
    # ========================================================

    st.subheader("10. 📊 Eksplorasi Grafik Fungsi Linear")

    a_grafik = st.slider(
        "Nilai a",
        min_value=-5.0,
        max_value=5.0,
        value=2.0,
        step=0.5,
        key="fungsi_linear_a"
    )

    b_grafik = st.slider(
        "Nilai b",
        min_value=-10.0,
        max_value=10.0,
        value=1.0,
        step=1.0,
        key="fungsi_linear_b"
    )

    x_grafik = list(range(-10, 11))

    y_grafik = [
        a_grafik * x + b_grafik
        for x in x_grafik
    ]

    df_fungsi = pd.DataFrame({
        "x": x_grafik,
        "f(x)": y_grafik
    })

    st.latex(r"f(x)=ax+b")

    st.line_chart(
        df_fungsi,
        x="x",
        y="f(x)"
    )

    st.info(
        f"Fungsi yang sedang dieksplorasi adalah "
        f"f(x) = {a_grafik}x + {b_grafik}"
    )

    # ========================================================
    # 11. FUNGSI SATU-SATU
    # ========================================================

    st.subheader("11. Fungsi Satu-Satu")

    st.markdown("""
    Fungsi satu-satu atau injektif adalah fungsi yang memetakan
    anggota domain yang berbeda ke anggota kodomain yang berbeda.

    Secara sederhana, tidak terdapat dua input berbeda yang menghasilkan
    output yang sama.
    """)

    st.latex(r"x_1\neq x_2\Rightarrow f(x_1)\neq f(x_2)")

    st.info("""
    Fungsi satu-satu sangat penting dalam pembahasan fungsi invers
    karena suatu fungsi harus dapat dibalik secara unik.
    """)

    # ========================================================
    # 12. FUNGSI INVERS
    # ========================================================

    st.subheader("12. Fungsi Invers")

    st.markdown("""
    Fungsi invers adalah fungsi yang membalikkan proses pemetaan
    suatu fungsi.

    Jika fungsi \(f\) memetakan \(x\) menjadi \(y\), maka fungsi invers
    memetakan \(y\) kembali menjadi \(x\).
    """)

    st.latex(r"f:x\rightarrow y")

    st.latex(r"f^{-1}:y\rightarrow x")

    st.markdown("""
    Hubungan fungsi dengan inversnya dapat dituliskan:
    """)

    st.latex(r"f^{-1}(f(x))=x")

    st.latex(r"f(f^{-1}(x))=x")

    # ========================================================
    # 13. MENENTUKAN FUNGSI INVERS
    # ========================================================

    st.subheader("13. Menentukan Fungsi Invers")

    st.markdown("""
    Misalkan:
    """)

    st.latex(r"f(x)=2x+3")

    st.markdown("""
    Langkah pertama adalah mengganti \(f(x)\) dengan \(y\).
    """)

    st.latex(r"y=2x+3")

    st.markdown("""
    Kemudian tukarkan \(x\) dan \(y\).
    """)

    st.latex(r"x=2y+3")

    st.markdown("""
    Selanjutnya selesaikan terhadap \(y\).
    """)

    st.latex(r"x-3=2y")

    st.latex(r"y=\frac{x-3}{2}")

    st.markdown("""
    Jadi fungsi inversnya adalah:
    """)

    st.latex(r"f^{-1}(x)=\frac{x-3}{2}")

    # ========================================================
    # 14. VERIFIKASI INVERS
    # ========================================================

    st.subheader("14. Verifikasi Fungsi Invers")

    st.markdown("""
    Fungsi dan inversnya dapat diverifikasi dengan komposisi.
    """)

    st.latex(r"f(x)=2x+3")

    st.latex(r"f^{-1}(x)=\frac{x-3}{2}")

    st.markdown("Verifikasi pertama:")

    st.latex(r"f(f^{-1}(x))=2\left(\frac{x-3}{2}\right)+3")

    st.latex(r"f(f^{-1}(x))=x")

    st.markdown("Verifikasi kedua:")

    st.latex(r"f^{-1}(f(x))=\frac{(2x+3)-3}{2}")

    st.latex(r"f^{-1}(f(x))=x")

    st.success("Kedua komposisi menghasilkan x, sehingga kedua fungsi merupakan invers.")

    # ========================================================
    # 15. INVERS FUNGSI LINEAR INTERAKTIF
    # ========================================================

    st.subheader("15. 🧮 Kalkulator Fungsi Invers Linear")

    a_inv = st.number_input(
        "Nilai a",
        value=2.0,
        step=1.0,
        key="a_invers"
    )

    b_inv = st.number_input(
        "Nilai b",
        value=3.0,
        step=1.0,
        key="b_invers"
    )

    if a_inv != 0:

        st.latex(r"f(x)=ax+b")

        st.success(
            f"Fungsi: f(x) = {a_inv}x + {b_inv}"
        )

        st.latex(
            f"f^{{-1}}(x)=\\frac{{x-({b_inv})}}{{{a_inv}}}"
        )

    else:

        st.error(
            "Nilai a tidak boleh 0 karena fungsi tersebut tidak memiliki bentuk invers linear."
        )

    # ========================================================
    # 16. KOMPOSISI FUNGSI
    # ========================================================

    st.subheader("16. Komposisi Fungsi")

    st.markdown("""
    Komposisi fungsi adalah penggabungan dua fungsi atau lebih
    sehingga keluaran suatu fungsi menjadi masukan bagi fungsi berikutnya.

    Komposisi fungsi \(f\) dan \(g\) ditulis:
    """)

    st.latex(r"(f\circ g)(x)=f(g(x))")

    st.markdown("""
    Artinya fungsi \(g\) dikerjakan terlebih dahulu, kemudian hasilnya
    dimasukkan ke fungsi \(f\).
    """)

    # ========================================================
    # 17. CONTOH KOMPOSISI
    # ========================================================

    st.subheader("17. Contoh Komposisi Fungsi")

    st.markdown("""
    Diketahui:
    """)

    st.latex(r"f(x)=2x+1")

    st.latex(r"g(x)=x^2")

    #st.markdown("Tentukan \(f\circ g\).")
    st.markdown("Tentukan komposisi fungsi:")
    st.latex(r"(f\circ g)(x)")

    st.latex(r"(f\circ g)(x)=f(g(x))")

    st.latex(r"(f\circ g)(x)=f(x^2)")

    st.latex(r"(f\circ g)(x)=2x^2+1")

    #st.markdown("Sekarang tentukan \(g\circ f\).")
    st.markdown("Sekarang tentukan komposisi fungsi:")
    st.latex(r"(g\circ f)(x)")

    st.latex(r"(g\circ f)(x)=g(f(x))")

    st.latex(r"(g\circ f)(x)=(2x+1)^2")

    st.latex(r"(g\circ f)(x)=4x^2+4x+1")

    st.markdown("**Perhatikan bahwa pada umumnya:**")
    
    st.latex(r"f\circ g\neq g\circ f")
    
    st.info("💡 Jadi, komposisi fungsi tidak bersifat komutatif.")

    # ========================================================
    # 18. KOMPOSISI TIGA FUNGSI
    # ========================================================

    st.subheader("18. Komposisi Tiga Fungsi")

    st.markdown("""
    Komposisi dapat dilakukan pada tiga fungsi atau lebih.

    Misalnya terdapat fungsi \(f\), \(g\), dan \(h\).
    """)

    st.latex(r"(f\circ g\circ h)(x)=f(g(h(x)))")

    st.markdown("""
    Fungsi \(h\) dikerjakan terlebih dahulu, kemudian \(g\),
    dan terakhir \(f\).
    """)

    # ========================================================
    # 19. KOMPOSISI INTERAKTIF
    # ========================================================

    st.subheader("19. 🧮 Kalkulator Komposisi Fungsi Linear")

    st.markdown("""
    Misalkan digunakan dua fungsi linear:
    """)

    col1, col2 = st.columns(2)

    with col1:

        a_f = st.number_input(
            "Koefisien a pada f",
            value=2.0,
            step=1.0,
            key="a_f_komposisi"
        )

        b_f = st.number_input(
            "Konstanta b pada f",
            value=1.0,
            step=1.0,
            key="b_f_komposisi"
        )

    with col2:

        a_g = st.number_input(
            "Koefisien a pada g",
            value=3.0,
            step=1.0,
            key="a_g_komposisi"
        )

        b_g = st.number_input(
            "Konstanta b pada g",
            value=2.0,
            step=1.0,
            key="b_g_komposisi"
        )

    st.latex(r"f(x)=ax+b")

    st.latex(r"g(x)=cx+d")

    hasil_a_fg = a_f * a_g
    hasil_b_fg = a_f * b_g + b_f

    hasil_a_gf = a_g * a_f
    hasil_b_gf = a_g * b_f + b_g

    st.markdown("### Hasil Komposisi")

    st.latex(
        f"(f\\circ g)(x)={hasil_a_fg:.2f}x+{hasil_b_fg:.2f}"
    )

    st.latex(
        f"(g\\circ f)(x)={hasil_a_gf:.2f}x+{hasil_b_gf:.2f}"
    )

    # ========================================================
    # 20. INVERS KOMPOSISI
    # ========================================================

    st.subheader("20. Invers dari Komposisi Fungsi")

    st.markdown("""
    Salah satu sifat penting fungsi invers adalah:
    """)

    st.latex(r"(f\circ g)^{-1}=g^{-1}\circ f^{-1}")

    st.markdown("""
    Perhatikan bahwa urutan fungsi pada invers komposisi menjadi
    terbalik.
    """)

    st.info("""
    📌 Jika suatu proses dilakukan dengan urutan:

    f → g

    maka proses kebalikannya dilakukan dengan urutan:

    g⁻¹ → f⁻¹
    """)

    # ========================================================
    # 21. PENERAPAN FUNGSI
    # ========================================================

    st.subheader("21. Penerapan Fungsi dalam Kehidupan")

    st.markdown("""
    Fungsi dapat digunakan untuk memodelkan berbagai hubungan,
    seperti:

    - harga barang dan jumlah pembelian;
    - jarak dan waktu;
    - suhu Celsius dan Fahrenheit;
    - biaya produksi dan jumlah produksi;
    - pendapatan dan jumlah barang;
    - konversi satuan;
    - pertumbuhan populasi.
    """)

    st.markdown("""
    Contoh hubungan suhu Celsius dan Fahrenheit:
    """)

    st.latex(r"F(C)=\frac{9}{5}C+32")

    st.markdown("""
    Fungsi tersebut mengubah suhu dalam Celsius menjadi Fahrenheit.
    """)

    # ========================================================
    # 22. INVERS DALAM PENERAPAN
    # ========================================================

    st.subheader("22. Penerapan Fungsi Invers")

    st.markdown("""
    Jika diketahui hubungan Celsius ke Fahrenheit:
    """)

    st.latex(r"F(C)=\frac{9}{5}C+32")

    st.markdown("""
    Fungsi invers dapat digunakan untuk mengubah Fahrenheit kembali
    menjadi Celsius.
    """)

    st.latex(r"C(F)=\frac{5}{9}(F-32)")

    st.markdown("""
    Misalnya suhu 86°F.
    """)

    st.latex(r"C(86)=\frac{5}{9}(86-32)")

    st.latex(r"C(86)=30")

    st.success("Jadi 86°F setara dengan 30°C.")

    # ========================================================
    # 23. PENERAPAN KOMPOSISI
    # ========================================================

    st.subheader("23. Penerapan Komposisi Fungsi")

    st.markdown("""
    Komposisi fungsi dapat digunakan ketika suatu proses terdiri
    dari beberapa tahapan.

    Misalnya harga barang mengalami diskon kemudian dikenakan pajak.

    Tahap pertama dapat dimodelkan dengan fungsi diskon:

    """)

    st.latex(r"g(x)=0,9x")

    st.markdown("""
    Kemudian dikenakan pajak 11%:
    """)

    st.latex(r"f(x)=1,11x")

    st.markdown("""
    Maka harga akhir dapat dinyatakan dengan:
    """)

    st.latex(r"(f\circ g)(x)=f(g(x))")

    st.latex(r"(f\circ g)(x)=1,11(0,9x)")

    st.latex(r"(f\circ g)(x)=0,999x")

    st.info("""
    Artinya, proses diskon kemudian pajak dapat dimodelkan
    menggunakan komposisi fungsi.
    """)

    # ========================================================
    # 24. EKSPLORASI DOMAIN DAN RANGE
    # ========================================================

    st.subheader("24. 🔎 Eksplorasi Domain dan Range")

    batas_bawah = st.number_input(
        "Batas bawah x",
        value=-5,
        step=1,
        key="domain_bawah"
    )

    batas_atas = st.number_input(
        "Batas atas x",
        value=5,
        step=1,
        key="domain_atas"
    )

    if batas_bawah <= batas_atas:

        x_domain = list(
            range(
                int(batas_bawah),
                int(batas_atas) + 1
            )
        )

        y_range = [
            2 * x + 1
            for x in x_domain
        ]

        df_domain = pd.DataFrame({
            "x": x_domain,
            "f(x)": y_range
        })

        st.dataframe(
            df_domain,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.error("Batas bawah harus lebih kecil atau sama dengan batas atas.")

    # ========================================================
    # 25. STUDI KASUS
    # ========================================================

    st.subheader("25. 🧩 Studi Kasus")

    st.markdown("""
    Sebuah toko memberikan diskon 20% terhadap harga barang.
    Setelah diskon, pelanggan dikenakan pajak sebesar 11%.

    Misalkan harga awal barang adalah \(x\).
    """)

    st.latex(r"g(x)=0,8x")

    st.markdown("Setelah dikenakan pajak:")

    st.latex(r"f(x)=1,11x")

    st.markdown("Harga akhir dapat ditentukan dengan komposisi:")

    st.latex(r"(f\circ g)(x)=1,11(0,8x)")

    st.latex(r"(f\circ g)(x)=0,888x")

    st.markdown("""
    Jika harga awal Rp1.000.000:
    """)

    st.latex(r"(f\circ g)(1.000.000)=888.000")

    st.success("Harga akhir setelah diskon dan pajak adalah Rp888.000.")

    # ========================================================
    # 26. LATIHAN
    # ========================================================

    st.subheader("26. ✏️ Latihan")

    st.markdown("""
    **Soal 1**

    Diketahui:
    """)

    st.latex(r"f(x)=3x+2")

    st.markdown("""
    Tentukan nilai \(f(5)\).

    **Soal 2**

    Diketahui:
    """)

    st.latex(r"f(x)=2x-3")

    st.markdown("""
    Tentukan fungsi invers \(f^{-1}(x)\).

    **Soal 3**

    Diketahui:
    """)

    st.latex(r"f(x)=2x+1")

    st.latex(r"g(x)=x^2")

    st.markdown("""
    Tentukan \(f\circ g\) dan \(g\circ f\).

    **Soal 4**

    Jelaskan perbedaan domain, kodomain, dan range.

    **Soal 5**

    Jelaskan mengapa komposisi fungsi pada umumnya tidak komutatif.

    **Soal 6**

    Jelaskan hubungan antara fungsi invers dan komposisi fungsi.

    **Soal 7**

    Sebuah toko memberikan diskon 15%, kemudian mengenakan pajak 11%.
    Buatlah model fungsi yang menyatakan harga akhirnya.

    **Soal 8**

    Diketahui fungsi konversi suhu Celsius ke Fahrenheit.
    Tentukan fungsi inversnya.
    """)

    # ========================================================
    # 27. KUIS
    # ========================================================

    st.subheader("27. 📝 Kuis")

    q1 = st.radio(
        "1. Jika f(x) = 2x + 3, maka f(4) adalah ...",
        [
            "7",
            "8",
            "11",
            "12"
        ],
        key="kuis_fungsi_1"
    )

    if q1:

        if q1 == "11":
            st.success("✅ Benar!")
        else:
            st.error("❌ Jawaban belum tepat.")

    q2 = st.radio(
        "2. Bentuk umum fungsi linear adalah ...",
        [
            "f(x) = ax² + bx + c",
            "f(x) = ax + b",
            "f(x) = a/x",
            "f(x) = aˣ"
        ],
        key="kuis_fungsi_2"
    )

    if q2:

        if q2 == "f(x) = ax + b":
            st.success("✅ Benar!")
        else:
            st.error("❌ Jawaban belum tepat.")

    q3 = st.radio(
        "3. Komposisi fungsi dituliskan sebagai ...",
        [
            "f + g",
            "f − g",
            "f ∘ g",
            "fg"
        ],
        key="kuis_fungsi_3"
    )

    if q3:

        if q3 == "f ∘ g":
            st.success("✅ Benar!")
        else:
            st.error("❌ Jawaban belum tepat.")

    q4 = st.radio(
        "4. Pada (f ∘ g)(x), fungsi yang dikerjakan terlebih dahulu adalah ...",
        [
            "f",
            "g",
            "f dan g bersamaan",
            "Tidak ada"
        ],
        key="kuis_fungsi_4"
    )

    if q4:

        if q4 == "g":
            st.success("✅ Benar!")
        else:
            st.error("❌ Jawaban belum tepat.")

    q5 = st.radio(
        "5. Sifat invers komposisi yang benar adalah ...",
        [
            "(f ∘ g)⁻¹ = f⁻¹ ∘ g⁻¹",
            "(f ∘ g)⁻¹ = g⁻¹ ∘ f⁻¹",
            "(f ∘ g)⁻¹ = f ∘ g",
            "(f ∘ g)⁻¹ = f + g"
        ],
        key="kuis_fungsi_5"
    )

    if q5:

        if q5 == "(f ∘ g)⁻¹ = g⁻¹ ∘ f⁻¹":
            st.success("✅ Benar!")
        else:
            st.error("❌ Jawaban belum tepat.")

    # ========================================================
    # 28. REFLEKSI
    # ========================================================

    st.subheader("28. 💭 Refleksi")

    st.markdown("""
    Setelah mempelajari fungsi, invers, dan komposisi fungsi,
    coba pikirkan:

    - Apa yang dimaksud dengan fungsi?
    - Apa perbedaan domain, kodomain, dan range?
    - Mengapa fungsi tertentu memiliki invers?
    - Mengapa urutan pada komposisi fungsi penting?
    - Bagaimana fungsi invers digunakan dalam kehidupan sehari-hari?
    - Bagaimana komposisi fungsi dapat digunakan untuk memodelkan
      proses yang terdiri dari beberapa tahap?
    """)

    # ========================================================
    # 29. RANGKUMAN
    # ========================================================

    st.subheader("29. 📚 Rangkuman")

    st.markdown("""
    ### Fungsi

    Fungsi merupakan aturan yang memasangkan setiap anggota domain
    dengan tepat satu anggota kodomain.
    """)

    st.latex(r"f:A\rightarrow B")

    st.markdown("""
    ### Nilai Fungsi

    Nilai fungsi diperoleh dengan mensubstitusikan nilai input
    ke dalam fungsi.
    """)

    st.latex(r"y=f(x)")

    st.markdown("""
    ### Fungsi Invers

    Fungsi invers membalikkan proses pemetaan fungsi.
    """)

    st.latex(r"f^{-1}(f(x))=x")

    st.latex(r"f(f^{-1}(x))=x")

    st.markdown("""
    ### Komposisi Fungsi

    Komposisi fungsi menggabungkan dua fungsi atau lebih.
    """)

    st.latex(r"(f\circ g)(x)=f(g(x))")

    st.markdown("""
    ### Invers Komposisi

    Urutan fungsi pada invers komposisi dibalik.
    """)

    st.latex(r"(f\circ g)^{-1}=g^{-1}\circ f^{-1}")

    st.success("""
    🎯 **Inti pembelajaran**

    Fungsi digunakan untuk memodelkan hubungan antara input dan output.
    Fungsi invers digunakan untuk membalikkan suatu proses, sedangkan
    komposisi fungsi digunakan untuk memodelkan proses yang terdiri
    dari beberapa tahapan.
    """)


#=====================================================================
# BARISAN DAN DERET
#=====================================================================
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



def tampilkan(materi):
    if materi == "Barisan dan Deret":
        #pass
        barisan_deret()

    elif materi == "Matematika Keuangan":
        matematika_keuangan()

    elif materi == "Fungsi, Invers dan Komposisi Fungsi":
        fungsi_invers_komposisi()
        #pass

    elif materi == "Transformasi Fungsi":
        transformasi_fungsi()
        #pass

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
