import urllib2
from BeautifulSoup import BeautifulSoup

temp=0
count=0
total=""
while(count<160):
    url = "http://cybercrime-tracker.net/index.php?s="+str(count)+"&m=40"
    temp=temp+1
    print "\n"+str(temp)+". Page:"
    count=count+40
    soup = BeautifulSoup(urllib2.urlopen(url).read())
    x = soup.findAll('tbody')
    for row in x:
        y = soup.findAll('tr')
        for td in y:
            first_column = td.findAll('td')[1]
            a=first_column.text.split("/",1)[0]
            print a.replace("-::URL","")
            total+= a + "\n"
#print total
