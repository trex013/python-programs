import CGPA
import os
class file_handler :
     """A file class that defines a file object with creating, editing, deleting, encrypting and decrypting of data"""
     def getfilename(self, data):
          """C"""
          self.data = data
          pos = self.data.find("Name:")
          epos = self.data.find("\n", pos)
          self.file_name = self.data[pos+5:epos]
          
     def store_new (self,data_to_be_stored):
          """Creates a new file with name 'file name'"""
          self.getfilename(data_to_be_stored)
          self.file_name += ".txt"
          stud = open(self.file_name, 'w')
          stud.write(data_to_be_stored)
          stud.close()

     def retrieval(self,file_to_be_retrieved):
          """Retrieves the file"""
          file = file_to_be_retrieved + ".txt"
          stud = open(file, 'r')
          data = stud.read()
          self.filecontent = data

     def delete_file(self, file):
          """deletes file of person"""
          os.remove(file)
          
     def check (self, data):
          """Checks directory"""
          files = {}; i = 1
          with os.scandir("./") as it:
               for entry in it:
                    if not entry.name.startswith('.') and entry.is_file():
                         file[i] = entry.name
                         i += 1
                         

          
          
#c = CGPA.output
x = file_handler()
h = "i love jesus"
x.store_new("Trex")
