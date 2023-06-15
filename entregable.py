import requests
import json

def obtener_datos(url):
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos = json.loads(respuesta.text)
        return datos
    else:
        print("Error al obtener los datos de la API")
        return None
    
url_de_api = "https://infra.datos.gob.ar/catalog/modernizacion/dataset/7/distribution/7.27/download/localidades-censales.json"
datos_api = obtener_datos(url_de_api)

print(datos_api)

