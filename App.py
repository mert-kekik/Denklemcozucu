import streamlit as st
from PIL import Image
from pix2tex.cli import LatexOCR
from latex2sympy2 import latex2sympy
import sympy
st.title("Denklem çözücü")
AI=LatexOCR()
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
	
