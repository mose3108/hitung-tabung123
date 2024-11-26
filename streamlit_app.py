import streamlit as st
import math

st.title("Menghitung :blue[Volume Tabung] :rocket:")

r = st.number_input("Masukan jari-jari(cm): ",0)
t = st.number_input("Masukan Tinggi(cm): ",0)

if st.button("Hitung volume",type="primary"):
  V = math.pi*(r**2)*t
  st.success(f'Volume tapbung adalah {v:.2f}')

