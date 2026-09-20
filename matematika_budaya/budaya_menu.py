import streamlit as st


def tenun_motif():
    st.header("🧵 Tenun dan Motif Tradisional")
    st.info("Materi akan dikembangkan.")


def batik_geometri():
    st.header("🎨 Batik dan Pola Geometri")
    st.info("Materi akan dikembangkan.")


def rumah_tradisional():
    st.header("🏠 Rumah Tradisional")
    st.info("Materi akan dikembangkan.")


def arsitektur_kesultanan():
    st.header("🕌 Arsitektur Kesultanan")
    st.info("Materi akan dikembangkan.")


def bubu():
    st.header("🐟 Bubu dan Alat Tangkap Tradisional")
    st.info("Materi akan dikembangkan.")


def perahu():
    st.header("🛶 Perahu Tradisional")
    st.info("Materi akan dikembangkan.")


def geometri_budaya():
    st.header("📐 Geometri dalam Budaya")
    st.info("Materi akan dikembangkan.")


def statistika_masyarakat():
    st.header("📊 Statistika dalam Kehidupan Masyarakat")
    st.info("Materi akan dikembangkan.")


def matematika_ekonomi():
    st.header("💰 Matematika Ekonomi dan Budaya")
    st.info("Materi akan dikembangkan.")


def tampilkan(materi):

    if materi == "Tenun dan Motif Tradisional":
        tenun_motif()

    elif materi == "Batik dan Pola Geometri":
        batik_geometri()

    elif materi == "Rumah Tradisional":
        rumah_tradisional()

    elif materi == "Arsitektur Kesultanan":
        arsitektur_kesultanan()

    elif materi == "Bubu dan Alat Tangkap Tradisional":
        bubu()

    elif materi == "Perahu Tradisional":
        perahu()

    elif materi == "Geometri dalam Budaya":
        geometri_budaya()

    elif materi == "Statistika dalam Kehidupan Masyarakat":
        statistika_masyarakat()

    elif materi == "Matematika Ekonomi dan Budaya":
        matematika_ekonomi()
