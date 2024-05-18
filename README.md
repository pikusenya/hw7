# Test project

Пет-проект, в рамках которого реализую свои знания языка python на примере следующего функционала:
/calculation - выполнение простых математических операций.
/text-editor - преобразование текста.
/parser - поиск емэйла или номера телефона.

## Built with
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/) [![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)

## Run Locally

Clone the project

```bash
  git clone https://github.com/pikusenya/hw7.git
```

Go to the project directory

```bash
  cd hw7
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python view.py
```


## Usage/Examples

Edit req_to_site.py file:
```python
    response = requests.post("http://127.0.0.1:5000/calculation", json={"a": 5, "b": 10, "action": "-"})
    print(response.text)
```
Console output: -5

## License

[MIT](https://choosealicense.com/licenses/mit/)
