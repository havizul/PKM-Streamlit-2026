import streamlit as st

# ============================================================
# KONFIGURASI
# ============================================================

st.set_page_config(
    page_title="Media Pembelajaran Matematika",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CSS
# ============================================================

st.markdown("""
<style>

    /* =========================
       GLOBAL
       ========================= */

    .main {
        padding-top: 1rem;
    }

    /* =========================
       JUDUL
       ========================= */

    .main-title {
        font-size: 30px;
        font-weight: 700;
        color: #1f4e79;
        margin-bottom: 5px;
    }

    .subtitle {
        color: #666;
        font-size: 15px;
        margin-bottom: 20px;
    }

    /* =========================
       TOP NAVIGATION
       ========================= */

    div[data-testid="stHorizontalBlock"] {
        gap: 0.5rem;
    }

    /* Radio horizontal */

    div[role="radiogroup"] {
        gap: 0.3rem;
    }

    div[role="radiogroup"] label {
        background-color: #f1f5f9;
        padding: 10px 18px;
        border-radius: 8px;
        border: 1px solid #d9e2ec;
        cursor: pointer;
        transition: 0.2s;
    }

    div[role="radiogroup"] label:hover {
        background-color: #e3f2fd;
        border-color: #90caf9;
    }

    /* =========================
       SIDEBAR
       ========================= */

    section[data-testid="stSidebar"] {
        background-color: #f8fafc;
    }

    .sidebar-title {
        font-size: 20px;
        font-weight: 700;
        color: #1f4e79;
        margin-bottom: 15px;
    }

    .phase-title {
        font-size: 14px;
        font-weight: 700;
        color: #2f75b5;
        margin-top: 18px;
        margin-bottom: 5px;
        padding: 6px 8px;
        background-color: #eaf3fb;
        border-radius: 5px;
    }

    /* =========================
       CONTENT BOX
       ========================= */

    .content-box {
        background-color: #f8fbff;
        border-left: 5px solid #2f75b5;
        padding: 18px;
        border-radius: 8px;
        margin-bottom: 20px;
    }

    .info-box {
        background-color: #eef7ee;
        border-left: 5px solid #70ad47;
        padding: 15px;
        border-radius: 8px;
        margin: 15px 0;
    }

    .example-box {
        background-color: #fff8e7;
        border-left: 5px solid #f4b183;
        padding: 15px;
        border-radius: 8px;
        margin: 15px 0;
    }

    /* =========================
       FOOTER
       ========================= */

    .footer {
        text-align: center;
        color: #777;
        padding: 30px 0;
        margin-top: 50px;
        border-top: 1px solid #ddd;
    }

</style>
""", unsafe_allow_html=True)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">📐 Media Pembelajaran Matematika</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Matematika SMA — Fase E dan F</div>',
    unsafe_allow_html=True
)


# ============================================================
# MENU UTAMA HORIZONTAL
# ============================================================

menu_utama = st.radio(
    "",
    [
        "🏠 Beranda",
        "📚 Materi Matematika",
        "🎓 Media Pembelajaran"
    ],
    horizontal=True,
    label_visibility="collapsed"
)


# ============================================================
# DATA MATERI
# ============================================================

fase_e = [
    "Bilangan Berpangkat",
    "Persamaan dan Fungsi Eksponensial",
    "SPtLDV",
    "Persamaan dan Fungsi Kuadrat",
    "Trigonometri I",
    "Statistika"
]

fase_f_umum = [
    "Barisan dan Deret",
    "Matematika Keuangan",
    "Fungsi, Invers dan Komposisi Fungsi",
    "Transformasi Fungsi",
    "Lingkaran",
    "Statistika Bivariat",
    "Kaidah Pencacahan",
    "Peluang"
]

fase_f_lanjut = [
    "Polinomial",
    "Matriks",
    "Transformasi Geometri",
    "Trigonometri",
    "Pemodelan Fungsi",
    "Irisan Kerucut (Lingkaran & Elips)",
    "Distribusi Peluang (Binom & Normal)",
    "Limit Fungsi (Tambahan)",
    "Turunan & Penerapannya (Tambahan)",
    "Integral (Tambahan)"
]


# ============================================================
# SESSION STATE
# ============================================================

if "materi_terpilih" not in st.session_state:
    st.session_state.materi_terpilih = "Bilangan Berpangkat"


# ============================================================
# SIDEBAR SUBMENU
# ============================================================

if menu_utama == "📚 Materi Matematika":

    with st.sidebar:

        st.markdown(
            '<div class="sidebar-title">📚 Materi Matematika</div>',
            unsafe_allow_html=True
        )

        # ----------------------------------------------------
        # FASE E
        # ----------------------------------------------------

        st.markdown(
            '<div class="phase-title">FASE E — KELAS X</div>',
            unsafe_allow_html=True
        )

        for materi in fase_e:

            if st.button(
                materi,
                key="fase_e_" + materi,
                use_container_width=True
            ):
                st.session_state.materi_terpilih = materi

        # ----------------------------------------------------
        # FASE F UMUM
        # ----------------------------------------------------

        st.markdown(
            '<div class="phase-title">FASE F — UMUM (KELAS XI & XII)</div>',
            unsafe_allow_html=True
        )

        for materi in fase_f_umum:

            if st.button(
                materi,
                key="fase_f_umum_" + materi,
                use_container_width=True
            ):
                st.session_state.materi_terpilih = materi

        # ----------------------------------------------------
        # FASE F LANJUT
        # ----------------------------------------------------

        st.markdown(
            '<div class="phase-title">FASE F — LANJUT</div>',
            unsafe_allow_html=True
        )

        for materi in fase_f_lanjut:

            if st.button(
                materi,
                key="fase_f_lanjut_" + materi,
                use_container_width=True
            ):
                st.session_state.materi_terpilih = materi


# ============================================================
# SIDEBAR MEDIA PEMBELAJARAN
# ============================================================

elif menu_utama == "🎓 Media Pembelajaran":

    with st.sidebar:

        st.markdown(
            '<div class="sidebar-title">🎓 Media Pembelajaran</div>',
            unsafe_allow_html=True
        )

        media = [
            "Bilangan Berpangkat",
            "Persamaan dan Fungsi Eksponensial",
            "SPtLDV",
            "Persamaan dan Fungsi Kuadrat",
            "Trigonometri I",
            "Statistika"
        ]

        for materi in media:

            if st.button(
                materi,
                key="media_" + materi,
                use_container_width=True
            ):
                st.session_state.materi_terpilih = materi


# ============================================================
# HALAMAN BERANDA
# ============================================================

if menu_utama == "🏠 Beranda":

    st.header("🏠 Selamat Datang")

    st.markdown("""
    <div class="content-box">

    ## Media Pembelajaran Matematika

    Aplikasi ini menyediakan materi pembelajaran Matematika
    untuk jenjang SMA berdasarkan Fase E dan F.

    Gunakan menu horizontal di bagian atas untuk memilih
    kategori pembelajaran.

    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:

        st.info("""
        ### 📘 Fase E

        Materi Matematika Kelas X.

        Meliputi:
        - Eksponen
        - Eksponensial
        - SPtLDV
        - Fungsi Kuadrat
        - Trigonometri
        - Statistika
        """)

    with col2:

        st.success("""
        ### 📗 Fase F Umum

        Materi Matematika Kelas XI dan XII.

        Meliputi:
        - Barisan dan Deret
        - Matematika Keuangan
        - Fungsi
        - Lingkaran
        - Peluang
        """)

    with col3:

        st.warning("""
        ### 📕 Fase F Lanjut

        Materi Matematika lanjutan.

        Meliputi:
        - Polinomial
        - Matriks
        - Vektor
        - Kalkulus
        - Distribusi Peluang
        """)

    st.divider()

    st.subheader("🎯 Tujuan Pembelajaran")

    st.markdown("""
    Siswa diharapkan mampu:

    - memahami konsep matematika;
    - menggunakan rumus dan prosedur matematika;
    - melakukan penalaran matematis;
    - menyelesaikan masalah kontekstual;
    - menginterpretasikan hasil perhitungan;
    - menggunakan teknologi sebagai alat pembelajaran matematika.
    """)


# ============================================================
# HALAMAN MATERI MATEMATIKA
# ============================================================

elif menu_utama == "📚 Materi Matematika":

    materi = st.session_state.materi_terpilih

    st.header(f"📖 {materi}")

    # ========================================================
    # FASE E
    # ========================================================

    if materi == "Bilangan Berpangkat":

        st.subheader("Bilangan Berpangkat")

        st.markdown("""
        Bilangan berpangkat digunakan untuk menyatakan
        perkalian berulang suatu bilangan.
        """)

        st.latex(r"a^n=a\times a\times a\times\cdots\times a")

        st.subheader("Sifat-Sifat Eksponen")

        st.latex(r"a^m\cdot a^n=a^{m+n}")

        st.latex(r"\frac{a^m}{a^n}=a^{m-n}")

        st.latex(r"(a^m)^n=a^{mn}")

        st.latex(r"(ab)^n=a^nb^n")

        st.latex(r"a^0=1")

        st.latex(r"a^{-n}=\frac{1}{a^n}")

        st.subheader("Contoh")

        st.latex(r"\frac{2^5\times2^3}{2^4}")

        st.latex(r"=2^{5+3-4}")

        st.latex(r"=2^4=16")

    # --------------------------------------------------------
    # EKSPONENSIAL
    # --------------------------------------------------------

    elif materi == "Persamaan dan Fungsi Eksponensial":

        st.subheader("Persamaan Eksponensial")

        st.latex(r"a^{f(x)}=a^{g(x)}")

        st.markdown("""
        dengan:

        \[
        a>0,\qquad a\neq1
        \]
        """)

        st.subheader("Contoh")

        st.latex(r"2^{x+1}=2^5")

        st.latex(r"x+1=5")

        st.latex(r"x=4")

        st.subheader("Fungsi Eksponensial")

        st.latex(r"f(x)=a^x")

        st.markdown("""
        Jika \(a>1\), fungsi mengalami pertumbuhan.

        Jika \(0<a<1\), fungsi mengalami peluruhan.
        """)

        st.subheader("Penerapan")

        st.markdown("""
        Fungsi eksponensial dapat digunakan untuk:

        - pertumbuhan penduduk;
        - pertumbuhan bakteri;
        - bunga majemuk;
        - pertumbuhan investasi;
        - peluruhan.
        """)

    # --------------------------------------------------------
    # SPTLDV
    # --------------------------------------------------------

    elif materi == "SPtLDV":

        st.subheader(
            "Sistem Pertidaksamaan Linear Dua Variabel"
        )

        st.markdown("""
        SPtLDV adalah sistem yang terdiri atas dua atau lebih
        pertidaksamaan linear dengan dua variabel.
        """)

        st.latex(r"ax+by\leq c")

        st.latex(r"ax+by\geq c")

        st.subheader("Contoh")

        st.latex(r"""
        \begin{cases}
        x+y\leq6\\
        x\geq0\\
        y\geq0
        \end{cases}
        """)

        st.subheader("Langkah Penyelesaian")

        st.markdown("""
        1. Tentukan garis batas.
        2. Tentukan titik potong.
        3. Gambarkan garis.
        4. Tentukan daerah yang memenuhi.
        5. Tentukan irisan semua daerah.
        """)

    # --------------------------------------------------------
    # KUADRAT
    # --------------------------------------------------------

    elif materi == "Persamaan dan Fungsi Kuadrat":

        st.subheader("Persamaan Kuadrat")

        st.latex(r"ax^2+bx+c=0")

        st.subheader("Rumus Kuadrat")

        st.latex(
            r"x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}"
        )

        st.subheader("Diskriminan")

        st.latex(r"\Delta=b^2-4ac")

        st.markdown("""
        **Interpretasi:**

        - \(\Delta>0\) → dua akar real berbeda
        - \(\Delta=0\) → satu akar real kembar
        - \(\Delta<0\) → tidak memiliki akar real
        """)

        st.subheader("Fungsi Kuadrat")

        st.latex(r"f(x)=ax^2+bx+c")

        st.subheader("Sumbu Simetri")

        st.latex(r"x=-\frac{b}{2a}")

        st.subheader("Bentuk Puncak")

        st.latex(r"f(x)=a(x-h)^2+k")

    # --------------------------------------------------------
    # TRIGONOMETRI
    # --------------------------------------------------------

    elif materi == "Trigonometri I":

        st.subheader("Trigonometri I")

        st.markdown("""
        Trigonometri mempelajari hubungan antara sudut
        dan panjang sisi segitiga.
        """)

        st.subheader("Sinus")

        st.latex(
            r"\sin\theta=
            \frac{\text{sisi depan}}
            {\text{sisi miring}}"
        )

        st.subheader("Cosinus")

        st.latex(
            r"\cos\theta=
            \frac{\text{sisi samping}}
            {\text{sisi miring}}"
        )

        st.subheader("Tangen")

        st.latex(
            r"\tan\theta=
            \frac{\text{sisi depan}}
            {\text{sisi samping}}"
        )

        st.subheader("Identitas Dasar")

        st.latex(
            r"\sin^2\theta+\cos^2\theta=1"
        )

        st.subheader("Sudut Istimewa")

        data = {
            "Sudut": [
                "0°",
                "30°",
                "45°",
                "60°",
                "90°"
            ],
            "sin": [
                "0",
                "1/2",
                "√2/2",
                "√3/2",
                "1"
            ],
            "cos": [
                "1",
                "√3/2",
                "√2/2",
                "1/2",
                "0"
            ],
            "tan": [
                "0",
                "√3/3",
                "1",
                "√3",
                "Tidak terdefinisi"
            ]
        }

        st.table(data)

    # --------------------------------------------------------
    # STATISTIKA
    # --------------------------------------------------------

    elif materi == "Statistika":

        st.subheader("Statistika")

        st.markdown("""
        Statistika merupakan ilmu yang mempelajari
        pengumpulan, penyajian, pengolahan, analisis,
        dan interpretasi data.
        """)

        st.subheader("Mean")

        st.latex(
            r"\bar{x}=\frac{\sum x_i}{n}"
        )

        st.subheader("Median")

        st.write(
            "Median adalah nilai tengah setelah data diurutkan."
        )

        st.subheader("Modus")

        st.write(
            "Modus adalah nilai yang paling sering muncul."
        )

        st.subheader("Jangkauan")

        st.latex(
            r"R=x_{\max}-x_{\min}"
        )

        st.subheader("Kuartil")

        st.markdown("""
        - \(Q_1\) = kuartil bawah
        - \(Q_2\) = median
        - \(Q_3\) = kuartil atas
        """)

        st.subheader("Jangkauan Interkuartil")

        st.latex(
            r"IQR=Q_3-Q_1"
        )

        st.subheader("Simpangan Baku")

        st.latex(
            r"s=\sqrt{
            \frac{\sum(x_i-\bar{x})^2}{n-1}
            }"
        )

    # ========================================================
    # FASE F UMUM
    # ========================================================

    elif materi == "Barisan dan Deret":

        st.subheader("Barisan dan Deret")

        st.markdown("""
        Materi mencakup:

        - Barisan aritmetika
        - Deret aritmetika
        - Barisan geometri
        - Deret geometri
        - Penerapan barisan dan deret
        """)

        st.latex(
            r"U_n=a+(n-1)b"
        )

        st.latex(
            r"S_n=\frac{n}{2}(2a+(n-1)b)"
        )

    elif materi == "Matematika Keuangan":

        st.subheader("Matematika Keuangan")

        st.markdown("""
        Materi mencakup:

        - bunga tunggal;
        - bunga majemuk;
        - diskon;
        - pajak;
        - pertumbuhan nilai;
        - cicilan dan anuitas.
        """)

    elif materi == "Fungsi, Invers dan Komposisi Fungsi":

        st.subheader("Fungsi, Invers dan Komposisi Fungsi")

        st.latex(r"(f\circ g)(x)=f(g(x))")

        st.markdown("""
        Materi meliputi:

        - fungsi;
        - domain dan range;
        - fungsi satu-satu;
        - fungsi invers;
        - komposisi fungsi.
        """)

    elif materi == "Transformasi Fungsi":

        st.subheader("Transformasi Fungsi")

        st.markdown("""
        Materi meliputi:

        - translasi;
        - refleksi;
        - rotasi;
        - dilatasi;
        - perubahan grafik fungsi.
        """)

    elif materi == "Lingkaran":

        st.subheader("Lingkaran")

        st.latex(r"(x-a)^2+(y-b)^2=r^2")

        st.markdown("""
        Materi meliputi:

        - persamaan lingkaran;
        - pusat dan jari-jari;
        - kedudukan titik;
        - garis singgung lingkaran.
        """)

    elif materi == "Statistika Bivariat":

        st.subheader("Statistika Bivariat")

        st.markdown("""
        Materi meliputi:

        - dua variabel;
        - diagram pencar;
        - korelasi;
        - pola hubungan;
        - regresi linear sederhana.
        """)

    elif materi == "Kaidah Pencacahan":

        st.subheader("Kaidah Pencacahan")

        st.markdown("""
        Materi meliputi:

        - aturan penjumlahan;
        - aturan perkalian;
        - faktorial;
        - permutasi;
        - kombinasi.
        """)

    elif materi == "Peluang":

        st.subheader("Peluang")

        st.latex(
            r"P(A)=\frac{n(A)}{n(S)}"
        )

        st.markdown("""
        Materi meliputi:

        - ruang sampel;
        - kejadian;
        - peluang kejadian;
        - peluang komplemen;
        - peluang gabungan.
        """)

    # ========================================================
    # FASE F LANJUT
    # ========================================================

    elif materi == "Polinomial":

        st.subheader("Polinomial")

        st.markdown("""
        Materi meliputi:

        - bentuk polinomial;
        - operasi polinomial;
        - pembagian polinomial;
        - teorema sisa;
        - teorema faktor;
        - akar-akar polinomial.
        """)

    elif materi == "Matriks":

        st.subheader("Matriks")

        st.markdown("""
        Materi meliputi:

        - konsep matriks;
        - jenis matriks;
        - operasi matriks;
        - determinan;
        - invers matriks;
        - penerapan matriks.
        """)

    elif materi == "Transformasi Geometri":

        st.subheader("Transformasi Geometri")

        st.markdown("""
        Materi meliputi:

        - translasi;
        - refleksi;
        - rotasi;
        - dilatasi;
        - transformasi menggunakan matriks.
        """)

    elif materi == "Trigonometri":

        st.subheader("Trigonometri Lanjutan")

        st.markdown("""
        Materi meliputi:

        - identitas trigonometri;
        - persamaan trigonometri;
        - aturan sinus;
        - aturan cosinus;
        - fungsi trigonometri;
        - grafik fungsi trigonometri.
        """)

    elif materi == "Pemodelan Fungsi":

        st.subheader("Pemodelan Fungsi")

        st.markdown("""
        Materi meliputi:

        - identifikasi variabel;
        - pembentukan model;
        - fungsi linear;
        - fungsi kuadrat;
        - fungsi eksponensial;
        - interpretasi model.
        """)

    elif materi == "Irisan Kerucut (Lingkaran & Elips)":

        st.subheader("Irisan Kerucut")

        st.markdown("""
        Materi meliputi:

        - lingkaran;
        - elips;
        - fokus;
        - sumbu mayor dan minor;
        - persamaan irisan kerucut.
        """)

    elif materi == "Distribusi Peluang (Binom & Normal)":

        st.subheader("Distribusi Peluang")

        st.markdown("""
        Materi meliputi:

        - distribusi binomial;
        - distribusi normal;
        - parameter distribusi;
        - peluang berdasarkan distribusi.
        """)

    elif materi == "Limit Fungsi (Tambahan)":

        st.subheader("Limit Fungsi")

        st.markdown("""
        Materi tambahan sebagai pengantar kalkulus.

        Materi meliputi:

        - konsep limit;
        - limit fungsi aljabar;
        - limit kiri dan kanan;
        - limit di suatu titik.
        """)

    elif materi == "Turunan & Penerapannya (Tambahan)":

        st.subheader("Turunan dan Penerapannya")

        st.markdown("""
        Materi tambahan kalkulus:

        - konsep turunan;
        - aturan turunan;
        - turunan fungsi aljabar;
        - gradien garis singgung;
        - nilai maksimum dan minimum;
        - penerapan turunan.
        """)

    elif materi == "Integral (Tambahan)":

        st.subheader("Integral")

        st.markdown("""
        Materi tambahan kalkulus:

        - konsep integral;
        - integral tak tentu;
        - integral tentu;
        - antiturunan;
        - luas daerah.
        """)


# ============================================================
# MEDIA PEMBELAJARAN
# ============================================================

elif menu_utama == "🎓 Media Pembelajaran":

    st.header("🎓 Media Pembelajaran")

    st.markdown("""
    <div class="content-box">

    ## Media Pembelajaran Interaktif

    Pilih materi pada menu di sebelah kiri.

    Media pembelajaran nantinya dapat dikembangkan menjadi:

    - simulasi interaktif;
    - grafik dinamis;
    - kalkulator matematika;
    - latihan soal;
    - kuis;
    - evaluasi otomatis;
    - visualisasi GeoGebra;
    - visualisasi Python.

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">

📐 <b>Media Pembelajaran Matematika SMA</b><br>
Fase E dan F

</div>
""", unsafe_allow_html=True)
