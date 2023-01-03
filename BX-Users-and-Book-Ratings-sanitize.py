import sys



path = sys.argv[1]
db = None
newdb = list()
with open(path, 'r', encoding='latin-1') as file: # latin-1 fixes the encoding error. 
	db = file.readlines()

for row in db:
	el = row.split(';')		
	newdb.append((el[0].replace('"',""), el[1], el[2].replace('"',"").replace("\r\n","")))

with open(path + "new", 'a+') as file:
	for row in newdb:
		file.write(row[0] + ";" + row[1] + ";" + row[2])
