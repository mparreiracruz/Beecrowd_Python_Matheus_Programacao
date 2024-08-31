'''
beecrowd | 1010
Cálculo Simples
Adaptado por Neilor Tonin, URI  Brasil

Timelimit: 1

https://judge.beecrowd.com/pt/problems/view/1010
'''
linha_01 = input().split()
codigo_peca_01 = int(linha_01[0])
numero_de_pecas_01 = int(linha_01[1])
valor_unitario_peca_01 = float(linha_01[2])

linha_02 = input().split()
codigo_peca_02 = int(linha_02[0])
numero_de_pecas_02 = int(linha_02[1])
valor_unitario_peca_02 = float(linha_02[2])

valor_total = (numero_de_pecas_01 * valor_unitario_peca_01) + (numero_de_pecas_02 * valor_unitario_peca_02)

print('VALOR A PAGAR: R$ {:.2f}'.format(valor_total))
