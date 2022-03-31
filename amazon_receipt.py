from selenium import webdriver
import time

### #下記1の部分に、chromedriverを置いているファイルパスを入力してください
chrome = webdriver.Chrome(executable_path='#1')
chrome.get("https://www.amazon.co.jp/")
chrome.implicitly_wait(10)

### 下記#2のところに、Amazonログインに必要なメールアドレスを入力してください
chrome.find_element_by_partial_link_text('ログイン').click()
email_elem = chrome.find_element_by_id("ap_email")
email_elem.send_keys("#2")
email_elem.submit()
time.sleep(3)

### 下記#3のところに、Amazonログインに必要なパスワードを入力してください
password_elem = chrome.find_element_by_id("ap_password")
password_elem.send_keys("#3")
password_elem.submit()
time.sleep(3)


#2021年度のデータを開きます　必要に応じて変更してください
elem = chrome.find_element_by_id("nav-orders")
elem.click()
elem2 = chrome.find_element_by_id("a-autoid-1")
elem2.click()
elem3 = chrome.find_element_by_id("orderFilter_3")
elem3.click()
time.sleep(3)


total = 0
index = 0
html_file_number = 1

pages_remaining = True
current_URL_address = chrome.current_url
while pages_remaining:
    try:
        time.sleep(3)
        receipt_link_element = chrome.find_elements_by_xpath("//a[@class='a-link-normal']")
        receipt_link_element2 = [x.text for x in receipt_link_element]
        receipt_link_url = [x.get_attribute('href') for x in receipt_link_element]
        link_format = receipt_link_url[::1]
        link_data = [s for s in link_format if "invoice" in s]
        for receipt_page in link_data:
              chrome.get(receipt_page)
              time.sleep(1)
              receipt_page_html = chrome.page_source
              i_format = "{0:03d}".format(html_file_number)
              receipt_link_file = open(i_format + ".html", "w")
              receipt_link_file.write(receipt_page_html)
              receipt_link_file.close()
              print(receipt_link_file)
              print(i_format)
              html_file_number += 1
        break
    except:
        chrome.close()
  
