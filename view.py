from flask import Flask, request
from controller import controller

app = Flask("test_prjct")


@app.route("/")
def start():
    """
    Функция возвращает стартовый запрос приветствия.
    """
    return "this is test prjct"


@app.route("/helpme")
def helpme():
    """
    Функция возвращает информацию со справкой по работе проекта.
    """
    return ''' Доступные команды: /calculation, /text_editor, /parser.
Calculation: производит математические операции +, -, * и /.
Данные передавать в виде словаря со следующими ключами: {"a": int, "b": int, "action": +, -, * или /}

Text_editor: преобразует передаваемый текст.
Данные передавать в виде словаря со следующими ключами: {"text": "текст", "action": upper, lower, trim или alter}
Upper возвращает "ТЕКСТ" буквами, lower возвращает "текст" строчными буквами, trim убирает пробелы из текста, alter возвращает перевернутый "тскет"

Parser: находит емэйлы или номера телефонов в тексте.
Данные передавать в виде словаря со следующими ключами: {"text": "текст", "action": email или number}
'''


@app.route("/calculation", methods=["POST"])
def calculation():
    """
    Функция создаёт запрос для выполнения математических операций с данными.
    Return:
        результат математических операций.
    """
    data = request.json
    return controller.calculate(data)


@app.route("/text_editor", methods=["POST"])
def text_editor():
    """
    Функция создаёт запрос для преобразования передаваемого текста.
    Return:
        преобразованный текст.
    """
    data = request.json
    return controller.text_editor(data)

@app.route("/parser", methods=["POST"])
def parser():
    """
    Функция создаёт запрос для поиска в передаваемом тексте емэйлов
    или номеров телефонов.
    Return:
        номера телефонов или емэйлы из текста.
    """
    data = request.json
    return controller.parser(data)


if __name__ == "__main__":
    app.run(debug=True)
