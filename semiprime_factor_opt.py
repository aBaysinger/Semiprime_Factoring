import math
import decimal

'''
Sieve function first checks if n is a perfect square by checking sqrt mod 1 == 0.
If not a perfect square, round the sqrt up then convert back to long int called rootn.
Check if rootn is even. If even add one to make odd. (This is needed so our index function works properly)
Initialize prime array as bytearray of all true values with ((rootn - 3) / 2) number of elements. This equals the number of odd numbers from 0 - sqrt(n).
Each potential factor m can be found by the equation m = 2*i + 3 where i is m's index in the array of generated primes.
If the i index of the prime list is true: check if its corresponding number divides n. If it does, p and q have been found.
Else continue to eliminate multiples of that number by marking them false in the list. (This can be started at the square of m and incremented by m until end of list)
Loop to the next prime marked true in the prime list and repeat process.

Optimizations:
In its standard form, the sieve of Eratosthenes will struggle with large n inputs. 
The first optimization I made was to only generate prime numbers up to the square root of n. 
This is because there is guaranteed to be a factor of n in the range 0-sqrt(n) and this range is much smaller than sqrt(n)-n. 
The next optimization I made was to immediately check if n is a perfect square. 
I found that the loop would run until exit when n was a perfect square and to avoid this waste of time I could just quickly check before running the loop.  
Further, I was able to figure a way to exclude even numbers from my algorithm's considerations, reducing iterations and comparisons by half.
I found that m = 2i + 3, where m will be a potential factor of n and i is it's corresponding index in the generated list. 
Because we only need to look at odd numbers as potential primes, I reduced the size of the list initialization to the number of odd numbers up to sqrt(n) (this helped with memory efficiency as well).
'''
def sieveEratos(n):
	sqrn = decimal.Decimal(math.sqrt(n))
	if sqrn % 1 == 0:
		print str(n) + " = " + str(sqrn) + " * " + str(sqrn)
		return
	rootn = long(math.ceil(sqrn))
	if rootn % 2 == 0:
		rootn = rootn + 1
	prime = bytearray(b'\x01') * ((rootn - 3) / 2)
	for i in xrange(0, ((rootn - 3) / 2)):
		m = 2*i + 3
		if prime[i]:
			if n % m == 0:
				p = m
				q = n / p
				print str(n) + " = " + str(p) + " * " + str(q)
				return
			else:
				continue
		for j in xrange(m*m, ((rootn - 3) / 2), m):
			prime[j] = False
		
txt = open("nums.txt", "r")
for line in txt:
	n = long(line)
	sieveEratos(n)
	
