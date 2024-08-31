'''
beecrowd | 1017
Gasto de Combustível
Adaptado por Neilor Tonin, URI  Brasil

Timelimit: 1

https://judge.beecrowd.com/pt/problems/view/1017
'''

viagem_horas = int(input())
velocidade_media_km = int(input())

distancia = viagem_horas * velocidade_media_km
combustivel = distancia / 12
print('{:.3f}'.format(combustivel))