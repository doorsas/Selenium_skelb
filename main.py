from  selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait





driver = webdriver.Chrome()

trim = []
for i in range(4):
    driver.get('https://www.skelbiu.lt/skelbimai/' + str(i+1) + '?autocompleted=1&keywords=subaru&body=0&fuel=0&transmission=0&color=0&defect=0&cities=0&distance=0&mainCity=0&search=1&category_id=3426&type=0&user_type=0&ad_since_min=0&ad_since_max=0&visited_page=1&orderBy=-1&detailsSearch=0&facets=0')

    # search = driver.find_element_by_id('searchKeyword')
    #
    # search.send_keys('Subaru')
    # search.send_keys(Keys.RETURN)
    time.sleep(3)

    # print(driver.page_source)
    # # driver.find_element_by_class_name('loader-container')
    elements = driver.find_elements(By.CLASS_NAME,'simpleAds')
    new_list = []
    c = []
    for element in elements:
        aprasymas = element.find_element(By.CLASS_NAME,'adsTextReview')
        detales = element.find_element(By.CLASS_NAME,'adsTextMoreDetails')
        kaina = element.find_element(By.CLASS_NAME,'adsPrice')
        linkas = element.find_element(By.TAG_NAME, 'a')
        if len(aprasymas.text) == 0:
            pass
        else:
            new_list.append(aprasymas.text)
        if len(detales.text) == 0:
            pass
        else:
            new_list.append(detales.text)
        if len(kaina.text) == 0:
            pass
        else:
            new_list.append(kaina.text)
        if len(linkas.get_attribute("href")) == 0:
            pass
        else:
            new_list.append(linkas.get_attribute("href"))

        bum = "/////////////////////////////"
        new_list.append(bum)
    trim.append(new_list)


df = pd.DataFrame(trim)

writer = pd.ExcelWriter('test7.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Subaru', index=False)
writer.save()

