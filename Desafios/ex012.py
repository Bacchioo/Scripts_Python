pp = float(input('Qual é o preço do produto? R$'))
r = pp - (pp * 5/100)
print('O novo preço do produto é de R${:.2f}'.format(r))