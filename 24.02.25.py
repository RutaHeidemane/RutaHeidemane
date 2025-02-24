#%%  1.uzd.


def greet(name):
    print(f'sveika, {name}')
    
def heelo (name):
    print(f'hello{name}')
    
greet("Anna")

#%%  2.uzd.

def sum_numbers(a, b):
    result = a + b
    return result
print(sum_numbers(5, 3))
    
#%%  3.uzd.

def is_even(n):
   
    i = 2 
    if n % i == 0:
        return("True:")
    else:
        return("False:")
print(is_even(40))
    
#%%  4.uzd.      
        
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
print(factorial(5))
             
#%%    
    
def fizzbuzz(n):
    if n % 3 == 0 and n % 5==0:
        print("FizzBuzz")
    if n % 3 ==0
        print("Fizz")
    if n % 5==0:
         print("Buzz")
     print(FizzBuzz)






