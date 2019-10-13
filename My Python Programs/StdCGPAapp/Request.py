class Request:
     __requests = {}
     def __init__(self, ui, model):
          self.ui = ui
          self.model = model
          self.getRequestList()

     def getRequestList(self):
          i=0
          for key, value in enumerate(vars(Request)):
               if value.find("__") == -1 and value.find("getRequest") == -1 and value.find("fireRe"):
                    self.__requests[i] = value
                    i += 1
                    
     def getRequests(self):
          return self.__requests

     def fireRequest(self, requestId):
          getattr(self, self.__requests[requestId])()

     def exit(self):
          print("Thanks for using this app\nBye!!....")
          
     def createNewRecord(self):
          rec = self.ui.retrieveRecordFromUser()
          success = self.model.addRecord(rec)
          self.ui.report(1,success.id)
          
     def displayRecords(self):
          data = self.model.getRecords();
          if data != []:
               self.ui.showRecords(data)
          else :
               self.ui.report(2, "\n*****Error:: No Records available******")
     
     def displayRecord(self):
          _id = self.ui.getRecordId()
          data = self.model.getRecord(_id)
          if data:
               self.ui.showRecord(data)
          else :
               self.ui.report(2,"\n*****Error:: Record not found******")
          
          
     def dummy(self):
          print("Request firing is working")
          
