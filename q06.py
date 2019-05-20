##
## Por cada clave de la columna 5 (cadena de tres letras), obtenga
## el valor mas pequeño y el valor mas grande asociado a esa clave.
##
## aaa,0,6
## bbb,4,7
## ccc,0,1
## ddd,5,5
## eee,0,0
## fff,4,9
## ggg,3,3
## hhh,6,8
## iii,2,7
## jjj,2,5
##
data = open("data.csv",'r').readlines()
data = [row[0:-1] for row in data] #quito las \n
data = [row.split('\t') for row in data] #parto el archivo por las \t
lastcolumn = [row[4] for row in data]
lastcolumn = [(row.split(',')) for row in lastcolumn]
lastcolumn = [[(pair.split(':')) for pair in row] for row in lastcolumn]
lastcolumn = [[[pair[0], int(pair[1])]for pair in row]for row in lastcolumn]
pairs = []
for row in lastcolumn:
  for pair in row:
    pairs.append(pair)
elements = list(set([pair[0] for pair in pairs]))
dic = {}
for element in elements:
    dic[element] = [100,0]
    
for pair in pairs:
  num = int(pair[1])
  if num > (dic[pair[0]][1]):
    dic[pair[0]][1] = num
  elif num < (dic[pair[0]][0]):
    dic[pair[0]][0] = num
result = list(dic.items())
result.sort()
for element, total in result:
  print(element,',',total[0],',',total[1])