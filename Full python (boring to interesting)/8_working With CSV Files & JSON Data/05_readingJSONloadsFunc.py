import json

# json string always use double quotes ("").
stringsOfJsonData = '{"name": "Zophie", "isCat": "true", "miceCaught": 0, "feline": null}'

jasonDataAsPythonValue = json.loads(stringsOfJsonData)
print(jasonDataAsPythonValue)