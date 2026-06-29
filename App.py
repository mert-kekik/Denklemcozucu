import os
import streamlit as st
from PIL import Image

# İzin hatalarını aşmak için ortam yollarını /tmp dizinine yönlendiriyoruz
os.environ["HOME"] = "/tmp"
os.environ["XDG_CACHE_HOME"] = "/tmp"
os.environ["XDG_CONFIG_HOME"] = "/tmp"
os.environ["PIX2TEX_CHECKPOINT_DIR"] = "/tmp/pix2tex"

# Kütüphaneleri import ediyoruz
from pix2tex.cli import LatexOCR
from latex2sympy2 import latex2sympy
import sympy

st.title("Denklem çözücü")

@st.cache_resource
def modeli_yukle():
    # Modelin varsayılan olarak /tmp dizinini kullanmasını sağlıyoruz
    return LatexOCR()

AI = modeli_yukle()

photo = st.camera_input("denklemin fotoğrafını çekin")

if photo is not None:
    st.success("Fotoğraf alındı")
    st.image(photo)
    
    # Görüntüyü işle ve metne çevir
    edited_photo = Image.open(photo)
    denklem_metni = AI(edited_photo)
    
    st.latex(denklem_metni)
    
    # Denklem çözme kısmı
    try:
        mat_ifade = latex2sympy(denklem_metni)
        cozum = sympy.solve(mat_ifade)
        st.success(f"Çözüm: {cozum}")
    except Exception as e:
        st.error("Denklem hatalı veya okunamadı, lütfen tekrar çekin.")
