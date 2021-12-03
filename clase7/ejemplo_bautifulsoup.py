# Ejemplo uso de la biblioteca Beautiful Soup
# Documentación oficial:
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
from bs4 import BeautifulSoup
import requests

url = input("Escribe la URL del sitio web: ")

agrega_http = requests.get("http://" + url)
datos = agrega_http.text

soup = BeautifulSoup(datos, features="lxml")
for link in soup.find_all('a'):
    print(link.get('href'))


    