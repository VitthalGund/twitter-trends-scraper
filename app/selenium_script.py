from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pymongo import MongoClient
import time
import uuid
import requests
import os
from dotenv import load_dotenv

load_dotenv()

# MongoDB setup
client = MongoClient(os.getenv("MONGO_URI"))
db = client["twitter_trends"]
collection = db["trending_topics"]

# Selenium setup with ProxyMesh
PROXY = os.getenv("PROXYMESH_URL")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--proxy-server=%s" % PROXY)
driver = webdriver.Chrome(options=chrome_options)

# Login to Twitter
driver.get("https://twitter.com/login")
time.sleep(2)

username = driver.find_element(By.NAME, "session[username_or_email]")
password = driver.find_element(By.NAME, "session[password]")

username.send_keys(os.getenv("TWITTER_USERNAME"))
password.send_keys(os.getenv("TWITTER_PASSWORD"))
password.send_keys(Keys.RETURN)
time.sleep(2)

# Scrape trending topics
driver.get("https://twitter.com/home")
time.sleep(2)

trending_topics = driver.find_elements(
    By.XPATH, "//section//span[text()='Trending']/following-sibling::span"
)
trends = [topic.text for topic in trending_topics[:5]]

# Generate unique ID and get current IP
unique_id = str(uuid.uuid4())
ip_address = requests.get("https://api.my-ip.io/ip").text
end_time = time.strftime("%Y-%m-%d %H:%M:%S")

# Store data in MongoDB
data = {
    "_id": unique_id,
    "trend1": trends[0],
    "trend2": trends[1],
    "trend3": trends[2],
    "trend4": trends[3],
    "trend5": trends[4],
    "datetime": end_time,
    "ip_address": ip_address,
}

collection.insert_one(data)
driver.quit()
