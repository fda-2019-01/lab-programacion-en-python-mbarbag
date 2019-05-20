##
## Imprima la cantidad de registros por letra para la 
## primera columna, ordenados alfabeticamente.
##
## A,8
## B,7
## C,5
## D,6
## E,14
##
data = open("data.csv",'r').readlines()
data = [row[0:-1] for row in data] #quito las \n
data = [row.split('\t') for row in data] #parto el archivo por las \t
firstcolumn = [(row[0]) for row in data]
firstcolumn.sort()
elements = list(set(firstcolumn))
elements.sort()
for element in elements:
  print(element,',',firstcolumn.count(element))