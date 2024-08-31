'''
beecrowd | 1013
O Maior
Adaptado por Neilor Tonin, beecrowd  Brasil

Timelimit: 1

https://judge.beecrowd.com/pt/problems/view/1013
'''

linha_01 = input().split()

A = int(linha_01[0])
B = int(linha_01[1])
C = int(linha_01[2])

maior_entre_A_B = (A + B + abs(A - B)) / 2
tmp = maior_entre_A_B
maior_entre_tmp_C = (tmp + C + abs(tmp - C)) / 2

print('{} eh o maior'.format(int(maior_entre_tmp_C)))
