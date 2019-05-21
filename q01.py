##
## Imprima la suma de la segunda columna.
##

data = open("data.csv",'r').readlines()
data = [row[0:-1] for row in data] #quito las \n
data = [row.split('\t') for row in data] #parto el archivo por las \t
secondcolumn = [int(row[1]) for row in data]
suma = 0
for element in secondcolumn:
  suma += element
print(suma)
