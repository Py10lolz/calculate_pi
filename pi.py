from math import factorial, sqrt, pi

# used in Ramanujan's formula for Pi

R = 2*sqrt(2)/9801

# used in Chudnovsky algorithm
A = 545140134
B = 13591409
C = 640320
#########
def summation(function, lower_limit, upper_limit):
	result = 0
	for num in range(lower_limit, upper_limit):
		result += function(num)
	return result
#########
def product(function, lower_limit, upper_limit):
	result = 1
	for num in range(lower_limit, upper_limit):
		result *= function(num)
	return result
# π formulas
def leibniz_sum(n=100000):
	if type(n) != int: raise Exception("the number of terms can only be an integer")
	if n <= 0: raise Exception("the number of terms must be positive")
	func = lambda n: (-1)**n / (2*n+1)
	result = 4*summation(func, 0, n)
	print(f"π ≈ {result} (using leibniz sum with {n} terms)")
def ramanujan_sum(n=2):
	if type(n) != int: raise Exception("the number of terms can only be an integer")
	if n <= 0: raise Exception("the number of terms must be positive")
	func = lambda n: R*factorial(4*n)*(1103+26390*n)/((factorial(n)*396**n)**4)
	result = 1/summation(func, 0, n)
	print(f"π ≈ {result} (using ramanujan's sum with {n} terms)")
def wallis_product(n=100000):
	if type(n) != int: raise Exception("the number of terms can only be an integer")
	if n <= 0: raise Exception("the number of terms must be positive")
	func = lambda n: (4*n**2)/(4*n**2-1)
	result = 2*product(func, 1, n+1)
	print(f"π ≈ {result} (using wallis product with {n} factors)")
def chudnovsky_algorithm(n=2):
	if type(n) != int: raise Exception("the number of terms can only be an integer")
	if n <= 0: raise Exception("the number of terms must be positive")
	func = lambda n: 12*((-1)**n*factorial(6*n)*(A*n+B))/(factorial(3*n)*factorial(n)**3*C**(3*n + 1.5))
	result = 1/summation(func, 0, n)
	print(f"π ≈ {result} (using chudnovsky algorithm with {n} terms)")
for function in [leibniz_sum, wallis_product, ramanujan_sum, chudnovsky_algorithm]:
	function()