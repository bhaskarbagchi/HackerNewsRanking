from bs4 import BeautifulSoup
import requests

for i in xrange(28):
	name = 'https://news.ycombinator.com/news?p='
	page = requests.get(name +`(i+1)`)

	soup = BeautifulSoup(page.text)

	headings = soup.find_all('tr', { 'class':'athing' })
	comments = soup.find_all('td', { 'class':'subtext'})

	for i in xrange(len(headings)):
		if headings[i].span:
			print headings[i].span.string.strip()
		xx = headings[i].find_all('a')
		for x in xx:
			if x.parent.name == 'td':
				data = x.string
				udata=data.encode("utf-8").strip()
				asciidata=udata.decode("ascii","ignore")
				print asciidata
		if comments[i].span:
			print comments[i].span.string
		xx = comments[i].find_all('a')
		for x in xx:
			print x.string
