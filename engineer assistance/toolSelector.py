from filesDo import CsvCodes

csvFile=CsvCodes()

class ToolSelector():
  def __init__(self):
    self.listOfStraight=csvFile.loadCsv("toolsAmpermostaghim.csv")
    self.listOfSM=csvFile.loadCsv("toolsAmperSM.csv")
  
  def find_closest_numbers(self,numbers, reference):
    larger_numbers = [num for num in numbers if num > reference]
    smaller_numbers = [num for num in numbers if num < reference]
    
    closest_larger = None
    closest_smaller = None
    result = []
    if larger_numbers:
        closest_larger = min(larger_numbers, key=lambda x: x - reference)
        result=closest_larger
    
    if closest_larger and (closest_larger - reference > 40):
        closest_smaller = max(smaller_numbers) if smaller_numbers else None
        result=closest_smaller
    if reference >= 500:
        result=closest_larger
      
    if reference in numbers:
      result= reference
      
    return result
  def get_tools(self, kw=0.37,hp=0.5,voltage=220,way="straight"):
    toolsData=[]
    toolselected=[]
    systemNeeds=''
    if way=="sm":
       toolsData= self.listOfSM[1]
    elif way == "straight":
      toolsData= self.listOfStraight[1]
    else:
      return "your way is not recognized"
    voltageSelected=0
    if voltage ==320:
     voltageSelected = 1
    elif voltage == 420:
      voltageSelected=2
      
    for tool in toolsData:
     if tool[voltageSelected]!= '0':
       numbers = tool[voltageSelected].split('_')
       if numbers[0]== str(kw) or numbers[1]== str(hp) :   
        systemNeeds = f"{numbers[0]}_{numbers[1]}"
        
    
    for tool in toolsData:
     if tool[voltageSelected] == systemNeeds:
       toolselected=tool[3:]
    if toolselected:
      return [f"contactor = {toolselected[0]} , bmetal = {toolselected[1]} and feus = {toolselected[2]}",toolselected]
    else:
      return ["with this voltage you cant use this KW and HP in yor system",[]]
  
       

    
    
tools=ToolSelector()
print(tools.get_tools(voltage=420 ,kw=290 , hp=400))