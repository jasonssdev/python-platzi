#Function
def add(a:int,b:int) -> int:
    return a + b

print(add(5,10))

#lambda function
lambda_add = lambda a, b : a + b
print(lambda_add(5,10))

# superior order functions
#map
number_list = range(11)
squared_numbers = list(map(lambda x: x**2, number_list))
print(squared_numbers)

#filter
even_numbers = list(filter(lambda x: x % 2 == 0, number_list))
print(even_numbers)

# Try Except

def counter(text:str )-> int:
    try:
        return print(len(text))
    except Exception as e:
        print(f"Un error ha ocurrido -> {e}")

# Recursividad

def factorial(n:int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(5))

