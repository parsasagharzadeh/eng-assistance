import csv
import json
import ast

class CsvCodes:
  def __init__(self) :
    pass
  def exportList(self,list):
    return ast.literal_eval(list)
  def saveCsv(self, fileName,rowName,data):
    file= open(fileName,"w",newline="")
    writer=csv.writer(file)
    writer.writerow(rowName)
    writer.writerows(data)
    file.close()
    return True
  def loadCsv(self,fileName):
    file=open(fileName)
    data=csv.reader(file)
    header=next(data)
    output=[]
    for info in data:
      
      output.append(info)
    file.close()
    return [output]
  
  def saveJson(self,fileName,dataDic):
    dicData = json.dumps(dataDic)
    with open(fileName,'w') as jsonFile:
     json.dump(dicData,jsonFile)
  
          
  def loadJson(self,fileName):
    data=[]
    with open('functions.json', 'r') as json_file:
      data =json.load(json_file)
      data =json.loads(data)

    return data
  
    