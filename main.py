from selenium import webdriver
import time
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import json


def htmlCodes():
    file = open("html.html", "r")
    return file.read()


def main():
    all_users = []

    options = webdriver.ChromeOptions()
    options.add_experimental_option("debuggerAddress", "localhost:9222")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    all_user_codes = htmlCodes()
    all_user_soup = BeautifulSoup(all_user_codes, "html.parser")
    all_users_element = all_user_soup.find_all("tr")
    iter = 1
    for user in all_users_element:
        print(iter)
        iter += 1
        user_detail = user.find_all("td")
        user_id: str = user_detail[1].getText()

        current_user_url = f"http://erp.circlenetworkbd.com/mac-customer/{user_id}"
        driver.get(current_user_url)
        table_element = driver.find_elements(
            By.XPATH, '//*[@id="container"]/div/div/div/div/div[2]/table'
        )[0]

        table_html = table_element.get_attribute("innerHTML")
        table_soup = BeautifulSoup(table_html, "html.parser")

        all_the_entry = table_soup.find_all("tr")
        user_data = {}
        for entry in all_the_entry:
            key = entry.find("th").getText()
            value = entry.find("td").getText()
            user_data[key] = value

        address = user_data["Address"].split(",")
        flat_no = address[0]
        building = address[1]
        road = address[2]
        block = address[3]
        user_data["Address"] = {
            "flat_no": flat_no,
            "building": building,
            "road": road,
            "block": block,
        }
        all_users.append(user_data)

    json_data = json.dumps(all_users)
    json_file = open("data.json", "w")
    json_file.write(json_data)
    json_file.close()


if __name__ == "__main__":
    main()
