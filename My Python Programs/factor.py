class Fraction:
     de = 1
     def __init__(self, nu, de):
          self.nu = nu
          self.de = de

     def __add__(self, other):
          des = [self.de ,  other.de]
          lcm_ = lcm(des)
          nus = ((lcm_/self.de)*self.nu) + ((lcm_/other.de)*other.nu)
          return Fraction(nus, lcm_)
     
     def __str__(self):
          return "{} / {}".format(int(self.nu), self.de)

def factor(data, tester = 2):
     for x in data:
          if x % tester == 0:
               continue
          else:
               return 1
     return tester

def divideList(iterable, by):
     value = []
     for x in iterable:
          value.append(int(x/by))

     return value

def cnt(it, test):
     for x in it:
          if test >= x:
               return True
          else:
               return False

def mul(arr):
     d = 1
     for x in arr:
          d *= x
     return d

def factors(data):
     factors = []
     tester = 2
     while True:
          fact = factor(data, tester)
          data = divideList(data, fact)
          if fact == 1:
               tester += 1
               if cnt(data, tester):
                    break
               continue
          
          factors.append(fact)
          
          
          
     return data, factors

def lcm(data):
     x,factors_ = factors(data)
     return mul(factors_)
     
#x = [250,125,625]

#print("LCM: ",lcm(x))

x = Fraction(2,3) + Fraction(1,3) +Fraction(4,3)

print(x)
