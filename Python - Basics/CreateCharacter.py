"""
Arquivo: CreateCharacter.py
Tema: Criação de personagem de RPG com validação dos argumentos e barras de atributos

Conceitos praticados:
- sys.stdout.reconfigure() → muda a saída para UTF-8, para o print() mostrar ● e ○ no
                             terminal do Windows
- Função com parâmetros    → create_character(name, strength, intelligence, charisma)
                             recebe o nome e os três atributos do personagem
- if / elif                → testa um erro por vez, na ordem, e devolve a mensagem com return
- isinstance()             → isinstance(name, str) exige nome em texto e
                             isinstance(stat, int) exige atributos inteiros
- Valor falsy              → not name recusa o nome vazio ('')
- len() e in               → len(name) > 10 limita o nome a 10 caracteres e " " in name
                             recusa nomes com espaço
- any() + gerador          → any(not isinstance(stat, int) for stat in (...)) testa os três
                             atributos de uma vez
- Operadores de comparação → < 1 e > 4, ligados por or, limitam cada atributo de 1 a 4;
                             a soma != 7 exige exatamente 7 pontos no total
- Operador * em strings    → full_dot * strength + empty_dot * (10 - strength) monta a barra
                             de 10 bolinhas de cada atributo
- f-string com \n          → junta o nome e as linhas STR, INT e CHA numa string só

Aplicação: print(create_character('Jose', 2, 2, 3)) imprime:
  Jose
  STR ●●○○○○○○○○
  INT ●●○○○○○○○○
  CHA ●●●○○○○○○○
"""

import sys
sys.stdout.reconfigure(encoding="utf-8")


full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):
    
    if not isinstance(name, str):
        return 'The character name should be a string';
    elif not name:
        return 'The character should have a name';
    elif len(name) > 10:
        return 'The character name is too long';
    elif " " in name:
        return 'The character name should not contain spaces';
    elif any(not isinstance(stat, int) for stat in (strength, intelligence, charisma)):
        return 'All stats should be integers';
    elif strength < 1 or intelligence < 1 or charisma < 1:
        return 'All stats should be no less than 1';
    elif strength > 4 or intelligence > 4 or charisma > 4:
        return 'All stats should be no more than 4';
    elif  strength + intelligence + charisma != 7:
        return 'The character should start with 7 points';
    
    
    strs = (full_dot * strength) + (empty_dot * (10 - strength));
    inte = (full_dot * intelligence) + (empty_dot * (10 - intelligence));
    crs = (full_dot * charisma) + (empty_dot * (10 - charisma));
    
    return f'{name}\nSTR {strs}\nINT {inte}\nCHA {crs}';


print(create_character('Jose',2,2,3));
