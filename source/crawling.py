from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=Service('./data/chromedriver'), options=chrome_options)

driver.get('https://map.naver.com/v5/search/%EA%B0%80%EC%82%B0%EB%94%94%EC%A7%80%ED%84%B8%EB%8B%A8%EC%A7%80%20%EB%A7%9B%EC%A7%91?c=14,0,0,0,dh')
driver.maximize_window()
driver.implicitly_wait(time_to_wait=5)


from bs4 import BeautifulSoup
import time

name_list, score_list, review_count, address_list, menu_name, menu_price = [],[],[],[],[],[]

def find_info():
    driver.switch_to.default_content()
    driver.switch_to.frame('entryIframe')
    
    time.sleep(0.5)    
    
    name_list.append(driver.find_element(By.CLASS_NAME, 'Fc1rA').text)
    
    
    s = driver.find_element(By.CLASS_NAME, 'dAsGb').text
    el = driver.find_elements(By.CLASS_NAME, 'PXMot')
    time.sleep(0.5)    
    
    if '별점' in s and '방문자리뷰' in s:
        score_list.append(el[0].find_element(By.TAG_NAME, 'em').text)
        review_count.append(el[1].find_element(By.TAG_NAME, 'em').text)
    elif '별점' in s:
        score_list.append(el[0].find_element(By.TAG_NAME, 'em').text)
        review_count.append(None)
    elif '방문자리뷰' in s:
        score_list.append(None)
        review_count.append(el[0].find_element(By.TAG_NAME, 'em').text)
    else:
        score_list.append(None)
        review_count.append(None)
        
    address_list.append(driver.find_element(By.CLASS_NAME, 'LDgIH').text)
    
    for x in driver.find_elements(By.CLASS_NAME, 'tpj9w._tab-menu'):
        if x.text == '메뉴':
            x.click()
            break
    time.sleep(0.5)  
    
    x = driver.find_elements(By.CLASS_NAME, 'name')
    y=  driver.find_elements(By.CLASS_NAME, 'Sqg65')
    z= driver.find_elements(By.CLASS_NAME, 'tit')
    
    if x:
        menu_name.append(driver.find_element(By.CLASS_NAME, 'name').text)
        menu_price.append(driver.find_element(By.CLASS_NAME, 'price').text)
    elif y:
        menu_name.append(driver.find_element(By.CLASS_NAME, 'Sqg65').text)
        menu_price.append(driver.find_element(By.CLASS_NAME, 'SSaNE').text)
    elif z:
        menu_name.append( 
            driver.find_element(By.CLASS_NAME, 'tit').text.replace(\
        driver.find_element(By.CLASS_NAME, 'ico_group').text, ''))      
        menu_price.append(driver.find_element(By.CLASS_NAME, 'price').text)
    else:
        menu_name.append(None)
        menu_price.append(None)
        
    driver.switch_to.default_content()
    driver.switch_to.frame('searchIframe')
    time.sleep(0.5)  
    



for i in range(1, 7):
    driver.switch_to.default_content()
    driver.switch_to.frame('searchIframe')
    scroll = driver.find_element(By.CLASS_NAME, 'tzwk0')
    
    for _ in range(20):
        scroll.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.5)

    source = driver.page_source
    soup = BeautifulSoup(source, 'html.parser')
    
    current_page_names = []
    
    
    for x in soup.find_all('span', class_='place_bluelink TYaxT'):
        xx = x.get_text()
        if xx in name_list:
            continue
        current_page_names.append(xx)
    
    for _ in range(20):
        scroll.send_keys(Keys.PAGE_UP)
        time.sleep(0.5)
    time.sleep(1)
    
    for name in current_page_names:
        if name == 'KFC 가산디지털':
            continue
        if name in name_list:
            continue
        for x in driver.find_elements(By.CLASS_NAME, 'tzwk0'):
            if x.find_element(By.CLASS_NAME, 'place_bluelink.TYaxT').text == name:
                x.click()
                time.sleep(1)
                find_info()
                break
        else:
            while 1:
                            
                scroll = driver.find_element(By.CLASS_NAME, 'tzwk0')
                scroll.send_keys(Keys.PAGE_DOWN)
                time.sleep(0.5)
                
                for x in driver.find_elements(By.CLASS_NAME, 'tzwk0'):
                    if x.find_element(By.CLASS_NAME, 'place_bluelink.TYaxT').text == name:
                        x.click()
                        time.sleep(1)
                        find_info()
                        break
        if len(name_list) != len(score_list) != len(review_count) != \
            len(address_list) != len(menu_name) != len(menu_price):
            break
    if i == 6:
        break
        
    for x in driver.find_elements(By.CLASS_NAME, 'mBN2s'):
        if int(x.text) == i + 1:
            x.click()
    time.sleep(1)

import pandas as pd
df = pd.DataFrame({'이름':name_list , '평점':score_list , '리뷰 수' :review_count, '주소':address_list , '대표 메뉴' :menu_name , '대표 메뉴 가격': menu_price})




import time
dist, dist_min = [], []

for address in address_list:
    if '뉴티캐슬' in address:
        dist.append(0)
        dist_min.append(0)
        continue
    search_bar= driver.find_element(By.ID, 'directionGoal1')

    search_bar.clear()
    search_bar.send_keys(address)
    search_bar.send_keys(Keys.ENTER)
    
    
    time.sleep(1)
    
    driver.find_element(By.CLASS_NAME, 'btn.btn_direction.active').click()
    
    time.sleep(1)
    dist_min.append(driver.find_element(By.CLASS_NAME, 'value.ng-star-inserted').text)
    dist.append(driver.find_element(By.CLASS_NAME, 'summary_text').text)
    
    