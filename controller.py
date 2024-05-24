from validator import validator
from typing import Union
import re


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
            return str(self.calc_sum(a, b))
        elif action == "-":
            return str(self.calc_diff(a, b))
        elif action == "*":
            return str(self.calc_mult(a, b))
        elif action == "/":
            return str(self.calc_div(a, b))

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
            return self.text_upper(str(text))
        elif action == "lower":
            return self.text_lower(str(text))
        elif action == "trim":
            return self.text_trim(str(text))
        elif action == "alter":
            return self.text_alter(str(text))

# Блок методов для парсинга в тексте емэйлов и номеров телефонов
    def text_email(self, text: str) -> str:
        """
        Метод ищет емэйлы в тексте.
        Args:
            text: текст
        Return:
            емэйлы
        """
        emails = re.findall(r'[\w\.-]+@[\w\.-]+', text)
        return ', '.join(emails)

    def text_number(self, text: str) -> str:
        """
        Метод ищет номера телефонов в тексте.
        Args:
            text: текст
        Return:
            номера телефонов
        """
        phone_numbers = re.findall(r'(?:7|8|\+7)(?:[\s\(-]?|\s\()[\d]{3}(?:\)|-|\s)*[\d]{3}[-\s]?[\d]{2}[-\s]?[\d]{2}', text)
        return ', '.join(phone_numbers)

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
            return self.text_email(text)
        if action == "number":
            return self.text_number(text)


controller = Controller()
