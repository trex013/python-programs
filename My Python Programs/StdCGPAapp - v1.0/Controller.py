from Model import Model as model
from Ui import Ui as ui
from Request import Request as request

class Controller:
     def __init__(self):
          self.model = model()
          self.ui = ui()
          self.ui.newSession()
          self.requestHandler()

     def requestHandler(self):
          self.request = request(self.ui, self.model)
          self.listenForRequest()

     def listenForRequest(self):
          # Prints out the Menu Request
          entry = self.ui.showMenu(self.request.getRequests())
          
          # Checks for the exit Option
          if entry == 0:
               self.request.exit()
               del(self.ui, self.model, self.request)
               return True
          
          # Performs the menu selected
          self.request.fireRequest(entry)

          # to create the loop
          self.requestHandler()
          
          
          
          
Controller()
