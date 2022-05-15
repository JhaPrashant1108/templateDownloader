from scraper import *
from downloader import *

import json

imgLinkScraper = imgLinkScraper()
imgLinkDictScraped = imgLinkScraper.scraper()


imgLinkAdded = imgLinkAdder(imgLinkDictScraped)
imgLinkDictAdded = imgLinkAdded.adder()

downloadImage = downloader(imgLinkDictAdded)
imgLinkDictDownloaded = downloadImage.download()














print("hello world")
