# Semiprime_Factoring
A program that takes large semiprime numbers and finds their two prime factors.

The requirement for this project was to develop an algorithm that could take a large semiprime (a number that is the product of two prime numbers) and find its two prime factors. It uses the sieve of Eratosthenes to generate prime numbers and then tests them against the input semiprime until it finds one of the semiprime's factors. Once one is found, the other can be quickly deduced. 
 
A boolean list is initialized to contain true values for each index that corresponds with numbers 0-n. 
I then loop through this list, and if the current index is true, I mark all the multiples of that number false. 
This way, only primes will have a true value while all other elements will have a false value. 
As I handle each prime in the process of the algorithm, I check if it evenly divides the input semiprime n. 
If it does, then n's second factor can quickly be figured from q = n/p. 

Included in this repository is the algorithm's code implementation and an input text file containing a significant number of large semiprime numbers. 

Run this program in a terminal with Python2. Make sure nums.txt is in the same directory.
