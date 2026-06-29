import os
# İzin hatalarını aşmak için en kritik ayarlar
os.environ["HOME"] = "/tmp"
os.environ["XDG_CACHE_HOME"] = "/tmp"
os.environ["XDG_CONFIG_HOME"] = "/tmp"
os.environ["PIX2TEX_CHECKPOINT_DIR"] = "/tmp/pix2tex"

import streamlit as st
from PIL import Image
from pix2tex.cli import LatexOCR
from latex2sympy2 import latex2sympy
import sympy

st.title("Denklem Çözücü")

@st.cache_resource
def modeli_yukle():
    # Klasörü biz oluşturuyoruz, kütüphane oluşturmaya çalışıp hata almasın
    os.makedirs("/tmp/pix2tex", exist_ok=True)
    return LatexOCR()

AI = modeli_yukle()

photo = st.camera_input("Denklemin fotoğrafını çekin")

if photo is not None:
    st.success("Fotoğraf alındı")
    st.image(photo)
    
    try:
        edited_photo = Image.open(photo)
        denklem_metni = AI(edited_photo)
        st.latex(denklem_metni)
        
        # Matematiksel çözüm
        mat_ifade = latex2sympy(denklem_metni)
        cozum = sympy.solve(mat_ifade)
        st.success(f"Çözüm: {cozum}")
        
    except Exception as e:
        st.error("Denklem okunamadı veya çözülemedi. Lütfen net bir fotoğraf çekin.")
