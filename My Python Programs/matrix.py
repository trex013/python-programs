class Matrix:
     "A Class to control matrices"
     matrix = [[]]
     
     def __init__(self, row , col):
          "Creator"
          self.row = row
          self.col = col
          return

     def __add__(self, other):
          "addition"
          mat = []
          if self.row == other.row:
               print("good")
               for i in range(self.row):
                    for j in range(self.col):
                         mat.append(self.A[i][j] + other.A[i][j])
               print(mat)
               return mat
          
          else:
               print ("failed")
               
               
     def __sub__(self, other):
          "subtract"
          mat = []
          if self.row == other.row:
               print("good")
               for i in range(self.row):
                    for j in range(self.col):
                         mat.append(self.A[i][j] - other.A[i][j])
               print(mat)
               return mat
          else:
               print ("failed to subtract")

     def __mul__(self, other):
          "Multiply"
          if self.row == other.col:
               print("passed")
               mat = []
               print("good")
               #mat = other.col
               c = 0;
               for i in range(self.row):
                    for n in [1,2,3]:
                         for j in range(self.col):
                              try:
                                   c = c + self.A[i][j] * other.A[j][i]
                                   print(self.A[i][j],"**",other.A[j][i])
                              except:
                                   pass
                              
                         print(self.A[i][j],"**",other.A[j][i])
                    print (c)
                    mat.append(c)
                    c= 0
               print(mat)
               return mat
          else:
               print ("failed")

     def insert_data(self):
          "Insert entries"
          A = []; B = []
          print("Enter Values for The matrix ")
          for i in range(self.row):
               for j in range(self.col):
                   B.append(int(input("Enter Entry (%d,%d): " %(i+1,j+1))))
               A.append(B)
               B = []
          self.A = A

     def display(self):
          """show """
          for n in self.A:
               rows = str(n)
               rows = rows.replace("["," ")
               rows = rows.replace(",","   ")
               rows =  rows.replace("'"," ")
               rows = rows.replace("]"," ")
               print (rows)
               
x=Matrix(3,2)
m = Matrix(2,3)
x.insert_data()
m.insert_data()
#x.display()
x+m
x*m
