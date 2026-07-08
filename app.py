import streamlit as st
import os
from groq import Groq

# Título Principal
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
                # IMPORTANTE: Hemos actualizado el modelo a 'llama3-8b-8192' que es el actual.
                client = Groq(api_key=api_key)
                prompt_sistema = f"""Eres un experto en Recursos Humanos y diseño organizacional para la empresa SURA.
                Tu tarea es crear un análisis de cargo profesional para el puesto de '{cargo}' en el área de '{area}'.
                
                El output debe ser SÓLO en formato Markdown con el siguiente esquema preciso:
                
                ### 🎯 Misión del Cargo
                [Una frase concisa]
                
                ### 📋 Funciones Principales
                1. [Función 1]
                2. [Función 2]
                3. [Función 3]
                
                ### 🛠️ Hard Skills (Técnicas)
                - [Habilidad 1]
                - [Habilidad 2]
                - [Habilidad 3]
                
                ### 🧠 Soft Skills (Comportamentales)
                - [Habilidad 1]
                - [Habilidad 2]
                - [Habilidad 3]
                """
                
                response = client.chat.completions.create(
                    messages=[
                        {"role": "system", "content": "Eres un asistente útil de RRHH."},
                        {"role": "user", "content": prompt_sistema}
                    ],
                    model="llama3-8b-8192", # Este modelo SÍ funciona actualmente en Groq
                    temperature=0.5, # Un poco más preciso
                )
                
                st.markdown(response.choices[0].message.content)
                st.success("✅ Perfil generado con éxito.")
                
            except Exception as e:
                st.error(f"🚨 Error crítico de conexión con Groq: {e}")
                st.info("Verifica que tu API Key en los Secrets de Streamlit sea la correcta.")

st.divider()
st.caption("Herramienta desarrollada para SURA - Desafío Talento 2024")
