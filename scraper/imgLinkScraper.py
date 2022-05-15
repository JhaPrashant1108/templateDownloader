import requests
from bs4 import BeautifulSoup
import json

class imgLinkScraper:
    def __init__(self):
        self.imgLinkDict = {}
        self.basicUrl = "https://imgflip.com"
        self.url = "https://imgflip.com/memetemplates?page="
        self.imageUrl = "https://imgflip.com/s/meme/"
        self.memeGenerator = "https://imgflip.com/memegenerator"

    def scraper(self):
        k = 1
        for i in range(50):
            getUrl = self.url+str(i+1)
            htmlContent = requests.get(getUrl).content
            soup = BeautifulSoup(htmlContent,'html.parser')
            for divs in soup.findAll("div",{"class":"mt-box"}):
                previewImage = 'https:'+divs.find("img",{"class":"shadow"})['src']
                imgLinks = divs.find("a",{"class":"mt-caption l but"})
                name = imgLinks['title'].replace(" Meme Generator","")
                generator = self.memeGenerator+"/"+"/".join(imgLinks['href'].split("/")[2:])
                self.imgLinkDict['Image'+str(k)]={'Title':name,'Template Link':generator,'Preview Image Link':previewImage}
                k = k+1
        outFile = open("scraper/output/imgLinks.json", "w") 
        json.dump(self.imgLinkDict, outFile, indent = 4) 
        outFile.close() 
        print("[imgLinkScraper][scraper]")
        return self.imgLinkDict
