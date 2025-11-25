import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Diagnóstico M360", page_icon="📊", layout="wide")

# --- ESTILOS VISUALES (TU MARCA) ---
st.markdown("""
    <style>
    .main {background-color: #f5f7f9;}
    h1 {color: #2c3e50;}
    .stButton>button {background-color: #d35400; color: white; border-radius: 5px;}
    </style>
    """, unsafe_allow_html=True)

# --- ENCABEZADO ---
st.title("📊 Plataforma de Diagnóstico Estratégico M360")
st.markdown("### Inteligencia de Negocios para Pymes y Startups")
st.write("Complete los módulos a continuación para que nuestro sistema M360 analice la salud de su organización basándose en el Cuadro de Mando Integral.")
st.markdown("---")

# --- BARRA LATERAL (SIDEBAR) ---
with st.sidebar:
    # Logo simulado (puedes cambiar este link por el de tu logo real más adelante)
    st.image("https://www.management360.com.ar/wp-content/uploads/2021/04/logo-m360.png", width=200)
    st.header("Panel de Control")
    st.info("Este diagnóstico analiza 4 pilares clave de su empresa.")
    cliente = st.text_input("Nombre de su Empresa", "Mi Empresa S.A.")
    rol = st.selectbox("Su Rol", ["Dueño / Gerente General", "Mando Medio / Jefe", "Operativo"])

# --- LÓGICA DE PREGUNTAS (LOS 4 PILARES) ---

# Creamos pestañas para que sea ordenado
tab1, tab2, tab3, tab4 = st.tabs(["💰 Financiero", "⚙️ Procesos", "👥 Clientes", "🚀 Aprendizaje"])

scores = {"Financiero": 0, "Procesos": 0, "Clientes": 0, "Aprendizaje": 0}

with tab1:
    st.header("Pilar Financiero & Estratégico")
    st.write("Objetivo: Rentabilizar")
    
    f1 = st.radio("1. ¿Dispone hoy de un Estado de Resultados mensual confiable?", 
                  ["Sí, lo reviso mensualmente.", "Lo tengo, pero llega tarde o no lo entiendo.", "No, me manejo por saldo de caja/banco."])
    
    f2 = st.radio("2. ¿Están separadas las cuentas de la empresa de las personales?", 
                  ["Totalmente separadas.", "Mezcladas ocasionalmente.", "Todo sale de la misma bolsa."])
    
    # Lógica de Puntos (Simple para el MVP)
    if f1 == "Sí, lo reviso mensualmente.": scores["Financiero"] += 50
    elif f1 == "Lo tengo, pero llega tarde o no lo entiendo.": scores["Financiero"] += 25
    
    if f2 == "Totalmente separadas.": scores["Financiero"] += 50
    elif f2 == "Mezcladas ocasionalmente.": scores["Financiero"] += 25

with tab2:
    st.header("Pilar de Procesos Internos")
    st.write("Objetivo: Organizar y Optimizar")
    
    p1 = st.radio("1. ¿Cómo fluye la información entre áreas (Ventas -> Operaciones)?", 
                  ["Fluida y documentada.", "A veces se pierde info clave.", "Caótica, depende de la memoria."])
    
    p2 = st.radio("2. ¿Cuál es la principal causa de retrasos hoy?", 
                  ["No solemos tener retrasos.", "Cambios de último momento del cliente.", "Falta de materiales o herramientas.", "Errores de comunicación interna."])
    
    if p1 == "Fluida y documentada.": scores["Procesos"] += 50
    elif p1 == "A veces se pierde info clave.": scores["Procesos"] += 25
    
    if p2 == "No solemos tener retrasos.": scores["Procesos"] += 50
    elif p2 == "Cambios de último momento del cliente.": scores["Procesos"] += 30

with tab3:
    st.header("Pilar de Clientes")
    st.write("Objetivo: Satisfacción y Ventas")
    
    c1 = st.radio("1. ¿Miden la satisfacción del cliente formalmente?", 
                  ["Sí, encuestas post-venta.", "Informalmente (si no se quejan, está bien).", "No medimos."])
    
    c2 = st.radio("2. ¿Tienen un proceso de ventas predecible?", 
                  ["Sí, tenemos embudo y CRM.", "Depende de la habilidad del vendedor.", "Esperamos que el cliente llame."])
    
    if c1 == "Sí, encuestas post-venta.": scores["Clientes"] += 50
    elif c1 == "Informalmente (si no se quejan, está bien).": scores["Clientes"] += 25
    
    if c2 == "Sí, tenemos embudo y CRM.": scores["Clientes"] += 50
    elif c2 == "Depende de la habilidad del vendedor.": scores["Clientes"] += 25

with tab4:
    st.header("Pilar de Aprendizaje y Cultura")
    st.write("Objetivo: Sostenibilidad y Equipo")
    
    a1 = st.radio("1. ¿El equipo tiene roles y responsabilidades claros?", 
                  ["Sí, manuales de puesto escritos.", "Se sabe de palabra.", "Es confuso, todos hacen todo."])
    
    a2 = st.radio("2. Clima laboral y herramientas:", 
                  ["Buen clima y herramientas ordenadas.", "Prisa constante ('apagar incendios').", "Desorden y falta de herramientas."])
    
    if a1 == "Sí, manuales de puesto escritos.": scores["Aprendizaje"] += 50
    elif a1 == "Se sabe de palabra.": scores["Aprendizaje"] += 25
    
    if a2 == "Buen clima y herramientas ordenadas.": scores["Aprendizaje"] += 50
    elif a2 == "Prisa constante ('apagar incendios').": scores["Aprendizaje"] += 25

st.markdown("---")

# --- BOTÓN DE GENERAR REPORTE ---
if st.button("GENERAR DIAGNÓSTICO M360"):
    
    st.success(f"Diagnóstico completado para: {cliente}")
    
    # 1. VISUALIZACIÓN (RADAR CHART TIPO CMI)
    categories = list(scores.keys())
    values = list(scores.values())
    
    fig = go.Figure(data=go.Scatterpolar(
      r=values,
      theta=categories,
      fill='toself',
      name=cliente
    ))
    fig.update_layout(
      polar=dict(
        radialaxis=dict(visible=True, range=[0, 100])
      ),
      showlegend=False,
      title="Su Cuadro de Mando Integral M360"
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # 2. ANÁLISIS AUTOMÁTICO (IA SIMULADA)
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🚨 Áreas Críticas (Rojo)")
        for area, puntaje in scores.items():
            if puntaje < 50:
                st.error(f"**{area} ({puntaje}/100):**")
                if area == "Financiero":
                    st.write("• Usted está 'volando a ciegas'. Sin un Estado de Resultados por lo percibido, no puede tomar decisiones reales.")
                    st.write("• **Recomendación M360:** Implementar separación de cuentas Dumit/Krawi urgente.")
                elif area == "Procesos":
                    st.write("• La comunicación informal está costando dinero en retrabajos.")
                    st.write("• **Recomendación M360:** Digitalizar la orden de pedido para evitar 'teléfono descompuesto'.")
                elif area == "Aprendizaje":
                    st.write("• Cultura de 'incendio'. La falta de roles claros genera dependencia del dueño.")
    
    with col2:
        st.subheader("✅ Fortalezas y Siguientes Pasos")
        st.write("Basado en sus respuestas, hemos generado su **Plan de Ruta Preliminar**.")
        st.info("Para implementar estas soluciones y pasar de la estrategia a la ejecución, agende su sesión de devolución con nuestros socios.")
        
        # Call to Action
        st.markdown(f"""
        <div style="background-color: #d4edda; padding: 10px; border-radius: 5px; border: 1px solid #c3e6cb;">
            <h4 style="color: #155724; margin:0;">🚀 Próximo paso: Ejecución</h4>
            <p>¿Quiere que Management360 implemente este tablero en su empresa?</p>
            <a href="https://www.management360.com.ar/contacto" target="_blank"><strong>Contactar ahora</strong></a>
        </div>
        """, unsafe_allow_html=True)
