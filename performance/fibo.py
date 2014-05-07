import os
def fibo(n):
    return fibo(n - 1) + fibo(n - 2) if n > 1 else 1

fibo(40)
