c = float(input('Indorme a temperatura em °C: '))
f = 32 + (c * (9/5))
k = c + 273
print('A temperatura de {}°C corresponde a {:.1f}°F!'.format( c, f))
print('E em Kelvin corresponde a {:.1f} K'.format(k))