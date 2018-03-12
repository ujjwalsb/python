# !/usr/bin/python3
# 07_lucky.py - Opens several Google Search Results.

import requests, sys, webbrowser, bs4

print('Googling.....')
res = requests.get('https://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()


# Retrieve top results link.
soup = bs4.BeautifulSoup(res.text,'html.parser')

# open a browser tab for each results.

''' Inspect the element from google search, every main link is under
	<h3 class="r"> so we will consider this.
	We cannot take <a href=""> because every small links have that,
	and we don't want to open that.'''

linkElems = soup.select('.r a')		# To find all <a> in class r of CSS.

numOpen = min(5, len(linkElems))
for i in range(numOpen):
	webbrowser.open('https://google.com' + linkElems[i].get('href'))