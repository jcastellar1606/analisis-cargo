import streamlit as st
from openai import OpenAI

# Configuración de OpenAI
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="JobArchitect SURA", layout="wide")
st.title("🏢 JobArchitect: Análisis de Cargos Inteligente")

with st.sidebar:
    st.header("Configuración de Cargo")
    cargo = st.text_input("Nombre del cargo")
    departamento = st.selectbox("Área / Departamento", 
                                ["Seguros y Siniestros", "Innovación y Tecnología", 
                                 "Gestión Financiera", "Talento y Cultura", "Riesgos Corporativos"])
    
    objetivo = st.selectbox("Foco Estratégico", 
                            ["Transformación Digital y Analítica", "Optimización de la Experiencia del Cliente", 
                             "Crecimiento Sostenible y Mercado", "Eficiencia Operativa y Automatización"])
    
    generar = st.button("Generar Perfil con IA")

if generar and cargo:
    with st.spinner('Construyendo el perfil ideal...'):
        prompt = f"""Crea un análisis de cargo profesional para el puesto de '{cargo}' 
        dentro del departamento de '{departamento}'. 
        El foco estratégico es: '{objetivo}'.
        
        Por favor, entrega:
        1. Misión del cargo (en una frase impactante).
        2. Funciones principales (lista de 3 elementos).
        3. Hard Skills (3 habilidades técnicas necesarias).
        4. Soft Skills (3 competencias humanas clave).
        """
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        
        st.markdown("---")
        st.markdown(response.choices[0].message.content)
        st.success("Perfil generado con éxito.")
