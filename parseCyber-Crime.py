import urllib2
from BeautifulSoup import BeautifulSoup
from datetime import date
from datetime import timedelta


control = True
while control:
    print " The Last 10 Days: "
    url = "http://cybercrime-tracker.net/index.php"
    soup = BeautifulSoup(urllib2.urlopen(url).read())
    
    x = soup.findAll('tbody')
    for row in x:
        y = soup.findAll('tr')
        for td in y:
            dates = td.findAll('td')[0]
            date_splitted  = dates.text.split("-")
            
            domain_column = td.findAll('td')[1]
            domain=domain_column.text.split("/",1)[0]
            
            if len(date_splitted)>2: 
                time = date(int(date_splitted[2]), int(date_splitted[1]), int(date_splitted[0])) 
                today = date.today()
                
                if time > (today - timedelta(days=10)) :
                    print dates.text +"\t|\t"+domain.replace("www.","")+"\n",
                else:
                    control=False
                    break
                
                
