##
## Genere una lista de tuplas, donde cada tupla contiene en la primera 
## posicion, el valor de la segunda columna; la segunda parte de la 
## tupla es una lista con las letras de la primera columna que aparecen
## asociadas a dicho valor de la segunda columna. Esto es:
##
##    ('0', ['C'])
##    ('1', ['E', 'B', 'D', 'A', 'A', 'E'])
##    ('2', ['A', 'E', 'D'])
##    ('3', ['A', 'B', 'D', 'E', 'E'])
##    ('4', ['E', 'B'])
##    ('5', ['B', 'C', 'D', 'D', 'E', 'E', 'E'])
##    ('6', ['C', 'E', 'A', 'B'])
##    ('7', ['A', 'C', 'E', 'D'])
##    ('8', ['E', 'E', 'A', 'B'])
##    ('9', ['A', 'B', 'E', 'C'])
##
##
data = open("data.csv",'r').readlines()
data = [row[0:-1] for row in data] #quito las \n
data = [row.split('\t') for row in data] #parto el archivo por las \t
columns = [[row[0],row[1]] for row in data]
elements = list(set([row[1] for row in columns]))
dic = {}
for element in elements:
    dic[element] = []

for row in columns:
  dic[row[1]] += [row[0]]
result = list(dic.items())
result.sort()
for element, total in result:
  print((element,total))