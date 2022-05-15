from lib2to3.pgen2 import driver
from selenium import webdriver
import json
import time


class imgLinkAdder:
    def __init__(self , imgLinkDict):
        self.imgLinkDict = imgLinkDict

    def adder(self):
        driver = webdriver.Chrome(executable_path = 'seleniumdriver/chromedriver.exe')
        for i in self.imgLinkDict:
            driver.get(self.imgLinkDict[i]['Template Link'])
            driver.maximize_window()
            print("Scraping Details " + str(i))
            time.sleep(5)
            textField = []
            styles = []
            try:
                textField = driver.find_elements_by_class_name('drag-box')
                for k in range(len(driver.find_elements_by_class_name('drag-box'))):
                    styles.append(driver.find_elements_by_class_name('drag-box')[k].get_attribute('style'))
            except:
                print('Try again for ' + str(i))           
            imgUrl = ""
            try:
                imgUrl = driver.find_element_by_xpath('//*[@id="mm-preview-outer"]/div[4]/img').get_attribute('src')
            except:
                try:
                    imgUrl = driver.find_element_by_xpath('//*[@id="vgif-preview"]/source').get_attribute('src')
                except:
                    print('Try Again For ' + str(i) )
            textFieldNumber = len(textField)
            self.imgLinkDict[i]={'Title':self.imgLinkDict[i]['Title'],
                                'Image Link':imgUrl,
                                'Template Link':self.imgLinkDict[i]['Template Link'],
                                'Preview Image Link':self.imgLinkDict[i]['Preview Image Link'],
                                'Text Fields':textFieldNumber,
                                'Styles':styles}
            outFile = open("scraper/output/imgLinks.json", "w") 
            json.dump(self.imgLinkDict, outFile, indent = 4) 
            outFile.close() 
            print('Details Scraped for ' + str(i))
        driver.close()
        print("[imgLinkAdder][adder]")
        return self.imgLinkDict

    def checker(self):
        absent = []
        for i in self.imgLinkDict:
            if self.imgLinkDict[i]["Text Fields"]==0 or len(self.imgLinkDict[i]["Styles"]) == 0 or self.imgLinkDict[i]["Image Link"] == "" or self.imgLinkDict[i]["Text Fields"]!=len(self.imgLinkDict[i]["Styles"]):
                absent.append(i)

        return absent
