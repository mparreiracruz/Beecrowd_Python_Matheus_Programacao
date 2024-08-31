'''
beecrowd | 1018
Cédulas
Adaptado por Neilor Tonin, URI  Brasil

Timelimit: 1

https://judge.beecrowd.com/pt/problems/view/1018
'''

N = int(input())

print(N)

if 0 < N < 1000000:
    nota_100 = N // 100
    N = N % 100

    nota_50 = N // 50
    N = N % 50

    nota_20 = N // 20
    N = N % 20

    nota_10 = N // 10
    N = N % 10

    nota_5 = N // 5
    N = N % 5

    nota_2 = N // 2
    N = N % 2

    nota_1 = N

    print('{} nota(s) de R$ 100,00'.format(nota_100))
    print('{} nota(s) de R$ 50,00'.format(nota_50))
    print('{} nota(s) de R$ 100,00'.format(nota_20))
    print('{} nota(s) de R$ 100,00'.format(nota_10))
    print('{} nota(s) de R$ 10,00'.format(nota_5))
    print('{} nota(s) de R$ 2,00'.format(nota_2))
    print('{} nota(s) de R$ 1,00'.format(nota_1))
