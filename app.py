import streamlit as st
from groq import Groq
import mistune

st.set_page_config(page_title="Análisis de Cargos Inteligente", layout="centered")

st.markdown("""
<style>
    @media print {
        .eczjsme14, .eczjsme18, .stAppDeployButton, #MainMenu,
        [data-testid="stSidebar"], [data-testid="stHeader"],
        [data-testid="stToolbar"], [data-testid="stDecoration"],
        [data-testid="stStatusWidget"], .st-emotion-cache-18ni7ap {
            display: none !important;
        }
        .stApp { margin: 0 !important; padding: 0 !important; }
        section.main { padding-top: 0 !important; }
        .stButton, [data-testid="stDownloadButton"],
        .stAlert, .st-emotion-cache-1mi3fwe { display: none !important; }
        .stMarkdown { display: block !important; }
        @page { margin: 1.5cm; }
    }
</style>
""", unsafe_allow_html=True)

st.title("🏢 Análisis de Cargos Inteligente")
st.markdown("Asistente experto de diseño organizacional.")

with st.sidebar:
    st.header("Configuración")
    cargo = st.text_input("Nombre del cargo", placeholder="Ej: Analista de Riesgos")
    area = st.selectbox("Área", ["Seguros", "Tecnología", "Finanzas", "Talento Humano"])
    nivel = st.selectbox("Nivel", ["", "Junior", "Intermedio", "Senior", "Líder"])
    btn_generar = st.button("Generar Análisis", type="primary", use_container_width=True)

if "historial" not in st.session_state:
    st.session_state.historial = []

@st.cache_data(ttl=3600, show_spinner=False)
def generar_perfil(cargo: str, area: str, nivel: str) -> str:
    api_key = st.secrets.get("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY no configurada en secrets")
    
    client = Groq(api_key=api_key)
    
    nivel_txt = f" con nivel {nivel}" if nivel else ""
    prompt = f"""Actúa como experto en diseño organizacional. Analiza el cargo '{cargo}' en el área de '{area}'{nivel_txt}.
    
    REGLAS DE FORMATO (Obligatorio):
    1. Usa H2 (##) para el título del cargo.
    2. Usa H3 (###) para cada sección (Misión, Funciones, Competencias Técnicas, Competencias Blandas).
    3. Para la Misión, usa una línea de texto normal debajo del título.
    4. Para las Funciones y Skills, usa lista numerada (1.) o viñetas (-).
    5. NO incluyas introducciones ni relleno. Ve directo al grano."""
    
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.3-70b-versatile",
    )
    return response.choices[0].message.content

if btn_generar:
    if not cargo.strip():
        st.warning("⚠️ Ingresa un nombre de cargo")
    else:
        with st.spinner('Construyendo perfil estratégico...'):
            try:
                contenido = generar_perfil(cargo.strip(), area, nivel)
                
                st.session_state.historial.insert(0, {
                    "cargo": cargo, "area": area, "nivel": nivel, "contenido": contenido
                })
                
                st.success("¡Perfil generado con éxito!")
                st.markdown("---")
                st.markdown(contenido)
                
                col1, col2 = st.columns(2)
                with col1:
                    st.download_button(
                        "📥 Descargar .md",
                        data=contenido,
                        file_name=f"{cargo.replace(' ', '_')}_{area}.md",
                        mime="text/markdown",
                        use_container_width=True
                    )
                with col2:
                    html_clean = f"""<!DOCTYPE html>
<html lang="es">
<head><meta charset="utf-8">
<title>{cargo} - {area}</title>
<style>
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    body {{ font-family: 'Segoe UI', Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 2cm; color: #1a1a1a; line-height: 1.6; }}
    h2 {{ color: #1f4e79; border-bottom: 2px solid #1f4e79; padding-bottom: 6px; margin: 30px 0 15px; font-size: 22px; }}
    h3 {{ color: #2e75b6; margin: 20px 0 10px; font-size: 17px; }}
    p {{ margin: 8px 0; }}
    ul, ol {{ margin: 8px 0 8px 25px; }}
    li {{ margin: 4px 0; }}
    strong {{ color: #1f4e79; }}
    .header {{ text-align: center; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px double #1f4e79; }}
    .header h1 {{ font-size: 24px; color: #1f4e79; }}
    .header p {{ color: #666; font-size: 14px; }}
    @media print {{ @page {{ margin: 1.5cm; }} body {{ padding: 0; }} }}
</style>
</head>
<body>
<div class="header">
    <h1>{cargo}</h1>
    <p>Área: {area} | Nivel: {nivel or 'No especificado'}</p>
</div>
{mistune.html(contenido)}
<p style="text-align:center;color:#999;font-size:11px;margin-top:40px;border-top:1px solid #ddd;padding-top:10px;">
    Generado por Análisis de Cargos Inteligente
</p>
</body>
</html>"""
                    st.download_button(
                        "🖨️ Vista para imprimir",
                        data=html_clean,
                        file_name=f"{cargo.replace(' ', '_')}_{area}.html",
                        mime="text/html",
                        use_container_width=True
                    )
                
            except Exception as e:
                st.error(f"🚨 Error: {e}")

if st.session_state.historial:
    with st.expander(f"📋 Historial ({len(st.session_state.historial)})", expanded=False):
        for i, h in enumerate(st.session_state.historial):
            st.caption(f"{h['cargo']} | {h['area']} | {h['nivel'] or '—'}")
            if st.button(f"Ver #{i+1}", key=f"hist_{i}"):
                st.markdown("---")
                st.markdown(h["contenido"])

st.divider()
st.caption("Gestión de Talento Humano • v2.0")
