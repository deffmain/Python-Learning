# Python — Fundamentos

> Anotações práticas sobre o que é Python e onde ele é usado, declaração de variáveis, regras e convenções de nomenclatura, comentários e a função `print()`.

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
