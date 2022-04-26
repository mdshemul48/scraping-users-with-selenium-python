from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class web:
    driver = None
    url: str = None

    def __init__(self) -> None:
        options = webdriver.ChromeOptions()
        options.add_experimental_option("debuggerAddress", "localhost:9222")
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), options=options
        )

    def get(self, url: str) -> webdriver.Chrome:
        self.driver.get(url)
        return self.driver


def main():
    url = "https://circlenetworkbd.net/"
    w = web()
    website = w.get(url)

    pagecourse: str = website.page_source
    print(pagecourse)


if __name__ == "__main__":
    main()
