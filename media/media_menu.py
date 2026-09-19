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


# ... (fungsi lain sama, tinggal ganti st.subheader → st.markdown("#### ..."))


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

    st.markdown("**Contoh fungsi statistik:**")

    st.code(
        """=AVERAGE(A2:A20)
=MEDIAN(A2:A20)
=STDEV.S(A2:A20)
=MAX(A2:A20)
=MIN(A2:A20)""",
        language="text"
    )

    # ✅ Tambahan: link konsisten dengan fungsi lain
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
