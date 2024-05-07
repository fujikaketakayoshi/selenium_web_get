#import ppretty
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Chromeドライバのパスとオプションを設定
chrome_path = '/usr/local/bin/chromedriver'
chrome_options = Options()
chrome_options.add_argument('--headless')  # ヘッドレスモードで起動

# Chromeドライバを起動
driver = webdriver.Chrome(options=chrome_options)

# 指定したURLのページを開く
url = 'https://fujikaketakayoshi.github.io/react_portfolio/'
driver.get(url)

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

# ページのソースコードを取得
html = driver.page_source

# ドライバを終了
driver.quit()

#print(html)

soup = BeautifulSoup(html, "html.parser")

elems = soup.select('a')

for i in elems:
	print(i