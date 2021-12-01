import os
import shutil

# Copiar ficheros situados en el mismo directorio
shutil.copytree(src="dir_prueba", dst="dir_prueba_2", ignore=shutil.ignore_patterns('*.txt'))

