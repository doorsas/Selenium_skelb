from  selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait





driver = webdriver.Chrome()

trim = []
# driver.get('https://e.seb.lt/web/ipank.p?lang=LIT&act=VPFONDINFO&isin=SE0016076111')
#
# #
#
# element = WebDriverWait(driver, 10).until(
# EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/div/table/tbody/tr[1]/td[2]")))
# print (element.text)

driver.get('https://sebgroup.lu/private/our-funds/our-luxembourg-funds')

input = WebDriverWait(driver, 10).until(
EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div[1]/div[3]/button")))



input.send_keys(Keys.ENTER)




#     # search = driver.find_element_by_id('searchKeyword')
#     #
#     # search.send_keys('Subaru')
#     # search.send_keys(Keys.RETURN)
#     time.sleep(3)
#
#     # print(driver.page_source)
#     # # driver.find_element_by_class_name('loader-container')
#     elements = driver.find_elements(By.CLASS_NAME,'simpleAds')
#     new_list = []
#     c = []
#     for element in elements:
#         aprasymas = element.find_element(By.CLASS_NAME,'adsTextReview')
#         detales = element.find_element(By.CLASS_NAME,'adsTextMoreDetails')
#         kaina = element.find_element(By.CLASS_NAME,'adsPrice')
#         linkas = element.find_element(By.TAG_NAME, 'a')
#         if len(aprasymas.text) == 0:
#             pass
#         else:
#             new_list.append(aprasymas.text)
#         if len(detales.text) == 0:
#             pass
#         else:
#             new_list.append(detales.text)
#         if len(kaina.text) == 0:
#             pass
#         else:
#             new_list.append(kaina.text)
#         if len(linkas.get_attribute("href")) == 0:
#             pass
#         else:
#             new_list.append(linkas.get_attribute("href"))
#
#         bum = "/////////////////////////////"
#         new_list.append(bum)
#     trim.append(new_list)
#
#
# df = pd.DataFrame(trim)
#
# writer = pd.ExcelWriter('test7.xlsx', engine='xlsxwriter')
# df.to_excel(writer, sheet_name='Subaru', index=False)
# writer.save()

