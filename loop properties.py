#!/usr/bin/python3

a,b = 0,1
while b < 100:
    print (b, end = ",")
    a,b = b , a+b
print ("\nDone.\n")

lines_file = open('lines.txt')
for line in lines_file.readlines():
    print(line, end= " ")