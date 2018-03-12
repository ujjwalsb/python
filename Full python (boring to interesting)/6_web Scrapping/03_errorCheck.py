import requests

res = requests.get('http://www.inventwithpython.com/page_that_does_not_exist')

try:
	res.raise_for_status()
except Exception as exc:
	print('There was a problem: %s' % (exc))