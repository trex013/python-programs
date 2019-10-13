doc = [['ftutfj', 'gtjufchj'], ['a', 'b'], [2, 3], [5, 4], [10, 12], 4.4]
n  = 1
o = " "
for i in range(2):
     o += doc[0][i] +"\t"+ doc[1][i] + str(doc[2][i]) + str(doc[3][i]) + str(doc[4][i]) + "\n"
     n +=1
print(o)
