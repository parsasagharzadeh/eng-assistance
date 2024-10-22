
from filesDo import CsvCodes
csvFile = CsvCodes()
class PriceCalculator():
  def __init__(self):
    self.PriceList=csvFile.loadCsv("toolsPrice.csv")
    
  def getToolsPrice(self,toolname,model,amount):
    toolsList=[]
    toolRow=0
    if toolname == "bmetal":
      toolRow=2
    elif toolname == "feus":
      toolRow=4
    elif toolname=="cable" :
      toolRow=6
      
    for item in self.PriceList[1]:
      
      if item[toolRow]==model:
       toolsList.append([item[toolRow],int(item[toolRow+1])*amount])
       
    else:
      print("this tool didnt find") 
    
    # return[f"your list is {toolsList[0]} that worth {toolsList[1]} toman",toolsList]
    print(f"your list is {toolsList[0][0]} {toolname} model {model} amper  that worth {toolsList[0][1]} toman")
    return toolsList[0]
        
price_calculator = PriceCalculator()
print(price_calculator.getToolsPrice("contactor","95",14))
      