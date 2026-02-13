import streamlit as st
import random
import time

# Configuración de marca
st.set_page_config(page_title="Área Kósmica - Despegue", layout="centered")

# Inyección de CSS con máxima prioridad
st.markdown("""
    <style>
    /* Fondo de la App */
    .stApp { 
        background-color: #1A493A !important; 
    }
    
    /* Forzar color de todos los textos generales */
    h1, h2, h3, p, span, label, .stMarkdown { 
        color: #E5D076 !important; 
    }

    /* BOTÓN: Aquí es donde forzamos la visibilidad de la letra */
    div.stButton > button {
        background-color: #E5D076 !important; /* Fondo Crema */
        color: #1A493A !important;           /* Texto Verde Oscuro */
        font-weight: 900 !important;          /* Letra extra negrita */
        font-size: 24px !important;           /* Tamaño grande */
        text-transform: uppercase !important; /* Todo en mayúsculas */
        border-radius: 12px !important;
        border: 3px solid #E5D076 !important;
        height: 80px !important;
        width: 100% !important;
        display: block !important;
    }

    /* Efecto al pasar el mouse para que el comercial sepa que hizo clic */
    div.stButton > button:hover {
        background-color: #FFFFFF !important;
        color: #1A493A !important;
        border-color: #FFFFFF !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🚀 DESPEGUE KÓSMICO")

# Centrar el logo circular
col1, col2, col3 = st.columns([1,2,1])
with col2:
    try:
        st.image("logo.png", width=150)
    except:
        st.write("🌌 **ÁREA KÓSMICA**")

st.write("Un sabor de otro planeta.")

# Control de ventas en COP
cajas = st.number_input("Cajas:", min_value=1, step=1)

if st.button("¡QUE DESPEGUE ESTe PARCHE!"):
    contenedor_animacion = st.empty()
    ruta_espacial = ["Tierra 🌍", "Marte 🔴", "Júpiter 🟠", "Saturno 🪐", "Urano 💎", "Neptuno 🔵"]
    resultado_idx = random.randint(0, 2)

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
        3: ("Saturno 🪐", "4 Polas + Merch", "¡Elegancia! Portavasos nuevos."),
        4: ("Urano 💎", "5 Polas + Vaso", "¡Llegó a casa! Vaso oficial ÁK."),
        5: ("Neptuno 🔵", "6 Polas + Kit", "¡CORONÓ EL SISTEMA! El propio patrón.")
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
