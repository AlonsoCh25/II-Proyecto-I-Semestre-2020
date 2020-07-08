import csv

class csv_class:
    def __init__(self, archivo, metodo):
        self.archivo = self.read(archivo, metodo)

    #Se define la funcion read, que retorna una matriz del archivo csv
    def read(self, archivo, metodo):
        f = open(archivo, metodo)
        data = csv.reader(f)
        data = [row for row in data]
        #Elimina los elementos vacios generados en el csv
        for i in data:
            if i == []:
                data.remove(i)
        return data

    #Se define la funcion write, para modificar la variable matriz.
    def write(self, matriz):
        self.archivo = matriz

    #La funcion retorna la matriz cargada en el archivo csv
    def get_matriz(self):
        return self.archivo

    #La funcion actualiza el archivo csv con la variable matriz
    def update_matriz(self, archivo, metodo):
        a = self.archivo
        f = open(archivo, metodo)
        with f:
            writer = csv.writer(f)
            writer.writerows(a)

#Cargar el archivo CSV.
archivo_csv = csv_class("ScoreBoard.csv","rt")
matriz_csv = archivo_csv.get_matriz()

"""Para escribir una nueva matriz en la variable"""
# archivo_csv.write("Nueva matriz")
"""Para guardar la matriz en el archivo csv"""
# archivo_csv.update_matriz("matriz.csv","w")
"""NOTA"""
#Primero se debe escribir la matriz en la variable y luego guardarla en el archivo csv.
