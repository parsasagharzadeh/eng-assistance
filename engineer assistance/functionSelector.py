from filesDo import CsvCodes 
file= CsvCodes()
import inspect


class FuncSelector():
  def __init__(self):
    self.methodNames=[]
    self.listOfFunction=[]
    
  def saveMethodsInfo(self,cls):
    # استخراج متدها و فیلتر کردن فقط متدهای عمومی
    self.methodNames=[name for name, obj in inspect.getmembers(cls, predicate=inspect.isfunction) if not name.startswith('_')]
    file.saveCsv("functions.csv",[1,2,3,4,5,6,7,8],[self.methodNames,self.update_methodes_name()])
    return [self.methodNames,self.update_methodes_name()]  
  def update_methodes_name(self):
    myClass= FuncSelector()
    for methodName in self.methodNames:
      method = getattr(myClass, methodName)  
      self.listOfFunction.append(method)
    return self.listOfFunction
      
  def addFunc(self,functionName,function,params):
    data = [functionName,function,[params]]
    self.functions.append(data)
    
    state=file.saveCsv("functions.csv",["data"],self.functions)
    if state:
      return "function added to list"
    else:
      return "function could not add to list"
    
  def selectFunction(self,functionName,params):
   
   for item in self.functions:
     if item[0] == functionName:
      if len(file.exportList(item[2]))>0:
        return self.listOfFunction[int(item[1])](params)
      else:
        return self.listOfFunction[int(item[1])]()
     

select = FuncSelector()
# select.addFunc("add",1,"numbers")
print(select.saveMethodsInfo(FuncSelector)[1][-1]
)
