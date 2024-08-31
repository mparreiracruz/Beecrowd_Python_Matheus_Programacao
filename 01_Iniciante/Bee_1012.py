'''
beecrowd | 1012
Área
Adaptado por Neilor Tonin, URI  Brasil

Timelimit: 1

https://judge.beecrowd.com/pt/problems/view/1012
'''
linha_01 = input().split()

A = float(linha_01[0])
B = float(linha_01[1])
C = float(linha_01[2])
pi = 3.14159

triangulo_retangulo = (A * C)/2
circulo = C**2 * pi
trapezio = ((A + B) * C) / 2
quadrado = B**2
retangulo = A * B

print('TRIANGULO: {:.3f}'.format(triangulo_retangulo))
print('CIRCULO: {:.3f}'.format(circulo))
print('TRAPEZIO: {:.3f}'.format(trapezio))
print('QUADRADO: {:.3f}'.format(quadrado))
print('RETANGULO: {:.3f}'.format(retangulo))



