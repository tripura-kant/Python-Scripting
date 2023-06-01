Question 1-3

l = []

for i in range(2000, 3201):

	if (i%7==0) and (i%5!=0):

		l.append(str(i))

print ('.'.join(l))	
print(l)


Question 2

def fact(x):
	if x == 0:
		return 1
	return x * fact(x - 1)


x = int(input())
print(fact(x))

Question 3

n = int(input())

d = dict()

for i in range(1, n + 1):
	d[i] = i * i

print(d)

#
