# Leer un fichero JSON
import json

with open('./clase7/fichero_json.json') as fichero:
    # .loads (decode) toma un string como input y devuelve un diccionario
    datos = json.loads(fichero.read())
    print(datos)

# Lee solo un dato del fichero
print(datos["nombre"])
##

with open('./clase7/ejemplo_persona_JSON.json', 'w') as json_fichero:
    json.dump(datos, json_fichero)

