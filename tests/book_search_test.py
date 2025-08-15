import allure
import os
import pytest
from pages.book_search_page import BookSearch

@allure.epic("Google Book Search")
@allure.story("Verify rating book")

@pytest.mark.parametrize(
    'book_name, amount, rating',
    [
        ('Frankenstein', '150', 4.8),
        ('Dracula', '200', 4.4)
    ]
)

def test_google_book_search(reset_google_page, book_name, amount, rating):

    driver = reset_google_page

    book_search = BookSearch(driver)
    try:
        with allure.step(f"Search {book_name} book on Google:"):
            book_search.searchBook(book_name)
        with allure.step(f"Go to Shopping tab: "):
            book_search.clickShoppingTab()
        with allure.step(f"Order prices from high to low: "):
            book_search.clickHighToLowPrices()
        with allure.step(f"Fill the max amount field: "):
            book_search.fillMaxAmount(amount)
        with allure.step(f"Verify product rating: "):
            book_search.verifySecondProdRating(rating)

    except Exception as e:
        reports_folder = "allure-report"
        os.makedirs(reports_folder, exist_ok=True)  # garante que a pasta exista

        screenshot_name = f"screenshot_{book_name}.png"
        screenshot_path = os.path.join(reports_folder, screenshot_name)
        reset_google_page.save_screenshot(screenshot_path)

        allure.attach.file(screenshot_path,
            name="Screenshot_Error",
            attachment_type=allure.attachment_type.PNG
    )
        raise e