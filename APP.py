import streamlit as st

# 1. DEFINICIÓN DEL CATÁLOGO (Arreglo de Registros/Diccionarios)
# Cada elemento en la lista actúa como un "Registro" con sus campos correspondientes.
if "catalogo" not in st.session_state:
    st.session_state.catalogo = [
        {
            "id_producto": "WPN-REB-01",
            "nombre": "Rebellion",
            "descripcion": "Espada demoniaca creada por el caballero oscuro legendario Sparda, con la capacidad de despertar el poder demoniaco latente.",
            "categoria": "Cuerpo a Cuerpo",
            "precio_orbes_rojos": 99999,
            "stock_disponible": 0,
            "requiere_poderes_demonio": True
        },
        {
            "id_producto": "WPN-EYI-02",
            "nombre": "Ebony & Ivory",
            "descripcion": "Pistolas semiautomáticas personalizadas para disparar ráfagas de energía espiritual a alta velocidad, creadas por la Armera legendaria Nell Goldstein",
            "categoria": "Arma de Fuego",
            "precio_orbes_rojos": 99999,
            "stock_disponible": 0,
            "requiere_poderes_demonio": False
        },
        {
            "id_producto": "WPN-ALA-03",
            "nombre": "Alastor",
            "descripcion": "Espada demoniaca que contiene la voluntad del demonio con el que comparte nombre. Esta posee poderes electricos y le otorga a su portador la capacidad de volar.",
            "categoria": "Cuerpo a Cuerpo",
            "precio_orbes_rojos": 50000,
            "stock_disponible": 1,
            "requiere_poderes_demonio": True
        },
        {
            "id_producto": "WPN-COA-04",
            "nombre": "Coyote-A",
            "descripcion": "Escopeta recortada de dos cañones con gran potencia de fuego.",
            "categoria": "Arma de Fuego",
            "precio_orbes_rojos": 35000,
            "stock_disponible": 5,
            "requiere_poderes_demonio": False
        },
        {
            "id_producto": "WPN-IFR-05",
            "nombre": "Ifrit",
            "descripcion": "Guanteletes con poder de las llamas procedentes del mismo Infierno.",
            "categoria": "Cuerpo a Cuerpo",
            "precio_orbes_rojos": 50000,
            "stock_disponible": 1,
            "requiere_poderes_demonio": True
        },
        {
            "id_producto": "WPN-LAG-06",
            "nombre": "Lanzagranadas",
            "descripcion": "Poderoso lanzador de granadas de gran alcance.",
            "categoria": "Arma de Fuego",
            "precio_orbes_rojos": 35000,
            "stock_disponible": 1,
            "requiere_poderes_demonio": True
        },
        {
            "id_producto": "WPN-CER-07",
            "nombre": "Cerberus",
            "descripcion": "Nunchaku de hielo de tres cabezas el cual puede invocar pilares de este elemento.",
            "categoria": "Cuerpo a Cuerpo",
            "precio_orbes_rojos": 50000,
            "stock_disponible": 1,
            "requiere_poderes_demonio": True
        },
    ]

# 2. LÓGICA ALGORÍTMICA: Búsqueda Secuencial por Campo Clave
def buscar_arma_por_id(id_a_buscar):
    # Algoritmo que recorre el arreglo registro por registro
    for arma in st.session_state.catalogo:
        if arma["id_producto"].strip().upper() == id_a_buscar.strip().upper():
            return arma  # Devuelve el registro completo si coincide el ID
    return None  # Devuelve Nada si no lo encuentra

# 3. DISEÑO DE LA INTERFAZ DE USUARIO (Frontend con Streamlit)
st.title("⚔️ Devil May Buy ⚔️")
st.subheader("Plataforma de armamento para Cazadores de Demonios profesionales")
st.markdown("---")

# Componente: Barra de Búsqueda
st.write("### 🔍 Sistema de Búsqueda por Código de Registro")
id_ingresado = st.text_input("Ingresa el ID del arma (Ej: WPN-REB-01, WPN-EBY-02):", placeholder="WPN-...")

if id_ingresado:
    # Llamada al algoritmo de búsqueda
    resultado = buscar_arma_por_id(id_ingresado)
    
    if resultado:
        st.success(f"¡Registro Encontrado! Mapeando datos de: **{resultado['nombre']}**")
        
        # Mostrar los campos del registro de forma estética
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"**ID Producto (Clave):** `{resultado['id_producto']}`")
            st.write(f"**Categoría:** {resultado['categoria']}")
        with col2:
            st.write(f"**Precio:** {resultado['precio_orbes_rojos']:,} 🔴 Orbes Rojos")
            st.write(f"**Stock en Tienda:** {resultado['stock_disponible']} unidades")
            st.write(f"**Requiere Poderes demoniacos:** {'Sí' if resultado['requiere_poderes_demonio'] else 'No'}")
        
        st.info(f"**Descripción del Artefacto:** {resultado['descripcion']}")
    else:
        st.error("❌ Código inválido. Ese objeto no existe en nuestro inventario infernal.")

st.markdown("---")

# Componente: Catálogo General (Vista completa de los registros)
st.write("### 📜 Inventario Completo disponible en la Base de Datos")
for arma in st.session_state.catalogo:
    with st.expander(f"📦 {arma['nombre']} (ID: {arma['id_producto']})"):
        st.write(arma["descripcion"])
        st.write(f"**Precio:** {arma['precio_orbes_rojos']:,} Orbes | **Stock:** {arma['stock_disponible']} unidades")
