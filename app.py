import streamlit as st
import streamlit.components.v1 as components

# Configuración básica de la página web
st.set_page_config(page_title="Simulador Mundial 2026", layout="wide")

# Intentar leer el archivo HTML que subiste previamente
try:
    with open("index.html", "r", encoding="utf-8") as f:
        html_code = f.read()
    
    # Renderizar el HTML dentro de la interfaz de Streamlit
    components.html(html_code, height=1000, scrolling=True)
    
except FileNotFoundError:
    st.error("Error: No se encontró el archivo index.html. Asegúrate de haberlo subido al mismo repositorio.")
