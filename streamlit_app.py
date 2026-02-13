import streamlit as st
import random
import time

# Configuración de página
st.set_page_config(page_title="Área Kósmica - Despegue", layout="centered")

# CSS Corregido y Optimizado
st.markdown("""
    <style>
    .stApp {
        background-color: #1A493A; /* Verde Profundo */
    }
    h1, h2, h3, p, span, label {
        color: #E5D076 !important; /* Crema */
    }
    /* Estilo del Botón - Forzando visibilidad del texto */
    div.stButton > button {
        background-color: #E5D076 !important;
        color: #1A493A !important; /* Texto en verde oscuro para contraste */
        font-weight: 900 !important;
        font-size: 20px !important;
        border-radius: 10px;
        border: 2px solid #E5D076;
        height: 3em;
        width: 100%;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: #304244 !important; /* Cambio a Gris Azulado al pasar el mouse */
        color: #E5D076 !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🚀 DESPEGUE KÓSMICO")
st.write("¿Pola o miedo? Vamos al espacio.")

# Entrada del comercial para cajas de 24 polas
cajas = st.number_input("Cajas de 24 vendidas:", min_value=1, step=1)

if st.button("¡QUE DESPEGUE ESTA CHIMBA!"):
    # Definición de la ruta espacial
    ruta = ["Tierra 🌍", "Marte 🔴", "Júpiter 🟠", "Saturno 🪐", "Urano 💎", "Neptuno 🔵"]
    
    # Lógica de niveles (1 a 6)
    resultado_idx = random.randint(0, 5) 
    
    # Animación gráfica de "Saltos"
    contenedor_viaje = st.empty()
    for i in range(resultado_idx + 1):
        planeta_actual = ruta[i]
        contenedor_viaje.markdown(f"### 🚀 El cohete está saltando a: **{planeta_actual}**")
        time.sleep(0.8) # Pausa para crear tensión
    
    # Datos de premios
    premios = {
        0: ("Tierra 🌍", "+1 Pola", "¡Breve, mor! Una Urano pa' la sed."),
        1: ("Marte 🔴", "+2 Polas", "¡Melo! El margen va subiendo."),
        2: ("Júpiter 🟠", "+3 Polas", "¡Ufff, qué chimba! Coronó el trío."),
        3: ("Saturno 🪐", "+2 Polas + Merch", "¡Elegancia! Portavasos nuevos."),
        4: ("Urano 💎", "+2 Polas + Vaso", "¡Llegó a casa! Vaso oficial ÁK."),
        5: ("Neptuno 🔵", "+3 Polas + Kit", "¡CORONÓ EL SISTEMA! El propio patrón.")
    }
    
    planeta, premio, mensaje = premios[resultado_idx]
    
    # RESULTADO FINAL
    st.balloons()
    st.header(f"📍 Aterrizaje en: {planeta}")
    st.subheader(f"🎁 RECOMPENSA: {premio}")
    
    # Imagen de la pola Urano
    try:
        st.image("pola.png", width=450)
    except:
        st.error("No se encontró la imagen 'mock up pola final.jpg'")
        
    st.success(mensaje)
