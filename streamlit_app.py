import streamlit as st
import math,time


st.title("Menghitung :blue[Volume Tabung] :rocket:")

r = st.number_input("Masukan jari-jari(cm): ",0)
t = st.number_input("Masukan Tinggi(cm): ",0)

if st.button("Hitung volume",type="primary"):
  loading = st.progress(0)
  for i in range(100):
    time.sleep(0.01)
    loading.progress(i+1)
    
  V = math.pi*(r**2)*t
  st.success(f'Volume tabung adalah {V:.2f}')

