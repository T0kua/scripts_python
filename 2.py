"""задача
является ли число степенью двойки"""
i = 2
ack = False
x = int(input("input:"))
if x // 2 :
	while i < x :
		i = i * 2 
	if i == x : 
		ack = "True"
print(ack)