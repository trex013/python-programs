#!/usr/bin/python3

def isprime(n):
    if n == 1:
        print("1 is Special")
        return False
    
    for x in range(2, n):
        if n % x == 0:
            print ( "The number {} equals {} x {} " .format(n , x, n // x))
            return False
        
    else :
            print( n," is prime. ")
            return True
    
    
    
for n in range(1,100):
    isprime(n)