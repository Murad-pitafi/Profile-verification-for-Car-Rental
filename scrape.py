
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 


# Set up the Chrome WebDriver with headless options
options = Options()
options.headless = True

# Specify the path to your chromedriver (replace with your actual path)
chromedriver_path = r"C:\Users\Nizam\Downloads\chromedriver-win64 (1)\chromedriver-win64\chromedriver.exe"  # Update this path

service = Service(executable_path=chromedriver_path)

# Initialize the WebDriver with the service argument
driver = webdriver.Chrome(service=service, options=options)

# Visit a public Instagram profile
profile_url = 'https://www.instagram.com/anushkasen0408/?hl=en'
driver.get(profile_url)
time.sleep(3)  # Wait for the page to load

# Extract some public data (example: profile name and followers count)
try:
    # Corrected find_element method
    name = driver.find_element(By.XPATH, '//*[@id="mount_0_0_fG"]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/header/section/div[1]/div[1]/h2').text
    followers = driver.find_element(By.XPATH, '//*[@id="mount_0_0_fG"]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/header/section/div[2]/ul/li[1]/div/button').get_attribute('title')
    print(f"Name: {name}")
    print(f"Followers: {followers}")
except Exception as e:
    print("Error:", e)
    
    
driver.quit()
