import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Simulador Mundial 2026", layout="wide")

try:
with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()
components.html(html_code, height=1000, scrolling=True)
except FileNotFoundError:
st.error("Error: No se encontró el archivo index.html. Asegúrate de haberlo subido al mismo repositorio.")
