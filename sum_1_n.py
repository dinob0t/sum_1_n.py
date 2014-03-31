""" 
Algorithm to sum numbers 1 to n
On 4 year old macbook, recursive code is faster to n ~ 30
"""
import time
n = 30


def sum_1_n_for(n):
	total = 0;
	for i in range(1,n+1):
		total += i	
	return total

def sum_1_n_recur(n):
	if n > 0:
		return n + sum_1_n_recur(n - 1)
	else:
		return n


t0 = time.time()
print "Sum 1 to n with for loop is %d" %sum_1_n_for(n)
t1 = time.time()
print "Time taken %f s" %(t1-t0)


t0 = time.time()
print "Sum 1 to n recursively is %d" %sum_1_n_recur(n)
t1 = time.time()
print "Time taken %f s" %(t1-t0)



