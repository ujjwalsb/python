import json

pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'feline': None}

stringOfJsonData = json.dumps(pythonValue)
print(stringOfJsonData)