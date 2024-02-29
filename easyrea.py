from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import TimeoutException
import time

website = "https://easyrea.com/massification"
driver = webdriver.Chrome()
driver.get(website)

time.sleep(5)
############################
# USER LOGIN
############################
username_field = driver.find_element(By.XPATH, "//input[@id='login']")
username_field.send_keys('lalani') 

password_field = driver.find_element(By.XPATH, "//input[@id='password']")
password_field.send_keys('Lalaniakash3') 

# Submit the form
password_field.send_keys(Keys.RETURN)

#############################
# FIND Products
# #############################
time.sleep(20)
for i in range(1, 51):
    
    product_elements = WebDriverWait(driver, 60).until(
        EC.presence_of_all_elements_located((By.XPATH, "//*[@id='view']/div/div/div[2]/div[3]/div/div[{1}]".format(i)))
    )
    print("Product Element: ", product_elements)
    # Iterate over each product element and extract the product name and price
    for product_element in product_elements:
        # Extract product name
        # //div[@class='product-colisage']//span[contains(text(),'Massive quantity')]
        product_name = product_element.find_element(By.XPATH, '//*[@id="view"]/div/div/div[2]/div[3]/div/div[1]/div/div/div/app-product-grid-front/a/div/div[2]/div[2]/div[1]/div[1]/div/span')
        product_name = product_name.text
        print("Product Name:", product_name)
        
        pieces = product_element.find_element(By.XPATH, "//*[@id='view']/div/div/div[2]/div[3]/div/div[1]/div/div/div/app-product-grid-front/a/div/div[2]/div[2]/div[2]/app-product-common-conditionnement/div/div[1]/span")
        print("Pieces: ", pieces.text)
        pack_quality = product_element.find_element(By.XPATH, "//*[@id='view']/div/div/div[2]/div[3]/div/div[1]/div/div/div/app-product-grid-front/a/div/div[2]/div[2]/div[2]/app-product-common-conditionnement/div/div[2]/span")
        print("Pack Quality: ", pack_quality.text)
        
        price = product_element.find_element(By.XPATH, "//*[@id='view']/div/div/div[2]/div[3]/div/div[1]/div/div/div/app-product-grid-front/a/div/div[2]/div[2]/div[2]/div/app-product-common-prix-container/div/div/div/div[2]/div[1]/span[1]")
        price = price.text
        print("Product Price:", price)
        
        # image url
        img_elemnt = product_element.find_element(By.XPATH, '//*[@id="view"]/div/div/div[2]/div[3]/div/div[1]/div/div/div/app-product-grid-front/a/div/div[2]/div[1]/img')
        img_url = img_elemnt.get_attribute('src')
        print("Image: ", img_url)

        print("-" * 50)

time.sleep(100)
# Close the browser

driver.quit()