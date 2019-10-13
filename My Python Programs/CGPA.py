"""A program to store and Compute CGPA"""
import os

class StudentCGPA :
     """This creates an Object of students Details"""
     _student = []
     _sem = {}
     _CGPA = 0
     def __init__(self, name, matno, dept,no_of_years_of_study) :
          """Gives The students Object its properties"""
          self._student.append(name)
          self._student.append(matno)
          self._student.append(dept)
          self._student.append(no_of_years_of_study)

     def convertgradetoGP(self, grade):
           """Converts grade to GP"""
           if grade == "a" or grade == "A": return 5
           if grade == "b" or grade == "B": return 4
           if grade == "c" or grade == "C": return 3
           if grade == "d" or grade == "D": return 2
           if grade == "e" or grade == "E": return 1
          
     def getcourse_and_grade(self):
          "gets the courses and grade"
          print ("\nCourse & Grade input")
          no_of_courses = int(input("\tEnter number of courses: "))
          course = []; grade = []; cu = []
          for n in range(0,no_of_courses):
               x = input("\tEnter Course: ")
               course.append(x)
               y = input("\tEnter Grade: ")
               grade.append(y)
               z = int(input("\tEnter Credit Unit: "))
               cu.append(z)
          gp = list(map(self.convertgradetoGP , grade ))
          qp = list(map(lambda x,y: x*y, cu , gp))
          courses = [course, grade, cu,gp,qp]
          return courses
          
          
     def semester (self):
          """Collects the Course and their Grades for each year and semester"""
          Sgpa = 0
          for n in range(1, int(self._student[3])+1):
               for i in range(1,3) :
                    self._sem[i] = courses = self.getcourse_and_grade()
                    cu = courses[2][:]
                    qp = courses[4][:]
                    tcu = reduce(cu)
                    tqp = reduce(qp)
                    # Because grade point average is sum of qp divided by sum of cu
                    gpa = tqp/tcu
                    self._sem[n].append(gpa)
                    Sgpa = Sgpa + gpa
                    q = input("Do you want to enter next semesters Courses and Grade now?(y/n) ")
                    if q == "n" or q == "N" :
                         break
                    else :
                         pass

               q = input("Do you Want to Continue to the next years Data? (y/n) ")
               if q == "n" or q == "N" : break
               self._CGPA = Sgpa
               del Sgpa
               
     def output(self):
          """Output in string format"""
          x = ("Name: ","Mat-No: ","Department: ", "No of years of study: ")
          semester_data = []
          output = "--"*20
          output += "\n"
          for i,n in enumerate(x):
               output += n + self._student[i] +"\n"
          output += "--"*20 + "\n"
          output += "Course \t Grade \t Credit Unit \t Grade Point \t Quality Point \t\n"
          for semester in self._sem :
               semdata = self._sem[semester]
               for m in range(len(semdata[0])):
                    output += semdata[0][m] +"\t"+ semdata[1][m] +"\t"+ \
                     str(semdata[2][m])+"\t\t"+str(semdata[3][m])+ "\t\t"+ str(semdata[4][m]) +"\t\n"
                    
          output += "CGPA: " + str(self._CGPA) + "\n"
          output += "This are all data stored in output\n\n"
          return output
     
     def pDetails (self) :
          x = self.output()
          print (self.output())
         # print (self._student,"CGPA: ",self._CGPA )# _student is a list of students details like name, matno etc & CGPA is a float 
          print (self._sem[1])#_sem is a dictionary, _sem[i] is a list with 5 list elements and one float at the end of the list it also consist of the grade etc
          return x

def reduce (x):
          x = list(x)
          sum = 0
          for n in x:
               sum += n
          return sum
                    
