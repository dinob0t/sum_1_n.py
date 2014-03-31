""" 
Algorithm to sum numbers 1 to n
"""

n = 100


def sum_1_n_for(n):
	total = 0;
	for i in range(1,n+1):
		total += i	
	return total

print "Sum 1 to n is %d" %sum_1_n_for(n)


