from datetime import datetime
# Переменные предназначены для хранения данных.
# Название переменной в Python должно начинаться
# с алфавитного символа или со знака подчеркивания
# и может содержать алфавитно-цифровые символы
# и знак подчеркивания. И кроме того, название
# переменной не должно совпадать с названием
# ключевых слов языка Python. Ключевых слов
# не так много, их легко запомнить:


name = input("Как тебя зовут? ")
print(f"Hello {name} !")
age = int(input("Сколько тебе лет ?"))
PythonAge = datetime.now().year - 1994
print(f"А мне {PythonAge} )")
