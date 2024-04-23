dias = int(input('Quantos dias? '))
KM = float(input('Quantos KM rodados? '))

t = (dias * 60) + (KM * 0.15)
print('O total de dias a pagar será de R${}!'.format(dias * 60))
print('O total de KM rodados será de R${:.2f}!'.format(KM * 0.15))
print('Dando um total de R${:.2f}!'.format(t))