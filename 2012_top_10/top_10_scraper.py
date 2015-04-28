from bs4 import BeautifulSoup
import requests

page = requests.get('http://www.daemonology.net/hn-daily/2012-12.html')
soup = BeautifulSoup(page.text)
h2s = soup.find_all('h2', { 'class':'' })
uls = soup.find_all('ul')

number = len(h2s)

for i in xrange(number):
	print '<date>' + h2s[i].string + '</date>'
	heads = uls[i].find_all('span', { 'class':'storylink'})
	for j in xrange(len(heads)):
	# for head in heads:
		data = heads[j].a.string
		udata=data.encode("utf-8").strip()
		asciidata=udata.decode("ascii","ignore")
		print '\t' + '<rank>' + `j` + '</rank>' + ' <title>' + asciidata + '</title>'