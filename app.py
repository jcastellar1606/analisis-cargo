import streamlit as st
from groq import Groq

# Configuración de Groq
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.set_page_config(page_title="JobArchitect IA", layout="wide")
st.title("🏢 JobArchitect: Análisis de Cargos Inteligente")

with st.sidebar:
    cargo = st.text_input("Nombre del cargo")
    area = st.selectbox("Área", ["Seguros", "Tecnología", "Finanzas", "Riesgos"])
    generar = st.button("Generar Perfil IA")

if generar and cargo:
    with st.spinner('Generando perfil con Llama 3...'):
        prompt = f"Crea un perfil profesional para el cargo '{cargo}' en el área de '{area}'. Incluye misión, 3 funciones, 3 hard skills y 3 soft skills. Sé preciso y profesional."
        
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama3-8b-8192",
        )
        
        st.markdown(chat_completion.choices[0].message.content)
