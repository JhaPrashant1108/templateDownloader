import json
import sys
import os
import urllib.request
import requests

class downloader:
    def __init__(self , imgLinkDict):
        self.imgLinkDict = imgLinkDict
        self.templateImages = os.path.join(os.getcwd(), 'downloader', 'images', 'templateImages')
        self.previewImages = os.path.join( os.getcwd(),'downloader', 'images', 'previewImages')


    def download(self):
        for i in self.imgLinkDict:
            title = self.imgLinkDict[i]['Title'].replace("?","").replace("/" , " ").replace("*","")
            imageLink = self.imgLinkDict[i]['Image Link']
            name = str(i) + "." + imageLink.split(".")[-1].split("?")[0]
            previewname = 'Preview-' + str(i) + "."  + self.imgLinkDict[i]['Preview Image Link'].split(".")[-1]
            previewLink = self.imgLinkDict[i]['Preview Image Link']
            imageLocation = os.path.join(self.templateImages, name)
            previewLocation = os.path.join(self.previewImages, previewname)
            self.imageDownloader(imageLink,imageLocation,name)
            self.imageDownloader(previewLink,previewLocation,previewname)
            self.imgLinkDict[i]["Image Saved As"] = name
            self.imgLinkDict[i]["Preview Saved As"] = previewname
            outFile = open("scraper/output/imgLinks.json", "w") 
            json.dump(self.imgLinkDict, outFile, indent = 4) 
            outFile.close() 
        return self.imgLinkDict


    def imageDownloader( self , src, path , name):
        page = requests.get(src)
        with open(path,'wb') as f:
            f.write(page.content)
        print(name+' Downloaded')