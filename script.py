from scraper import *
from downloader import *

import json

# imgLinkScraper = imgLinkScraper()
# imgLinkDictScraped = imgLinkScraper.scraper()


# imgLinkAdded = imgLinkAdder(imgLinkDictScraped)
# imgLinkDictAdded = imgLinkAdded.adder()

# downloadImage = downloader(imgLinkDictAdded)
# imgLinkDictDownloaded = downloadImage.download()

outFile = open("scraper/output/imgLinks.json", ) 
imgLinkDictDownloaded = json.load(outFile)













print("hello world")