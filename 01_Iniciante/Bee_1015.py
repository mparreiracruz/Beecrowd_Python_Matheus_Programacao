'''
beecrowd | 1015
Distância Entre Dois Pontos
Adaptado por Neilor Tonin, URI  Brasil

Timelimit: 1

https://judge.beecrowd.com/pt/problems/view/1015
'''

linha_01 = input().split()
linha_02 = input().split()
x_1 = float(linha_01[0])
y_1 = float(linha_01[1])
x_2 = float(linha_02[0])
y_2 = float(linha_02[1])

formula = ((x_2 - x_1)**2 + (y_2 - y_1)**2)**0.5

print('{:.4f}'.format(formula))
