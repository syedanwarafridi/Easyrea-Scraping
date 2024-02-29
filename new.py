from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import csv
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException

csv_file = 'HomeDec/IndoorFur1.csv'
website = "https://easyrea.com/produits/d?codeFamille=dmo&codeSousFamille=dmoct"
driver = webdriver.Chrome()
driver.get(website)

time.sleep(5)
username_field = driver.find_element(By.XPATH, "//input[@id='login']")
username_field.send_keys('lalani') 

password_field = driver.find_element(By.XPATH, "//input[@id='password']")
password_field.send_keys('Lalaniakash3') 

password_field.send_keys(Keys.RETURN)
time.sleep(20)

for i in range(4):
    WebDriverWait(driver, 10).until(EC.url_contains('easyrea.com/produits'))

    product_elements = WebDriverWait(driver, 500).until(
        EC.visibility_of_all_elements_located((By.CLASS_NAME, 'grid-product-child'))
    )
    # print(len(product_elements))
    for j, product in enumerate(product_elements):
        
        
        try:
            title = product.find_element(By.CLASS_NAME, 'product-title').text
            reference = product.find_element(By.CLASS_NAME, 'product-reference').text
            price = product.find_element(By.CLASS_NAME, 'new-price').text
            stock_status = product.find_element(By.CLASS_NAME, 'state-status').text
            image_url = product.find_element(By.CLASS_NAME, 'img-thumbnail').get_attribute('src')
            
            # Scroll to the product before clicking
            driver.execute_script("arguments[0].scrollIntoView(true);", product)
            try:
                product.click()
                
                WebDriverWait(driver, 10).until(
                    EC.invisibility_of_element_located((By.CLASS_NAME, 'loaderWrapper')))
                
                carousel_div = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "ui-carousel-items-container"))
                    )
                
                image_elements = carousel_div.find_elements(By.TAG_NAME, "img")
                image_links = [img.get_attribute("src") for img in image_elements]
                # print("Images Links: ", image_links)
                
                description_element = WebDriverWait(driver, 5).until(
                    EC.visibility_of_element_located((By.CLASS_NAME, 'cp-description'))
                )
                description = description_element.text
                
                product_info_elem = WebDriverWait(driver, 5).until(
                    EC.visibility_of_element_located((By.XPATH, '//*[@id="view"]/div/div/div[2]/div[4]/div/app-product-volet/div/div[2]/app-product-volet-infos/div/div[2]/div[2]/div[1]/div/ul[1]'))
                )
                product_info = product_info_elem.text
                
                
                # //*[@id="view"]/div/div/div[2]/div[4]/div/app-product-volet/div/div[2]/app-product-volet-infos/div/div[2]/div[2]/div[1]
                logistic_info_elem = WebDriverWait(driver, 5).until(
                    EC.visibility_of_element_located((By.XPATH, '//*[@id="view"]/div/div/div[2]/div[4]/div/app-product-volet/div/div[2]/app-product-volet-infos/div/div[2]/div[2]/div[2]/div/ul[1]'))
                )
                logistic_info = logistic_info_elem.text
                # print(logistic_info)
            except Exception as desc_error:
                description = 'None'
                image_links = 'None'
                product_info = 'None'
                logistic_info = 'None'
                print(f"Error while clicking and retrieving description: {str(desc_error)}")

        except Exception as e:
            
            print(f"Error while processing product {j + 1}: {str(e)}")
            continue  

        # Write data to CSV after processing each product
        with open(csv_file, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([title, reference, price, stock_status, image_url, product_info, logistic_info, description, image_links])
            print(f"Title {j + 1}:", title)
            print(f"Price {j + 1}:", price)
            print(description)
            print("______" * 10)
        # time.sleep(2)
        if j < len(product_elements) - 1:
            product.click()
            print(j)
        else:
            print("Last Product of the page...")
            

    try:
        next_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='view']/div/div/div[2]/app-pagination/div/div/button[2]"))
        )
        next_button.click()
        time.sleep(5)
        print("Moving to the next page...")
    except TimeoutException:
        print("Timeout waiting for the next button to be visible.")
    except ElementClickInterceptedException:
        print("Element click intercepted. You may need to handle this specific case.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

time.sleep(2)
driver.quit()