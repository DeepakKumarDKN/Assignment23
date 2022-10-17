#TODO: Excercises

# 1. Use iter and next method to access all the elements of a given set using while loop
"""
elements = {1,2,3,4,5,6,7,8,9,10}
it = iter(elements)
try:
  while True:
    print(next(it), end=" ")
except StopIteration:
  pass

"""

# 2. Create a generator to produce first n odd natural numbers
"""
def oddNumbers(n):
  a=1
  while n:
    yield a
    a=a+2
    n=n-1
  
for i in oddNumbers(int(input('Enter the number:'))):
  print(i, end=" ")
"""

# 3. Create a generator to produce first n even natural numbers
"""
def evenNumbers(n):
  a=2
  while n:
    yield a
    a=a+2
    n=n-1
for i in evenNumbers(10):
  print(i, end=" ")
"""

# 4 Create a generator to produce squares of first N natural numbers
"""
def squareNumbers(n):
  a=1
  while n:
    yield a**2
    a=a+1
    n=n-1

for i in squareNumbers(10):
  print(i, end=" ")
"""

#5. Create a generator to produce first n terms of Fibonacci series
"""
def fibonacci(n):
  a,b=0,1
  while n:
    yield a
    a,b = b, a+b
    n=n-1

for i in fibonacci(10):
  print(i, end=" ")
"""

# TODO: 6. Create a generator to produce first n prime numbers
"""
def isPrime(num):
  for i in range(2,num):
    if num % i ==0:
      return False
  return True

def primeGenerator(n):
  num = 2
  while n:
    if isPrime(num):
      yield num
      n=n-1
    num+=1
  return


it = primeGenerator(10)
for i in it:
  print(i, end=" ")
"""

# 7. Create an endless iterator using generator method to produce terms of Fibonacci series

# def fib():
#   a,b = 0,1
#   while True:
#     yield a 
#     a,b =b,a+b

# it = fib()
# fibList = []
# while True:
#   ans = input('Do you want to geneate one more elemenent[y/n]:')
#   if ans == 'y':
#     fibList.append(next(it))
#   else:
#     print(fibList)
#     break


# 8. Create an endless iterator using generator method to produce Prime numbers
"""
def primeNumber():
  num= 2
  while True:
    factor = 0
    for i in range(1,num+1):
      if num % i == 0:
        factor+=1
    if factor ==2:
      yield num
    num+=1

it = primeNumber()
primeNumberList = []
while True:
  ans = input('Do you want to find One More Prime Number:')
  if ans == "y":
    primeNumberList.append(next(it))
  else:
    print(primeNumberList)
    break
"""

# 9. Define a function which takes lengths of three sides of a triangle as arguments and
# display the perimeter or triangle. Define and apply a decorator which checks for the
# validity of the triangle on the basis of lengths of the side. This makes the perimeter to
# be displayed when the triangle can exist with the given lengths of the sides.

def decorFunction(func):
  def validityTriangle(a,b,c):
    """A triangle is valid if sum of its two sides is greater than the third side"""
    if a+b>c or b+c>a or c+a>b:
      func(10,20,5)
  return validityTriangle


@decorFunction
def perimeterTriangle(a,b,c):
  perimeter = a+b+c
  print('Permieter is:', perimeter)
perimeterTriangle(10,20,5)

