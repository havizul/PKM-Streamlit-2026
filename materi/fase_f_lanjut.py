import streamlit as st
import pandas as pd
import numpy as np
import math



def tampilkan(materi):
    if materi == "Polinomial":
        polinomial()

    elif materi == "Matriks":
        matriks()

    elif materi == "Transformasi geometri":
        transformasi_geometri()

    elif materi == "Trigonometri":
        trigonometri()

    elif materi == "Pemodelan fungsi":
        pemodelan_fungsi()

    elif materi == "Vektor":
        vektor()

    elif materi == "Irisan kerucut (lingkaran & elips)":
        irisan_kerucut()

    elif materi == "Distribusi peluang (binom & normal)":
        distribusi_peluang()

    elif materi == "Limit Fungsi (Tambahan)":
        limit_fungsi()

    elif materi == "Turunan & Penerapannya (Tambahan)":
        turunan()

    elif materi == "Integral (Tambahan)":
        integral()

    else:
      pass
