import math as m
import decimal
inp=[]
while True:
	n=int(input())
	if n==0:
		break;
	inp.append(n)
for i in inp:
	sq=m.sqrt(i)
	d = decimal.Decimal(sq)
	p=d.as_tuple().exponent
	if p==0:
		print("yes")
	else:
		print("no")
	
	
