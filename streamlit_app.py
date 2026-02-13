import streamlit as st
import random
import time

# Forzamos el estilo visual del Manual
st.markdown("""
    <style>
    .main { background-color: #1A493A; }
    .stMarkdown, h1, h2, h3, p { color: #E5D076 !important; }
    div.stButton > button {
        background-color: #E5D076 !important;
        color: #1A493A !important;
        font-weight: bold;
        border-radius: 15px;
        width: 100%;
    }
    </style>
""", unsafe_allow_box_with_html=True)

st.title("🚀 DESPEGUE KÓSMICO")
st.write("Herramienta exclusiva para Comerciales")

# Input de cajas (24 polas c/u)
cajas_pedidas = st.number_input("Cantidad de cajas:", min_value=1, value=1, step=1)

if st.button("¡QUE DESPEGUE ESTA CHIMBA!"):
    # Simulación de carga
    progreso = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        progreso.progress(i + 1)
    
    # Lógica de niveles (1 a 6)
    resultado = random.randint(1, 6)
    
    # Diccionario de premios ajustado al tope de 3 polas
    premios = {
        1: ("Tierra 🌍", "1 Pola", "¡Breve, mor! Una Urano pa' la sed."),
        2: ("Marte 🔴", "2 Polas", "¡Melo! El margen va subiendo."),
        3: ("Júpiter 🟠", "3 Polas", "¡Ufff, qué chimba! Coronó el trío."),
        4: ("Saturno 🪐", "2 Polas + Merch", "¡Elegancia! Portavasos nuevos pal' parche."),
        5: ("Urano 💎", "2 Polas + Vaso", "¡Llegó a casa! El vaso oficial es suyo."),
        6: ("Neptuno 🔵", "3 Polas + Kit", "¡CORONÓ EL SISTEMA! Usted es el propio patrón.")
    }
    
    nombre_planeta, regalo, frase = premios[resultado]
    
    # RESULTADO VISUAL
    st.balloons()
    st.header(f"¡Llegaste a {nombre_planeta}!")
    st.subheader(f"PREMIO: {regalo}")
    
    # Manejo de imagen con Try/Except para evitar el TypeError
    try:
        st.image("pola.jpg", caption="Urano: Un sabor de otro planeta", width=350)
    except Exception:
        st.warning("⚠️ No se encontró el archivo 'pola.jpg'. Asegúrate de que la imagen esté en la misma carpeta.")
    
    st.info(frase)
