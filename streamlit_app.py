import streamlit as st
import random
import time

# Configuración de marca
st.set_page_config(page_title="Área Kósmica - Despegue", layout="centered")

# CSS Corporativo - Verde #1A493A y Crema #E5D076
st.markdown("""
    <style>
    .stApp { background-color: #1A493A; }
    h1, h2, h3, p, span, label { color: #E5D076 !important; }
    div.stButton > button {
        background-color: #E5D076 !important;
        color: #1A493A !important; 
        font-weight: 900 !important;
        font-size: 24px !important;
        border-radius: 12px;
        width: 100%;
        height: 3em;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🚀 DESPEGUE KÓSMICO")
st.write("Un sabor de otro planeta.")

# Control de ventas en COP
cajas = st.number_input("Cajas de 24 vendidas ($240.000 COP):", min_value=1, step=1)

if st.button("¡QUE DESPEGUE ESTA CHIMBA!"):
    contenedor_animacion = st.empty()
    ruta_espacial = ["Tierra 🌍", "Marte 🔴", "Júpiter 🟠", "Saturno 🪐", "Urano 💎", "Neptuno 🔵"]
    resultado_idx = random.randint(0, 5)

    # Simulación de vuelo gráfico
    for i in range(resultado_idx + 1):
        for frame in range(1, 12):
            estela = "." * frame
            contenedor_animacion.markdown(f"### 🚀{estela} Surcando hacia **{ruta_espacial[i]}**")
            time.sleep(0.06)
        time.sleep(0.3) 

    # Diccionario de premios
    premios = {
        0: ("Tierra 🌍", "1 Pola", "¡Breve, mor! Una Urano pa' la sed."),
        1: ("Marte 🔴", "2 Polas", "¡Melo! El margen va subiendo."),
        2: ("Júpiter 🟠", "3 Polas", "¡Ufff, qué chimba! Coronó el trío."),
        3: ("Saturno 🪐", "2 Polas + Merch", "¡Elegancia! Portavasos nuevos."),
        4: ("Urano 💎", "2 Polas + Vaso", "¡Llegó a casa! Vaso oficial ÁK."),
        5: ("Neptuno 🔵", "3 Polas + Kit", "¡CORONÓ EL SISTEMA! El propio patrón.")
    }
    
    planeta, premio, mensaje = premios[resultado_idx]
    
    # Resultado Final
    st.balloons()
    contenedor_animacion.header(f"📍 Aterrizaje: {planeta}")
    st.subheader(f"🎁 PREMIO: {premio}")
    
    # Imagen local pola.png
    try:
        st.image("pola.png", width=400)
    except:
        st.error("⚠️ No se encontró 'pola.png' en el repositorio.")
        
    st.success(mensaje)

    # Botón de reinicio para el comercial
    if st.button("Registrar otra venta"):
        st.rerun()
