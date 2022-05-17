from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import openpyxl
excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = "University Location"
sheet.append(["University Name","Address","Phone Number"])
chrome_driver_path= "C:/Users/Md Javed/Downloads/Chrome Driver/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

university = pd.read_csv("C:/Users/Md Javed/Downloads/University List.csv")
university_name = university["University Name"][0:1895]
for universities in university_name:
    driver.get("https://www.google.co.in/")
    search = driver.find_element_by_name("q")
    search.send_keys(universities)
    search.send_keys(Keys.ENTER)
    try:
        address_click = driver.find_element_by_link_text("Address")
        address_click.click()
        address = driver.find_element_by_class_name("sXLaOe")
        phone = driver.find_element_by_css_selector("span.LrzXr.zdqRlf.kno-fv a span")
        print (f"University Name : {universities}, Address : {address.text}, Phone :{phone.text}")
        sheet.append([universities, address.text, phone.text])
    except Exception as e:
        print(f"University Name : {universities},Address : Address Not Found, Phone : Phone Number Not Found")
        sheet.append([universities,"Address Not Found", "Phone Number Not Found"])
# driver.close()
excel.save("University Location.xlsx")
driver.quit()