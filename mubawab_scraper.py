import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv 
import time 


options= webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')

driver = webdriver.Chrome(options=options)
url = 'https://www.mubawab.ma/fr/ct/marrakech/immobilier-a-louer'


driver.get(url)
time.sleep(3)

ads = driver.find_elements(By.CLASS_NAME, 'listingBox')
print(f"Found {len(ads)} ads on this page!")
all_data=[]

total_pages=3


for page in range(1,total_pages+1):
    print(f"---Fetching Page {page}---")
    
    if page == 1:
        url = "https://www.mubawab.ma/fr/ct/marrakech/immobilier-a-louer"
    else:
        url = f"https://www.mubawab.ma/fr/ct/marrakech/immobilier-a-louer:p:{page}"
    driver.get(url)
    time.sleep(2)
    ads = driver.find_elements(By.CLASS_NAME, "listingBox")

for ad in ads:
    try:
        title= ad.find_element(By.CLASS_NAME , "listingTit").text
        raw_price = ad.find_element(By.CLASS_NAME, "priceTag").text


        clean_price = raw_price.replace("DH","").replace(" ","").strip()
        price = int(clean_price) if clean_price.isdigit() else raw_price
        title_element = ad.find_element(By.CLASS_NAME, "listingTit")
        link = title_element.find_element(By.TAG_NAME, "a").get_attribute("href")

        all_data.append({"Title": title,
                         "Price": price,
                         "URL": link
                         })
        
        print(f"Title:{title}| price:{price}")


    except:
        continue
print(f"\n Done! Total ads saved from all pages: {len(all_data)}")
df = pd.DataFrame(all_data)
df.to_csv("mubawab_marrakech.csv",index=False, encoding="utf-8-sig")
print("csv file created successfully!")
driver.quit()






