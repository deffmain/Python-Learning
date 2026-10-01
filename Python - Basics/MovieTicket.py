"""
Arquivo: MovieTicket.py
Tema: Reserva de ingresso de cinema com condicionais e operadores booleanos

Conceitos praticados:
- if                        → age > 17 verifica se o usuário pode reservar um ingresso
- if / else                 → age >= 21 decide se ele pode ver sessões noturnas (Evening)
- and                       → is_member and age >= 21 decide o desconto de membro (discount)
- or                        → is_weekend or show_time == 'Evening' decide a taxa extra
                              (extra_charges)
- Condição composta         → age >= 21 or age >= 18 and (show_time != 'Evening' or is_member)
                              libera a reserva; o and é avaliado antes do or
- if / elif / else aninhado → dentro da reserva, seat_type define service_charges
- Operadores de comparação  → >, >=, == e != comparam age, show_time e seat_type

Valores usados:
  discount        → 3 para membros com 21 anos ou mais
  extra_charges   → 2 no fim de semana ou em sessão noturna
  service_charges → Premium 5, Gold 3, outros assentos 1
"""

base_price = 15
age = 21
seat_type = 'Gold'
show_time = 'Evening'

if age > 17:
    print('User is eligible to book a ticket')

if age >= 21:
    print('User is eligible for Evening shows')
else:
    print('User is not eligible for Evening shows')

is_member = False
is_weekend = False

discount = 0
if is_member and age >= 21:
    discount = 3
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')
print('Discount:', discount)

extra_charges = 0
if is_weekend or show_time == 'Evening':
    extra_charges = 2
    print('Extra charges will be applied')
else:
    print('No extra charges will be applied')
print('Extra charges:', extra_charges)

if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member):
    print('Ticket booking condition satisfied')

    service_charges = 0
    if seat_type == 'Premium':
        service_charges = 5
    elif seat_type == 'Gold':
        service_charges = 3
    else:
        service_charges = 1
    print('Service charges:', service_charges)

    
else:
    print('Ticket booking failed due to restrictions')
