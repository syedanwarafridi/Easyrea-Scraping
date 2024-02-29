# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
# import time
# import csv
# # from selenium.webdriver.chrome.options import Options
# # from selenium.common.exceptions import StaleElementReferenceException, TimeoutException, ElementClickInterceptedException

# csv_file = 'HoomeDec_IndoorFurnoture.csv'
# website = "https://easyrea.com/produits/d?codeFamille=dmo"
# driver = webdriver.Chrome()
# driver.get(website)

# time.sleep(5)
# username_field = driver.find_element(By.XPATH, "//input[@id='login']")
# username_field.send_keys('lalani') 

# password_field = driver.find_element(By.XPATH, "//input[@id='password']")
# password_field.send_keys('Lalaniakash3') 

# password_field.send_keys(Keys.RETURN)
# time.sleep(20)

# for i in range(19):
        
#     WebDriverWait(driver, 10).until(EC.url_contains('easyrea.com/produits'))

#     product_elements = WebDriverWait(driver, 500).until(
#         EC.visibility_of_all_elements_located((By.CLASS_NAME, 'grid-product-child'))
#     )
    
#     with open(csv_file, 'w', newline='', encoding='utf-8') as file:
#         writer = csv.writer(file)
#         writer.writerow(["Title", "Reference", "Price", "Stock Status", "Image URL", "Description"])

#         for product in product_elements:
                
#                 title = product.find_element(By.CLASS_NAME, 'product-title').text
#                 reference = product.find_element(By.CLASS_NAME, 'product-reference').text
#                 price = product.find_element(By.CLASS_NAME, 'new-price').text
#                 stock_status = product.find_element(By.CLASS_NAME, 'state-status').text
#                 image_url = product.find_element(By.CLASS_NAME, 'img-thumbnail').get_attribute('src')
                
#                 product.click()
                
#                 try:
#                     description_element = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.CLASS_NAME, 'cp-description')))
#                     # description_elements = description_element.find_elements(By.CSS_SELECTOR, '.listKeyValue .keyValue')

#                     description = description_element.text
#                 except:
#                     description = 'None'
#                     print("Description Not Found")
                
#                 writer.writerow([title, reference, price, stock_status, image_url, description])
#                 # print("Title:", title)
#                 # print("Reference:", reference)
#                 # print("Price:", price)
#                 # print("Stock Status:", stock_status)
#                 # print("Image URL:", image_url)
#                 # print("Description:", description)
#                 # print("-------" * 5)
            
#     next_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='view']/div/div/div[2]/app-pagination/div/div/button[2]")))
#     next_button.click()
#     print("Moving to next page...")
            

# time.sleep(2)
# driver.quit()


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import csv
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException

csv_file = 'home_textile/textile1.csv'
website = "https://easyrea.com/produits/d?codeFamille=dte&codeSousFamille=dteri"
driver = webdriver.Chrome()
driver.get(website)

time.sleep(5)
username_field = driver.find_element(By.XPATH, "//input[@id='login']")
username_field.send_keys('lalani') 

password_field = driver.find_element(By.XPATH, "//input[@id='password']")
password_field.send_keys('Lalaniakash3') 

password_field.send_keys(Keys.RETURN)
time.sleep(20)

for i in range(5):
    WebDriverWait(driver, 10).until(EC.url_contains('easyrea.com/produits'))

    product_elements = WebDriverWait(driver, 500).until(
        EC.visibility_of_all_elements_located((By.CLASS_NAME, 'grid-product-child'))
    )
    
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

                description_element = WebDriverWait(driver, 5).until(
                    EC.visibility_of_element_located((By.CLASS_NAME, 'cp-description'))
                )
                description = description_element.text
            except Exception as desc_error:
                description = 'None'
                print(f"Error while clicking and retrieving description: {str(desc_error)}")

        except Exception as e:
            # Handle errors related to product information
            print(f"Error while processing product {j + 1}: {str(e)}")
            continue  # Skip to the next iteration if an error occurs for this product

        # Write data to CSV after processing each product
        with open(csv_file, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([title, reference, price, stock_status, image_url, description])
            print(f"Title {j + 1}:", title)
            print(f"Price {j + 1}:", price)
            print(description)

    try:
        next_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='view']/div/div/div[2]/app-pagination/div/div/button[2]"))
        )
        next_button.click()
        print("Moving to the next page...")
    except TimeoutException:
        print("Timeout waiting for the next button to be visible.")
    except ElementClickInterceptedException:
        print("Element click intercepted. You may need to handle this specific case.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

time.sleep(2)
driver.quit()
