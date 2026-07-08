import streamlit as st
from groq import Groq

st.set_page_config(page_title="JobArchitect SURA", layout="centered")

# --- UI Mejorada ---
st.title("🏢 JobArchitect: Análisis de Cargos")
st.markdown("### Bienvenido al asistente de diseño organizacional de SURA.")
st.info("Utiliza la barra lateral para definir el perfil que deseas estructurar.")

with st.sidebar:
    st.header("Configuración")
    cargo = st.text_input("Nombre del cargo", placeholder="Ej: Analista de Riesgos")
    area = st.selectbox("Área", ["Seguros", "Tecnología", "Finanzas", "Riesgos", "Talento Humano"])
    btn_generar = st.button("🚀 Generar Análisis")

# --- Lógica de IA ---
if btn_generar and cargo:
    api_key = st.secrets.get("GROQ_API_KEY")
    client = Groq(api_key=api_key)
    
    with st.spinner('Construyendo perfil estratégico...'): # Visualmente más profesional
        try:
            prompt = f"Analiza el cargo '{cargo}' en el área de '{area}'. Estructura: Misión, 3 funciones, 3 Hard Skills, 3 Soft Skills."
            response = client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model="llama-3.3-70b-versatile",
            )
            
            # --- Presentación con Expanders ---
            st.success("¡Perfil generado con éxito!")
            with st.expander("Ver Análisis Completo", expanded=True):
                st.markdown(response.choices[0].message.content)
                
        except Exception as e:
            st.error("Error al conectar con la IA. Por favor verifica tu API Key.")

st.divider()
st.caption("Desarrollado para SURA - Innovación Talento Humano")
