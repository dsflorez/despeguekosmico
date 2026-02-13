import streamlit as st
import random
import time

# Configuración de marca basada en el Manual
st.set_page_config(page_title="Área Kósmica - Despegue", layout="centered")

# CSS para aplicar colores corporativos
st.markdown(f"""
    <style>
    .stApp {{
        background-color: #1A493A; /* Verde Profundo Pantone 3308 C */
        color: #E5D076; /* Crema Pantone 134 C */
    }}
    .stButton>button {{
        background-color: #E5D076;
        color: #1A493A;
        font-family: 'Arial Black';
        border-radius: 20px;
    }}
    </style>
    """, unsafe_allow_box_with_html=True)

st.title("🚀 DESPEGUE KÓSMICO")
st.subheader("Un sabor de otro planeta")

# Entrada del Comercial
cajas = st.number_input("Cajas compradas (24 polas c/u):", min_value=1, step=1)
if st.button("¡QUE DESPEGUE ESTA CHIMBA!"):
    with st.status("Calculando trayectoria sideral...", expanded=True) as status:
        time.sleep(1)
        st.write("Tanqueando con Urano...")
        time.sleep(1)
        st.write("Saliendo de la atmósfera...")
        
    # Lógica de niveles
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
    st.header(f"PREMIO: {premio}")
    # Aquí cargarías la imagen 'mock up pola final.jpg' que subiste
    st.image("pola.png", width=300) 
    st.success(mensaje)
