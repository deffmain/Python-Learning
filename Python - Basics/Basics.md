# Python — Fundamentos

> Anotações práticas sobre o que é Python e onde ele é usado, declaração de variáveis, regras e convenções de nomenclatura, comentários, a função `print()`, tipos de dados, strings e seus métodos, inteiros e floats, atribuição aumentada, condicionais e operadores de comparação, valores truthy e falsy, operadores booleanos, funções (embutidas e personalizadas, parâmetros e argumentos, `return` e `None`) e escopo local e global.

---

## O que é Python e usos comuns

Python é uma linguagem de programação de uso geral conhecida por sua simplicidade e facilidade de uso. Essa facilidade de uso tornou o Python a linguagem de programação mais popular nos tempos modernos.

Python é usado em muitos campos como ciência de dados e aprendizado de máquina, desenvolvimento web, scripting e automação, sistemas embarcados, IoT e muito mais.

Python é a principal linguagem que a maioria dos cientistas de dados e engenheiros de machine learning usa atualmente. Bibliotecas como Pandas e NumPy tornam a análise de dados menos cansativa, enquanto outras como TensorFlow e Scikit-learn facilitam muito o machine learning e o trabalho com modelos de IA.

No desenvolvimento web, frameworks Python como Django, FastAPI e Flask permitem que desenvolvedores construam sistemas back-end escaláveis e seguros com esforço mínimo. Muitas plataformas de mídia social como Instagram e Pinterest usam Python no back-end.

Profissionais de cibersegurança e hackers éticos usam Python para detectar vulnerabilidades e ameaças como malware e vírus, criar varreduras de segurança automatizadas e analisar ameaças.

Python roda bem em microcomputadores como o Raspberry Pi e placas compatíveis com MicroPython, então você pode criar todos os tipos de projetos de IoT como dispositivos para casas inteligentes, estações de monitoramento do tempo e mais.

Python é amplamente usado em DevOps para escrever scripts de CI/CD e gerenciar infraestrutura em pipelines de desenvolvimento. Também é comumente usado para construir serviços de back-end e APIs internas.

Em testes de software, ferramentas Python como pytest são usadas para criar suítes de teste confiáveis, enquanto administradores de sistema dependem do Python para monitoramento de servidor, gerenciamento de logs e tarefas em nível de sistema.

Finalmente, uma das maiores forças do Python é a automação. Você pode escrever scripts simples para ajudar com tarefas repetitivas como extrair dados de planilhas, enviar e-mails e trabalhar com arquivos na sua máquina local.

Bibliotecas como Selenium e BeautifulSoup também facilitam a interação com sites, para que você possa extrair dados públicos, automatizar tarefas por meio de uma interface web e até gerenciar implantações em nuvem para seus projetos.

---

## Variáveis e convenções de nomenclatura

### Declarando variáveis

Em Python, variáveis são como caixas rotuladas para armazenar e referenciar dados de diferentes tipos. Para criar uma variável, escreva seu nome à esquerda, seguido pelo operador de atribuição (`=`) e o valor que você quer armazenar à direita. Aqui está um exemplo de como criar as variáveis `name` e `age`:

```python
name = 'John Doe'
age = 25
```

No exemplo acima, a variável `name` armazena o valor `'John Doe'`. Esse valor é uma string, que é uma série de caracteres usada para representar texto. Strings são escritas com aspas simples ou duplas, por exemplo `'Hello'` ou `"Hello"`. Em aulas futuras, você aprenderá mais sobre como trabalhar com strings em Python.

### Regras de nomenclatura

Ao nomear variáveis em Python, há algumas regras importantes que você deve ter em mente:

- Os nomes das variáveis só podem começar com uma letra ou um underscore (`_`), não com um número.
- Os nomes das variáveis só podem conter caracteres alfanuméricos (`a-z`, `A-Z`, `0-9`) e underscores (`_`).
- Os nomes das variáveis são sensíveis a maiúsculas e minúsculas: `age`, `Age` e `AGE` são todos considerados únicos.
- Os nomes das variáveis não podem ser palavras-chave reservadas do Python, como `if`, `class` ou `def`.

> Na prática, o Python 3 também aceita letras acentuadas e de outros alfabetos (`ação = 1` e `preço = 2.5` funcionam). Usar só `a-z`, `A-Z`, `0-9` e `_` é a recomendação da PEP 8, não uma exigência da linguagem.

Se você quebrar alguma dessas regras, seu programa Python vai gerar um `SyntaxError`:

```text
    5variable_name = 5
    ^
SyntaxError: invalid decimal literal
```

> A mensagem exata depende da versão do Python: no 3.12, começar o nome com número mostra `invalid decimal literal`; versões mais antigas mostravam `invalid syntax`. Usar uma palavra reservada (`class = 5`) mostra `invalid syntax`.

### Convenções de nomenclatura

Agora vamos revisar algumas convenções comuns de nomenclatura para variáveis em Python.

Primeiro, os nomes das variáveis devem estar em minúsculas, com as palavras separadas por underscore. Isso é chamado de snake case:

```python
my_variable_name = 'freeCodeCamp'
```

Em seguida, você deve usar nomes descritivos para variáveis. Por exemplo, se você quiser salvar a idade de um usuário como uma variável, `user_age` é melhor do que `age` ou uma abreviação como `ua`:

```python
user_age = 30
```

Dessa forma, você pode comunicar facilmente o propósito de uma variável para outros membros da equipe (ou para você mesmo no futuro) em uma base de código grande.

Outra convenção é evitar usar nomes de variáveis com uma única letra. Nomes de uma letra são comuns em Python, mas devem ser evitados porque não comunicam propósito ou significado:

```python
x = 56 # O que significa x?
```

### Comentários

O símbolo de cerquilha (`#`) e o texto que o segue formam um comentário. Comentários permitem que você adicione notas e explicações ao seu código.

Em Python, comentários começam com o símbolo de cerquilha (`#`), e a linguagem ignora tudo depois do símbolo `#` naquela linha:

```python
# Este é um comentário de uma linha
```

Comentários de múltiplas linhas podem ser criados usando comentários de uma única linha consecutivos:

```python
# Este é um
# comentário de
# múltiplas linhas
```

Você pode usar comentários para explicar seu código, deixar lembretes para si mesmo ou esclarecer por que uma linha existe. Comentários são especialmente úteis quando você está aprendendo ou trabalhando em equipes.

No entanto, você não deve usar comentários para explicar o que seus nomes de variáveis significam. Em vez disso, os nomes que você escolher para suas variáveis devem ser descritivos e comunicar para que elas servem e seguir as outras regras de nomenclatura mencionadas anteriormente para evitar erros de sintaxe.

---

## A função print()

O terminal é a área onde você pode ver a saída de texto de um programa. Python inclui `print()` como uma função embutida, o que significa que você pode usá-la sem precisar defini-la. A função `print()` envia texto e outros valores para o terminal. Vamos dar uma olhada mais de perto em como ela funciona.

Um programa inicial comum exibe `Hello world!` no terminal. Você pode escrever esse programa em Python usando a função `print`.

Para fazer isso, você só precisa colocar a string `Hello world!` entre os parênteses de abertura e fechamento que você usa para chamar a função `print`:

```python
print('Hello world!') # Hello world!
```

Você aprenderá mais sobre strings e funções em Python em lições futuras. Por enquanto, apenas considere strings como uma sequência de caracteres cercada por aspas simples (`'`) ou duplas (`"`).

No exemplo `print('Hello world!')`, a string `'Hello world!'` é um **argumento** passado para a função `print`. Você também pode usar a função `print` para mostrar múltiplos valores ou argumentos ao mesmo tempo separando-os com vírgulas. Por exemplo:

```python
print('My favorite colors are', 'blue', 'green', 'red')

# Saída: My favorite colors are blue green red
```

Python adiciona automaticamente um espaço entre cada item quando você os separa com vírgulas. Isso é útil quando você quer imprimir várias informações juntas.

---

## Tipos de dados

Antes de trabalhar com variáveis em Python, é importante entender os tipos de dados. Um tipo de dado descreve o tipo de valor que uma variável contém, por exemplo, um número ou um pedaço de texto. Linguagens de programação usam tipos de dados para saber como armazenar e trabalhar com diferentes tipos de informação.

### Tipagem dinâmica

Python é uma linguagem dinamicamente tipada. Isso significa que você não especifica o tipo de dado de uma variável quando a cria. Python determina o tipo a partir do valor atribuído à variável.

Aqui estão alguns exemplos:

```python
name = 'John Doe' # Python sabe que isto é uma string
age = 25 # Python sabe que isto é um inteiro
```

Uma variável pode depois receber um valor de um tipo diferente:

```python
age = 25
age = 'Twenty-five'
```

Após a segunda atribuição, `age` contém uma string em vez de um inteiro.

### Os quatro tipos básicos

Por enquanto, concentre-se em quatro tipos de dados que você usará ao longo deste módulo:

- **Inteiro**: Um número inteiro sem decimais, por exemplo, `10` ou `-5`.

  ```python
  my_integer_var = 10
  print('Integer:', my_integer_var) # Integer: 10
  ```

- **Float**: Um número com ponto decimal, como `4.41` ou `-0.4`.

  ```python
  my_float_var = 4.50
  print('Float:', my_float_var) # Float: 4.5
  ```

- **String**: Uma sequência de caracteres entre aspas simples ou duplas como `'Hello world!'`.

  ```python
  my_string_var = 'hello'
  print('String:', my_string_var) # String: hello
  ```

- **Booleano**: Um tipo verdadeiro ou falso, escrito como `True` ou `False`.

  ```python
  my_boolean_var = True
  print('Boolean:', my_boolean_var) # Boolean: True
  ```

---

## Strings e imutabilidade

Uma string é uma sequência de caracteres cercada por aspas simples ou duplas. O Python trata ambas as formas como strings, então você pode usar qualquer uma delas. Aqui estão alguns exemplos:

```python
my_str_1 = 'Hello'
my_str_2 = "World"
```

### Strings multilinha

Se você precisar de uma string multilinha, pode usar aspas duplas triplas ou aspas simples triplas:

```python
my_str_3 = """Multiline
string"""
my_str_4 = '''Another
multiline
string'''
```

### Aspas dentro da string

Se sua string contém aspas simples ou duplas, então você tem duas opções:

- Use o tipo oposto de aspas. Ou seja, se sua string contém aspas simples, use aspas duplas para envolver a string e vice-versa:

  ```python
  msg = "It's a sunny day"
  quote = 'She said, "Hello World!"'
  ```

- Escape a aspa simples ou dupla na string com uma barra invertida (`\`). Com este método, você pode usar aspas simples ou duplas para envolver a própria string:

  ```python
  msg = 'It\'s a sunny day'
  quote = "She said, \"Hello!\""
  ```

### O operador in

Às vezes, pode ser necessário verificar se uma string contém um ou mais caracteres. Para isso, o Python fornece o operador `in`, que retorna um booleano que especifica se o caractere ou os caracteres existem na string ou não.

Aqui estão alguns exemplos:

```python
my_str = 'Hello world'

print('Hello' in my_str)  # True
print('hey' in my_str)    # False
print('hi' in my_str)     # False
print('e' in my_str)      # True
print('f' in my_str)      # False
```

### Tamanho e indexação

Vamos agora ver como é possível obter o tamanho de uma string e como trabalhar com caracteres individuais em uma string, um processo que chamamos de **indexação**. Para obter o comprimento de uma string, você pode usar a função embutida `len()`. Aqui está um exemplo:

```python
my_str = 'Hello world'
print(len(my_str))  # 11
```

Cada caractere em uma string tem uma posição chamada índice. O índice é baseado em zero, significando que o índice do primeiro caractere de uma string é `0`, o índice do segundo caractere é `1` e assim por diante. Para acessar um caractere pelo seu índice, você usa colchetes (`[]`) com o índice do caractere que deseja acessar dentro. Aqui estão alguns exemplos:

```python
my_str = "Hello world"

print(my_str[0])  # H
print(my_str[6])  # w
```

### Indexação negativa

A indexação negativa também é permitida, então você pode obter o último caractere de qualquer string com `-1`, o penúltimo caractere com `-2` e assim por diante:

```python
my_str = "Hello world"

print(my_str[-1])  # d
print(my_str[-2])  # l
```

### Imutabilidade

No Python, valores podem ser mutáveis ou imutáveis. Um valor mutável pode ser alterado depois de criado, enquanto um valor imutável não pode.

Você pode apontar uma variável para um novo valor, o que é chamado de reatribuição, mas não pode mudar o valor imutável em si adicionando, removendo ou substituindo qualquer um de seus elementos.

Strings são imutáveis em Python, mas você ainda pode reatribuir uma variável para uma string diferente:

```python
greeting = 'hi'
greeting = 'hello'
print(greeting) # hello
```

Mas a modificação direta de uma string não é permitida:

```python
greeting = 'hi'
greeting[0] = 'H' # TypeError: 'str' object does not support item assignment
```

Inteiros, floats e booleanos também são imutáveis. Você vai aprender sobre outros tipos imutáveis em lições futuras.

---

## Métodos de string

Um método é uma função que você chama em um valor. Para chamar um método de string, escreva a string ou o nome da variável seguido de um ponto e da chamada do método. Você vai aprender mais sobre métodos quando estudar classes e objetos. Aqui estão alguns métodos comuns de string:

### upper() — tudo em maiúsculas

Retorna uma nova string com todos os caracteres convertidos para maiúsculas.

```python
my_str = 'hello world'

uppercase_my_str = my_str.upper()
print(uppercase_my_str)  # HELLO WORLD
```

### lower() — tudo em minúsculas

Retorna uma nova string com todos os caracteres convertidos para minúsculas.

```python
my_str = 'Hello World'

lowercase_my_str = my_str.lower()
print(lowercase_my_str)  # hello world
```

### strip() — remove do início e do fim

Retorna uma nova string com os caracteres especificados no início e no fim removidos. Se nenhum argumento for passado, remove os espaços em branco do início e do fim.

```python
my_str = '  hello world  '

trimmed_my_str = my_str.strip()
print(trimmed_my_str)  # hello world
```

### replace(old, new) — substitui

Retorna uma nova string com todas as ocorrências de `old` substituídas por `new`.

```python
my_str = 'hello world'

replaced_my_str = my_str.replace('hello', 'hi')
print(replaced_my_str)  # hi world
```

### split(separator) — divide em uma lista

Divide uma string em um separador especificado em uma lista de strings. Uma lista agrupa valores entre colchetes. Se nenhum separador for especificado, `split()` divide pelo espaço em branco.

```python
my_str = 'hello world'

split_words = my_str.split()
print(split_words)  # ['hello', 'world']
```

### join() — junta em uma string

Junta as strings em uma coleção em uma única string com um separador.

```python
my_list = ['hello', 'world']

joined_my_str = ' '.join(my_list)
print(joined_my_str)  # hello world
```

### startswith(prefix) — começa com

Retorna um booleano indicando se uma string começa com o prefixo especificado.

```python
my_str = 'hello world'

starts_with_hello = my_str.startswith('hello')
print(starts_with_hello)  # True
```

### endswith(suffix) — termina com

Retorna um booleano indicando se uma string termina com o sufixo especificado.

```python
my_str = 'hello world'

ends_with_world = my_str.endswith('world')
print(ends_with_world)  # True
```

### find(substring) — índice da primeira ocorrência

Retorna o índice da primeira ocorrência de `substring`, ou `-1` se não encontrar nenhuma.

```python
my_str = 'hello world'

world_index = my_str.find('world')
print(world_index)  # 6
```

### count(substring) — conta ocorrências

Retorna o número de ocorrências não sobrepostas de uma substring em uma string.

```python
my_str = 'hello world'

o_count = my_str.count('o')
print(o_count)  # 2
```

### capitalize() — primeira letra maiúscula

Retorna uma nova string com o primeiro caractere em maiúscula e os outros caracteres em minúscula.

```python
my_str = 'hello world'

capitalized_my_str = my_str.capitalize()
print(capitalized_my_str)  # Hello world
```

### isupper() — está tudo em maiúsculas?

Retorna `True` se a string contém pelo menos um caractere com caixa e todos os caracteres com caixa são maiúsculas. Caso contrário, retorna `False`.

```python
my_str = 'hello world'

is_all_upper = my_str.isupper()
print(is_all_upper)  # False
```

### islower() — está tudo em minúsculas?

Retorna `True` se a string contém pelo menos um caractere com caixa e todos os caracteres com caixa são minúsculas. Caso contrário, retorna `False`.

```python
my_str = 'hello world'

is_all_lower = my_str.islower()
print(is_all_lower)  # True
```

### title() — primeira letra de cada palavra maiúscula

Retorna uma nova string com a primeira letra de cada palavra em maiúsculas e as demais letras em minúsculas.

```python
my_str = 'hello world'

title_case_my_str = my_str.title()
print(title_case_my_str)  # Hello World
```

### Resumo

| Método               | Retorna                                                                    |
| -------------------- | -------------------------------------------------------------------------- |
| `upper()`            | nova string em maiúsculas                                                  |
| `lower()`            | nova string em minúsculas                                                  |
| `strip()`            | nova string sem os espaços (ou os caracteres indicados) do início e do fim |
| `replace(old, new)`  | nova string com `old` trocado por `new`                                    |
| `split(separator)`   | lista de strings                                                           |
| `join()`             | uma string com os itens da coleção unidos pelo separador                   |
| `startswith(prefix)` | `True` ou `False`                                                          |
| `endswith(suffix)`   | `True` ou `False`                                                          |
| `find(substring)`    | índice da primeira ocorrência, ou `-1`                                     |
| `count(substring)`   | número de ocorrências não sobrepostas                                      |
| `capitalize()`       | nova string com só o primeiro caractere em maiúscula                       |
| `isupper()`          | `True` ou `False`                                                          |
| `islower()`          | `True` ou `False`                                                          |
| `title()`            | nova string com a primeira letra de cada palavra em maiúscula              |

---

## Inteiros e floats

Inteiros e floats são os principais tipos de dados numéricos em Python. Com eles, você pode armazenar dados numéricos e realizar operações matemáticas.

Vamos ver o que são inteiros e floats, como realizar cálculos aritméticos com eles e algumas funções embutidas que o Python oferece para trabalhar com ambos.

### Inteiros

Inteiros são números inteiros sem pontos decimais, incluindo números positivos, números negativos e zero:

```python
my_int_1 = 56
my_int_2 = -4

print(type(my_int_1)) # <class 'int'>
print(type(my_int_2)) # <class 'int'>
```

Aqui está como realizar uma operação de adição com inteiros:

```python
my_int_1 = 56
my_int_2 = 12

sum_ints = my_int_1 + my_int_2
print('Integer Addition:', sum_ints) # Integer Addition: 68
```

Aqui está como realizar uma subtração com inteiros:

```python
my_int_1 = 56
my_int_2 = 12

# Subtração
diff_ints = my_int_1 - my_int_2
print('Integer Subtraction:', diff_ints) # Integer Subtraction: 44
```

Aqui está como realizar uma operação de multiplicação com inteiros:

```python
my_int_1 = 12
my_int_2 = 4

# Multiplicação
product_ints = my_int_1 * my_int_2
print('Integer Multiplication:', product_ints) # Integer Multiplication: 48
```

E aqui está como realizar uma operação de divisão com inteiros:

```python
my_int_1 = 56
my_int_2 = 12

# Divisão
div_ints = my_int_1 / my_int_2
print('Division:', div_ints) # Division: 4.666666666666667
```

### Floats

Floats representam números em forma de ponto flutuante, incluindo zero, como `3.14`, `-0.5` ou `0.0`.

```python
my_float_1 = -12.0
my_float_2 = 4.9

print(type(my_float_1)) # <class 'float'>
print(type(my_float_2)) # <class 'float'>
```

Aqui está uma operação de adição com floats:

```python
my_float_1 = 5.4
my_float_2 = 12.0

float_addition = my_float_1 + my_float_2
print('Float Addition:', float_addition) # Float Addition: 17.4
```

Aqui está uma operação de subtração com floats:

```python
my_float_1 = 5.4
my_float_2 = 12.0

float_subtraction = my_float_2 - my_float_1
print('Float Subtraction:', float_subtraction) # Float Subtraction: 6.6
```

Aqui está uma operação de multiplicação com floats:

```python
my_float_1 = 5.4
my_float_2 = 12.0

float_multiplication = my_float_2 * my_float_1
print('Float Multiplication:', float_multiplication) # Float Multiplication: 64.80000000000001
```

E aqui está uma operação de divisão com floats:

```python
my_float_1 = 5.4
my_float_2 = 12.0

float_division = my_float_2 / my_float_1
print('Float Division:', float_division) # Float Division: 2.222222222222222
```

### Misturando inteiros e floats

Se você adicionar um inteiro e um float, o resultado é automaticamente convertido para um float:

```python
my_int = 56
my_float = 5.4

sum_int_and_float = my_int + my_float

print(sum_int_and_float) # 61.4
print(type(sum_int_and_float)) # <class 'float'>
```

Isso é verdade para outras operações aritméticas básicas também, como subtração, multiplicação e divisão. Se você misturar inteiros e floats, Python retornará um float como resultado.

### Módulo, divisão inteira e exponenciação

Você também pode realizar cálculos aritméticos mais complexos, como obter o resto de dois números com o operador módulo, divisão inteira e exponenciação com inteiros e floats.

O operador módulo (`%`) retorna o resto quando o valor à esquerda é dividido pelo valor à direita:

```python
my_int_1 = 56
my_int_2 = 12

my_float_1 = 5.4
my_float_2 = 12.0

mod_ints = my_int_1 % my_int_2
mod_floats = my_float_2 % my_float_1

print('Integer Modulo:', mod_ints) # Integer Modulo: 8
print('Float Modulo:', mod_floats) # Float Modulo: 1.1999999999999993
```

A divisão inteira divide dois números e retorna o maior inteiro menor ou igual ao resultado. Isso é feito com o operador de barra dupla para frente (`//`):

```python
my_int_1 = 56
my_int_2 = 12

my_float_1 = 5.4
my_float_2 = 12.0

floor_div_ints = my_int_1 // my_int_2
floor_div_floats = my_float_2 // my_float_1

print('Integer Floor Division:', floor_div_ints) # Integer Floor Division: 4
print('Float Floor Division:', floor_div_floats) # Float Floor Division: 2.0
```

A exponenciação eleva um número à potência de outro e é feita com o operador de dois asteriscos (`**`):

```python
my_int_1 = 56
my_int_2 = 12

my_float_1 = 5.4
my_float_2 = 12.0

exp_ints = my_int_1 ** my_int_2
exp_floats = my_float_1 ** my_float_2

print('Integer Exponentiation:', exp_ints) # Integer Exponentiation: 951166013805414055936
print('Float Exponentiation:',  exp_floats) # Float Exponentiation: 614787626.1765089
```

### Imprecisão dos floats

Às vezes, você pode notar que o resultado de uma operação envolvendo floats tem mais dígitos decimais do que o esperado. Por exemplo, a soma `0.1 + 0.2` é igual a `0.30000000000000004` em vez de `0.3`.

Isso acontece porque os números são armazenados em formato binário e algumas frações não podem ser representadas exatamente em binário. Como resultado, elas são armazenadas como aproximações finitas, da mesma forma que a fração `1/3` não pode ser representada com um número finito de dígitos em decimal e é truncada após um certo número de seus dígitos infinitos (`0.33333...`).

Isso leva a pequenos erros de arredondamento.

### Conversão com float() e int()

Python também fornece funções internas para converter dados numéricos ou strings em inteiros ou floats.

A função `float()` retorna um número de ponto flutuante construído a partir do número fornecido:

```python
my_int_1 = 56
my_float_1 = float(my_int_1)

print(my_float_1)  # 56.0
print(type(my_float_1))  # <class 'float'>
```

A função `int()` retorna um inteiro construído a partir do número fornecido:

```python
my_float = 12.92563
my_int = int(my_float)

print(my_int)  # 12
print(type(my_int))  # <class 'int'>
```

Além disso, você pode usar as mesmas funções internas para converter uma string em um float ou integer:

```python
my_str_int = '45'
my_str_float = '7.8'

converted_int = int(my_str_int)
converted_float = float(my_str_float)

print(converted_int, type(converted_int))  # 45 <class 'int'>
print(converted_float, type(converted_float))  # 7.8 <class 'float'>
```

### round(), abs() e pow()

Aqui estão algumas outras funções embutidas que o Python oferece para trabalhar com inteiros e floats.

- `round()`: Arredonda um número para o número especificado de casas decimais. Por padrão essa função arredonda para o inteiro mais próximo e retorna um número inteiro sem casas decimais:

  ```python
  my_int_1 = 4.798
  my_int_2 = 4.253

  rounded_int_1 = round(my_int_1)
  rounded_int_2 = round(my_int_2, 1)

  print(rounded_int_1) # 5
  print(rounded_int_2) # 4.3
  ```

  > Repare: quando o número está exatamente no meio, `round()` arredonda para o inteiro **par** mais próximo. `round(2.5)` dá `2` e `round(3.5)` dá `4`.

- `abs()`: Retorna o valor absoluto de um número:

  ```python
  num = -15

  absolute_value = abs(num)
  print(absolute_value) # 15
  ```

- `pow()`: eleva um número à potência de outro ou realiza exponenciação modular.

  ```python
  result_1 = pow(2, 3)  # Equivale a 2 ** 3
  print(result_1)  # 8

  result_2 = pow(2, 3, 5)  # (2 ** 3) % 5
  print(result_2)  # 3
  ```

---

## Atribuição aumentada

A atribuição aumentada aplica uma operação a uma variável e armazena o resultado de volta na mesma variável, tudo em um único passo.

### Sintaxe

A sintaxe básica de uma atribuição aumentada é assim:

```python
variable <operator>= value
```

Para variáveis numéricas, esta é uma forma mais curta de escrever a seguinte atribuição:

```python
variable = variable <operator> value
```

Por exemplo, você pode usar a atribuição aumentada para adicionar `5` a uma variável existente:

```python
my_var = 10
my_var += 5

print(my_var) # 15
```

E aqui está a mesma coisa, mas sem atribuição aumentada:

```python
my_var = 10
my_var = my_var + 5

print(my_var) # 15
```

A vantagem da atribuição aumentada é que ela fornece uma forma concisa e legível de atualizar o valor de uma variável sem repetir o nome da variável. Por sua vez, isso reduz a redundância e os erros potenciais que podem surgir de um erro de digitação ou algo semelhante.

### Outros operadores

Operadores aritméticos e bit a bit têm formas de atribuição aumentada. Já vimos o operador de atribuição de adição (`+=`), então vamos ver outros.

- O operador de atribuição de subtração (`-=`) subtrai o operando da direita da variável da esquerda e armazena a diferença na variável da esquerda:

  ```python
  count = 14
  count -= 3

  print(count) # 11
  ```

- O operador de atribuição de multiplicação (`*=`) multiplica a variável à esquerda pelo operando à direita e armazena o produto de volta na variável à esquerda:

  ```python
  product = 65
  product *= 7

  print(product) # 455
  ```

- O operador de atribuição de divisão (`/=`) divide a variável à esquerda pela da direita e armazena o resultado de volta na variável à esquerda:

  ```python
  price = 100
  price /= 4

  print(price) # 25.0
  ```

- O operador de atribuição de divisão inteira (`//=`) realiza a divisão inteira da variável à esquerda pelo valor à direita e armazena o resultado de volta na variável à esquerda:

  ```python
  total_pages = 23
  total_pages //= 5

  print(total_pages) # 4
  ```

- O operador de atribuição de módulo (`%=`) calcula o resto da variável à esquerda dividida pela da direita e armazena o resultado de volta na variável à esquerda:

  ```python
  bits = 35
  bits %= 2

  print(bits) # 1
  ```

- O operador de atribuição de exponenciação (`**=`) eleva a variável à esquerda à potência da variável à direita e armazena o resultado de volta na variável à esquerda:

  ```python
  power = 2
  power **= 3

  print(power) # 8
  ```

### Atribuição aumentada com strings

Você também pode usar alguns operadores de atribuição aumentada com strings. Por exemplo, o operador de atribuição de adição facilita a concatenação de strings:

```python
greet = 'Hello'
greet += ' World'

print(greet) # Hello World
```

E o operador de atribuição de multiplicação pode ser usado para repetir uma string:

```python
greet = 'Hello'
greet *= 3

print(greet) # HelloHelloHello
```

Os operadores de atribuição de subtração e divisão geram um `TypeError` quando usados com strings:

```python
greet = 'Hello'
greet -= ' World' # TypeError: unsupported operand type(s) for -=: 'str' and 'str'
```

```python
greet = 'Hello'
greet /= 'World' # TypeError: unsupported operand type(s) for /=: 'str' and 'str'
```

### Resumo

| Operador | Equivale a   | Operação        |
| -------- | ------------ | --------------- |
| `+=`     | `x = x + y`  | adição          |
| `-=`     | `x = x - y`  | subtração       |
| `*=`     | `x = x * y`  | multiplicação   |
| `/=`     | `x = x / y`  | divisão         |
| `//=`    | `x = x // y` | divisão inteira |
| `%=`     | `x = x % y`  | módulo (resto)  |
| `**=`    | `x = x ** y` | exponenciação   |

---

## Condicionais e operadores de comparação

As instruções condicionais, ou condicionais, permitem controlar o fluxo do programa com base no fato de determinadas condições serem verdadeiras ou falsas.

Mas antes de entrarmos em detalhes, vamos revisar os elementos básicos das instruções condicionais, começando pelos operadores de comparação. Os operadores de comparação permitem comparar dois ou mais valores e retornam um valor booleano.

Em uma lição anterior, você aprendeu que os valores booleanos são um dos tipos de dados em Python e só podem ser verdadeiros (`True`) ou falsos (`False`).

### Operadores de comparação

Segue uma tabela com os operadores de comparação em Python:

| Operador | Nome             | Descrição                                                           |
| -------- | ---------------- | ------------------------------------------------------------------- |
| `==`     | Igual            | Verifica se dois valores são iguais.                                |
| `!=`     | Não é igual      | Verifica se dois valores são diferentes.                            |
| `>`      | Maior que        | Verifica se o valor à esquerda é maior que o valor à direita.       |
| `<`      | Menor que        | Verifica se o valor à esquerda é menor que o valor à direita.       |
| `>=`     | Maior ou igual a | Verifica se o valor à esquerda é maior ou igual ao valor à direita. |
| `<=`     | Menor ou igual a | Verifica se o valor à esquerda é menor ou igual ao valor à direita. |

Aqui estão algumas dessas expressões que resultam em `True` ou `False`:

```python
print(3 > 4) # False
print(3 < 4) # True
print(3 == 4) # False
print(4 == 4) # True
print(3 != 4) # True
print(3 >= 4) # False
print(3 <= 4) # True
```

### A instrução if

Esses operadores podem ser usados em condicionais para comparar valores e executar determinado código com base no resultado da condicional, se verdadeira (`True`) ou falsa (`False`).

Em Python, a condicional mais básica é a instrução `if`. Aqui está a sintaxe básica:

```python
if condition:
    pass # Código executado se condition for True
```

- As instruções `if` começam com a palavra-chave `if`.
- `condition` é uma expressão que avalia para `True` ou `False`, seguida por dois pontos (`:`).
- O corpo da instrução `if` constitui um bloco de código, que é um grupo de instruções que pertencem ao mesmo contexto. Os espaços no início de uma linha são chamados de indentação. Em Python, a indentação determina quais instruções pertencem a um bloco de código.

No exemplo acima, o corpo da instrução `if` contém uma instrução `pass`. Quando uma instrução `pass` é executada, nada acontece. Esta é uma palavra-chave especial que pode ser usada como um marcador para código futuro e é útil quando blocos de código vazios não são permitidos.

O código dentro do corpo da instrução `if` é executado somente quando a condição é avaliada como verdadeira (`True`). Por exemplo:

```python
age = 18

if age >= 18:
    print('You are an adult') # You are an adult
```

Os quatro espaços antes de `print('You are an adult')` recuam essa linha e a posicionam dentro do bloco `if`.

O código a seguir geraria uma exceção `IndentationError`, que é a maneira do Python sinalizar que a indentação é necessária em um determinado ponto do código:

```python
age = 18

if age >= 18:
print('You are an adult') # IndentationError: expected an indented block after 'if' statement on line 3
```

Embora você possa usar qualquer número de espaços (desde que seja consistente) para determinar cada nível de indentação, o guia de estilo do Python recomenda o uso de quatro espaços.

Os blocos também são encontrados em loops e funções, sobre os quais você aprenderá em lições futuras.

Voltando ao nosso exemplo, se `age` for menor que `18`, nada será impresso no terminal:

```python
age = 12

if age >= 18:
    print('You are an adult') # Nada aparece no terminal
```

### A cláusula else

Mas e se você também quiser imprimir algo se `age` for menor que `18`? É aí que entra a cláusula `else`. A cláusula `else` é executada quando a condição do `if` é falsa. Aqui está a sintaxe de uma instrução `if…else`:

```python
if condition:
    pass # Código executado se condition for True
else:
    pass # Código executado se condition for False
```

Por exemplo:

```python
age = 12

if age >= 18:
    print('You are an adult')
else:
    print('You are not an adult yet') # You are not an adult yet
```

Observe que não é possível inserir nenhuma instrução entre o bloco `if` e a cláusula `else`. O código a seguir geraria um erro `SyntaxError`:

```python
age = 12

if age >= 18:
    print('You are an adult')
print('Almost there!')
else: # SyntaxError: invalid syntax
    print('You are not an adult yet')
```

### A cláusula elif

Pode haver situações em que você queira levar em conta múltiplas condições. Para isso, o Python permite que você estenda sua instrução `if` com a palavra-chave `elif` (else if).

Eis a sintaxe:

```python
if condition1:
    pass # Código executado se condition1 for True
elif condition2:
    pass # Código executado se condition1 for False e condition2 for True
else:
    pass # Código executado se todas as condições forem False
```

Por exemplo:

```python
age = 12

if age >= 18:
    print('You are an adult')
elif age >= 13:
    print('You are a teenager')
else:
    print('You are a child') # You are a child
```

Observe que você pode usar quantas cláusulas `elif` quiser:

```python
age = 2

if age >= 65:
    print('You are a senior citizen')
elif age >= 30:
    print('You are an adult in your prime')
elif age >= 18:
    print('You are a young adult')
elif age >= 13:
    print('You are a teenager')
elif age >= 3:
    print('You are a young child')
else:
    print('You are a toddler or an infant') # You are a toddler or an infant
```

---

## Truthy, falsy e operadores booleanos

Na lição anterior, você aprendeu como usar operadores de comparação e declarações condicionais para controlar o fluxo dos seus programas.

Embora eles sejam muito poderosos, você frequentemente encontrará situações em que precisa comparar múltiplos valores ao mesmo tempo. Isso pode levar a declarações condicionais aninhadas, por exemplo:

```python
is_citizen = True
age = 25

if is_citizen:
    if age >= 18:
        print('You are eligible to vote') # You are eligible to vote
    else:
        print('You are not eligible to vote')
else:
    print('You are not eligible to vote')
```

O exemplo acima primeiro verificará se `is_citizen` é `True`. Se for o caso, ele então irá para a declaração `if` aninhada e verificará se `age` é maior ou igual a `18`. Como `age` é maior ou igual a `18`, a mensagem exibida no terminal será `You are eligible to vote`. Se `is_citizen` fosse `False`, então a mensagem impressa no terminal teria sido `You are not eligible to vote`.

Se você estiver trabalhando com declarações condicionais mais complexas, pode usar os operadores `and`, `or` e `not` do Python.

Mas antes de mergulharmos nesses operadores, vamos dar uma olhada no que são valores truthy e falsy.

### Valores truthy e falsy

Em Python, todo valor tem um valor booleano inerente, ou um sentido embutido de se ele deve ser tratado como `True` ou `False` em um contexto lógico. Muitos valores são considerados **truthy**, ou seja, eles avaliam para `True` em um contexto lógico. Outros são **falsy**, significando que eles avaliam para `False`.

Aqui estão alguns valores falsy:

- `False`
- Inteiro `0`
- Número de ponto flutuante `0.0`
- Strings vazias `""`

Outros valores como números diferentes de zero e strings não vazias são truthy.

Se você quer verificar se um valor é truthy ou falsy, você pode usar a função embutida `bool()`. Ela converte explicitamente um valor para seu equivalente booleano e retorna `True` para valores truthy e `False` para valores falsy. Aqui estão alguns exemplos:

```python
print(bool(False)) # False
print(bool(0))  # False
print(bool('')) # False

print(bool(True)) # True
print(bool(1)) # True
print(bool('Hello')) # True
```

### Operadores booleanos

Agora que você entende os valores truthy e falsy, podemos dar uma olhada nos operadores booleanos, que também são conhecidos como operadores lógicos. Estes são operadores especiais que permitem combinar múltiplas expressões para criar uma lógica de tomada de decisão mais complexa no seu código.

Existem três operadores booleanos em Python: `and`, `or` e `not`.

### O operador and

Vamos primeiro analisar o operador `and`.

O operador `and` recebe dois operandos e retorna o primeiro operando se ele for falsy; caso contrário, retorna o segundo operando. Ambos os operandos devem ser truthy para que uma expressão resulte em um valor truthy.

Aqui está um exemplo:

```python
is_citizen = True
age = 25

print(is_citizen and age) # 25
```

No exemplo acima, o número 25 é impresso no terminal porque o operador `and` avaliará o segundo operando se o primeiro operando for `True`. O operador `and` é conhecido como um operador de curto-circuito. Short-circuiting significa que o Python verifica os valores da esquerda para a direita e para assim que determina o resultado final.

Você frequentemente usará `and` dentro de declarações `if` para verificar se múltiplas condições são atendidas. Veja como você pode refatorar o exemplo anterior para usar o operador `and` em vez de declarações `if` aninhadas:

```python
is_citizen = True
age = 25

if is_citizen and age >= 18:
    print('You are eligible to vote') # You are eligible to vote
else:
    print('You are not eligible to vote')
```

No exemplo acima, `is_citizen` é `True` e `age >= 18` avalia para `True`. Como ambos os operandos do operador `and` são truthy, a condição `is_citizen and age >= 18` é avaliada como `True` e a chamada `print` no bloco `if` é executada.

### O operador or

Agora vamos analisar o operador `or`. Esse operador retorna o primeiro operando se ele for truthy; caso contrário, retorna o segundo operando. Uma expressão `or` resulta em um valor truthy se pelo menos um dos operandos for truthy. O operador `or` também é conhecido como operador de curto-circuito. Aqui está um exemplo:

```python
age = 19
is_employed = False

print(age or is_employed) # 19
```

O código acima imprimirá o número 19 porque o primeiro operando `age` é truthy.

Se você precisa verificar se uma ou mais expressões são `True`, então você pode usar o operador `or` em uma condicional assim:

```python
age = 19
is_student = True

if age < 18 or is_student:
    print('You are eligible for a student discount') # You are eligible for a student discount
else:
    print('You are not eligible for a student discount')
```

Neste caso, `age < 18` é `False`, mas `is_student` é `True`. Como pelo menos uma condição é verdadeira, toda a expressão `or` é avaliada como `True` e a mensagem de desconto no bloco `if` é exibida.

### O operador not

O último operador que vamos analisar é o operador `not` que recebe um único operando e inverte seu valor booleano. Ele converte valores truthy em `False` e valores falsy em `True`. Ao contrário dos operadores anteriores que analisamos, `not` sempre retorna `True` ou `False`.

Aqui estão alguns exemplos:

```python
print(not '') # True, porque a string vazia é falsy
print(not 'Hello') # False, porque uma string não vazia é truthy
print(not 0) # True, porque 0 é falsy
print(not 1) # False, porque 1 é truthy
print(not False) # True, porque False é falsy
print(not True) # False, porque True é truthy
```

É comum usar o operador `not` em condicionais para verificar se um valor é falsy, assim:

```python
is_admin = False

if not is_admin:
    print('Access denied for non-administrators.') # Access denied for non-administrators.
else:
    print('Welcome, Administrator!')
```

Como `is_admin` é `False`, então `not is_admin` está dizendo `not False`, que é `True`. Então a mensagem `Access denied for non-administrators.` será exibida.

---

## Funções

Funções são pedaços reutilizáveis de código que executam quando você faz uma chamada a elas. Python oferece funções embutidas, incluindo `print()`, que você usou em lições anteriores.

### input() e int() — funções embutidas

Outra função interna útil é `input()`, que permite solicitar uma entrada do usuário:

```python
name = input('What is your name?') # O usuário digita "Kolade" e pressiona Enter
print('Hello', name) # Saída: Hello Kolade
```

Por outro lado, `int()` converte um número, um booleano ou uma string que representa um inteiro em um inteiro:

```python
print(int(3.14)) # 3
print(int('42')) # 42
print(int(True)) # 1
print(int(False)) # 0
```

### Criando funções com def

Você também pode escrever suas próprias funções customizadas. Para fazer isso, você usa a palavra-chave `def`, seguida do nome que deseja dar à sua função, um par de parênteses e dois pontos. Então, em uma nova linha, você escreve o código que sua função deve executar. O código que a função executa também é chamado de corpo da função.

Aqui está um exemplo de uma função personalizada chamada `hello` que imprime a string `Hello World` no terminal:

```python
def hello():
    print('Hello World')
```

Para executar a função, você precisa chamá-la pelo nome seguido de um par de parênteses:

```python
hello() # Hello World
```

Observe a indentação antes de `print('Hello World')`. Como você deve se lembrar das lições anteriores, o Python depende da indentação para determinar quais grupos de instruções pertencem juntos. Esses grupos de instruções são chamados de blocos de código.

### Parâmetros e argumentos

Aqui está outra função simples que imprime a soma de dois números no terminal:

```python
def calculate_sum(a, b):
    print(a + b)
```

Você pode ver que nossa função, `calculate_sum`, tem `a` e `b` em seus parênteses, separados por uma vírgula. Esses são chamados de parâmetros. Pense nos parâmetros como variáveis substitutas que funcionam como "espaços" para os valores que você passa para as funções quando as chama.

Para usar os parâmetros, você precisa passar "argumentos". Argumentos são os valores que você passa para uma função quando a chama.

Aqui está como chamar a função `calculate_sum` para somar os números `3` e `1`:

```python
calculate_sum(3, 1) # 4
```

Se você chamar a função sem o número correto de argumentos, você receberá um `TypeError`:

```python
calculate_sum() # TypeError: calculate_sum() missing 2 required positional arguments: 'a' and 'b'
```

### return e o valor None

Funções também usam uma palavra-chave especial `return` para sair da função e retornar um valor. Se você não usar explicitamente `return`, o Python retornará `None` por padrão.

`None` é um valor especial que representa a ausência de um valor. É o único valor do tipo de dado `NoneType`. `None` é imutável e falso, o que significa que não pode ser alterado e é avaliado como `False` em um contexto booleano.

Aqui está um exemplo:

```python
def calculate_sum(a, b):
    print(a + b)

my_sum = calculate_sum(3, 1) # 4
print(my_sum) # None
```

Você pode ver que a função `calculate_sum` imprime a soma de `a` e `b`, mas não retorna nada explicitamente. Então, quando atribuímos seu resultado a `my_sum`, o valor é na verdade `None`. Para corrigir isso, você pode usar a palavra-chave `return` para enviar de volta o resultado:

```python
def calculate_sum(a, b):
    return a + b

my_sum = calculate_sum(3, 1)
print(my_sum) # 4
```

Agora, `calculate_sum` retorna a soma de `a` e `b`, que é armazenada em `my_sum`.

---

## Escopo

O escopo determina onde você pode usar uma variável no seu código.

Python tem regras adicionais de escopo. Por enquanto, foque no escopo local e global.

### Escopo global e escopo local

Uma variável criada fora de uma função tem escopo global. Você pode usá-la tanto dentro quanto fora das funções.

Uma variável criada dentro de uma função tem escopo local. Você só pode usá-la dentro dessa função. Parâmetros de função também são variáveis locais.

Aqui está um exemplo de escopo local e global:

```python
tax_rate = 0.1

def calculate_tax(price):
    tax = price * tax_rate
    return tax

print(calculate_tax(50)) # 5.0
print(tax_rate) # 0.1
print(tax) # NameError: name 'tax' is not defined
```

A variável `tax_rate` é global porque foi criada fora da função. A função `calculate_tax` pode lê-la, e a segunda chamada de `print()` também pode lê-la.

O parâmetro `price` e a variável `tax` são locais para `calculate_tax`. Eles estão disponíveis enquanto essa função executa, mas não fora dela. A última chamada de `print()` gera um `NameError` porque `tax` não está definido no escopo global.

> Repare: dentro da função, você pode ler a variável global, mas atribuir um valor a ela (`tax_rate = 0.2`) cria uma variável local com o mesmo nome. A global continua valendo `0.1`.
