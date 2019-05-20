##
## Imprima la suma de la columna 2 por cada letra de la 
## primera columna, ordneados alfabeticamente.
##
## A,37
## B,36
## C,27
## D,23
## E,67
##
data = open("data.csv",'r').readlines()
data = [row[0:-1] for row in data] #quito las \n
data = [row.split('\t') for row in data] #parto el archivo por las \t
columns = [[row[0],row[1]] for row in data]
elements = list(set([row[0] for row in columns]))
dic = {}
for element in elements:
    dic[element] = 0
for row in columns:
  dic[row[0]] += int(row[1])
result = list(dic.items())
result.sort()
for element, total in result:
  print('{},{}'.format(element,total))
