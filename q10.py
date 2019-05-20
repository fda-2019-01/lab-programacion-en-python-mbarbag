##
## Imprima una tabla en formato CSV que contenga por cada clave 
## de la columna 5, la correspondiente cantidad de registros 
## asociados (filas en el archivo)
##
## aaa,13
## bbb,16
## ccc,23
## ddd,23
## eee,15
## fff,20
## ggg,13
## hhh,16
## iii,18
## jjj,18
##
##
data = open("data.csv",'r').readlines()
data = [row[0:-1] for row in data] #quito las \n
data = [row.split('\t') for row in data] #parto el archivo por las \t
lastcolumn = [row[4] for row in data]
lastcolumn = [(row.split(',')) for row in lastcolumn]
lastcolumn = [[(pair.split(':')) for pair in row] for row in lastcolumn]
lastcolumne = [[pair[0]for pair in row]for row in lastcolumn]
columne = []
for row in lastcolumne:
  for element in row:
    columne.append(element)
columne.sort()
elements = list(set(columne))
elements.sort()
for element in elements:
  print(element,',',columne.count(element))
  