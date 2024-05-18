from validator import validator
from typing import Union


class Controller:
    # Блок методов для математических вычислений.
    def calc_sum(self, a, b) -> Union[int, float]:
        """
        Метод суммирует передаваемые аргументы.
        Args:
            2 числа
        Return:
            сумма 2х чисел
        """
        return a + b

    def calc_diff(self, a, b) -> Union[int, float]:
        """
        Метод вычетает из первого аргумента второй.
        Args:
            2 числа
        Return:
            разность 2-х чисел
        """
        return a - b

    def calc_mult(self, a, b) -> Union[int, float]:
        """
        Метод перемножает передаваемые аргументы.
        Args:
            2 числа
        Return:
            результат перемножения 2-х чисел
        """
        return a * b

    def calc_div(self, a, b) -> Union[int, float]:
        """
        Метод делит первый аргумент на второй.
        Args:
            2 числа
        Return:
            результат деления 2-х чисел
        """
        return a / b

    def calculate(self, data: dict) -> str:
        """
        Метод производит математические операции над передаваемыми данными.
        Args:
            словарь, содержащий 2 числа и выбор нужной операции
        Return:
            результат математической операции
        """
        error = validator.val_calculate(data)
        if error:
            return error

        a, b, action = data.values()

        if action == "+":
            return str(controller.calc_sum(a, b))
        elif action == "-":
            return str(controller.calc_diff(a, b))
        elif action == "*":
            return str(controller.calc_mult(a, b))
        elif action == "/":
            return str(controller.calc_div(a, b))

# Блок методов для преобразования текста
    def text_upper(self, text: str) -> str:
        """
        Метод преобразовывает текст в заглавные буквы.
        Args:
            text: текст
        Return:
            текст заглавными буквами
        """
        return text.upper()

    def text_lower(self, text: str) -> str:
        """
        Метод преобразовывает текст в строчные буквы.
        Args:
            text: текст
        Return:
            текст строчными буквами
        """
        return text.lower()

    def text_trim(self, text: str) -> str:
        """
        Метод удаляет пробелы в передаваемом тексте.
        Args:
            text: текст
        Return:
            текст без пробелов
        """
        return text.strip()

    def text_alter(self, text: str) -> str:
        """
        Метод переворачивает передаваемый текст.
        Args:
            text: текст
        Return:
            перевернутый текст
        """
        return text[::-1]

    def text_editor(self, data: dict) -> str:
        """
        Метод преобразовывает передаваемый текст.
        Args:
            словарь сданными: текст и необходимая операция преобразования текста
        Return:
            преобразованный текст
        """
        error = validator.val_text_editor(data)
        if error:
            return error

        text, action = data.values()

        if action == "upper":
            return controller.text_upper(str(text))
        elif action == "lower":
            return controller.text_lower(str(text))
        elif action == "trim":
            return controller.text_trim(str(text))
        elif action == "alter":
            return controller.text_alter(str(text))

# Блок методов для парсинга в тексте емэйлов и номеров телефонов
    def text_email(self, text: str) -> str:
        """
        Метод ищет емэйлы в тексте.
        Args:
            text: текст
        Return:
            емэйлы
        """
        pass

    def text_number(self, text: str) -> str:
        """
        Метод ищет номера телефонов в тексте.
        Args:
            text: текст
        Return:
            номера телефонов
        """
        pass

    def parser(self, data: dict) -> str:
        """
        Метод нужную информацию (емэйл, номер телефона) в тексте.
        Args:
            словарь с данными: текст и необходимая операция
        Return:
            результат поиска в виде строки
        """
        error = validator.val_parser(data)
        if error:
            return error

        text, action = data.values()

        if action == "email":
            return controller.text_email(str(text))
        if action == "number":
            return controller.text_number(str(text))


controller = Controller()
