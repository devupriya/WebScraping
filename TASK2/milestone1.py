import os
import requests
from bs4 import BeautifulSoup
directory = "milestone11"
parent_dir = "C:\\Users\\Rajan\\Desktop\\joy projects\\undone\\ID_568_3500\\"
path = os.path.join(parent_dir, directory)
os.mkdir(path)
print("Directory '% s' created" % directory)
url = 'https://www.griffith.ie/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
 
urls = []
i = 0
for link in soup.find_all('a'):
    if "https:" in str(link.get('href')):
       if i < 22 :
            i += 1
            r = requests.get(link.get('href')) 
            name = "C:\\Users\\Rajan\\Desktop\\joy projects\\undone\\ID_568_3500\\milestone11\\D" + str(i) + ".txt"
            f = open(name, "a")
            f.write(str(r.content))
print("The operation has been done"); 
           
       
    



