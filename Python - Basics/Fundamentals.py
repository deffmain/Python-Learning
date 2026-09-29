"""
Arquivo: Fundamentals.py
Tema: Variáveis, concatenação, f-strings e fatiamento de strings

Conceitos praticados:
- Concatenação (+)        → full_name junta first_name e last_name com um espaço; employee_info
                            e experience_info também são montados com +
- Operador +=             → acrescenta ', Apartment 4B' ao final de address
- str()                   → converte employee_age e experience_years (int) em texto para
                            concatenar com strings
- f-string                → employee_card monta a ficha do funcionário com {full_name},
                            {employee_age}, {position} e {salary}
- Fatiamento [início:fim] → employee_code[0:3], [4:8] e [9:11] extraem o departamento,
                            o ano e as iniciais
- Índice negativo         → employee_code[-3:] pega os três últimos caracteres
- print()                 → exibe as mensagens montadas e os trechos fatiados no terminal
"""

first_name = 'John'
last_name = 'Doe'
full_name = first_name + ' ' + last_name
address = '123 Main Street'
address += ', Apartment 4B'
employee_age = 28
employee_info = full_name + ' is ' + str(employee_age) + ' years old'
print(employee_info)
experience_years = 5
experience_info = 'Experience: ' + str(experience_years) + ' years'
print(experience_info)
position = 'Data Analyst'
salary = 75000
employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}'
print(employee_card)
employee_code = 'DEV-2026-JD-001'
department = employee_code[0:3]
print(department)
year_code = employee_code[4:8]
print(year_code)
initials = employee_code[9:11]
print(initials)
last_three = employee_code[-3:]

print(last_three)
