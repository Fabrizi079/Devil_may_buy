import streamlit as st

# 1. DEFINICIÓN DEL CATÁLOGO (Arreglo de Registros/Diccionarios)
# Cada elemento en la lista actúa como un "Registro" con sus campos correspondientes.
if "catalogo" not in st.session_state:
    st.session_state.catalogo = [
        {
            "id_producto": "WPN-REB-01",
            "nombre": "Rebellion",
            "descripcion": "Espada mágica heredada por Dante de su padre Sparda. Excelente balance para combos aéreos.",
            "categoria": "Cuerpo a Cuerpo",
            "precio_orbes_rojos": 50000,
            "dano_base": 85,
            "elemento_magico": "Despertar",
            "stock_disponible": 1,
            "requiere_sangre_demonio": True
        },
        {
            "id_producto": "WPN-EBY-02",
            "nombre": "Ebony & Ivory",
            "descripcion": "Pistolas semiautomáticas personalizadas para disparar ráfagas de energía espiritual a alta velocidad.",
            "categoria": "Arma de Fuego",
            "precio_orbes_rojos": 35000,
            "dano_base": 30,
            "elemento_magico": "Espiritual",
            "stock_disponible": 5,
            "requiere_sangre_demonio": False
        },
        {
            "id_producto": "WPN-YAM-03",
            "nombre": "Yamato",
            "descripcion": "Katana legendaria capaz de cortar a través del propio tejido del espacio-tiempo. Propiedad de Vergil.",
            "categoria": "Cuerpo a Cuerpo",
            "precio_orbes_rojos": 99999,
            "dano_base": 95,
            "elemento_magico": "Oscuridad / Espacio",
            "stock_disponible": 0, # Agotado
            "requiere_sangre_demonio": True
        }
    ]

# 2. LÓGICA ALGORÍTMICA: Búsqueda Secuencial por Campo Clave
def buscar_arma_por_id(id_a_buscar):
    # Algoritmo que recorre el arreglo registro por registro
    for arma in st.session_state.catalogo:
        if arma["id_producto"].strip().upper() == id_a_buscar.strip().upper():
            return arma  # Devuelve el registro completo si coincide el ID
    return None  # Devuelve Nada si no lo encuentra

# 3. DISEÑO DE LA INTERFAZ DE USUARIO (Frontend con Streamlit)
st.title("⚔️ Devil May Cry - Devil Arm Shop")
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
            st.write(f"**Daño Base:** {resultado['dano_base']} pts")
            st.write(f"**Elemento Mágico:** {resultado['elemento_magico']}")
        with col2:
            st.write(f"**Precio:** {resultado['precio_orbes_rojos']:,} 🔴 Orbes Rojos")
            st.write(f"**Stock en Tienda:** {resultado['stock_disponible']} unidades")
            st.write(f"**Requiere Sangre Demonio:** {'Sí' if resultado['requiere_sangre_demonio'] else 'No'}")
        
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