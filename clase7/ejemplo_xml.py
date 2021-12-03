import xml.etree.ElementTree as ET

# Importar XML desde un fichero
arbol = ET.parse('./clase7/ejemplo_xml.xml')
raiz = arbol.getroot()

# Acceder a elementos determinados
for child in raiz:
    print("Tag: ", child.tag, "Atributos: ", child.attrib)

# Acceder al child utilizando índices
print(raiz[0][1].text)

# Acceder a sub elemento utilizando el método Element
for neighbor in raiz.iter('neighbor'):
    print(neighbor.attrib)