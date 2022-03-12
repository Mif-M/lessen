##Переменные и типы данных

###Переменные

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
