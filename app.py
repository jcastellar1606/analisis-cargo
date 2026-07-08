import streamlit as st
import os
from groq import Groq

# Configuración de la página
st.set_page_config(page_title="JobArchitect SURA", layout="wide")
st.title("🏢 JobArchitect: Análisis de Cargos Inteligente")

# 1. Configuración de la interfaz (Sidebar)
with st.sidebar:
    st.header("Configuración del Cargo")
    cargo = st.text_input("Nombre del cargo")
    area = st.selectbox("Área", ["Seguros", "Tecnología", "Finanzas", "Riesgos", "Talento Humano"])
    generar = st.button("Generar Perfil con IA")

# 2. Lógica del botón
if generar and cargo:
    api_key = st.secrets.get("GROQ_API_KEY")
    if not api_key:
        st.error("❌ Error: Configura la GROQ_API_KEY en los Secrets de Streamlit.")
    else:
        with st.spinner('La IA está analizando el cargo...'):
            try:
                client = Groq(api_key=api_key)
                prompt_sistema = f"""Eres un experto en Recursos Humanos para SURA.
                Crea un análisis de cargo profesional para '{cargo}' en el área de '{area}'.
                Entrega el resultado en formato Markdown con: Misión, 3 Funciones, 3 Hard Skills y 3 Soft Skills."""
                
                response = client.chat.completions.create(
                    messages=[{"role": "user", "content": prompt_sistema}],
                    model="llama-3.3-70b-versatile", # <--- ESTE es el modelo activo y estable ahora
                )
                
                st.markdown(response.choices[0].message.content)
                st.success("✅ Perfil generado con éxito.")
                
            except Exception as e:
                st.error(f"🚨 Error de conexión: {e}")

st.divider()
st.caption("Herramienta desarrollada para SURA - Desafío Talento 2024")
