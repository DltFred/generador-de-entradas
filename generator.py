import os
svg_ruta = "template.svg" 
carpeta_salida = "entradas_generadas"
os.makedirs(carpeta_salida, exist_ok=True)

def generar_entradas_svg(grupos):
    with open(svg_ruta, "r") as file:
        contenido_svg = file.read()

    numero_entrada = 1

    for grupo in grupos:
        nombre_grupo = grupo['nombre']
        mesas_por_grupo = grupo['cantidad-mesas']
        asientos_por_mesa = grupo['asientos-por-mesa']

        for mesa in range(1, mesas_por_grupo + 1):
            for asiento in range(1, asientos_por_mesa + 1):
                entrada_formateada = f"ENTRADA N° {numero_entrada:03d}"
                mesa_asiento = f"MESA: {nombre_grupo}{mesa:02d}-{asiento:02d}"

                nuevo_contenido_svg = contenido_svg.replace("ENTRADA N&#xb0; 001", entrada_formateada)
                nuevo_contenido_svg = nuevo_contenido_svg.replace("MESA : A01 - 01", mesa_asiento)  

                with open(os.path.join(carpeta_salida, f"entrada-{nombre_grupo}{mesa:02d}-{asiento:02d}.svg"), "w") as new_file:
                    new_file.write(nuevo_contenido_svg)

                numero_entrada += 1

grupos = [
    {'nombre': 'A', 'cantidad-mesas': 12, 'asientos-por-mesa': 8},
    {'nombre': 'B', 'cantidad-mesas': 8, 'asientos-por-mesa': 8},
    {'nombre': 'C', 'cantidad-mesas': 12, 'asientos-por-mesa': 8},
    {'nombre': 'D', 'cantidad-mesas': 8, 'asientos-por-mesa': 2}
]

generar_entradas_svg(grupos)