# Funciones para interactuar con la API

from urllib import response
import requests

urls = {
    "url_generacion_renovables_2025_diaria": "https://apidatos.ree.es/es/datos/generacion/estructura-renovables?start_date=2025-01-01T00:00&end_date=2025-12-30T23:59&time_trunc=day",
    "url_transporte_cortes_2025_diaria": "",
    "url_demanda_2025_diaria": "",
    "url_intercambios_2025_diaria": "https://apidatos.ree.es/es/datos/intercambios/todas-fronteras-programados?start_date=2025-01-01T00:00&end_date=2025-12-30T23:59&time_trunc=day",
}


def obtener_datos_api(url):
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        return respuesta.json()
    else:
        return {"error": "No se pudieron obtener los datos"}


for url in urls:
    datos = obtener_datos_api(url)
    # print(datos)
