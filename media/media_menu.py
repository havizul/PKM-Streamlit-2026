import streamlit as st


def media_geogebra():

    st.markdown("#### 📐 GeoGebra")

    st.markdown(r"""
    **GeoGebra** merupakan media pembelajaran matematika interaktif yang
    dapat digunakan untuk mengeksplorasi konsep secara visual dan dinamis.

    Dalam pembelajaran matematika, GeoGebra dapat digunakan untuk:

    - grafik fungsi,
    - geometri,
    - transformasi,
    - trigonometri,
    - kalkulus,
    - statistik,
    - visualisasi 2D dan 3D.
    """)

    st.info(r"""
    💡 **Contoh penggunaan**

    Gunakan GeoGebra untuk memvisualisasikan grafik fungsi, titik,
    transformasi geometri, limit, turunan, dan integral.
    """)

    st.link_button(
        "🌐 Buka GeoGebra",
        "https://www.geogebra.org/",
        use_container_width=True
    )


def media_desmos():

    st.markdown("#### 🧮 Desmos")

    st.markdown(r"""
    **Desmos** merupakan media grafik interaktif yang dapat digunakan
    untuk mengeksplorasi hubungan antara persamaan matematika dan
    representasi grafik.

    Cocok digunakan untuk:

    - fungsi,
    - persamaan,
    - pertidaksamaan,
    - trigonometri,
    - transformasi,
    - statistik,
    - pemodelan matematika.
    """)

    st.info(r"""
    💡 **Contoh penggunaan**

    Masukkan persamaan fungsi dan ubah parameter secara interaktif
    untuk mengamati perubahan grafik.
    """)

    st.link_button(
        "🌐 Buka Desmos",
        "https://www.desmos.com/calculator",
        use_container_width=True
    )


def media_wayground():

    st.markdown("#### 📊 Wayground")

    st.markdown(r"""
    **Wayground** dapat digunakan sebagai media pembelajaran interaktif
    berbasis kuis dan aktivitas.

    Media ini dapat dimanfaatkan untuk:

    - asesmen formatif,
    - kuis matematika,
    - latihan soal,
    - evaluasi pemahaman,
    - aktivitas interaktif.
    """)

    st.info(r"""
    💡 **Contoh penggunaan**

    Dosen/guru dapat membuat kuis matematika kemudian menggunakannya
    sebagai evaluasi atau aktivitas pembelajaran.
    """)

    st.link_button(
        "🌐 Buka Wayground",
        "https://wayground.com/",
        use_container_width=True
    )


def media_wordwall():

    st.markdown("#### 🎮 Wordwall")

    st.markdown(r"""
    **Wordwall** merupakan media pembelajaran interaktif yang dapat
    digunakan untuk membuat berbagai aktivitas pembelajaran.

    Contohnya:

    - kuis,
    - mencocokkan pasangan,
    - roda acak,
    - pengelompokan,
    - teka-teki,
    - kartu belajar.
    """)

    st.info(r"""
    💡 **Contoh penggunaan**

    Materi matematika dapat dikemas menjadi aktivitas permainan sehingga
    mahasiswa atau siswa dapat belajar sambil berlatih.
    """)

    st.link_button(
        "🌐 Buka Wordwall",
        "https://wordwall.net/",
        use_container_width=True
    )


def media_gimkit():

    st.markdown("#### 🎯 Gimkit")

    st.markdown(r"""
    **Gimkit** merupakan platform pembelajaran berbasis permainan yang
    dapat digunakan untuk membuat aktivitas kuis interaktif.

    Dapat digunakan untuk:

    - latihan soal,
    - kuis matematika,
    - review materi,
    - evaluasi pembelajaran.
    """)

    st.info(r"""
    💡 **Contoh penggunaan**

    Gunakan Gimkit sebagai aktivitas review setelah mahasiswa mempelajari
    suatu topik matematika.
    """)

    st.link_button(
        "🌐 Buka Gimkit",
        "https://www.gimkit.com/",
        use_container_width=True
    )


def media_matlab():

    st.markdown("#### 💻 MATLAB")

    st.markdown(r"""
    **MATLAB** merupakan perangkat lunak komputasi numerik yang dapat
    digunakan untuk pembelajaran matematika dan pemodelan.

    Dapat digunakan untuk:

    - operasi matriks,
    - visualisasi fungsi,
    - kalkulus,
    - statistik,
    - metode numerik,
    - pemodelan matematika.
    """)

    st.info(r"""
    💡 **Contoh penggunaan**

    MATLAB dapat digunakan untuk melakukan perhitungan numerik dan
    visualisasi grafik fungsi matematika.
    """)

    st.link_button(
        "🌐 MATLAB",
        "https://www.mathworks.com/products/matlab.html",
        use_container_width=True
    )


def media_python():

    st.markdown("#### 🐍 Python")

    st.markdown(r"""
    **Python** dapat digunakan sebagai media pembelajaran matematika
    berbasis komputasi.

    Beberapa pustaka yang dapat digunakan:

    - NumPy → komputasi numerik.
    - Pandas → pengolahan data.
    - Matplotlib → visualisasi.
    - SymPy → matematika simbolik.
    - Streamlit → aplikasi pembelajaran interaktif.
    """)

    st.info(r"""
    💡 **Contoh penggunaan**

    Python dapat digunakan untuk membuat kalkulator matematika,
    visualisasi fungsi, simulasi probabilitas, analisis data, dan
    aplikasi pembelajaran interaktif.
    """)

    st.code(
        """import sympy as sp

x = sp.symbols('x')

f = x**2 + 3*x + 2

print(sp.diff(f, x))""",
        language="python"
    )

    st.markdown(r"""
    Contoh tersebut digunakan untuk menentukan turunan simbolik
    menggunakan Python.
    """)

    st.link_button(
        "🌐 Python",
        "https://www.python.org/",
        use_container_width=True
    )


def media_spreadsheet():

    st.markdown("#### 📈 Spreadsheet")

    st.markdown(r"""
    **Spreadsheet** seperti Microsoft Excel dan Google Sheets dapat
    digunakan sebagai media pembelajaran matematika dan statistika.

    Dapat digunakan untuk:

    - perhitungan matematika,
    - tabel data,
    - statistik deskriptif,
    - grafik,
    - simulasi,
    - analisis data.
    """)

    st.info(r"""
    💡 **Contoh penggunaan**

    Mahasiswa dapat menggunakan spreadsheet untuk menghitung rata-rata,
    median, standar deviasi, membuat grafik, serta melakukan analisis
    data sederhana.
    """)

    st.markdown(r"""
    **Contoh fungsi statistik:**
    """)

    st.code(
        """=AVERAGE(A2:A20)
=MEDIAN(A2:A20)
=STDEV.S(A2:A20)
=MAX(A2:A20)
=MIN(A2:A20)""",
        language="text"
    )

    # ✅ Link konsisten dengan fungsi media lainnya
    col1, col2 = st.columns(2)

    with col1:
        st.link_button(
            "🌐 Google Sheets",
            "https://sheets.google.com/",
            use_container_width=True
        )

    with col2:
        st.link_button(
            "🌐 Microsoft Excel",
            "https://www.microsoft.com/microsoft-365/excel",
            use_container_width=True
        )
