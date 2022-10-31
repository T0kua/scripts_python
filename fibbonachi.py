num = int(input())


def fibonacci(n):
	l = [0,1]
	print(0)
	print(1)
	for i in range(2,n):
		print(l[i - 1] + l[i - 2] )
		l.append(l[i - 1] + l[i - 2] )
	#complete the recursive function


fibonacci(num)