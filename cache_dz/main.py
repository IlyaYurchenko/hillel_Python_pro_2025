from pymemcache.client import base

client = base.Client(('localhost', 11211))

def fib_numbers(n):
    if n < 0:
        raise ValueError("Input should be a non-negative integer.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    
    cached = client.get(f"fib{n}")
    if cached is not None:
        return(int(cached))
    
    value = fib_numbers(n-1) + fib_numbers(n-2)
    client.set(f"fib{n}", str(value))
    print(f"Fibonacci number for {n} is {value}")
    return value
    

fib_numbers(10)