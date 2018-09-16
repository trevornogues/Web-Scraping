#Open random wikipedia pages
from urllib.request import urlopen 
from bs4 import BeautifulSoup 
import re
import random

pages = set()
randomNum = random.randint(0,100)

def getLinks(pageUrl, depth):
    if depth == randomNum:
        print("Wiki Page #", (depth +1), ":", pageUrl[6:])
        print()
        print("Wow!", randomNum+1,  "degrees of separation, or should I say", randomNum+1, "links of \n separation landed you on the Wikipedia page for " + pageUrl[6:] +"!")
    elif depth < randomNum:
        print("Wiki Page #", (depth +1), ":", pageUrl[6:])
        global pages
        html = urlopen("https://en.wikipedia.org"+pageUrl)
        bsObj = BeautifulSoup(html, "html.parser")
        link = random.choice(bsObj.findAll("a", href=re.compile("^(/wiki/)")))
        if link.attrs['href'] not in pages: 
            newPage = link.attrs['href'] 
            pages.add(newPage) 
            getLinks(newPage, depth + 1)
        
print()
print("Welcome!")
print()
article = input("Enter the link of your favorite actor Firstname_Lastname (example: Ashton_Kutcher): ")
                
print(randomNum) 

getLinks("/wiki/"+article, 0) 