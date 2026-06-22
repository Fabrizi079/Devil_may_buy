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
            "requiere_poderes_demonio": True,
            "imagen": "https://static.wikia.nocookie.net/devilmaycry/images/9/91/Rebellion_DMC5.png/revision/latest/scale-to-width-down/1000?cb=20181028035650",
        },
        {
            "id_producto": "WPN-EYI-02",
            "nombre": "Ebony & Ivory",
            "descripcion": "Pistolas semiautomáticas personalizadas para disparar ráfagas de energía espiritual a alta velocidad, creadas por la Armera legendaria Nell Goldstein",
            "categoria": "Arma de Fuego",
            "precio_orbes_rojos": 99999,
            "stock_disponible": 0,
            "requiere_poderes_demonio": False,
            "imagen": "https://static.wikia.nocookie.net/devilmaycry/images/0/08/DMC5_Ebony_%26_Ivory.png/revision/latest/scale-to-width-down/1000?cb=20190326004640",
        },
        {
            "id_producto": "WPN-ALA-03",
            "nombre": "Alastor",
            "descripcion": "Espada demoniaca que contiene la voluntad del demonio con el que comparte nombre. Esta posee poderes electricos y le otorga a su portador la capacidad de volar.",
            "categoria": "Cuerpo a Cuerpo",
            "precio_orbes_rojos": 50000,
            "stock_disponible": 1,
            "requiere_poderes_demonio": True,
            "imagen": "https://static.wikia.nocookie.net/devilmaycry/images/b/b9/Alastor_%28DA%29_DMC1.png/revision/latest?cb=20150418055040",
        },
        {
            "id_producto": "WPN-COA-04",
            "nombre": "Coyote-A",
            "descripcion": "Escopeta recortada de dos cañones con gran potencia de fuego.",
            "categoria": "Arma de Fuego",
            "precio_orbes_rojos": 35000,
            "stock_disponible": 5,
            "requiere_poderes_demonio": False,
            "imagen": "https://static.wikia.nocookie.net/devilmaycry/images/e/ef/DMC5_Coyote-A.png/revision/latest/scale-to-width-down/1000?cb=20181105001547",
        },
        {
            "id_producto": "WPN-IFR-05",
            "nombre": "Ifrit",
            "descripcion": "Guanteletes con poder de las llamas procedentes del mismo Infierno.",
            "categoria": "Cuerpo a Cuerpo",
            "precio_orbes_rojos": 50000,
            "stock_disponible": 1,
            "requiere_poderes_demonio": True,
            "imagen": "https://static.wikia.nocookie.net/devilmaycry/images/3/3e/Ifrit_DMC.png/revision/latest?cb=20260517113859",
        },
        {
            "id_producto": "WPN-LAG-06",
            "nombre": "Lanzagranadas",
            "descripcion": "Poderoso lanzador de granadas de gran alcance.",
            "categoria": "Arma de Fuego",
            "precio_orbes_rojos": 35000,
            "stock_disponible": 5,
            "requiere_poderes_demonio": True,
            "imagen": "https://static.wikia.nocookie.net/devilmaycry/images/7/70/DMC1_-_Grenade_Gun.png/revision/latest?cb=20150629100757",
        },
        {
            "id_producto": "WPN-CER-07",
            "nombre": "Cerberus",
            "descripcion": "Nunchaku de hielo de tres cabezas el cual puede invocar pilares de este elemento.",
            "categoria": "Cuerpo a Cuerpo",
            "precio_orbes_rojos": 50000,
            "stock_disponible": 1,
            "requiere_poderes_demonio": True,
            "imagen": "https://static.wikia.nocookie.net/devilmaycry/images/d/d9/DMC3_Cerberus.png/revision/latest/scale-to-width-down/1000?cb=20181111191829",
        },
        {
            "id_producto": "WPN-AYR-08",
            "nombre": "Agni y Rudra",
            "descripcion": "Dos espadas gemelas que poseen poderes de fuego y viento respectivamente, en sus mangos se encuentran las cabezas de los demonios con los que comparten nombre",
            "categoria": "Cuerpo a Cuerpo",
            "precio_orbes_rojos": 50000,
            "stock_disponible": 1,
            "requiere_poderes_demonio": True,
            "imagen": "https://static.wikia.nocookie.net/devilmaycry/images/b/be/Agni_%26_Rudra.png/revision/latest/scale-to-width-down/1000?cb=20190215213557",
        },
        {
            "id_producto": "WPN-NEV-09",
            "nombre": "Nevan",
            "descripcion": "Guitarra eléctrica que puede enviar descargas eléctricas mientras tocas notas de música, asi como invocar murcielagos eléctricos, tambien puede transformarse en una guadaña para ataques de cuerpo a cuerpo.",
            "categoria": "Cuerpo a Cuerpo y a distancia",
            "precio_orbes_rojos": 50000,
            "stock_disponible": 1,
            "requiere_poderes_demonio": True,
            "imagen": "https://static.wikia.nocookie.net/devilmaycry/images/a/a3/DA_Nevan.gif/revision/latest?cb=20130220035201",
        },
        {
            "id_producto": "WPN-BEO-10",
            "nombre": "Beowulf",
            "descripcion": "Guanteletes y espinilleras de luz capaces de propinar poderosos golpes y patadas.",
            "categoria": "Cuerpo a Cuerpo",
            "precio_orbes_rojos": 50000,
            "stock_disponible": 1,
            "requiere_poderes_demonio": True,
            "imagen": "https://static.wikia.nocookie.net/devilmaycry/images/9/9c/Beowulf_DMC5.png/revision/latest?cb=20201215201528",
        },
        {
            "id_producto": "WPN-GIL-11",
            "nombre": "Gilgamesh",
            "descripcion": "Guanteletes y botas con la capacidad de aumentar la fuerza de los ataques gracias a los motores integrados en los mismos.",
            "categoria": "Cuerpo a Cuerpo",
            "precio_orbes_rojos": 50000,
            "stock_disponible": 1,
            "requiere_poderes_demonio": True,
            "imagen": "https://static.wikia.nocookie.net/devilmaycry/images/e/e0/Gilgamesh_DMC4.jpg/revision/latest?cb=20080228182948",
        },
        {
            "id_producto": "WPN-LUC-12",
            "nombre": "Lucifer",
            "descripcion": "Mochila capaz de generar una innumerable cantidad de espadas espectrales capaces de flotar alededor del usuario.",
            "categoria": "A distancia",
            "precio_orbes_rojos": 50000,
            "stock_disponible": 1,
            "requiere_poderes_demonio": True,
            "imagen": "https://static.wikia.nocookie.net/devilmaycry/images/a/aa/Lucifer_DMC4.png/revision/latest?cb=20120419203920",
        },
        {
            "id_producto": "WPN-LAM-13",
            "nombre": "Lanzamisiles",
            "descripcion": "Lanzamisiles de gran potencia pero baja velocidad capas de destruir demonios de un disparo.",
            "categoria": "Arma de fuego",
            "precio_orbes_rojos": 35000,
            "stock_disponible": 5,
            "requiere_poderes_demonio": True,
            "imagen": "https://static.wikia.nocookie.net/devilmaycry/images/a/ad/Missile_Launcher.jpg/revision/latest?cb=20150629110937",
        },
        {
            "id_producto": "WPN-PAN-14",
            "nombre": "Pandora",
            "descripcion": "Maletin que puede cambiar a 666 formas difeerentes, cada una con sus propios ataques.",
            "categoria": "A distancia",
            "precio_orbes_rojos": 50000,
            "stock_disponible": 1,
            "requiere_poderes_demonio": True,
            "imagen": "https://static.wikia.nocookie.net/devilmaycry/images/8/83/Pandora_DMC4.png/revision/latest?cb=20181106170129",
        },
        {
            "id_producto": "WPN-ART-15",
            "nombre": "Artemis",
            "descripcion": "Arma demoniaca con la capacidad de disparar flechas imbuidas de energia demoniaca.",
            "categoria": "A distancia",
            "precio_orbes_rojos": 50000,
            "stock_disponible": 1,
            "requiere_poderes_demonio": True,
            "imagen": "https://static.wikia.nocookie.net/devilmaycry/images/5/5d/Artemis.gif/revision/latest?cb=20130220052115",
        },
        {
            "id_producto": "WPN-BAL-16",
            "nombre": "Balrog",
            "descripcion": "Set de guantes, botas y hombreras que poseen el poder sellado del rey del fuego infernal.",
            "categoria": "Cuerpo a Cuerpo",
            "precio_orbes_rojos": 50000,
            "stock_disponible": 1,
            "requiere_poderes_demonio": True,
            "imagen": "https://static.wikia.nocookie.net/devilmaycry/images/1/1f/DMC5_Balrog.png/revision/latest/scale-to-width-down/1000?cb=20181028111101",
        },
        {
            "id_producto": "WPN-CAV-17",
            "nombre": "Cavaliere",
            "descripcion": "Motocicleta demoniaca con la capacidad de ssepararse y convertirse en dos motosierras.",
            "categoria": "Cuerpo a Cuerpo",
            "precio_orbes_rojos": 90000,
            "stock_disponible": 1,
            "requiere_poderes_demonio": True,
            "imagen": "https://static.wikia.nocookie.net/devilmaycry/images/b/b3/DMC5_Cavaliere.png/revision/latest/scale-to-width-down/1000?cb=20181028111659",
        },
        {
            "id_producto": "WPN-DRF-18",
            "nombre": "Dr. Faust",
            "descripcion": "Sombrero magico que otorga la capacidad de disparar orbes rojos",
            "categoria": "A distancia",
            "precio_orbes_rojos": 50000,
            "stock_disponible": 1,
            "requiere_poderes_demonio": True,
            "imagen": "https://static.wikia.nocookie.net/devilmaycry/images/4/4c/DMC5_Dr._Faust.png/revision/latest/scale-to-width-down/1000?cb=20181022132806",
        },
        {
            "id_producto": "WPN-KCE-19",
            "nombre": "King Cerberus",
            "descripcion": "Nunchaku de hielo de 3 cabezas similar al cerberus original, pero con la capacidad de convertirse en un Baston de 3 segmentos con poderes electricos y en un baston completo con poderes de fuego",
            "categoria": "Cuerpo a Cuerpo",
            "precio_orbes_rojos": 50000,
            "stock_disponible": 1,
            "requiere_poderes_demonio": True,
            "imagen": "https://static.wikia.nocookie.net/devilmaycry/images/e/ee/DMC5_King_Cerberus.png/revision/latest/scale-to-width-down/1000?cb=20181028235925"
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
        col_datos, col_imagen = st.columns([2, 1])
        with col_datos:
            st.write(f"**ID Producto (Clave):** `{resultado['id_producto']}`")
            st.write(f"**Categoría:** {resultado['categoria']}")
            st.write(f"**Precio:** {resultado['precio_orbes_rojos']:,} 🔴 Orbes Rojos")
            st.write(f"**Stock en Tienda:** {resultado['stock_disponible']} unidades")
            st.write(f"**Requiere Poderes demoniacos:** {'Sí' if resultado['requiere_poderes_demonio'] else 'No'}")
        with col_imagen:
            # use_column_width hace que la imagen se adapte perfectamente al tamaño de la columna
            st.image(resultado["imagen"], caption=resultado["nombre"], use_container_width=True)
            
        
        st.info(f"**Descripción del Artefacto:** {resultado['descripcion']}")
    else:
        st.error("❌ Código inválido. Ese objeto no existe en nuestro inventario infernal.")

st.markdown("---")

# Componente: Catálogo General (Vista completa de los registros)
st.write("### 📜 Inventario Completo disponible en la Base de Datos")
for arma in st.session_state.catalogo:
    with st.expander(f"📦 {arma['nombre']} (ID: {arma['id_producto']})"):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(arma["descripcion"])
            st.write(f"**Precio:** {arma['precio_orbes_rojos']:,} Orbes | **Stock:** {arma['stock_disponible']} unidades")
        with col2:
            st.image(arma["imagen"], use_container_width=True)
