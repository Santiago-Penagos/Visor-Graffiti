import json  # Para leer el archivo de grafitis

ARCHIVO_GRAFITIS = "grafitis.json"


def leer_grafitis():
    """Lee el catalogo desde el archivo JSON y devuelve la lista."""
    with open(ARCHIVO_GRAFITIS, encoding="utf-8") as f:
        return json.load(f)


def construir_enlace_maps(latitud, longitud):
    """Arma el enlace de Google Maps a partir de las coordenadas (sin API key)."""
    return f"https://www.google.com/maps?q={latitud},{longitud}"


def obtener_grafitis():
    """Devuelve cada grafiti con su enlace_maps ya construido."""
    grafitis = leer_grafitis()
    for g in grafitis:
        g["enlace_maps"] = construir_enlace_maps(g["latitud"], g["longitud"])
    return grafitis
