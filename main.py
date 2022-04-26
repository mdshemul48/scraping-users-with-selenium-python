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

    def get(self, url: str) -> None:
        self.driver.get(url)


def main():
    url = "https://www.google.com"
    w = web()
    print("hello world")
    w.get(url)


if __name__ == "__main__":
    main()
