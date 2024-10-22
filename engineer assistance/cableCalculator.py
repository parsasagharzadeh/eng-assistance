
from filesDo import CsvCodes
csvFile = CsvCodes()
class CableCUL():
  def __init__(self):
    self.cableInfo=csvFile.loadCsv("cableAmper.csv")
    self.lastAmper=0
    self.lastDistance=0
  def addCableWithAmper(self,size=1.5,amper=[]):
    cable=[]
    rowName=[0,10,50,100,150,200,250,300,350,400,450,500,600,700,800,900,1000]
    cable.append(str(size))
    for amper in amper:
      cable.append(str(amper))
      
    print(cable)
      # csvFile.save("cableAmper.csv",rowName,cable)
    
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
   
    
  def getSize(self,amper=5,distance=10):
    self.lastAmper=amper
    self.lastDistance=distance
    cableDistances =[0,10,50,100,150,200,250,300,350,400,450,500,600,700,800,900,1000] 
    distanceSelected =self.find_closest_numbers(cableDistances,distance)
    distanceIndex = cableDistances.index(distanceSelected)
    ampers=[int(ampers[distanceIndex]) for ampers in self.cableInfo[1:][0]]
    amperSelected=self.find_closest_numbers(ampers,amper)
    amperIndex = ampers.index(amperSelected)
    cableSelectedSize = self.cableInfo[1][amperIndex][0]
    print(cableSelectedSize)
  
  def returnCableList(self):
    print(self.cableInfo[1][0])
    
    
cable=CableCUL()
# cable.addCableWithAmper(1.5,[27,15,7,5,0,0,0,0,0,0,0,0,0,0,0,0])
cable.getSize(85,50)