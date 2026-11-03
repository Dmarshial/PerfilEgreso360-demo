import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="PerfilEgreso 360", page_icon="🎯", layout="wide")

st.markdown("""
<style>
.stApp { background-color: #12181f; color: #f4efe3; }
h1, h2, h3 { font-family: 'Oswald', sans-serif; }
</style>
""", unsafe_allow_html=True)

st.title("🎯 PerfilEgreso 360")
st.caption("Demo pública · Visualiza el logro del Perfil de Egreso")

# Demo data
np.random.seed(42)
lineas = ["Evaluación y diagnóstico", "Prescripción del ejercicio", "Intervención profesional",
          "Investigación aplicada", "Gestión", "Comunicación y liderazgo"]
n = 40
logros = np.clip(np.random.normal(78, 12, (n, len(lineas))), 40, 98)

df = pd.DataFrame(logros, columns=lineas)
df["estudiante"] = [f"EST-{i:03d}" for i in range(1, n+1)]
df["cohorte"] = np.random.choice(["2023", "2024", "2025"], n)

meta = st.sidebar.slider("Meta institucional (%)", 70, 95, 85)

st.sidebar.success("Datos de demostración cargados")

tab1, tab2, tab3 = st.tabs(["Ficha Individual", "Cohorte", "Carrera"])

with tab1:
    est = st.selectbox("Estudiante", df["estudiante"])
    row = df[df["estudiante"] == est].iloc[0]
    logro_global = row[lineas].mean()
    c1, c2 = st.columns([1, 2])
    with c1:
        st.metric("Logro perfil", f"{logro_global:.0f}%")
        nivel = "Estratégico" if logro_global >= 90 else "Integrado Alto" if logro_global >= 80 else "En Desarrollo" if logro_global >= 70 else "Crítico"
        st.metric("Nivel", nivel)
    with c2:
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(r=row[lineas].tolist() + [row[lineas].iloc[0]], theta=lineas + [lineas[0]], fill='toself', name='Logro'))
        fig.add_trace(go.Scatterpolar(r=[meta]*7, theta=lineas + [lineas[0]], line=dict(dash='dash'), name='Meta'))
        fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 100])), showlegend=True, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='#f4efe3')
        st.plotly_chart(fig, use_container_width=True)

with tab2:
    coh = st.selectbox("Cohorte", sorted(df["cohorte"].unique()))
    sub = df[df["cohorte"] == coh]
    prom = sub[lineas].mean()
    st.metric("Logro promedio cohorte", f"{prom.mean():.0f}%")
    fig2 = go.Figure()
    fig2.add_trace(go.Scatterpolar(r=prom.tolist() + [prom.iloc[0]], theta=lineas + [lineas[0]], fill='toself'))
    fig2.update_layout(polar=dict(radialaxis=dict(range=[0, 100])), paper_bgcolor='rgba(0,0,0,0)', font_color='#f4efe3')
    st.plotly_chart(fig2, use_container_width=True)

with tab3:
    prom_c = df[lineas].mean()
    c1, c2, c3 = st.columns(3)
    c1.metric("Logro global", f"{prom_c.mean():.0f}%")
    c2.metric("Meta", f"{meta}%")
    brechas = (meta - prom_c).clip(lower=0)
    c3.metric("Brechas críticas", int((brechas >= 20).sum()))
    st.bar_chart(brechas)

st.info("Esta es la versión demo pública. Sube tus actas reales en la versión completa para análisis institucional.")
