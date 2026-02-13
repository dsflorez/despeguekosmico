import streamlit as st
import random
import time

# Inyectamos el CSS con el nombre de parámetro correcto
st.markdown("""
    <style>
    .stApp {
        background-color: #1A493A; /* Verde Profundo */
    }
    h1, h2, h3, p, span, label {
        color: #E5D076 !important; /* Crema */
    }
    div.stButton > button {
        background-color: #E5D076 !important;
        color: #1A493A !important;
        font-weight: bold;
        border-radius: 15px;
        border: none;
    }
    </style>
""", unsafe_allow_html=True) # <-- CORRECCIÓN AQUÍ

st.title("🚀 DESPEGUE KÓSMICO")
st.subheader("Cerveza Artesanal Cannábica")

# Input para el comercial
cajas = st.number_input("Cajas de 24 unidades vendidas:", min_value=1, step=1)

if st.button("¡QUE DESPEGUE ESTA CHIMBA!"):
    with st.spinner('Calculando órbita...'):
        time.sleep(1.5)
    
    # Lógica de planetas y premios
    resultado = random.randint(1, 6)
    planetas = {
        1: ("Tierra 🌍", "+1 Pola", "¡Breve, mor! Una Urano pa' la sed."),
        2: ("Marte 🔴", "+2 Polas", "¡Melo! El margen va subiendo."),
        3: ("Júpiter 🟠", "+3 Polas", "¡Ufff, qué chimba! Coronó el trío."),
        4: ("Saturno 🪐", "+2 Polas + Merch", "¡Elegancia! Portavasos nuevos pal' parche."),
        5: ("Urano 💎", "+2 Polas + Vaso", "¡Llegó a casa! El vaso oficial es suyo."),
        6: ("Neptuno 🔵", "+3 Polas + Kit", "¡CORONÓ EL SISTEMA! Usted es el propio patrón.")
    }
    
    planeta, premio, mensaje = planetas[resultado]
    
    st.balloons()
    st.header(f"¡Llegaste a {planeta}!")
    st.success(f"PREMIO: {premio}")
    
    # Mostramos el mockup de la pola
    st.image("pola.png", width=400)
    st.info(mensaje)
