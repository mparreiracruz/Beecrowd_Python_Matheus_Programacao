'''
beecrowd | 1008
Salário
Adaptado por Neilor Tonin, URI  Brasil

Timelimit: 1

https://judge.beecrowd.com/pt/problems/view/1008
'''

numero_empregado = int(input())
horas_trabalhadas = int(input())
salario_por_hora = float(input())

salario = horas_trabalhadas * salario_por_hora

print('NUMBER = {}'.format(numero_empregado))
print('SALARY = U$ {:.2f}'.format(salario))
