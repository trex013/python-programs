
class Ui:

     cols = [
          "first-name",
          "last-name",
          "date of birth",
          "Department",
          "current level",
          "mat-no",
          "course-details"
     ]

     courseDetails = [
          "course code",
          "course title",
          "credit unit",
          "score"
     ]

     data = {"course-details":[]}

     def h1(strng):
          Ui.nl()
          Ui.hr()
          print ("{}".format(strng).title().center(54," "))
          Ui.hr()

     def center(strng):
          print ("{}".format(strng).title().center(54," "))
          
     def sep(strng):
          cnt = 0
          newS = ""
          for i in strng:
               if i.isupper():
                    newS += " "+i
               else :
                    newS += i
          return newS

     def hr():
          print ("******"*6)

     def nl():
          print("\n")


     def prompt(msg):
          return input("\n-> {}:: ".format(msg))

     def alert(msg):
          print("\n-> {}**".format(msg))

     def get(msg, tabsize = 3):
          return input("\tEnter {}: ".format(msg).expandtabs(tabsize))
     
     def newSession(self):
          print("App has started...")

     def getCourses(self):     
          courses = []
          while True:
               course = {}   
               for cd in self.courseDetails:
                    if cd == "score":
                         val = Ui.prompt("Do you want to enter Score now (y/n)")
                         if val != "y" and val != "Y":
                              course[cd] = 0
                              continue
                    course[cd] = Ui.get(cd.title())
               courses.append(course)
               val = Ui.prompt("Do you want to enter another course now (y/n)")
               if val == "n" or val == "N":
                    break
               
          return courses
     
     def retrieveRecordFromUser(self):   
          Ui.h1("get user input")
          for col in self.cols:
               if col == "course-details":
                    val = Ui.prompt("Do you want to enter Course Details now (y/n)")
                    if val == "y" or val == "Y":
                         Ui.h1(col.title())
                         self.data[col] = self.getCourses()
               else :
                    self.data[col] = Ui.get(col.title())
                    
          return self.data
          
     def showMenu(self, events):
          Ui.h1("Menu")
          for key in events:
               print("Press: {} to {}".format(key, Ui.sep(events[key]).title()))
          Ui.hr()          
          return int(input(">> "))

     def showAvaiableId(self):
          pass

     def showRecord(self, rec):
          Ui.nl()
          Ui.hr()
          Ui.nl()
          for key in rec.data:
               print("\t".expandtabs(2), "{} : {}".format(key.title(),rec.data[key]))
          Ui.nl()
          Ui.hr()

     def showRecords(self, data):
          #[data->id,data, ]
          Ui.h1("all records")
          for rec in data:
               print("\t".expandtabs(2), "{}. ".format(rec.id),end="")
               tab = "\t".expandtabs(1)
               for key in rec.data:
                    print(tab+"| {} : {}".format(key.title(),rec.data[key]))
                    tab = "\t".expandtabs(8)
               Ui.nl()
          Ui.hr()
     
     def getRecordId(self):
          return int(Ui.prompt("Enter Record Id: "))
     
     def report(self, type_,msg):
          if type_ == 1:
               Ui.alert("Id: {} has been entered successfully. ".format(msg))
          if type_ == 2:
               Ui.alert(msg.title())


#Ui().report(1,"Hi")
x = Ui().retrieveRecordFromUser()
print(x)
               
