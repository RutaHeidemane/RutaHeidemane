#%%  first

def hello(name="bob"):
    print(f'Hello {name}!')
    
    hello("riri")

def f(x,y,z):
    #pass
    result = 5*x+y+z/2
   # print(result)
    return result
f(2,5,10)
print(f(2,5,10))

r1 = f(2,5,10)
print(r1)

#%%  second

def y(x):
   # pass
    result = 5 * x + 2
    return result

print(y(0))
print(y(1))
print(y(2))

def factorial(n):
    result= 1
    for i in range(1,n+1):
        result *= i
    return result

#%%



 def rootFinder(a=0,b=0,c=0):
     D = b**2 - 4*a*c
    x1 = (-b - D**0.5)/(2 * a)
    x2 = (-b + D**0.5)/(2 * a)
    return x1,x2
    
    
s1,s2 = rootFinder(3,4,5):
print(s1,s2)   

#%%
  
 def y(x)  
    result =(2x + 3)/0.5
    return result

print(y(0))
print(y(1))
print(y(2))
print(y(3))
print(y(4))
    
   

    
