import requests, bs4

res = requests.get('http://nostarch.com')
res.raise_for_status()

noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
print(type(noStarchSoup))



# ===============================================================
# If there is a html file in the directory.

exampleFile = open('exampleOf_05_createBeautifulSoupObject.html')
exampleSoup = bs4.BeautifulSoup(exampleFile, 'html.parser')
print(type(exampleSoup))