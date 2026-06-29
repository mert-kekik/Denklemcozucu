import os
import streamlit as st
from PIL import Image
from pix2tex.cli import LatexOCR
from latex2sympy2 import latex2sympy
import sympy

os.environ["HOME"] = "/tmp"
st.title("Denklem çözücü")



@st.cache_resource
def modeli_yukle():
    return LatexOCR()

AI = modeli_yukle()

photo=st.camera_input("denklemin fotoğrafını çekin")
if photo is not None :
	st.success("fotoğraf alındı")
	st.image(photo)
	edited_photo=Image.open(photo)
	denklem_metni=AI(edited_photo)
	st.latex(denklem_metni)
	try:
		mat_ifade=latex2sympy(denklem_metni)
		cozum=sympy.solve(mat_ifade)
		st.success(cozum)
	except Exception as e :
		st.error("denklem hatalı lütfen tekrar yükleyin")
	
	
