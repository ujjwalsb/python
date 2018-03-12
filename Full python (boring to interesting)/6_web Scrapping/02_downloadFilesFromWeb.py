import requests

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')

print(type(res))
res.status_code == requests.codes.ok
print(len(res.text))

print(res.text[:250])