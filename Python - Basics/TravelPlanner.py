"""
Arquivo: TravelPlanner.py
Tema: Planejador de viagem com condicionais aninhadas e operadores booleanos

Conceitos praticados:
- Valor falsy              → if not distance_mi trata a distância 0 e imprime "False"
- if / elif / else         → separa as faixas de distância: até 1, de 1 a 6 e mais de 6 milhas
- if / else aninhado       → dentro de cada faixa, decide se a viagem é possível
- and / not                → has_bike and not is_raining exige bicicleta e tempo sem chuva
- or                       → has_car or has_ride_share_app aceita carro ou app de carona
- Operadores de comparação → <= e > comparam distance_mi com 1 e com 1 * 6

Regras:
  distance_mi é 0 (falsy)   → "False"
  distance_mi <= 1          → "True" se não estiver chovendo
  1 < distance_mi <= 6      → "True" se tiver bicicleta e não estiver chovendo
  distance_mi > 6           → "True" se tiver carro ou app de carona
  nos demais casos          → "False"
"""

distance_mi = 0;
is_raining = False;
has_bike = False;
has_car = True;
has_ride_share_app = False;

if not distance_mi:
    print("False");
elif distance_mi <= 1 and not is_raining:
    if not is_raining:
        print("True");
    else:
        print("False");
elif distance_mi > 1 and distance_mi <= (1 * 6):
    if has_bike and not is_raining:
        print("True");
    else:
        print("False");
elif distance_mi > (1 * 6):
    if has_car or has_ride_share_app:
        print("True");
    else:
        print("False");
else:
    print("False");
