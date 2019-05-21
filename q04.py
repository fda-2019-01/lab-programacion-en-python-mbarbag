##
## Imprima la cantidad de registros por cada mes.
##
## 01,3
## 02,4
## 03,2
## 04,4
## 05,3
## 06,3
## 07,5
## 08,6
## 09,3
## 10,2
## 11,2
## 12,3
##
data = open("data.csv",'r').readlines()
data = [row[0:-1] for row in data] #quito las \n
data = [row.split('\t') for row in data] #parto el archivo por las \t
thirdcolumn = [(row[2]).split('-') for row in data]
months = [(row[1]) for row in thirdcolumn]
elements = list(set(months))
elements.sort()
for element in elements:
  print('{},{}'.format(element,months.count(element)))