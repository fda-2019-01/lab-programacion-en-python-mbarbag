##
## Imprima por cada fila, la columna 1 y la suma de los valores
## de la columna 5
##
## E,22
## A,14
## B,14
## ....
## C,8
## E,11
## E,16
##
data = open("data.csv",'r').readlines()
data = [row[0:-1] for row in data] #quito las \n
data = [row.split('\t') for row in data] #parto el archivo por las \t
elements = [row[0] for row in data]
lastcolumn = [row[4].split(',') for row in data]
lastcolumn = [[(pair.split(':')) for pair in row] for row in lastcolumn]
values = [[pair[1]for pair in row]for row in lastcolumn]
total = []
for row in values:
  suma = 0
  for value in row:
    suma += int(value)
  total.append(suma)
lent = len(total)
for i in range(lent):
  print('{},{}'.format(elements[i],total[i]))