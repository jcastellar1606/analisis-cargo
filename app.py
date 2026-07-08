import streamlit as st
import os
from groq import Groq

# 1. Configuración de la interfaz (Sidebar)
with st.sidebar:
    st.header("Configuración")
    cargo = st.text_input("Nombre del cargo")
    area = st.selectbox("Área", ["Seguros", "Tecnología", "Finanzas", "Riesgos"])
    generar = st.button("Generar Perfil IA") # <--- AQUÍ se define 'generar'

# 2. Título principal
st.title("🏢 JobArchitect: Análisis de Cargos")

# 3. Lógica del botón (ahora 'generar' sí existe)
if generar and cargo:
    api_key = st.secrets.get("GROQ_API_KEY")
    if not api_key:
        st.error("Configura la GROQ_API_KEY en los Secrets.")
    else:
        client = Groq(api_key=api_key)
        with st.spinner('Construyendo perfil...'):
            try:
                prompt = f"Crea un perfil profesional para el cargo '{cargo}' en el área de '{area}'. Incluye Misión, 3 funciones, 3 hard skills y 3 soft skills."
                chat_completion = client.chat.completions.create(
                    messages=[{"role": "user", "content": prompt}],
                    model="llama3-8b-8192",
                )
                st.markdown(chat_completion.choices[0].message.content)
            except Exception as e:
                st.error(f"Error de conexión: {e}")
