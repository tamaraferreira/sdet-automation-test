import allure
import re
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class BookSearch:

    def __init__(self, driver):
        self.driver = driver
        self.search_field = (By.NAME, "q")
        self.shopping_tab_xpath = (By.XPATH, "//*[@role='navigation']//*[text()='Shopping']")
        self.high_price_button_xpath = (By.XPATH, "//*[contains(translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'do maior para o menor')]")
        self.max_amount_input = (By.XPATH, "//*[contains(@aria-label, 'Preço máximo')]")
        self.go_price_button = (By.XPATH, "//button[@class='iTnSe']")
        self.products_ratings = (By.XPATH, "//span[contains(@aria-label, 'Classificado')]")


    def searchBook(self, book_name):
        search_box = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.search_field)
        )
        search_box.send_keys(book_name + " book", Keys.ENTER)

    def clickShoppingTab(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.shopping_tab_xpath)
        ).click()

    def clickHighToLowPrices(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.high_price_button_xpath)
        ).click()

    def fillMaxAmount(self, max_amount):
        input_amount =WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.max_amount_input)
        )
        input_amount.clear()
        input_amount.send_keys(max_amount)
        self.driver.find_element(*self.go_price_button).click()

    def verifySecondProdRating(self, expected_rating):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located(self.products_ratings)
            )

            rating_elements = self.driver.find_elements(*self.products_ratings)

            rated_books_count = 0
            second_rating = None

            for elem in rating_elements:
                elem_aria_label = elem.get_attribute("aria-label")
                if elem_aria_label:
                    match = re.search(r"\d+(\.\d+)?", elem_aria_label.replace(',', '.'))
                    if match:
                        rated_books_count += 1
                        if rated_books_count == 2:
                            second_rating = float(match.group())
                            break

            if second_rating is None:
                with allure.step("No second reviewed book found."):
                    print("No second reviewed book found.")
                return

            with allure.step("Rating of the second book reviewed"):
                print(f"Rating of the second book reviewed is: {second_rating}")

            if second_rating >= expected_rating:
                with allure.step(f"The rating ({second_rating}) is bigger than or equal to ({expected_rating})."):
                    print(f"The rating ({second_rating}) is bigger than or equal to ({expected_rating}).")
            else:
                with allure.step(f"The rating ({second_rating}) is less than ({expected_rating})."):
                    print(f"The rating ({second_rating}) is less than ({expected_rating}).")

        except:
            print("No reviews could be found on this page..")