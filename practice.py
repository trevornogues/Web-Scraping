# Web Scraping Independent Project


# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# html = urlopen("http://pythonscraping.com/pages/page1.html")
# bsObj = BeautifulSoup(html.read(), "html.parser")
# print(bsObj.h1)

# try:
#     html = urlopen("http://www.pythonscraping.com/pages/page1.html")
#     except HTTPError as e: print(e)
#         return null, break, or do some other "Plan B"
#     else: #program continues. Note: If you return or break in the #exception catch, you do not need to use the "else" statement

#     if html is None:
#          print("URL is not found")
#     else: #program continues
    
# try:
#     badContent = bsObj.nonExistingTag.anotherTag
# except AttributeError as e: 
#     print("Tag was not found")
# else:

#     if badContent == None:
#         print ("Tag was not found")
#     else: 
#         print(badContent)

# from urllib.request import urlopen 
# from urllib.error import HTTPError 
# from bs4 import BeautifulSoup
# def getTitle(url): 
#     try:
#         html = urlopen(url) 
#     except HTTPError as e:
#         return None 
#     try:
#         bsObj = BeautifulSoup(html.read(), "html.parser")
#         title = bsObj.body.h1 
#     except AttributeError as e:
#         return None 
#     return title
#     title = getTitle("http://www.pythonscraping.com/pages/page1.html") 
#     if title == None:
#         print("Title could not be found") 
#     else:
#         print(title)

# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html") 
# bsObj = BeautifulSoup(html.read(), "html.parser")
    
# nameList = bsObj.findAll("span", {"class":"green", "class":"red"})
# for name in nameList:
#     print(name.get_text())

# nameList = bsObj.findAll(text="the prince") 
# print(len(nameList))

# allText = bsObj.findAll(id="text") 
# print(allText[0].get_text())

# from urllib.request import urlopen
# from bs4 import BeautifulSoup

# html = urlopen("http://www.pythonscraping.com/pages/page3.html")
# bsObj = BeautifulSoup(html, "html.parser")

# for child in bsObj.find("table",{"id":"giftList"}).children:
#     print(child)

# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# html = urlopen("http://www.pythonscraping.com/pages/page3.html") 
# bsObj = BeautifulSoup(html, "html.parser")

# for sibling in bsObj.find("table",{"id":"giftList"}).tr.next_siblings: 
#     print(sibling)

# from urllib.request import urlopen 
# from bs4 import BeautifulSoup
# html = urlopen("http://www.pythonscraping.com/pages/page3.html") 
# bsObj = BeautifulSoup(html, "html.parser") 
# print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"
#                         }).parent.previous_sibling.get_text())

# from urllib.request import urlopen 
# from bs4 import BeautifulSoup 
# import re

# html = urlopen("http://www.pythonscraping.com/pages/page3.html")
# bsObj = BeautifulSoup(html, "html.parser")
# images = bsObj.findAll("img", {"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")}) 
# for image in images:
#     print(image["src"])

# from urllib.request import urlopen 
# from bs4 import BeautifulSoup
# import re
# html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon") 
# bsObj = BeautifulSoup(html, "html.parser")
# for link in bsObj.find("div", {"id":"bodyContent"}).findAll("a",
#                         href=re.compile("^(/wiki/)((?!:).)*$")):
#     if 'href' in link.attrs: 
#         print(link.attrs['href'])

# from urllib.request import urlopen 
# from bs4 import BeautifulSoup 
# import datetime
# import random
# import re

# random.seed(datetime.datetime.now()) 
# def getLinks(articleUrl):
#     html = urlopen("http://en.wikipedia.org"+articleUrl)
#     bsObj = BeautifulSoup(html,"html.parser")
#     return bsObj.find("div", {"id":"bodyContent"}).findAll("a",
#                          href=re.compile("^(/wiki/)((?!:).)*$"))
# links = getLinks("/wiki/Jerry_Bilik")
# while len(links) > 0:
#     newArticle = links[random.randint(0, len(links)-1)].attrs["href"] 
#     print(newArticle)
#     links = getLinks(newArticle)

from urllib.request import urlopen 
from bs4 import BeautifulSoup 
import re

pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen("http://en.wikipedia.org"+pageUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages: #We have encountered a new page
                newPage = link.attrs['href'] 
                print(newPage) 
                pages.add(newPage) 
                getLinks(newPage)
getLinks("")


# from urllib.request import urlopen 
# from bs4 import BeautifulSoup 
# import re

# pages = set()
# def getLinks(pageUrl):
#     global pages
#     html = urlopen("http://en.wikipedia.org"+pageUrl) 
#     bsObj = BeautifulSoup(html, "html.parser")
#     try:
#         print(bsObj.h1.get_text())
#         print(bsObj.find(id ="mw-content-text").findAll("p")[0]) 
#         print(bsObj.find(id="ca-edit").find("span").find("a").attrs['href'])
#     except AttributeError:
#         print("This page is missing something! No worries though!")
#     for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")): 
#         if 'href' in link.attrs:
#             if link.attrs['href'] not in pages: #We have encountered a new page 
#                 newPage = link.attrs['href'] 
#                 print("----------------\n"+newPage) 
#                 pages.add(newPage)
#                 getLinks(newPage)
# getLinks("")

# from urllib.request import urlopen 
# from bs4 import BeautifulSoup 
# import re
# import datetime
# import random

# pages = set()
# random.seed(datetime.datetime.now())

#  #Retrieves a list of all Internal links found on a page
# def getInternalLinks(bsObj, includeUrl):
#     internalLinks = []
#     #Finds all links that begin with a "/"
#     for link in bsObj.findAll("a", href=re.compile("^(/|.*"+includeUrl+")")):
#         if link.attrs['href'] is not None:
#             if link.attrs['href'] not in internalLinks:
#                 internalLinks.append(link.attrs['href']) 
#     return internalLinks

# #Retrieves a list of all external links found on a page
# def getExternalLinks(bsObj, excludeUrl):
#     externalLinks = []
#     #Finds all links that start with "http" or "www" that do 
#     #not contain the current URL
#     for link in bsObj.findAll("a",
#                             href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")): 
#         if link.attrs['href'] is not None:
#             if link.attrs['href'] not in externalLinks: 
#                 externalLinks.append(link.attrs['href'])
#     return externalLinks

# def splitAddress(address):
#     addressParts = address.replace("http://", "").split("/") 
#     return addressParts

# def getRandomExternalLink(startingPage):
#     html = urlopen(startingPage)
#     bsObj = BeautifulSoup(html, "html.parser")
#     externalLinks = getExternalLinks(bsObj, splitAddress(startingPage)[0]) 
#     if len(externalLinks) == 0:
#         internalLinks = getInternalLinks(startingPage)
#         return getNextExternalLink(internalLinks[random.randint(0,
#                                 len(internalLinks)-1)])
#     else:
#         return externalLinks[random.randint(0, len(externalLinks)-1)]

# def followExternalOnly(startingSite):
#     externalLink = getRandomExternalLink("http://oreilly.com") 
#     print("Random external link is: "+externalLink) 
#     followExternalOnly(externalLink)

# followExternalOnly("http://oreilly.com")

#  Collects a list of all external URLs found on the site
# allExtLinks = set()
# allIntLinks = set()
# def getAllExternalLinks(siteUrl):
#     html = urlopen(siteUrl)
#     bsObj = BeautifulSoup(html, "html.parser")
#     internalLinks = getInternalLinks(bsObj,splitAddress(siteUrl)[0]) 
#     externalLinks = getExternalLinks(bsObj,splitAddress(siteUrl)[0]) 
#     for link in externalLinks:
#         if link not in allExtLinks: 
#             allExtLinks.add(link) 
#             print(link)
#     for link in internalLinks:
#         if link not in allIntLinks:
#             print("About to get link: "+link) 
#             allIntLinks.add(link) 
#             getAllExternalLinks(link)
# getAllExternalLinks("http://oreilly.com")

# from urllib.request import urlretrieve
# from urllib.request import urlopen
# from bs4 import BeautifulSoup

# html = urlopen("http://www.pythonscraping.com")
# bsObj = BeautifulSoup(html, "html.parser")
# imageLocation = bsObj.find("a", {"id":"logo"}).find("img")["src"]
# urlretrieve (imageLocation, "logo.jpg")

# import os
# from urllib.request import urlretrieve
# from urllib.request import urlopen
# from bs4 import BeautifulSoup

# downloadDirectory = "downloaded"
# baseUrl = "http://pythonscraping.com"

# def gertAbsoluteURL(baseUrl, source):
#     if source.startswith("http://www."):
#         url = "http://"+source[11:]
#     elif source.startswith("http://"):
#         url = source
#     elif source.startswith("www."):
#         url = source[4:]
#         url = "http://"+source
#     else:
#         url = baseUrl+"/"+source
#     if baseUrl not in url:
#         return None
#     return url

# def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):
#     path = absoluteUrl.replace("www.","")
#     path = path.replace(baseUrl,"")
#     path = downloadDirectory+path
#     directory = os.path.dirname(path)

#     if not os.path.exists(directory):
#         os.makedirs(directory)

#     return path


# html = urlopen("http://www.pythonscraping.com")
# bsObj = BeautifulSoup(html, "html.parser")
# downloadList = bsObj.findAll(src=True)


# for download in downloadList:
#     fileUrl = getAbsoluteURL(baseUrl, download["src"]) 
#     if fileUrl is not None:
#         print(fileUrl)

# urlretrieve(fileUrl, getDownloadPath(baseUrl, fileUrl, downloadDirectory))

# import csv

# csvFile =  open("../files/test.csv", 'w+')
# try:
#     writer = csv.writer(csvFile)
#     writer.writerow(('number','number plus 2','number times 2'))
#     for i in range(10):
#         writer.writerow((i,i+2,i*2))
# finally:
#     csvFile.close()

# import csv
# from urllib.request import urlopen 
# from bs4 import BeautifulSoup

# html = urlopen("http://en.wikipedia.org/wiki/Comparison_of_text_editors") 
# bsObj = BeautifulSoup(html,"html.parser")
# table = bsObj.findAll("table",{"class":"wikitable"})[0]
# rows = table.findAll("tr")

# csvFile = open("../files/editors.csv", 'wt')
# writer = csv.writer(csvFile)

# try:
#     for row in rows:
#         csvRow = []
#     for cell in row.findAll(['td', 'th']):
#         csvRow.append(cell.get_text())
#         writer.writerow(csvRow) 
# finally:
#     csvFile.close()








