## Переменные и типы данных

### Переменные

Переменные предназначены для хранения данных.
Название переменной в Python должно начинаться
с алфавитного символа или со знака подчеркивания
и может содержать алфавитно-цифровые символы и знак подчеркивания.
И кроме того, название переменной не должно совпадать с названием 
ключевых слов языка Python. Ключевых слов не так много, их легко запомнить:

<div class="container"><div class="line number1 index0 alt2"><code class="py color1">False</code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <code class="py plain">await&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </code><code class="py keyword">else</code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <code class="py keyword">import</code>&nbsp;&nbsp;&nbsp;&nbsp; <code class="py keyword">pass</code></div><div class="line number2 index1 alt1"><code class="py color1">None</code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <code class="py keyword">break</code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <code class="py keyword">except</code>&nbsp;&nbsp;&nbsp;&nbsp; <code class="py keyword">in</code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <code class="py keyword">raise</code></div><div class="line number3 index2 alt2"><code class="py color1">True</code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <code class="py keyword">class</code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <code class="py keyword">finally</code>&nbsp;&nbsp;&nbsp; <code class="py keyword">is</code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <code class="py keyword">return</code></div><div class="line number4 index3 alt1"><code class="py keyword">and</code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <code class="py keyword">continue</code>&nbsp;&nbsp; <code class="py keyword">for</code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <code class="py keyword">lambda</code>&nbsp;&nbsp;&nbsp;&nbsp; <code class="py keyword">try</code></div><div class="line number5 index4 alt2"><code class="py plain">as&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </code><code class="py keyword">def</code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <code class="py keyword">from</code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <code class="py plain">nonlocal&nbsp;&nbsp; </code><code class="py keyword">while</code></div><div class="line number6 index5 alt1"><code class="py keyword">assert</code>&nbsp;&nbsp;&nbsp;&nbsp; <code class="py keyword">del</code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <code class="py keyword">global</code>&nbsp;&nbsp;&nbsp;&nbsp; <code class="py keyword">not</code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <code class="py plain">with</code></div><div class="line number7 index6 alt2"><code class="py plain">async&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </code><code class="py keyword">elif</code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <code class="py keyword">if</code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <code class="py keyword">or</code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <code class="py keyword">yield</code></div></div>

Например, создадим переменную:

```python
name = "Tom"
```

Здесь определена переменная name, которая хранит строку "Tom".

В пайтоне применяется два типа наименования переменных: camel case и underscore notation.

Camel case подразумевает, что каждое новое подслово в наименовании переменной начинается с большой буквы. Например:

```python
userName = "Tom"
```
Underscore notation подразумевает, что подслова в наименовании переменной разделяются знаком подчеркивания. Например:

```python
user_name = "Tom"
```

И также надо учитывать регистрозависимость, поэтому переменные name и Name будут представлять разные объекты.

```python
# две разные переменные
name = "Tom"
Name = "Tom"
```

Определив переменную, мы можем использовать в программе. Например, попытаться вывести ее содержимое на консоль с помощью встроенной функции print:

```python
name = "Tom"  # определение переменной name
print(name)   # вывод значения переменной name на консоль
```

Отличительной особенностью переменной является то, что мы можем менять ее значение в течение работы программы:

```python
name = "Tom"  # переменной name равна "Tom"
print(name)   # выводит: Tom
name = "Bob"  # меняем значение на "Bob"
print(name)   # выводит: Bob
```

## Типы данных
Переменная хранит данные одного из типов данных.
В Python существует множество различных типов данных. 
В данном случае рассмотрим только самые базовые типы: 
**bool, int, float, complex** и **str**.

## Логические значения
Тип **bool** представляет два логических значения: 
**True** (верно, истина) или **False** (неверно, ложь). 
Значение **True** служит для того, чтобы показать, что что-то **истинно**. 
Тогда как значение **False**, наоборот, показывает, что что-то **ложно**. 
Пример переменных данного типа:

```python
isMarried = False
print(isMarried)    # False
 
isAlive = True
print(isAlive)      # True
```
Целые числа
Тип **int** представляет целое число, например, 1, 4, 8, 50. Пример

```python
age = 21
print("Возраст:", age)    # Возраст: 21
count = 15
print("Количество:", count) # Количество: 15
```

**По умолчанию** стандартные числа расцениваются как числа в **десятичной системе**.
Но Python также **поддерживает** числа в **двоичной, восьмеричной** и 
**шестнадцатеричной системах**.

Для указания, что число представляет двоичную систему, 
перед числом ставится префикс **0b**:

```python
a = 0b11
b = 0b1011
c = 0b100001
print(a)    # 3 в десятичной системе
print(b)    # 11 в десятичной системе
print(c)    # 33 в десятичной системе
```

Для указания, что число представляет восьмеричную систему, 
перед числом ставится префикс **0o**:

```python
a = 0o7
b = 0o11
c = 0o17
print(a)    # 7 в десятичной системе
print(b)    # 9 в десятичной системе
print(c)    # 15 в десятичной системе
```

Для указания, что число представляет шестнадцатеричную систему, 
перед числом ставится префикс **0x**:

```python
a = 0x0A
b = 0xFF
c = 0xA1
print(a)    # 10 в десятичной системе
print(b)    # 255 в десятичной системе
print(c)    # 161 в десятичной системе
```

Стоит отметить, что в какой-бы системе мы не передали число в функцию 
print для вывода на консоль, оно по умолчанию будет выводиться в десятичной системе.

### Дробные числа
Тип **float** представляет **число с плавающей точкой**, 
например, 1.2 или 34.76. В качесте разделителя 
целой и дробной частей используется **точка**.

```python
height = 1.68
pi = 3.14
weight = 68.
print(height)   # 1.68
print(pi)       # 3.14
print(weight)   # 68.0
```

Число с плавающей точкой **можно** определять в **экспоненциальной 
записи**:

```python
x = 3.9e3
print(x)  # 3900.0
 
x = 3.9e-3
print(x)  # 0.0039
```

Число **float** может иметь только **18 значимых символов**.
Так, в данном случае используются только два символа - 3.9.
И если число слишком велико или слишком мало, 
то мы можем записывать число **в подобной нотации, 
используя экспоненту**. Число после экспоненты указывает 
степень числа 10, на которое надо умножить основное число - 3.9.

### Комплексные числа
Тип **complex** представляет комплексные числа в формате вещественная_часть+мнимая_частьj - после мнимой части указывается суффикс j

```python
complexNumber = 1+2j
print(complexNumber)   # (1+2j)
```

### Строки
Тип **str** представляет строки. Строка представляет последовательность символов, 
заключенную в одинарные или двойные кавычки, например "hello" и 'hello'. 
В Python 3.x строки представляют набор символов в кодировке Unicode

```python
message = "Hello World!"
print(message)  # Hello World!
 
name = 'Tom'
print(name)  # Tom
```

При этом если строка имеет много символов, 
ее можем разбить ее на части и разместить их на разных строках кода. 
В этом случае вся строка заключается в круглые скобки, 
а ее отдельные части - в кавычки:

```python
text = ("Laudate omnes gentes laudate "
        "Magnificat in secula ")
print(text)
```

Если же мы хотим определить многострочный текст, то такой текст заключается в тройные двойные или одинарные кавычки:

```python
'''
Это комментарий
'''
text = '''Laudate omnes gentes laudate
Magnificat in secula
Et anima mea laudate
Magnificat in secula 
'''
print(text)
```

При использовани тройных одинарных кавычек не стоит путать их с комментариями: 
если текст в тройных одинарных кавычках присваивается переменной, то это строка, 
а не комментарий.

Управляющие последовательности в строке
Строка может содержать ряд специальных символов - управляющих последовательностей. 
Некоторые из них:

* \: позволяет добавить внутрь строки слеш

* \': позволяет добавить внутрь строки одинарную кавычку

* \": позволяет добавить внутрь строки двойную кавычку

* \n: осуществляет переход на новую строку

* \t: добавляет табуляцию (4 отступа)

Применим несколько последовательностей:

```python
text = "Message:\n\"Hello World\""
print(text)
```

### Вставка значений в строку
Python позволяет встравивать в строку значения других переменных. Для этого внутри строки переменные размещаются в фигурных скобках {}, а перед всей строкой ставится символ f:

```python
userName = "Tom"
userAge = 37
user = f"name: {userName}  age: {userAge}"
print(user)   # name: Tom  age: 37
```

В данном случае на место {userName} будет вставляться значение переменной userName. 
Аналогично на вместо {userAge} будет вставляться значение переменной userAge.

### Динамическая типизация
Python является языком с динамической типизацией. 
А это значит, что переменная не привязана жестко с определенному типу.

Тип переменной определяется исходя из значения, которое ей присвоено. 
Так, при присвоении строки в двойных или одинарных кавычках переменная имеет тип str. 
При присвоении целого числа Python автоматически определяет тип переменной как int. 
Чтобы определить переменную как объект float, ей присваивается дробное число, 
в котором разделителем целой и дробной части является точка.

При этом в процессе работы программы мы можем изменить тип переменной, 
присвоив ей значение другого типа:

```python
userId = "abc"  # тип str
print(userId)
 
userId = 234  # тип int
print(userId)
```

С помощью встроенной функции type() динамически можно узнать текущий тип переменной:

```python
userId = "abc"      # тип str
print(type(userId)) # <class 'str'>
 
userId = 234        # тип int
print(type(userId)) # <class 'int'>
```