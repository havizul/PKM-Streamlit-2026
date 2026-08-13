import streamlit as st

from data.menu import (
    MENU_UTAMA,
    FASE_E,
    FASE_F_UMUM,
    FASE_F_LANJUT,
    MEDIA_PEMBELAJARAN
)


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
# MENU UTAMA HORIZONTAL
# ============================================================

menu_utama = st.radio(
    "Menu Utama",
    MENU_UTAMA,
    horizontal=True,
    label_visibility="collapsed"
)

st.session_state.halaman = menu_utama


# ============================================================
# SIDEBAR
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

        with st.expander(
            "📘 FASE E — Kelas X",
            expanded=True
        ):

            for item in FASE_E:

                if st.button(
                    item,
                    key=f"fase_e_{item}",
                    use_container_width=True
                ):
                    st.session_state.materi = item

        # ----------------------------------------------------
        # FASE F UMUM
        # ----------------------------------------------------

        with st.expander(
            "📗 FASE F — Umum (Kelas XI & XII)",
            expanded=False
        ):

            #for item in FASE_F_UMUM:

            #    if st.button(
            #        item,
            #        key=f"fase_f_umum_{item}",
            #        use_container_width=True
            #    ):
            #        st.session_state.materi = item


            for item in FASE_F_UMUM:
    
            st.sidebar.markdown(
                f"""
                <a href="?menu={item}" target="_self"
                   style="
                       display: block;
                       width: 100%;
                       padding: 10px 14px;
                       margin: 4px 0;
                       background-color: #E8F0FE;
                       color: #1A73E8;
                       text-decoration: none;
                       border-radius: 6px;
                       font-weight: 500;
                       box-sizing: border-box;
                   ">
                   {item}
                </a>
                """,
                unsafe_allow_html=True
            )
    
        # ----------------------------------------------------
        # FASE F LANJUT
        # ----------------------------------------------------

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


# ============================================================
# SIDEBAR MEDIA PEMBELAJARAN
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
# HALAMAN MATERI
# ============================================================

elif menu_utama == "📚 Materi Matematika":

    materi = st.session_state.materi

    st.header(f"📖 {materi}")

    st.divider()

    st.info(
        f"Materi **{materi}** akan ditampilkan dari "
        "file materi pada tahap berikutnya."
    )


# ============================================================
# HALAMAN MEDIA PEMBELAJARAN
# ============================================================

elif menu_utama == "🎓 Media Pembelajaran":

    media = st.session_state.media

    st.header("🎓 Media Pembelajaran")

    st.divider()

    st.info(
        f"Media pembelajaran **{media}** akan dikembangkan "
        "pada tahap berikutnya."
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "📐 Media Pembelajaran Matematika SMA — Fase E & F"
)
