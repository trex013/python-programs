#factors = []; fact = []

def shortner( n, m):
    if n or m == None:
        n = (0,0)
        return  n  
    for i in range(len(n)-1):
        if n[i] == m[i]:
            del( n[i], m[i])
        #else: 
            #eturn 0,0,
    return n[0] , m[0]

def factorizer(n):
    #global factors, fact
    factors = []; fact = []
    
    for x in range(2, n):
        if n % x == 0:
           # print ( "The number {} equals {} x {} " .format(n , x, n // x))
            factors.append([x,n // x])
            v = n // x
            factorizer(v)
            for x in factors :
                for y in x:
                    fact.append(y)
                    
            fact.sort()
            fact = set(fact)
            fact = list(fact)            
            return fact

#print (shortner(factorizer(120), factorizer(150)))

def lowest_forms ( nu, de ):
    nu1, de1 = nu,de
    value = None; store = []; v = 1
    while True:
        value = list(shortner(factorizer(nu), factorizer(de)))
        nu , de = value
        
        if value != [0,0]:
            store = value[:]
            
        if value == [0,0] :
            break
        
    if store == []:
        if nu1 % de1 == 0 or  de1 % nu1 == 0:
            if nu1 > de1 :
                store = nu1//de1 , 1
            else :
                store = 1, de1//nu1
        else:
            store = nu1,de1    
    return store

print (lowest_forms(1,1)) 
