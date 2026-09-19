import streamlit as st
import pandas as pd
import numpy as np
import math

from textwrap import dedent

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


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

    st.subheader("Refleksi terhadap sumbu-X")
    st.latex(r"(x,y)\to(x,-y)")

    st.subheader("Refleksi terhadap sumbu-Y")
    st.latex(r"(x,y)\to(-x,y)")

    st.subheader("Refleksi terhadap titik asal O")
    st.latex(r"(x,y)\to(-x,-y)")

    st.subheader("Refleksi terhadap garis y = x")
    st.latex(r"(x,y)\to(y,x)")

    st.subheader("Refleksi terhadap garis y = -x")
    st.latex(r"(x,y)\to(-y,-x)")

    # =========================================================
    # 5. REFLEKSI TERHADAP GARIS VERTIKAL / HORIZONTAL
    # =========================================================

    st.subheader("Refleksi terhadap garis x = a")
    st.latex(r"(x,y)\to(2a-x,\;y)")
    st.caption("Di sini $a$ adalah konstanta yang menyatakan posisi garis cermin, bukan variabel titik.")  # FIX: klarifikasi

    st.subheader("Refleksi terhadap garis y = b")
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

    st.markdown(r"Rotasi berpusat di titik asal $O(0,0)$:")

    st.subheader("Rotasi 90° berlawanan arah jarum jam (CCW)")
    st.latex(r"(x,y)\to(-y,\;x)")

    st.subheader("Rotasi 90° searah jarum jam (CW)")
    st.latex(r"(x,y)\to(y,\;-x)")

    st.subheader("Rotasi 180°")
    st.latex(r"(x,y)\to(-x,\;-y)")

    st.subheader("Rotasi 270° berlawanan arah jarum jam (CCW)")
    st.latex(r"(x,y)\to(y,\;-x)")
    st.caption("Perhatikan: rotasi 270° CCW sama dengan rotasi 90° CW.")  # FIX: klarifikasi

    # =========================================================
    # 8. MATRIKS ROTASI
    # =========================================================

    st.header("5️⃣ Matriks Rotasi")

    st.markdown("Rotasi dapat direpresentasikan menggunakan matriks.")

    st.subheader("Rotasi 90° CCW")
    st.latex(r"R_{90}=\begin{pmatrix}0&-1\\1&0\end{pmatrix}")

    st.subheader("Rotasi 180°")
    st.latex(r"R_{180}=\begin{pmatrix}-1&0\\0&-1\end{pmatrix}")

    st.subheader("Rotasi 270° CCW")
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

    elif materi == "Transformasi geometri":
        transformasi_geometri()
        #pass

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
