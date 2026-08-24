import streamlit as st
from summa import summarizer

# 1. Configuración de la página
st.set_page_config(
    page_title="Resumiendo - Síntesis de textos en castellano", 
    page_icon="✂️",
    layout="centered"
)

# 2. Estilo minimalista personalizado compatible con modo claro y oscuro
st.markdown("""
<style>
    /* Asegurar que las cajas de texto tengan bordes limpios */
    .stTextArea textarea {
        border-radius: 8px;
    }
    
    /* Botón de acción con estilo sólido y texto siempre visible */
    .stButton > button {
        background-color: #2D3748;
        color: #FFFFFF !important;
        border-radius: 6px;
        padding: 0.5rem 1.8rem;
        border: none;
        font-weight: 500;
        transition: all 0.2s ease;
    }
    .stButton > button:hover {
        background-color: #1A202C;
        color: #FFFFFF !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. Encabezado con Tooltip que explica el origen y propósito
st.title(
    "✂️ Resumiendo",
    help=(
        "Herramienta interactiva de procesamiento del lenguaje natural (PLN) que aplica"
        " algoritmos de resumen extractivo (TextRank) para identificar y extraer las"
        " oraciones clave de un texto en español."
    )
)
st.write(
    "Una aplicación web para realizar resúmenes de textos en castellano. "
    "Por defecto, los resúmenes tendrán aproximadamente un **20%** de la longitud del original. "
    "Para que la aplicación funcione correctamente, se recomienda que los textos tengan una longitud **superior a 100 palabras**."
)

st.write("---")

# 4. Formulario de entrada con placeholder limpio
texto_usuario = st.text_area(
    label="Pega el texto aquí:",
    value="",
    placeholder="Introduce o pega aquí el texto en castellano que deseas resumir (mínimo recomendado: 100 palabras)...",
    height=220
)

# Contador orientativo de palabras
num_palabras = len(texto_usuario.strip().split()) if texto_usuario.strip() else 0
if num_palabras > 0:
    st.caption(f"Palabras detectadas: **{num_palabras}**")

# 5. Ajuste del ratio con tooltip nativo (táctil y escritorio)
ratio_seleccionado = st.slider(
    label="Ratio de compresión",
    min_value=0.1,
    max_value=0.5,
    value=0.2,
    step=0.05,
    help="Define la fracción del texto que se mantendrá en el resumen. Por ejemplo, 0.2 equivale al 20% del texto original."
)

# 6. Botón de acción y ejecución
if st.button("Enviar"):
    if not texto_usuario.strip():
        st.warning("⚠️ Por favor, pega algún texto antes de pulsar en Enviar.")
    elif num_palabras < 30:
        st.warning("⚠️ El texto es demasiado corto para extraer oraciones representativas. Introduce un texto más extenso (preferiblemente más de 100 palabras).")
    else:
        with st.spinner("Generando resumen..."):
            resumen_generado = summarizer.summarize(
                texto_usuario, 
                ratio=ratio_seleccionado, 
                language='spanish'
            )
            
            if resumen_generado:
                st.write("### Resumen:")
                st.info(resumen_generado)
            else:
                st.error("No se ha podido extraer un resumen con este texto y ratio. Prueba a aumentar el ratio de compresión o a introducir un texto con más párrafos.")
