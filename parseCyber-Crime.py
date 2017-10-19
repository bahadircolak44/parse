import urllib2
from BeautifulSoup import BeautifulSoup

url = "http://cybercrime-tracker.net/index.php"
soup = BeautifulSoup(urllib2.urlopen(url).read())
x = soup.findAll('tbody')
for row in x:
    y = soup.findAll('tr')
    for td in y:
        first_column = td.findAll('td')[1]
        print first_column.text
