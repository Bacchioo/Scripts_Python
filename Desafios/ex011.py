a = float(input('Digite a altura da parede: '))
l = float(input('Digite a largura da parede: '))

p = a * l
t = p / 2
print('Sua parede tem a dimensão de {:.2f} x {:.2f} tendo uma área de {:.2f} m²'.format(a, l, p))
print('Você ira precisar de {:.2f} litro(s) de tinta para pintar a parede'.format(t))