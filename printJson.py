import json

def printJson(aList):
    str1=""
    for item in aList:
        # cloth=item['cloth']
        str1+="\n"+"Вид ткани: " + item['cloth'] +" \n Достоинства: " +item['positive']+" \n Недостатки: "+ item['negative']
    return str1
        
if __name__ == '__main__':
    aList=[]
    fileObject = open("data3.json", "r", encoding="UTF-8")
    jsonContent = fileObject.read()
    aList = json.loads(jsonContent)
    print(printJson(aList))   