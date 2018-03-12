# ! /usr/bin/python3
# Downloads every single XKCD Comic.

import requests, os, bs4

url = 'http://xkcd.com'
os.makedirs('08_example_folder', exist_ok=True)

while not url.endswith('#'):
	# Download the page.
	print('Downloading the page %s...' %url)
	res = requests.get(url)
	res.raise_for_status()

	soup = bs4.BeautifulSoup(res.text, 'html.parser')

	# Find the URL of comic image.
	comicElem = soup.select('#comic img')
	if comicElem == []:
		print('could not find comic image.')
	else:
		comicUrl = comicElem[0].get('src')

		# Download the image.
		print('Downloading the image %s...' %(comicUrl))
		res = requests.get('http:'+comicUrl)
		res.raise_for_status()

		# Save the image to the folder.
		imageFile = open(os.path.join('08_example_folder', os.path.basename(comicUrl)), 'wb')
		for chunk in res.iter_content(100000):
			imageFile.write(chunk)
		imageFile.close()

	# Get previous button's url.
	prevLink = soup.select('a[rel="prev"]')[0]
	url = 'http://xkcd.com' + prevLink.get('href')

print('Done')