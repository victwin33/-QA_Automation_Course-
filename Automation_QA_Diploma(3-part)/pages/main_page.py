import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Клик по кнопке "Войти в аккаунт"')
    def click_on_enter_btn(self):
        self.move_to_element_and_click(MainPageLocators.ENTER_ACCOUNT_BTN)

    @allure.step('Найти ингредиент "Флюоресцентная булка"')
    def find_ingredient_bun(self):
        return self.find_element(MainPageLocators.INGREDIENT_BUN)

    @allure.step('Клик по ингредиенту "Флюоресцентная булка"')
    def click_on_bun(self):
        self.move_to_element_and_click(MainPageLocators.INGREDIENT_BUN)

    @allure.step('Клик по крестику в модальном окне')
    def click_close_btn(self):
        self.move_to_element_and_click(MainPageLocators.CLOSE_BTN)

    @allure.step('Проверка текст всплывающего окна')
    def check_popup_text(self):
        return self.get_text_of_element(MainPageLocators.INGREDIENT_POPUP_TITLE)

    @allure.step('Проверка закрытия всплывающего окна')
    def check_invisibility_of_popup(self):
        return self.check_invisibility(MainPageLocators.INGREDIENT_POPUP)

    @allure.step('Проверка,пока появится название бургера')
    def wait_visibility_burger_title(self):
        return self.wait_visibility_element(MainPageLocators.BURGER_CONSTRUCTOR_TITLE)

    @allure.step('Клик по кнопке "Оформить заказ"')
    def click_order_btn(self):
        self.move_to_element_and_click(MainPageLocators.CREATE_ORDER_BTN)

    @allure.step('Добавление булки в корзину')
    def add_bun_to_order_basket(self):
        self.drag_and_drop_element(MainPageLocators.INGREDIENT_BUN, MainPageLocators.ORDER_BASKET)

    @allure.step('Добавление начинки в корзину')
    def add_filling_to_order_basket(self):
        self.drag_and_drop_element(MainPageLocators.INGREDIENT_FILLING, MainPageLocators.ORDER_BASKET)

    @allure.step('Добавление соуса в корзину')
    def add_sauce_to_order_basket(self):
        self.drag_and_drop_element(MainPageLocators.INGREDIENT_SAUCE, MainPageLocators.ORDER_BASKET)

    @allure.step('Получение количества добавленного ингредиента')
    def check_counter_of_ingredients(self):
        return self.get_text_of_element(MainPageLocators.INGREDIENT_COUNTER)

    @allure.step('Получить номер заказа')
    def find_order_number(self):
        return self.find_element(MainPageLocators.ORDER_NUMBER)

    @allure.step('Проверить статус заказа')
    def check_order_status(self):
        return self.check_element(MainPageLocators.ORDER_STATUS_TEXT)

    @allure.step('Создание заказа и получение его номера')
    def make_order_and_get_order_number(self):
        self.wait_visibility_element(MainPageLocators.INGREDIENT_BUN)
        self.drag_and_drop_element(MainPageLocators.INGREDIENT_BUN, MainPageLocators.ORDER_BASKET)
        self.drag_and_drop_element(MainPageLocators.INGREDIENT_FILLING, MainPageLocators.ORDER_BASKET)
        self.find_element(MainPageLocators.CREATE_ORDER_BTN)
        self.move_to_element_and_click(MainPageLocators.CREATE_ORDER_BTN)
        self.wait_visibility_element(MainPageLocators.ORDER_STATUS_TEXT)
        self.wait_invisibility_element(MainPageLocators.DEFAULT_ORDER_NUMBER)
        order = self.get_text_of_element(MainPageLocators.ORDER_NUMBER)
        self.move_to_element_and_click(MainPageLocators.CLOSE_BTN)
        return order
