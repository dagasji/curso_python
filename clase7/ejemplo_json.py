import json

persona = '{"nombre": "Juan", "lenguajes": ["Python", "Shellscripts"]}'

print(persona)
print('Tipo: ', type(persona))

persona_dic = json.loads(persona)
print(persona_dic['nombre'])
# print('Tipo: ', type(persona_dic))

persona_json = json.dumps(persona_dic)
print(persona_json)




