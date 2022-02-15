import json
qutesList=[]
quoteItem1={}
quoteItem1['cloth']="хлопок"
quoteItem1['postive']="Легкий, легко пропускает воздух, прочный, хорошо переносит стирку"
quoteItem1['negative']="Легко окрашивается, сминается, выцветает, быстро изнашивается"
qutesList.append(quoteItem1)


jsonString = json.dumps(qutesList, ensure_ascii=False)
jsonFile = open("data.json", "w", encoding="UTF-8")
jsonFile.write(jsonString)
jsonFile.close()