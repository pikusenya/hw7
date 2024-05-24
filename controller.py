from validator import validator
from typing import Union
import re


class Controller:
    def calc_map_func(self, action, a, b):
        func_map = {
            "+": self.calc_sum,
            "-": self.calc_diff,
            "*": self.calc_mult,
            "/": self.calc_div
        }
        return str(func_map[action](a, b))

    def text_map_func(self, action, text):
        func_map = {
            "upper": self.text_upper,
            "lower": self.text_lower,
            "trim": self.text_trim,
            "alter": self.text_alter
        }
        return str(func_map[action](text))

    def parser_map_func(self, action, text):
        func_map = {
            "email": self.text_email,
            "number": self.text_number,
        }
        return str(func_map[action](text))
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
        Метод вычитает из первого аргумента второй.
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
        return self.calc_map_func(action, a, b)

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

        return self.text_map_func(action, text)

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
        phone_numbers = re.findall(r'(?:7|8|\+7)(?:[\s\(-]?|\s\()\d{3}(?:\)|-|\s)*\d{3}[-\s]?\d{2}[-\s]?\d{2}', text)
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

        return self.parser_map_func(action, text)


controller = Controller()
