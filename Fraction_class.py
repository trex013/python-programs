def shortner( n, m):
    if n  == None or m == None:
        n = (0,0)
        return  n  
    for i in range(len(n)-1):
        if n[i] == m[i]:
            del( n[i], m[i])

    return n[0] , m[0]

def factorizer(n):
    factors = []; fact = []
    for x in range(2, n):
        if n % x == 0:
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
                if nu1 == 0:
                    x = 1
                else :
                    x = de1 //nu1
                store = 1, x
        else:
            store = nu1,de1    
    return store

class Fraction(object):
    """A class that defines afraction object"""
    
    def __init__(self, num, den, whole = 0):
        self.num = num
        self.den = den
        self.whole_part = whole
        
    def whole_number_form(self):
        if self.whole_part >= 1: pass#self.num > self.den:
        
    def __str__(self):
        self.whole_part = self.num // self.den
        if self.whole_part > 0:
            self.num %= self.den
            return " %d : %r " %(self.whole_part ,lowest_forms(self.num,self.den)) 
        else :
            return str(lowest_forms(self.num,self.den)) 
    
    def __add__(self, other):
        num_value = self.num * other.den + self.den * other.num
        den_value = self.den * other.den
        x = lowest_forms(num_value, den_value)
        return Fraction(x[0], x[1])
    
    def __sub__(self,other):
        num_value = self.num * other.den - self.den * other.num
        den_value = self.den * other.den
        x = lowest_forms(num_value, den_value)   
        return Fraction(x[0], x[1])
    
    def __mul__(self, other):
        x = lowest_forms(self.num * other.num, self.den * other.den)
        return Fraction(x[0], x[1])
    
    def __truediv__(self, other):
        x = lowest_forms(self.num * other.den, self.den * other.num)
        return Fraction(x[0], x[1])
    
    #def __pow__(self,other):
    def __gt__(self,other):
        x, y = self.num/self.den, other.num/other.den
        if x > y:
            return True
        else:
            return False
    
    def __lt__(self,other):
        x, y = self.num/self.den, other.num/other.den
        if x < y:
            return True
        else:
            return False    
    
    def __ge__(self,other):
        x, y = self.num/self.den, other.num/other.den
        if x >= y:
            return True
        else:
            return False  
    
    def __le__(self,other):
        x, y = self.num/self.den, other.num/other.den
        if x <= y:
            return True
        else:
            return False  
    
    def __eq__(self,other):
        x, y = self.num/self.den, other.num/other.den
        if x == y:
            return True
        else:
            return False 
        
    def __ne__(self,other):
        x, y = self.num/self.den, other.num/other.den
        if x != y:
            return True
        else:
            return False        
    
x = Fraction(2,4)
y = Fraction(2,4)
z = x is y
print (z)
#print(z / x)#,str(x+y))
#print(x * y)