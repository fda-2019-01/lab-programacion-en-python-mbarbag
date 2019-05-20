##
## Imprima el valor maximo y minimo por cada letra de la columa 1.
##
## A,9,1
## B,9,1
## C,9,0
## D,7,1
## E,9,1
##
data = open("data.csv",'r').readlines()
data = [row[0:-1] for row in data] #quito las \n
data = [row.split('\t') for row in data] #parto el archivo por las \t
columns = [[row[0],row[1]] for row in data]
elements = list(set([row[0] for row in columns]))
dic = {}
for element in elements:
    dic[element] = [0,100]
    

for row in columns:
  num = int(row[1])
  if num > (dic[row[0]][0]):
    dic[row[0]][0] = num
  elif num < (dic[row[0]][1]):
    dic[row[0]][1] = num
result = list(dic.items())
result.sort()
for element, total in result:
  print(element,',',total[0],',',total[1])