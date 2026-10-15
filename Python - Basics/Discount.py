"""
Arquivo: Discount.py
Tema: Função com validação dos argumentos e cálculo de desconto

Conceitos praticados:
- Função com parâmetros    → apply_discount(price, discount) recebe o preço e o desconto
                             em porcentagem
- isinstance()             → isinstance(price, (int, float)) aceita int ou float usando uma
                             tupla de tipos; o mesmo teste vale para discount
- if / elif / else         → testa um erro por vez e devolve a mensagem com return; só
                             chega ao else quando price e discount são válidos
- Operadores de comparação → price <= 0 recusa preço zero ou negativo; discount < 0 or
                             discount > 100 recusa descontos fora de 0 a 100
- Operador -=              → price -= ((discount/100) * price) tira a porcentagem do preço

Aplicação: apply_discount(100, 20) devolve 80.0 (float, por causa da divisão com /).
"""


def apply_discount(price, discount):
    if not isinstance(price,(int, float)):
        return 'The price should be a number';
    elif not isinstance(discount,(int, float)):
        return 'The discount should be a number';
    elif price <= 0:
        return 'The price should be greater than 0';
    elif discount < 0 or discount >100:
        return 'The discount should be between 0 and 100';
    else:
        price -= ((discount/100) * price);
        return price;       
        

print(apply_discount(100, 20));
