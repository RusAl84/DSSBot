import json
from getKeywords import getKeywords 
from printJson import printJson


def getCloth(str1, state="positive"):
    fileObject = open("data3.json", "r", encoding="UTF-8")
    jsonContent = fileObject.read()
    aList = json.loads(jsonContent)
    keywords1=getKeywords(str1)
    print(keywords1)
    nList=[]
    cSet=set()
    for item in aList:
        countIntersections=0
        if state=="negative":
            keywords2=item['nkeywords']        
        if state=="positive":
            keywords2=item['pkeywords']
        for i1 in keywords1:
            for i2 in keywords2:
                if i1==i2:
                    countIntersections+=1
        item['countIntersections']=countIntersections
        nList.append(item)
        cSet.add(countIntersections)
    ciMax=max(list(cSet))
    qList=[]
    print(ciMax)
    for item in nList:
        if item['countIntersections']==ciMax:
            qList.append(item)
            # print(item['text'])
    # return qList
    str2=printJson(qList)
    return str2
    # print(qList)


if __name__ == '__main__':
    str1="/p легко хорошо пропускает воздух"
    str2 =getCloth(str1)
    print(str2)


