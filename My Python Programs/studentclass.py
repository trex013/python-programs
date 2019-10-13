
class Student:
     
     _name = str() 
     _dept = str()
     _info = dict()
     
     def __init__(self, name, dept):
          self._name = name.upper()
          self._dept = dept.upper()

     def setmoreinfo(self, **kwargs):
          self._info = kwargs.copy()

     def getinfo(self):
          data = dict(name=self._name  , dept=self._dept)
          data.update(self._info)
          return data

     def __str__(self):
          return str(self.getinfo())
        #  if len(self._info) < 1:
        #       output = "This is {}'s data who is in the department {}".format(self._name,self._dept)
      #    else :
          #     moreoutput = ""
            #   for data in self._info:
           #         moreoutput += "{} => {}\n".format(self._info[data],data)
              # output = """
              #                This is {}'s data who is in the department {}\n
              #                with the follow extra info\n{}
              #                """.format(self._name, self._dept, moreoutput)
               
           #    return output




     
"""******** Class to intantiate a Course **********"""
"""
          name :: this is the name of the course
          code :: this is course code
          score :: this the score allocated to the course
          cu :: this is the credit load of the course
          grade :: this is the grade of the course -- it is set only when setscore() is passed a parameter
          
"""
class Course:
    
     cname = str()
     _score = int()
     _code = str()
     _grade = str()
     _cu = int()
     passed = False;
     
     def __init__(self, name, code, cu):
          self.cname = name
          self._code = code
          self._cu = cu
           
     def getgrade(self): 
          return self._grade

     def setscore(self, score):
          self._score = score
          if self._score <= 39 and self._score >= 0 :
               grade = 'F'
          elif self._score<= 45 and self._score >= 40:
               grade = 'E'
          elif self._score <= 49 and self._score >=46:
               grade = 'D'
          elif self._score <=59 and self._score >=50:
               grade = 'C'
          elif self._score <=69 and self._score >=60:
               grade = 'B'
          elif self._score >= 70:
               grade = 'A'
          else:
               grade = False
               raise "Improper value for score inserted"
          self._grade = grade
          
     def getgp(self):
          grade = self._grade
          if grade == "a" or grade == "A": self.passed = True; return 5
          if grade == "b" or grade == "B": self.passed = True; return 4
          if grade == "c" or grade == "C": self.passed = True; return 3
          if grade == "d" or grade == "D": self.passed = True; return 2
          if grade == "e" or grade == "E": self.passed = True; return 1
          if grade == "f" or grade == "F": return 0

     def getcu(self):
          return self._cu

"""******** Class to intantiate a Semester**********"""
"""
     sem :: this is the semester the course was registered
     courses :: this is a list of courses
     
"""
class StudentData(Student,Course):
     
     _sem = int()
     courses = []
     
     def __init__(self, name, dept, sem, courses):
          self._sem = sem
          self.courses = courses
          super().__init__(name,dept)

     def getnoc(self):
          return len(self.courses)

     def gettotalcu(self):
          total = 0
          for course in self.courses:
               total += course.getcu()
          return total

     def getgpa(self):
          qp = []
          for course in self.courses:
               course.setscore(int(input("Enter Score for {}: ".format(course.cname))))
               if course.getgp() == 0: continue
               qp.append(course.getgp() * course.getcu())
          return qp

     def getfailedcourses(self):
          failed =[]
          for course in self.courses:
               if course.passed:
                    continue
               else:
                    failed.append(course.cname)
          return failed
     

def insertCourses():
     courses = []
     x = True
     while x:
            print("Enter Course: ")
            name = input("\tEnter Name: ")
            code = input("\tEnter Course Code: ")
            cu = int(input("\tEnter Credit Unit: "))
            courses.append(Course(name,code,cu))
            x = int(input(".....to continue, Press \"1\" else Press \"0\"..... "))
     return courses

def insertScore(x):
     for course in x.courses:
          course.setscore(int(input("enter score for {} : ".format(course.cname.upper() ))))

def present():
     data = []
     courses = []
     questions = ["Name", "Department","Semester", "Courses"]
     
     for question in questions:
          if question == "Courses" :
               courses = insertCourses()[:]
               data.append(courses)
          else :
               data.append(input("Enter {}: ".format(question)))

     data[2] = int(data[2])
     if (len(data) < 4): return False

     student1 = StudentData(*data)
     insertScore(student1)
     print(student1)
     return True




present();
#v = [Course("fd","feds",3), Course("fd2","3ed",2)]
#x = StudentData("Treasure", "Maths",1,v)


#print(x)

