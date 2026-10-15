"""
Arquivo: CaesarCipher.py
Tema: Cifra de César com fatiamento de strings, str.maketrans() e translate()

Funções praticadas:
- caesar()  → recusa shift que não seja int (isinstance()) ou que esteja fora de 1 a 25,
              monta o alfabeto deslocado com alphabet[shift:] + alphabet[:shift] e troca
              as letras com str.maketrans() e translate(), tratando maiúsculas e
              minúsculas; espaços e pontuação ficam como estão
- encrypt() → chama caesar(text, shift), usando o valor padrão encrypt=True
- decrypt() → chama caesar(text, shift, encrypt=False); com encrypt falso, o shift fica
              negativo (shift = - shift) e o deslocamento é desfeito

Aplicação: decrypt(encrypted_text, 13) decifra 'Pbhentr vf sbhaq va hayvxryl cynprf.'
e imprime "Courage is found in unlikely places."
"""


def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = - shift
    
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    return text.translate(translation_table)

def encrypt(text, shift):
    return caesar(text, shift)
    
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)

encrypted_text = 'Pbhentr vf sbhaq va hayvxryl cynprf.'
decrypted_text = decrypt(encrypted_text, 13);

print(decrypted_text);
