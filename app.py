import streamlit as st

from materi import fase_e
from materi import fase_f_umum
from materi import fase_f_lanjut
from media.media_menu import (
    media_geogebra,
    media_desmos,
    media_wayground,
    media_wordwall,
    media_gimkit,
    media_matlab,
    media_python,
    media_spreadsheet
)

from data.menu import (
    MENU_UTAMA,
    FASE_E,
    FASE_F_UMUM,
    FASE_F_LANJUT,
    MEDIA_PEMBELAJARAN,
    MATEMATIKA_BUDAYA
)

from matematika_budaya import budaya_menu



# ============================================================
# KONFIGURASI HALAMAN
# ============================================================

st.set_page_config(
    page_title="TM - IAIN PONTIANAK",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CSS
# ============================================================

st.markdown("""
<style>

.main-title {
    font-size: 32px;
    font-weight: 700;
    color: #1f4e79;
    margin-bottom: 0;
}

.subtitle {
    color: #666666;
    font-size: 15px;
    margin-bottom: 15px;
}

.sidebar-title {
    font-size: 21px;
    font-weight: 700;
    color: #1f4e79;
    margin-bottom: 10px;
}

.content-title {
    font-size: 28px;
    font-weight: 700;
    color: #1f4e79;
}

.info-box {
    padding: 20px;
    border-radius: 10px;
    background-color: #f7fbff;
    border-left: 5px solid #2f75b5;
    margin-bottom: 20px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# SESSION STATE
# ============================================================

if "halaman" not in st.session_state:
    st.session_state.halaman = "🏠 Beranda"

if "materi" not in st.session_state:
    st.session_state.materi = FASE_E[0]

if "media" not in st.session_state:
    st.session_state.media = MEDIA_PEMBELAJARAN[0]


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">📐 TADRIS MATEMATIKA - IAIN PONTIANAK</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Matematika SMA — Fase E dan F</div>',
    unsafe_allow_html=True
)


# ============================================================
# MENU UTAMA
# ============================================================

menu_utama = st.radio(
    "Menu Utama",
    MENU_UTAMA,
    horizontal=True,
    label_visibility="collapsed"
)

st.session_state.halaman = menu_utama


# ============================================================
# BERANDA
# ============================================================

if menu_utama == "🏠 Beranda":

    st.header("🏠 Beranda")

    st.markdown("""
    <div class="info-box">

    <h2>Selamat Datang</h2>

    <p>
    <b>Media Pembelajaran Matematika SMA</b>
    </p>

    <p>
    Aplikasi ini menyediakan materi pembelajaran Matematika
    berdasarkan Fase E dan F.
    </p>

    <p>
    Gunakan menu horizontal di bagian atas untuk memilih
    materi atau media pembelajaran.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.subheader("📚 Struktur Pembelajaran")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("""
        ### 📘 FASE E

        **Kelas X**

        6 materi:

        - Bilangan Berpangkat
        - Eksponensial
        - SPtLDV
        - Fungsi Kuadrat
        - Trigonometri I
        - Statistika
        """)

    with col2:
        st.success("""
        ### 📗 FASE F — UMUM

        **Kelas XI & XII**

        8 materi:

        - Barisan dan Deret
        - Matematika Keuangan
        - Fungsi
        - Transformasi Fungsi
        - Lingkaran
        - Statistika Bivariat
        - Pencacahan
        - Peluang
        """)

    with col3:
        st.warning("""
        ### 📕 FASE F — LANJUT

        10 materi:

        - Polinomial
        - Matriks
        - Transformasi Geometri
        - Trigonometri
        - Pemodelan Fungsi
        - Irisan Kerucut
        - Distribusi Peluang
        - Limit
        - Turunan
        - Integral
        """)


# ============================================================
# MATERI MATEMATIKA
# ============================================================

elif menu_utama == "📚 Materi Matematika":

    # --------------------------------------------------------
    # SIDEBAR
    # --------------------------------------------------------

    with st.sidebar:

        st.markdown(
            '<div class="sidebar-title">📚 Materi Matematika</div>',
            unsafe_allow_html=True
        )

        # ====================================================
        # FASE E
        # ====================================================

        with st.expander(
            "📘 FASE E — Kelas X",
            expanded=False #True
        ):

            for item in FASE_E:

                if st.button(
                    item,
                    key=f"fase_e_{item}",
                    use_container_width=True
                ):
                    st.session_state.materi = item
                    st.rerun()

        # ====================================================
        # FASE F UMUM
        # ====================================================

        with st.expander(
            "📗 FASE F — Umum (Kelas XI & XII)",
            expanded=False
        ):

            for item in FASE_F_UMUM:

                if st.button(
                    item,
                    key=f"fase_f_umum_{item}",
                    use_container_width=True
                ):
                    st.session_state.materi = item
                    st.rerun()

        # ====================================================
        # FASE F LANJUT
        # ====================================================

        with st.expander(
            "📕 FASE F — Lanjut",
            expanded=False
        ):

            for item in FASE_F_LANJUT:

                if st.button(
                    item,
                    key=f"fase_f_lanjut_{item}",
                    use_container_width=True
                ):
                    st.session_state.materi = item
                    st.rerun()


    # --------------------------------------------------------
    # TAMPILKAN MATERI
    # --------------------------------------------------------

    materi = st.session_state.materi

    if materi in FASE_E:
        fase_e.tampilkan(materi)

    elif materi in FASE_F_UMUM:
        fase_f_umum.tampilkan(materi)

    elif materi in FASE_F_LANJUT:
        fase_f_lanjut.tampilkan(materi)

    else:
        st.info(
            f"Materi **{materi}** belum dikembangkan."
        )


# ============================================================
# MEDIA PEMBELAJARAN
# ============================================================

elif menu_utama == "🎓 Media Pembelajaran":
    with st.sidebar:
        st.markdown(
            '<div class="sidebar-title">🎓 Media Pembelajaran</div>',
            unsafe_allow_html=True
        )

        for item in MEDIA_PEMBELAJARAN:

            if st.button(
                item,
                key=f"media_{item}",
                use_container_width=True
            ):
                st.session_state.media = item
                st.rerun()

    media = st.session_state.media

    st.header("🎓 Media Pembelajaran")

    st.divider()

    if media == "GeoGebra":
        media_geogebra()
        #pass

    elif media == "Desmos":
        media_desmos()
        #pass

    elif media == "Wayground":
        media_wayground()
        #pass

    elif media == "Wordwall":
        media_wordwall()
        #pass

    elif media == "Gimkit":
        media_gimkit()
        #pass

    elif media == "MATLAB":
        media_matlab()
        #pass

    elif media == "Python":
        media_python()
        #pass

    elif media == "Spreadsheet":
        media_spreadsheet()
        #pass

elif menu_utama == "🌿 Matematika dalam Budaya":
    with st.sidebar:
        st.markdown(
            '<div class="sidebar-title">🌿 Matematika dalam Budaya</div>',
            unsafe_allow_html=True
        )

        for item in MATEMATIKA_BUDAYA:

            if st.button(
                item,
                key=f"budaya_{item}",
                use_container_width=True
            ):
                st.session_state.budaya = item
                st.rerun()

    budaya = st.session_state.budaya

    st.header("🌿 Matematika dalam Budaya")

    st.divider()

    if budaya:
        budaya_menu.tampilkan(budaya)



# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "📐 Media Pembelajaran Matematika SMA — Fase E & F"
)
