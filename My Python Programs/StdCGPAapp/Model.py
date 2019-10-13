class Model:
     __records = []
     
     def addRecord(self, rec):
          _id = len(self.__records) + 1
          self.__records.append(Data(_id,**rec))
          return self.__records[-1]

     def getRecord(self, _id):
          ids = []
          for rec in self.__records:
               ids.append(rec.id)
               
          if _id in ids:
               loc = ids.index(_id)
               return self.__records[loc]
          return False

     def getRecords(self):
          return self.__records

class Data:
     def __init__(self, id_,**kargs):
          self.id = id_
          self.data = kargs
          

