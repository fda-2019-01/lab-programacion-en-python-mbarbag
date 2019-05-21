##
## Imprima la suma de la columna 2 por cada letra 
## de la columna 4, ordnados alfabeticamente.
##
## a,114
## b,40
## c,91
## d,65
## e,79
## f,110
## g,35
##
data = open("data.csv",'r').readlines()
data = [row[0:-1] for row in data] #quito las \n
data = [row.split('\t') for row in data] #parto el archivo por las \t
columns = [[row[1],row[3].split(',')] for row in data]
column2 = [row[1] for row in columns]
columne = []
for row in column2:
  for element in row:
    columne.append(element)
elements = list(set(columne))

dic = {}
for element in elements:
  dic[element] = 0

for row in columns:
  for element in row[1]:
    dic[element] += int(row[0])
result = list(dic.items())
result.sort()
for element, total in result:
  print('{},{}'.format(element,total))