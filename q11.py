##
## Imprima una tabla en formato CSV que contenga por registro,
## la cantidad de elementos de las columnas 4 y 5
## (filas en el archivo)
##
## E,3,5
## A,3,4
## B,4,4
## ...
## C,4,3
## E,2,3
## E,3,3
##
data = open("data.csv",'r').readlines()
data = [row[0:-1] for row in data] #quito las \n
data = [row.split('\t') for row in data] #parto el archivo por las \t
columns = [[row[0],row[3],row[4]] for row in data]
for row in columns:
  second = row[1].split(',')
  lens = len(second)
  third = row[2].split(',')
  lent = len(third)
  print('{},{},{}'.format(row[0],lens,lent))