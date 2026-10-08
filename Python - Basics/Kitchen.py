"""
Arquivo: Kitchen.py
Tema: Funções, parâmetros, return e escopo de variáveis (estoque de uma cozinha)

Funções praticadas:
- check_kitchen_stock() → lê as globais available_eggs, available_flour e available_sugar,
                          soma tudo em total_items (variável local) e imprime o estoque
                          com f-strings
- use_eggs()            → o parâmetro available_eggs é local e tem o mesmo nome da global;
                          se eggs_to_use for maior que o estoque, avisa e devolve o valor
                          sem mudança, senão devolve available_eggs - eggs_to_use com return
- make_fried_egg()      → guarda o teste available_eggs >= 1 em has_enough_eggs; se houver
                          ovo, chama use_eggs() e atualiza a variável local com o retorno;
                          no fim, devolve o estoque com return

Escopo na prática:
  use_eggs(available_eggs, 1) sem guardar o retorno não altera a global:
  print(available_eggs) continua mostrando 1.
  available_eggs = make_fried_egg(available_eggs) atualiza a global com o valor devolvido.
"""

available_eggs = 1
available_flour = 2
available_sugar = 3

def check_kitchen_stock():
    total_items = available_eggs + available_flour + available_sugar
    print(f'The kitchen has {total_items} total items:')
    print(f'- {available_eggs} eggs')
    print(f'- {available_flour} flour')
    print(f'- {available_sugar} sugar')

check_kitchen_stock()

def use_eggs(available_eggs, eggs_to_use):
    if eggs_to_use > available_eggs:
        print('The kitchen does not have enough eggs.')
        return available_eggs

    print(f'{eggs_to_use} egg(s) used out of {available_eggs} available.')
    return available_eggs - eggs_to_use

use_eggs(available_eggs, 1)
print(available_eggs)

def make_fried_egg(available_eggs):
    has_enough_eggs = available_eggs >= 1

    if has_enough_eggs:
        available_eggs = use_eggs(available_eggs, 1)
        print('Made a fried egg. Yummy!')
    else:
        print('Could not make a fried egg. Not enough eggs!')

    return available_eggs

available_eggs = make_fried_egg(available_eggs)

check_kitchen_stock()
