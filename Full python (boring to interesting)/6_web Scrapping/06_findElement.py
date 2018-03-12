import bs4

exampleFile = open('exampleOf_05_createBeautifulSoupObject.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')
elems = exampleSoup.select('#author')	# or select('p')

print(type(elems))			# <type 'list'>
print(len(elems))			# 1
print(type(elems[0]))		# <class 'bs4.element.Tag'>
print(elems[0].getText())	# Ujjwal Singh Baghel
print(str(elems[0]))		# <span id="author">Ujjwal Singh Baghel</span>
print(elems[0].attrs)		# {u'id': u'author'}


spanElem = exampleSoup.select('span')[0]

print(str(spanElem))		# <span id="author">Ujjwal Singh Baghel</span>
print(spanElem.get('id'))	# author
print(spanElem.get('some_nonexistent_addr')) == None 	# True
print(spanElem.attrs)		# {u'id': u'author'}