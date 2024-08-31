'''
beecrowd | 1009
Salário com Bônus
Adaptado por Neilor Tonin, URI  Brasil

Timelimit: 1

https://judge.beecrowd.com/pt/problems/view/1009
'''

nome = input()
salario = float(input())
valor_venda = float(input())

comissao = 0.15 * valor_venda
salario_total = salario + comissao

print('TOTAL = R$ {:.2f}'.format(salario_total))
