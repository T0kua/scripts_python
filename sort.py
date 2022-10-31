
v = [1,5,25,36,6,362,26,62,6,76,7,9,9,9,99,0,0,47,4,77,3,7,3,7,237,2,7,3,]
for j in range(len(v)) :
	for i in range(len(v)) :
		try :
			if v[i] > v[i+1] :
				v[i],v[i+1] = v[i+1],v[i]
		except:
			pass
print(v)