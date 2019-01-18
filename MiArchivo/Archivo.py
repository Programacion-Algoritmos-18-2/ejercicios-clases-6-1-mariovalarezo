import codecs
import sys


class Mi_archivo:
    """
    """
    def __init__(self):
        """
        """
        self.archivo = codecs.open("datos.txt", "r")  # Manda a abrir el archivp

    def obtener_informacion(self):
        return self.archivo.readlines()  # Retorna los datos contenidos en el txt

    def cerrar_archivo(self):
        self.archivo.close()  # Cierra el archivo
