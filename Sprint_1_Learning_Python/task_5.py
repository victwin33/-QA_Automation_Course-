class TestCase:

    def __init__(self, steps, result):
        self.steps = {}
        self.result = None

    def set_step(self,step_number, step_text):
        self.steps[step_number] = step_text

    def delete_step(self,step_number):
        del self.steps[step_number]

    def set_result(self,result):
        self.result = result

    def get_test_case(self):
        test_case = f'Шаги: {self.steps}, \nОжидаемый результат: {self.result}'
        print(test_case)


test_case_1 = TestCase(steps ={}, result = None)
test_case_1.set_step(step_number = 1, step_text = 'Перейти на сайт')
test_case_1.set_step(step_number = 3, step_text = 'Перейти в раздел Товары')
test_case_1.delete_step(step_number= 3)
test_case_1.set_step(step_number = 2, step_text = 'Перейти в раздел Товары')
test_case_1.set_step(step_number = 3, step_text =  'Нажать кнопку «В корзину» у первого товара')
test_case_1.set_result('Товар окажется в корзине')
test_case_1.get_test_case()

test_case_2 = TestCase(steps ={}, result = None)
test_case_2.set_step(step_number = 1, step_text ='Перейти на сайт')
test_case_2.set_step(step_number = 2, step_text = 'Перейти в раздел Корзина')
test_case_2.set_step(step_number = 3, step_text = 'Нажать кнопку "Удалить"')
test_case_2.set_result('Товар удален из корзины')
test_case_2.get_test_case()
