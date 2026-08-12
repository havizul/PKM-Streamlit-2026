import streamlit as st
from streamlit_option_menu import option_menu

# ============================================================
# KONFIGURASI HALAMAN
# ============================================================

st.set_page_config(
    page_title="Matematika Kelas X SMA",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# CSS
# ============================================================

st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

h1 {
    color: #1f4e79;
}

h2 {
    color: #2f75b5;
}

h3 {
    color: #5b9bd5;
}

.math-box {
    background-color: #f5f8fc;
    border-left: 5px solid #2f75b5;
    padding: 15px;
    border-radius: 8px;
    margin: 10px 0;
}

.example-box {
    background-color: #fff8e7;
    border-left: 5px solid #f4b183;
    padding: 15px;
    border-radius: 8px;
    margin: 10px 0;
}

.exercise-box {
    background-color: #eef7ee;
    border-left: 5px solid #70ad47;
    padding: 15px;
    border-radius: 8px;
    margin: 10px 0;
}

.footer {
    text-align: center;
    color: gray;
    margin-top: 50px;
    padding: 20px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HEADER
# ============================================================

st.title("📐 Matematika Kelas X SMA")

st.markdown("""
### Materi Pembelajaran Matematika

Aplikasi pembelajaran interaktif yang memuat materi:

1. Bilangan Berpangkat
2. Persamaan dan Fungsi Eksponensial
3. Sistem Pertidaksamaan Linear Dua Variabel (SPtLDV)
4. Persamaan dan Fungsi Kuadrat
5. Trigonometri I
6. Statistika
""")


# ============================================================
# MENU HORIZONTAL
# ============================================================

selected = option_menu(
    menu_title=None,
    options=[
        "Beranda",
        "Bilangan Berpangkat",
        "Eksponensial",
        "SPtLDV",
        "Fungsi Kuadrat",
        "Trigonometri I",
        "Statistika"
    ],
    icons=[
        "house",
        "123",
        "graph-up-arrow",
        "grid-3x3",
        "bezier2",
        "triangle",
        "bar-chart"
    ],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {
            "padding": "0!important",
            "background-color": "#f8f9fa"
        },
        "icon": {
            "color": "#2f75b5",
            "font-size": "18px"
        },
        "nav-link": {
            "font-size": "14px",
            "text-align": "center",
            "margin": "0px",
            "--hover-color": "#e7f1ff"
        },
        "nav-link-selected": {
            "background-color": "#2f75b5",
            "color": "white"
        },
    }
)


# ============================================================
# BERANDA
# ============================================================

if selected == "Beranda":

    st.header("🏠 Selamat Datang")

    st.markdown("""
    Aplikasi ini digunakan sebagai media pembelajaran Matematika
    untuk siswa kelas X SMA.

    Gunakan menu horizontal di atas untuk memilih materi.
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("""
        ### 🔢 Eksponen
        Memahami bilangan berpangkat, sifat eksponen,
        bentuk akar, dan penerapannya.
        """)

    with col2:
        st.success("""
        ### 📈 Fungsi
        Mempelajari fungsi eksponensial dan fungsi kuadrat
        serta grafiknya.
        """)

    with col3:
        st.warning("""
        ### 📊 Data
        Mempelajari statistika, penyajian data,
        ukuran pemusatan dan penyebaran.
        """)

    st.divider()

    st.subheader("📚 Tujuan Pembelajaran")

    st.markdown("""
    Setelah mempelajari materi ini, siswa diharapkan mampu:

    - memahami konsep bilangan berpangkat;
    - menyelesaikan persamaan eksponensial;
    - menganalisis fungsi eksponensial;
    - menentukan daerah penyelesaian SPtLDV;
    - menyelesaikan persamaan kuadrat;
    - menganalisis grafik fungsi kuadrat;
    - menggunakan konsep trigonometri;
    - mengolah dan menginterpretasikan data statistik.
    """)


# ============================================================
# 1. BILANGAN BERPANGKAT
# ============================================================

elif selected == "Bilangan Berpangkat":

    st.header("1. Bilangan Berpangkat")

    st.markdown("""
    Bilangan berpangkat digunakan untuk menyatakan perkalian
    berulang dari suatu bilangan.
    """)

    st.subheader("A. Pengertian")

    st.latex(r"a^n = \underbrace{a \times a \times a \times \cdots \times a}_{n\ faktor}")

    st.markdown("""
    Keterangan:

    - `a` = bilangan pokok atau basis
    - `n` = pangkat atau eksponen
    """)

    st.subheader("B. Sifat-Sifat Eksponen")

    st.latex(r"a^m \times a^n = a^{m+n}")

    st.latex(r"\frac{a^m}{a^n}=a^{m-n}")

    st.latex(r"(a^m)^n=a^{mn}")

    st.latex(r"(ab)^n=a^n b^n")

    st.latex(r"\left(\frac{a}{b}\right)^n=\frac{a^n}{b^n}")

    st.latex(r"a^0=1")

    st.latex(r"a^{-n}=\frac{1}{a^n}")

    st.subheader("C. Pangkat Pecahan")

    st.latex(r"a^{\frac{m}{n}}=\sqrt[n]{a^m}")

    st.subheader("D. Contoh Soal")

    st.markdown("""
    **Sederhanakan:**
    """)

    st.latex(r"\frac{2^5\times2^3}{2^4}")

    st.latex(r"=2^{5+3-4}")

    st.latex(r"=2^4=16")

    st.subheader("E. Latihan")

    st.markdown("""
    1. Sederhanakan \(3^4 \times 3^2\).

    2. Sederhanakan \(\frac{5^7}{5^3}\).

    3. Tentukan nilai \(2^{-3}\).

    4. Sederhanakan \((2^3)^4\).

    5. Tentukan nilai \(81^{1/2}\).
    """)


# ============================================================
# 2. EKSPONENSIAL
# ============================================================

elif selected == "Eksponensial":

    st.header("2. Persamaan dan Fungsi Eksponensial")

    st.subheader("A. Persamaan Eksponensial")

    st.markdown("""
    Persamaan eksponensial adalah persamaan yang variabelnya
    terdapat pada pangkat.
    """)

    st.latex(r"a^{f(x)}=a^{g(x)}")

    st.markdown("dengan:")

    st.latex(r"a>0,\qquad a\neq1")

    st.subheader("B. Contoh")

    st.latex(r"2^{x+1}=2^5")

    st.latex(r"x+1=5")

    st.latex(r"x=4")

    st.subheader("C. Fungsi Eksponensial")

    st.latex(r"f(x)=a^x")

    st.markdown("""
    Jika:

    - \(a>1\) → fungsi meningkat
    - \(0<a<1\) → fungsi menurun
    """)

    st.subheader("D. Contoh Fungsi")

    st.latex(r"f(x)=2^x")

    st.subheader("E. Pertumbuhan Eksponensial")

    st.latex(r"N(t)=N_0a^t")

    st.markdown("""
    Keterangan:

    - \(N_0\) = jumlah awal
    - \(a\) = faktor pertumbuhan
    - \(t\) = waktu
    """)

    st.subheader("F. Contoh Kontekstual")

    st.markdown("""
    Suatu bakteri berjumlah 100 dan jumlahnya menjadi dua kali
    lipat setiap satu jam.
    """)

    st.latex(r"N(t)=100(2)^t")

    st.subheader("G. Latihan")

    st.markdown("""
    1. Tentukan \(x\) jika \(3^{x}=81\).

    2. Tentukan \(x\) jika \(2^{x+2}=32\).

    3. Tentukan nilai \(f(3)\) untuk \(f(x)=2^x+1\).

    4. Gambarkan grafik \(y=3^x\).
    """)


# ============================================================
# 3. SPtLDV
# ============================================================

elif selected == "SPtLDV":

    st.header("3. Sistem Pertidaksamaan Linear Dua Variabel")

    st.markdown("""
    Sistem Pertidaksamaan Linear Dua Variabel (SPtLDV) merupakan
    sistem yang terdiri atas dua atau lebih pertidaksamaan linear
    dengan dua variabel.
    """)

    st.subheader("A. Bentuk Umum")

    st.latex(r"ax+by\leq c")

    st.latex(r"ax+by\geq c")

    st.latex(r"ax+by<c")

    st.latex(r"ax+by>c")

    st.subheader("B. Contoh Sistem")

    st.latex(r"""
    \begin{cases}
    x+y\leq6\\
    x\geq0\\
    y\geq0
    \end{cases}
    """)

    st.subheader("C. Langkah Penyelesaian")

    st.markdown("""
    **Langkah 1**

    Ubah pertidaksamaan menjadi persamaan garis batas.

    **Langkah 2**

    Tentukan minimal dua titik yang dilalui garis.

    **Langkah 3**

    Gambarkan garis pada bidang koordinat.

    **Langkah 4**

    Tentukan daerah penyelesaian menggunakan titik uji.

    **Langkah 5**

    Tentukan irisan semua daerah penyelesaian.
    """)

    st.subheader("D. Garis Batas")

    col1, col2 = st.columns(2)

    with col1:
        st.info("""
        **≤ atau ≥**

        Menggunakan garis penuh.
        """)

    with col2:
        st.warning("""
        **< atau >**

        Menggunakan garis putus-putus.
        """)

    st.subheader("E. Contoh")

    st.latex(r"x+y\leq6")

    st.markdown("""
    Garis batasnya adalah:
    """)

    st.latex(r"x+y=6")

    st.markdown("""
    Titik potong:

    - \(x=0\) → \(y=6\)
    - \(y=0\) → \(x=6\)

    Sehingga garis melalui titik \((0,6)\) dan \((6,0)\).
    """)

    st.subheader("F. Latihan")

    st.markdown("""
    Tentukan daerah penyelesaian:

    \[
    \begin{cases}
    2x+y\leq8\\
    x+2y\leq8\\
    x\geq0\\
    y\geq0
    \end{cases}
    \]
    """)


# ============================================================
# 4. FUNGSI KUADRAT
# ============================================================

elif selected == "Fungsi Kuadrat":

    st.header("4. Persamaan dan Fungsi Kuadrat")

    st.subheader("A. Persamaan Kuadrat")

    st.latex(r"ax^2+bx+c=0")

    st.markdown("""
    dengan \(a\neq0\).
    """)

    st.subheader("B. Faktorisasi")

    st.latex(r"x^2-5x+6=0")

    st.latex(r"(x-2)(x-3)=0")

    st.latex(r"x=2\quad\text{atau}\quad x=3")

    st.subheader("C. Rumus Kuadrat")

    st.latex(
        r"x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}"
    )

    st.subheader("D. Diskriminan")

    st.latex(r"\Delta=b^2-4ac")

    st.markdown("""
    Interpretasi diskriminan:

    | Diskriminan | Jumlah akar real |
    |---|---|
    | Δ > 0 | 2 akar berbeda |
    | Δ = 0 | 1 akar kembar |
    | Δ < 0 | Tidak ada akar real |
    """)

    st.subheader("E. Fungsi Kuadrat")

    st.latex(r"f(x)=ax^2+bx+c")

    st.subheader("F. Sumbu Simetri")

    st.latex(r"x=-\frac{b}{2a}")

    st.subheader("G. Titik Puncak")

    st.markdown("""
    Jika sumbu simetri adalah \(x=h\), maka titik puncak:
    """)

    st.latex(r"(h,f(h))")

    st.subheader("H. Bentuk Puncak")

    st.latex(r"f(x)=a(x-h)^2+k")

    st.subheader("I. Arah Parabola")

    st.markdown("""
    - Jika \(a>0\), parabola membuka ke atas.
    - Jika \(a<0\), parabola membuka ke bawah.
    """)

    st.subheader("J. Latihan")

    st.markdown("""
    1. Tentukan akar-akar \(x^2-7x+12=0\).

    2. Tentukan diskriminan \(2x^2-4x+3=0\).

    3. Tentukan sumbu simetri \(f(x)=x^2-6x+5\).

    4. Tentukan titik puncak \(f(x)=x^2-4x+3\).
    """)


# ============================================================
# 5. TRIGONOMETRI
# ============================================================

elif selected == "Trigonometri I":

    st.header("5. Trigonometri I")

    st.markdown("""
    Trigonometri mempelajari hubungan antara besar sudut
    dan panjang sisi pada segitiga.
    """)

    st.subheader("A. Segitiga Siku-Siku")

    st.markdown("""
    Terhadap sudut \(\theta\):

    - sisi depan = opposite
    - sisi samping = adjacent
    - sisi miring = hypotenuse
    """)

    st.subheader("B. Sinus")

    st.latex(r"\sin\theta=\frac{\text{sisi depan}}{\text{sisi miring}}")

    st.subheader("C. Cosinus")

    st.latex(r"\cos\theta=\frac{\text{sisi samping}}{\text{sisi miring}}")

    st.subheader("D. Tangen")

    st.latex(r"\tan\theta=\frac{\text{sisi depan}}{\text{sisi samping}}")

    st.subheader("E. SOH-CAH-TOA")

    st.success("""
    **SOH**

    Sin = Opposite / Hypotenuse

    **CAH**

    Cos = Adjacent / Hypotenuse

    **TOA**

    Tan = Opposite / Adjacent
    """)

    st.subheader("F. Contoh 3-4-5")

    st.markdown("""
    Sebuah segitiga siku-siku mempunyai sisi:

    - depan = 3
    - samping = 4
    - miring = 5
    """)

    st.latex(r"\sin\theta=\frac35")

    st.latex(r"\cos\theta=\frac45")

    st.latex(r"\tan\theta=\frac34")

    st.subheader("G. Sudut Istimewa")

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

    st.subheader("H. Identitas Trigonometri Dasar")

    st.latex(
        r"\sin^2\theta+\cos^2\theta=1"
    )

    st.latex(r"\tan\theta=\frac{\sin\theta}{\cos\theta}")

    st.subheader("I. Latihan")

    st.markdown("""
    1. Jika sisi depan = 6 dan sisi miring = 10,
       tentukan \(\sin\theta\).

    2. Jika sisi samping = 8 dan sisi miring = 10,
       tentukan \(\cos\theta\).

    3. Jika sisi depan = 5 dan sisi samping = 12,
       tentukan \(\tan\theta\).

    4. Tentukan nilai \(\sin 30^\circ\).

    5. Tentukan nilai \(\tan45^\circ\).
    """)


# ============================================================
# 6. STATISTIKA
# ============================================================

elif selected == "Statistika":

    st.header("6. Statistika")

    st.markdown("""
    Statistika merupakan ilmu yang mempelajari pengumpulan,
    penyajian, pengolahan, analisis, dan interpretasi data.
    """)

    st.subheader("A. Jenis Data")

    st.markdown("""
    Data dapat berupa:

    - Data kuantitatif
    - Data kualitatif
    - Data tunggal
    - Data berkelompok
    """)

    st.subheader("B. Penyajian Data")

    st.markdown("""
    Data dapat disajikan dalam bentuk:

    - tabel
    - diagram batang
    - diagram garis
    - diagram lingkaran
    - histogram
    - poligon frekuensi
    """)

    st.subheader("C. Mean")

    st.latex(
        r"\bar{x}=\frac{\sum x_i}{n}"
    )

    st.markdown("""
    Contoh data:

    6, 7, 8, 9, 10
    """)

    st.latex(
        r"\bar{x}=\frac{6+7+8+9+10}{5}=8"
    )

    st.subheader("D. Median")

    st.markdown("""
    Median adalah nilai tengah setelah data diurutkan.

    Contoh:

    5, 7, 8, 10, 12

    Median = 8
    """)

    st.subheader("E. Modus")

    st.markdown("""
    Modus adalah nilai yang paling sering muncul.

    Contoh:

    5, 6, 6, 7, 8, 6, 9

    Modus = 6
    """)

    st.subheader("F. Kuartil")

    st.markdown("""
    Kuartil membagi data menjadi empat bagian:

    - \(Q_1\) = kuartil bawah
    - \(Q_2\) = median
    - \(Q_3\) = kuartil atas
    """)

    st.subheader("G. Jangkauan")

    st.latex(
        r"R=x_{\max}-x_{\min}"
    )

    st.subheader("H. Jangkauan Interkuartil")

    st.latex(
        r"IQR=Q_3-Q_1"
    )

    st.subheader("I. Varians")

    st.latex(r"s^2=\frac{\sum(x_i-\bar{x})^2}{n-1}")

    st.subheader("J. Simpangan Baku")

    st.latex(
        r"s=\sqrt{\frac{\sum(x_i-\bar{x})^2}{n-1}}"
    )

    st.subheader("K. Latihan")

    st.markdown("""
    Diketahui data:

    \[
    5,\ 6,\ 7,\ 7,\ 8,\ 9,\ 10
    \]

    Tentukan:

    1. Mean
    2. Median
    3. Modus
    4. Jangkauan
    5. Kuartil bawah
    6. Kuartil atas
    """)


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.markdown("""
<div class="footer">

📐 <b>Matematika Kelas X SMA</b><br>
Media Pembelajaran Interaktif

</div>
""", unsafe_allow_html=True)