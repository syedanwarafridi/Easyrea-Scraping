import requests
from bs4 import BeautifulSoup
import time

# Website URL
website = "https://easyrea.com/produits/d?codeFamille=dmo"

# Send a GET request to the website and parse the HTML using Beautiful Soup
response = requests.get(website)
soup = BeautifulSoup(response.content, 'html.parser')

############################
# USER LOGIN
############################
# Find the login form fields
login_form = soup.find('form', id='loginForm')
username_field = login_form.find('input', id='login')
password_field = login_form.find('input', id='password')

# Your credentials
username = 'lalani'
password = 'Lalaniakash3'

# Populate the login form fields
login_data = {
    'login': username,
    'password': password
}

# Send a POST request to login
login_url = 'https://easyrea.com/login'
login_response = requests.post(login_url, data=login_data)

# Simulating a delay for login
time.sleep(5)

# After login, proceed with scraping the page
# Find all product elements
product_elements = soup.find_all('div', class_='grid-product-child')

for product in product_elements:
    # Extract product details
    title = product.find('span', class_='product-title').get_text(strip=True)
    reference = product.find('span', class_='product-reference').get_text(strip=True)
    price = product.find('span', class_='new-price').get_text(strip=True)
    stock_status = product.find('span', class_='state-status').get_text(strip=True)
    image_url = product.find('img', class_='img-thumbnail')['src']

    # Extract product description by visiting its detail page
    product_detail_url = product.a['href']
    product_detail_response = requests.get(product_detail_url)
    product_detail_soup = BeautifulSoup(product_detail_response.content, 'html.parser')
    description_element = product_detail_soup.find('div', class_='listKeyValue')
    if description_element:
        description = description_element.get_text(strip=True)
    else:
        description = "Description not found"

    # Print product details
    print("Title:", title)
    print("Reference:", reference)
    print("Price:", price)
    print("Stock Status:", stock_status)
    print("Image URL:", image_url)
    print("Description:", description)
    print("-------")

    # Simulating a delay before scraping the next product
    time.sleep(3)
