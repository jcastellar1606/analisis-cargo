import streamlit as st
from groq import Groq

st.set_page_config(page_title="JobArchitect SURA", layout="centered")

# --- UI Limpia ---
st.title("🏢 JobArchitect: Análisis de Cargos")
st.markdown("Asistente de diseño organizacional para SURA.")

with st.sidebar:
    st.header("Configuración")
    cargo = st.text_input("Nombre del cargo", placeholder="Ej: Analista de Riesgos")
    area = st.selectbox("Área", ["Seguros", "Tecnología", "Finanzas", "Riesgos", "Talento Humano"])
    btn_generar = st.button("🚀 Generar Análisis")

# --- Lógica de IA (Directa) ---
if btn_generar and cargo:
    api_key = st.secrets.get("GROQ_API_KEY")
    client = Groq(api_key=api_key)
    
    with st.spinner('Construyendo perfil estratégico...'):
        try:
            prompt = f"Analiza el cargo '{cargo}' en el área de '{area}'. Estructura: Misión, 3 funciones, 3 Hard Skills, 3 Soft Skills."
            response = client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model="llama-3.3-70b-versatile",
            )
            
            # Resultado directo (sin expander)
            st.success("¡Perfil generado con éxito!")
            st.markdown("---")
            st.markdown(response.choices[0].message.content)
                
        except Exception as e:
            st.error("Error al conectar con la IA. Por favor verifica tu API Key.")

st.divider()
st.caption("Desarrollado para SURA - Desafío Talento 2024")
st.caption("Gestión del Talento Humano")
