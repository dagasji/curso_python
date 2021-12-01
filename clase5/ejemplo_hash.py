import hashlib

nombre = 'quijote_modificado.txt'

nombre_codificado = nombre.encode()

nombre_hash = hashlib.sha512(nombre_codificado)

print('Objeto: ', nombre_hash)
print('Hexadecimal: ', nombre_hash.hexdigest())